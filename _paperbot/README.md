# 文献雷达（阶段 1–2：本地同步 + 每日抓取，不做网站）

```
RNA-ProteinVault/                         ← 本地 vault = GitHub 仓库 main 分支
├── .obsidian/ 00_Home/ concepts/ data/ notes/ projects/ templates/   ← 原有，不动
├── inbox/                ← bot 每天写入，你负责清空
├── index.md / starred.md / topics.md      ← 自动生成的三个汇总笔记，别手改
├── _dashboard.md         ← Dataview 面板（需要 Dataview 插件）
├── _paperbot/            ← 脚本、keywords.yml、seen.json、archive/
└── .github/workflows/papers.yml           ← 每天 06:00 在 GitHub 上跑
```

## 每天的循环
1. 06:00 bot 在 GitHub 上抓取、打分、写 `inbox/`、生成 `index.md`，提交。
2. 你打开 Obsidian（Obsidian Git 自动 pull，或手动 `git pull`），看 `index.md` 或 `_dashboard.md`。
3. 每篇三选一：`star: true` + 一句 `note` / 拖进对应 `NN_xxx` 目录 / 直接删（不会再回来）。
4. Obsidian Git 自动 push（或手动）。

## 调关键词：`_paperbot/keywords.yml`
| 症状 | 改哪里 |
|---|---|
| 每天太多 / 太少 | `max_per_day`、`min_score` |
| 老混进 scRNA-seq / 临床 | `negative` 加词或加大负分 |
| 漏了某个方向 | `positive` 加词；`must_match` 第二组加词 |
| 分类分错 | `topic_rules` 调顺序（先命中先得） |
| 想看被刷掉的 | `_paperbot/archive/<日期>.jsonl` |

本地试跑（不写文件）：`python3 _paperbot/fetch_papers.py --dry-run`

## 以后想加网站
仓库内容不用动：装 Quartz 到 `site/`，workflow 里加一个构建 job，把 `publish: true` 的笔记渲染上线即可。到时候再说。
