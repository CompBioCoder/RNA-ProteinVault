#!/usr/bin/env python3
"""从整个 vault 的 frontmatter 生成三个汇总页（每次运行整体重写，不要手改它们）：

    index.md    首页：最近 N 天入选论文，按分数排序
    starred.md  必读：所有 star: true 的论文，按分类分组
    topics.md   分类总览：所有 NN_xxx 目录（不论放在哪一层）的篇数 + 最新 5 篇

只统计 publish: true 的笔记。用法: python _paperbot/build_pages.py
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]      # vault 根目录 = 仓库根目录
CONTENT = ROOT
CONFIG = ROOT / "_paperbot" / "keywords.yml"
GENERATED = {"index.md", "starred.md", "topics.md", "README.md"}
SKIP_DIRS = {"site", "templates", "node_modules"}
TOPIC_RE = re.compile(r"^\d\d_")
SOURCE_LABEL = {"arxiv": "arXiv", "biorxiv": "bioRxiv", "medrxiv": "medRxiv", "pubmed": "PubMed"}


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def as_date(v) -> str:
    if isinstance(v, datetime):
        return v.date().isoformat()
    if isinstance(v, date):
        return v.isoformat()
    return str(v or "")[:10]


def truthy(v) -> bool:
    return v is True or str(v).strip().lower() in {"true", "yes", "1", "⭐"}


def topic_folder(parts: tuple[str, ...], exclude: set[str]) -> str:
    """路径里第一个形如 05_RNA Sequence Design 的目录名；不管它在哪一层。"""
    for part in parts[:-1]:
        if TOPIC_RE.match(part) and part not in exclude:
            return part
    return ""


def load_notes(exclude: set[str]) -> list[dict]:
    notes = []
    for path in sorted(CONTENT.rglob("*.md")):
        rel = path.relative_to(CONTENT)
        if rel.parent == Path(".") and rel.name in GENERATED:
            continue
        if any(part.startswith((".", "_")) or part in SKIP_DIRS for part in rel.parts):
            continue
        fm = read_frontmatter(path)
        if not fm.get("title"):
            continue
        folder = topic_folder(rel.parts, exclude) or (rel.parts[0] if len(rel.parts) > 1 else "")
        notes.append(
            dict(
                fm=fm,
                rel=rel.with_suffix("").as_posix(),
                title=str(fm["title"]).replace("|", "¦").replace("\n", " "),
                date=as_date(fm.get("date")),
                score=int(fm.get("score") or 0),
                star=truthy(fm.get("star")),
                topic=str(fm.get("topic") or (folder if TOPIC_RE.match(folder) else "")),
                source=str(fm.get("source") or ""),
                note=str(fm.get("note") or "").strip(),
                is_paper="paper" in (fm.get("tags") or []) or bool(fm.get("url")),
                publish=truthy(fm.get("publish")),
                folder=folder,
            )
        )
    return notes


def link(n: dict) -> str:
    star = "⭐ " if n["star"] else ""
    return f"{star}[[{n['rel']}|{n['title']}]]"


def write(path: Path, title: str, body: str) -> None:
    fm = yaml.safe_dump({"title": title, "publish": True, "date": date.today()}, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{fm}---\n\n{body.rstrip()}\n", encoding="utf-8")


def build_index(notes: list[dict], index_days: int) -> None:
    cutoff = (date.today() - timedelta(days=index_days)).isoformat()
    recent = [n for n in notes if n["is_paper"] and n["date"] >= cutoff]
    by_day: dict[str, list[dict]] = {}
    for n in recent:
        by_day.setdefault(n["date"], []).append(n)
    lines = [
        "每天自动抓取 arXiv / bioRxiv / PubMed，关键词打分后只留最相关的几篇。⭐ = 已标为必读。",
        "",
        "→ [[starred|必读清单]] · [[topics|分类总览]]",
        "",
    ]
    if not by_day:
        lines.append(f"最近 {index_days} 天没有入选论文。")
    for day in sorted(by_day, reverse=True):
        items = sorted(by_day[day], key=lambda n: (-n["score"], n["title"]))
        lines += [f"## {day}（{len(items)} 篇）", "", "| 分 | 论文 | 来源 | 分类 |", "|:-:|---|---|---|"]
        for n in items:
            lines.append(f"| {n['score']} | {link(n)} | {SOURCE_LABEL.get(n['source'], n['source'])} | {n['topic']} |")
        lines.append("")
    write(CONTENT / "index.md", "RNA × Protein 文献雷达", "\n".join(lines))


def build_starred(notes: list[dict]) -> None:
    starred = [n for n in notes if n["star"]]
    by_topic: dict[str, list[dict]] = {}
    for n in starred:
        by_topic.setdefault(n["topic"] or "未分类", []).append(n)
    lines = [f"共 {len(starred)} 篇。在 Obsidian 里把 frontmatter 的 `star` 改成 `true` 即可加入。", ""]
    for topic in sorted(by_topic):
        lines += [f"## {topic}", ""]
        for n in sorted(by_topic[topic], key=lambda n: n["date"], reverse=True):
            lines.append(f"- {n['date']} · {link(n)}" + (f"  \n  {n['note']}" if n["note"] else ""))
        lines.append("")
    write(CONTENT / "starred.md", "必读清单", "\n".join(lines))


def build_topics(notes: list[dict], exclude: set[str]) -> None:
    folders = sorted({n["folder"] for n in notes if TOPIC_RE.match(n["folder"]) and n["folder"] not in exclude})
    inbox = [n for n in notes if n["folder"] == "inbox"]
    lines = [f"inbox 里还有 **{len(inbox)}** 篇待处理（看完请挪进下面的目录，或标 star）。", ""]
    for folder in folders:
        items = sorted((n for n in notes if n["folder"] == folder), key=lambda n: n["date"], reverse=True)
        lines += [f"## {folder}（{len(items)} 篇）", ""]
        for n in items[:5]:
            lines.append(f"- {n['date']} · {link(n)}")
        if len(items) > 5:
            lines.append(f"- … 其余 {len(items) - 5} 篇见左侧目录")
        lines.append("")
    write(CONTENT / "topics.md", "分类总览", "\n".join(lines))


def main() -> int:
    cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) if CONFIG.exists() else {}
    exclude = set(cfg.get("topic_exclude") or [])
    notes = [n for n in load_notes(exclude) if n["publish"]]  # 没 publish: true 的笔记不上站，也不出现在汇总页
    build_index(notes, int(cfg.get("index_days", 7)))
    build_starred(notes)
    build_topics(notes, exclude)
    print(f"generated index/starred/topics from {len(notes)} notes", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
