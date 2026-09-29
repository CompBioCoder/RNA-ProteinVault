#!/usr/bin/env python3
"""每日抓取 RNA-蛋白相关文献 → 关键词打分 → 写入 vault 根目录的 inbox/。

用法（在 vault 根目录运行）:
    python _paperbot/fetch_papers.py            # 正常运行
    python _paperbot/fetch_papers.py --dry-run  # 只打印筛选结果，不写文件

依赖: pip install -r _paperbot/requirements.txt
数据: _paperbot/seen.json（去重表）、_paperbot/archive/YYYY-MM-DD.jsonl（未入选但相关的论文）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]      # vault 根目录 = 仓库根目录
INBOX = ROOT / "inbox"
DATA = ROOT / "_paperbot"
SEEN_FILE = DATA / "seen.json"
SKIP_DIRS = {"site", "templates", "node_modules"}   # 加上以 . 或 _ 开头的目录一律不扫
UA = {"User-Agent": "rna-protein-papers-bot/1.0 (+github actions)"}
SOURCE_LABEL = {"arxiv": "arXiv", "biorxiv": "bioRxiv", "medrxiv": "medRxiv", "pubmed": "PubMed"}


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def norm_ws(s: str | None) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i : i + n]


# ───────────────────────── 打分 ─────────────────────────

def term_re(term: str) -> re.Pattern:
    """词前缀匹配：'fold' 命中 folding，但 'rna' 不命中 mrna。"""
    return re.compile(r"(?<![a-z0-9])" + re.escape(term.lower()))


class Scorer:
    def __init__(self, cfg: dict):
        self.must = [[term_re(t) for t in group] for group in cfg.get("must_match", [])]
        self.pos = [(t, term_re(t), int(w)) for t, w in (cfg.get("positive") or {}).items()]
        self.neg = [(t, term_re(t), int(w)) for t, w in (cfg.get("negative") or {}).items()]
        self.topics = [(name, [term_re(t) for t in terms]) for name, terms in (cfg.get("topic_rules") or {}).items()]
        self.default_topic = cfg.get("default_topic", "inbox")
        self.title_bonus = int(cfg.get("title_bonus", 1))

    def score(self, paper: dict):
        """返回 (score, hits) 或 None（未通过硬性门槛）。"""
        title = paper["title"].lower()
        text = title + "\n" + paper["abstract"].lower()
        if not all(any(r.search(text) for r in group) for group in self.must):
            return None
        score, hits = 0, []
        for term, r, w in self.pos:
            n = min(len(r.findall(text)), 2)
            if n:
                score += w * n
                if r.search(title):
                    score += self.title_bonus
                hits.append(term)
        for term, r, w in self.neg:
            if r.search(text):
                score += w
                hits.append(f"-{term}")
        return score, hits

    def topic(self, paper: dict) -> str:
        text = (paper["title"] + "\n" + paper["abstract"]).lower()
        for name, regs in self.topics:
            if any(r.search(text) for r in regs):
                return name
        return self.default_topic


# ───────────────────────── 抓取 ─────────────────────────

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def fetch_arxiv(cfg: dict, since: str) -> list[dict]:
    terms = cfg.get("terms") or ["RNA"]
    q = "(" + " OR ".join(f'ti:"{t}" OR abs:"{t}"' for t in terms) + ")"
    if cfg.get("categories"):
        q += " AND (" + " OR ".join(f"cat:{c}" for c in cfg["categories"]) + ")"
    params = {
        "search_query": q,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": int(cfg.get("max_results", 200)),
    }
    r = requests.get("https://export.arxiv.org/api/query", params=params, headers=UA, timeout=90)
    r.raise_for_status()
    out = []
    for e in ET.fromstring(r.content).findall("a:entry", ATOM):
        published = e.findtext("a:published", "", ATOM)[:10]
        if published < since:
            continue
        short = re.sub(r"v\d+$", "", e.findtext("a:id", "", ATOM).rsplit("/", 1)[-1])
        out.append(
            dict(
                id=f"arxiv-{short}",
                title=norm_ws(e.findtext("a:title", "", ATOM)),
                abstract=norm_ws(e.findtext("a:summary", "", ATOM)),
                authors=[norm_ws(a.findtext("a:name", "", ATOM)) for a in e.findall("a:author", ATOM)],
                published=published,
                source="arxiv",
                url=f"https://arxiv.org/abs/{short}",
                doi=norm_ws(e.findtext("arxiv:doi", "", ATOM)),
                extra=", ".join(c.get("term", "") for c in e.findall("a:category", ATOM)),
            )
        )
    return out


def fetch_biorxiv(cfg: dict, since: str, until: str) -> list[dict]:
    wanted = {c.lower() for c in cfg.get("categories") or []}
    out = []
    for server in cfg.get("servers") or ["biorxiv"]:
        cursor = 0
        for _ in range(int(cfg.get("max_pages", 30))):
            url = f"https://api.biorxiv.org/details/{server}/{since}/{until}/{cursor}"
            r = requests.get(url, headers=UA, timeout=90)
            r.raise_for_status()
            coll = r.json().get("collection") or []
            if not coll:
                break
            for p in coll:
                cat = (p.get("category") or "").strip().lower()
                if wanted and cat not in wanted:
                    continue
                doi = norm_ws(p.get("doi"))
                out.append(
                    dict(
                        id=f"{server}-{doi.split('/')[-1]}",
                        title=norm_ws(p.get("title")),
                        abstract=norm_ws(p.get("abstract")),
                        authors=[a.strip() for a in (p.get("authors") or "").split(";") if a.strip()],
                        published=(p.get("date") or "")[:10],
                        source=server,
                        url=f"https://www.{server}.org/content/{doi}v{p.get('version', '1')}",
                        doi=doi,
                        extra=cat,
                    )
                )
            if len(coll) < 100:
                break
            cursor += 100
    return out


EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def _pubmed_date(art) -> str:
    for xp in (".//ArticleDate", ".//PubMedPubDate[@PubStatus='pubmed']", ".//Journal//PubDate"):
        node = art.find(xp)
        if node is not None and node.findtext("Year"):
            y = node.findtext("Year")
            m = (node.findtext("Month") or "01")[:3]
            months = {"jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
                      "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12"}
            m = months.get(m.lower(), m.zfill(2))
            d = (node.findtext("Day") or "01").zfill(2)
            return f"{y}-{m}-{d}"
    return ""


def fetch_pubmed(cfg: dict, days_back: int) -> list[dict]:
    params = {
        "db": "pubmed", "term": norm_ws(cfg["query"]), "reldate": days_back, "datetype": "edat",
        "retmax": int(cfg.get("max_results", 150)), "retmode": "json", "sort": "date",
    }
    r = requests.get(EUTILS + "esearch.fcgi", params=params, headers=UA, timeout=90)
    r.raise_for_status()
    ids = r.json().get("esearchresult", {}).get("idlist") or []
    out = []
    for chunk in chunks(ids, 50):
        r = requests.get(EUTILS + "efetch.fcgi", params={"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"},
                         headers=UA, timeout=90)
        r.raise_for_status()
        for art in ET.fromstring(r.content).findall(".//PubmedArticle"):
            pmid = art.findtext(".//PMID", "")
            t = art.find(".//ArticleTitle")
            doi = next((x.text for x in art.findall(".//ArticleIdList/ArticleId") if x.get("IdType") == "doi"), "")
            out.append(
                dict(
                    id=f"pubmed-{pmid}",
                    title=norm_ws("".join(t.itertext())) if t is not None else "",
                    abstract=norm_ws(" ".join("".join(x.itertext()) for x in art.findall(".//Abstract/AbstractText"))),
                    authors=[norm_ws(f"{a.findtext('ForeName', '')} {a.findtext('LastName', '')}")
                             for a in art.findall(".//AuthorList/Author") if a.find("LastName") is not None],
                    published=_pubmed_date(art),
                    source="pubmed",
                    url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    doi=norm_ws(doi),
                    extra=art.findtext(".//Journal/ISOAbbreviation") or art.findtext(".//Journal/Title") or "",
                )
            )
    return out


# ───────────────────────── 去重 ─────────────────────────

def read_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def keys_of(title: str, doi: str) -> set[str]:
    keys = set()
    if doi:
        keys.add("doi:" + doi.lower().strip())
    t = re.sub(r"[^a-z0-9]", "", (title or "").lower())[:120]
    if len(t) > 20:
        keys.add("title:" + t)
    return keys


def load_seen() -> dict:
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text(encoding="utf-8"))
    return {}


def keys_in_vault() -> set[str]:
    """已经在 content/ 里的论文（含你手动挪进 01–09 的）也算见过。"""
    keys = set()
    for md in ROOT.rglob("*.md"):
        parts = md.relative_to(ROOT).parts
        if any(p.startswith((".", "_")) or p in SKIP_DIRS for p in parts):
            continue
        fm = read_frontmatter(md)
        if fm.get("url") or fm.get("doi"):
            keys |= keys_of(str(fm.get("title", "")), str(fm.get("doi") or ""))
    return keys


# ───────────────────────── 写文件 ─────────────────────────

def write_paper(p: dict, score: int, hits: list[str], topic: str, today: date) -> Path:
    slug = re.sub(r"[^A-Za-z0-9.\-]+", "-", p["id"]).strip("-")
    path = INBOX / f"{today.isoformat()}-{slug}.md"
    authors = ", ".join(p["authors"][:8]) + (" et al." if len(p["authors"]) > 8 else "")
    fm = {
        "title": p["title"],
        "authors": authors,
        "date": today,
        "published": p["published"] or None,
        "source": p["source"],
        "url": p["url"],
        "doi": p["doi"] or None,
        "score": score,
        "hits": hits,
        "topic": topic,
        "star": False,
        "note": "",
        "tags": ["paper", p["source"]],
        "publish": True,
    }
    fm = {k: v for k, v in fm.items() if v is not None}
    src = SOURCE_LABEL.get(p["source"], p["source"])
    meta = " · ".join(x for x in [src, p["published"], p["extra"]] if x)
    body = (
        "---\n"
        + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10_000)
        + "---\n\n"
        f"**{authors}**  \n{meta} · [原文]({p['url']})\n\n"
        f"> [!abstract] Abstract\n> {p['abstract']}\n\n"
        "## Notes\n\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


# ───────────────────────── 主流程 ─────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(DATA / "keywords.yml"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    today = date.today()
    days_back = int(cfg.get("days_back", 3))
    since = (today - timedelta(days=days_back)).isoformat()
    until = today.isoformat()
    srcs = cfg.get("sources") or {}

    papers: list[dict] = []
    fetchers = {
        "arxiv": lambda c: fetch_arxiv(c, since),
        "biorxiv": lambda c: fetch_biorxiv(c, since, until),
        "pubmed": lambda c: fetch_pubmed(c, days_back),
    }
    for name, fn in fetchers.items():
        c = srcs.get(name) or {}
        if not c.get("enabled", False):
            continue
        try:
            got = fn(c)
            log(f"[{name}] {len(got)} 篇")
            papers += got
        except Exception as exc:  # 单个源挂了不影响其他源
            log(f"[{name}] 抓取失败: {exc}")

    seen = load_seen()
    known = set(seen) | keys_in_vault()
    scorer = Scorer(cfg)
    fresh, scored = [], []
    for p in papers:
        if not p["title"]:
            continue
        ks = keys_of(p["title"], p["doi"])
        if ks & known:
            continue
        known |= ks
        fresh.append((p, ks))
        res = scorer.score(p)
        if res is None:
            continue
        s, hits = res
        scored.append((s, hits, p))
    scored.sort(key=lambda x: -x[0])
    min_score, max_per_day = int(cfg.get("min_score", 4)), int(cfg.get("max_per_day", 8))
    selected = [x for x in scored if x[0] >= min_score][:max_per_day]
    rest = [x for x in scored if x not in selected]
    log(f"新论文 {len(fresh)} 篇，过门槛 {len(scored)} 篇，入选 {len(selected)} 篇")

    for s, hits, p in selected:
        log(f"  [{s:>2}] {p['title'][:90]}  ({p['source']}; {', '.join(hits)})")
    if args.dry_run:
        return 0

    INBOX.mkdir(parents=True, exist_ok=True)
    (DATA / "archive").mkdir(parents=True, exist_ok=True)
    for s, hits, p in selected:
        write_paper(p, s, hits, scorer.topic(p), today)
    if rest:
        with (DATA / "archive" / f"{today.isoformat()}.jsonl").open("a", encoding="utf-8") as f:
            for s, hits, p in rest:
                f.write(json.dumps({"score": s, "hits": hits, **p}, ensure_ascii=False) + "\n")

    for _, ks in fresh:  # 所有新见到的都记为 seen，明天不再重复评估
        for k in ks:
            seen[k] = today.isoformat()
    cutoff = (today - timedelta(days=365)).isoformat()
    seen = {k: v for k, v in seen.items() if v >= cutoff}
    DATA.mkdir(exist_ok=True)
    SEEN_FILE.write_text(json.dumps(seen, ensure_ascii=False, indent=0, sort_keys=True), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
