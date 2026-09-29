---
title: Obsidian 面板（不上站）
publish: false
---

> 这页只在 Obsidian 里用，需要 Dataview 插件。`publish: false` 所以不会出现在网站上。

## 本周 inbox（按分数）

```dataview
TABLE WITHOUT ID
  link(file.link, title) AS 论文, score AS 分, source AS 来源, topic AS 分类, star AS ⭐
FROM "inbox"
WHERE date >= date(today) - dur(7 days)
SORT score DESC
```

## 已标星但还没写 note 的

```dataview
LIST
FROM ""
WHERE star = true AND (!note OR note = "")
SORT date DESC
```

## inbox 里放了超过 14 天还没处理的

```dataview
TABLE WITHOUT ID link(file.link, title) AS 论文, date AS 抓取日
FROM "inbox"
WHERE date < date(today) - dur(14 days) AND star != true
SORT date ASC
```
