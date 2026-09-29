---
title: "SimRNA: a coarse-grained method for RNA folding simulations and 3D structure prediction"
created: "2022-08-04"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Michal J. Boniecki"
authors:
  - "Michal J. Boniecki"
  - "Grzegorz Lach"
  - "Wayne K. Dawson"
  - "Konrad Tomala"
  - "Pawel Lukasz"
  - "Tomasz Soltysinski"
  - "Kristian M. Rother"
  - "Janusz M. Bujnicki"
zotero_key: "EPFWC7C2"
item_type: "journalArticle"
publication_date: "2016-04-20 2016-4-20"
doi: "10.1093/nar/gkv1479"
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838351/"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# SimRNA: a coarse-grained method for RNA folding simulations and 3D structure prediction

## Source

- Zotero: [Open item](zotero://select/library/items/EPFWC7C2)
- DOI: [10.1093/nar/gkv1479](https://doi.org/10.1093%2Fnar%2Fgkv1479)
- Source: [Open source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838351/)
- PDF attached: yes

## Authors

Michal J. Boniecki; Grzegorz Lach; Wayne K. Dawson; Konrad Tomala; Pawel Lukasz; Tomasz Soltysinski; Kristian M. Rother; Janusz M. Bujnicki

## Abstract

RNA molecules play fundamental roles in cellular processes. Their function and interactions with other biomolecules are dependent on the ability to form complex three-dimensional (3D) structures. However, experimental determination of RNA 3D structures is laborious and challenging, and therefore, the majority of known RNAs remain structurally uncharacterized. Here, we present SimRNA: a new method for computational RNA 3D structure prediction, which uses a coarse-grained representation, relies on the Monte Carlo method for sampling the conformational space, and employs a statistical potential to approximate the energy and identify conformations that correspond to biologically relevant structures. SimRNA can fold RNA molecules using only sequence information, and, on established test sequences, it recapitulates secondary structure with high accuracy, including correct prediction of pseudoknots. For modeling of complex 3D structures, it can use additional restraints, derived from experimental or computational analyses, including information about secondary structure and/or long-range contacts. SimRNA also can be used to analyze conformational landscapes and identify potential alternative structures.

## Reading notes

### Research question

一个只有五个伪原子/核苷酸的粗粒化模型，能否从序列出发同时探索 RNA 的二级结构、三级折叠和可能的折叠中间态，并在有实验信息时自然接受约束？

### Method

- 每个核苷酸用 P、C4′ 和 3 个碱基原子表示；局部骨架项与序列依赖的长程相互作用共同构成统计势。
- 用 Metropolis/副本交换 Monte Carlo 采样构象，可加入位置、距离和二级结构三类约束。
- 用多个公开基准测试无约束折叠、二级结构约束折叠，以及结合实验长程接触的折叠；最终通过能量、聚类和 RMSD/INF 评价。

### Evidence

- 在较简单的 Ding 与 Das–Baker 数据集上，无约束模型分别有 145/153 和 9/10 个单链 RNA 达到统计显著的正确折叠；接触 INF 约 0.80，非经典接触恢复约 55%。
- 15 个含假结的结构中有 14 个无需二级结构约束即可得到显著正确模型。
- 对更困难的 RNA-Puzzles，单靠无约束折叠通常 RMSD 很高；加入二级结构和实验长程接触后，多数模型改善到约 10–17 Å。
- 在困难的 Seetin–Mathews 集合中，追加约束把平均模型 RMSD 从参考方法约 9.2 Å 改善到约 7.7 Å。

### Limitations

- 粗粒化表示的天然精度上限约为 2–3 Å，无法直接提供可靠的原子级几何。
- 统计势偏爱数据库中常见的经典碱基对与堆叠，对稀有但物理上稳定的非经典相互作用评分不足。
- 大 RNA 的搜索成本仍然很高；真实 RNA-Puzzles 对专家约束和外部信息依赖明显。

## Open questions / Gaps

- [已有候选方向] 如何把 SimRNA 的全局采样与 [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] 或 SWM 的全原子精修稳定串联？
- [已有候选方向] 能否用学习得到的长程接触替代昂贵或缺失的实验约束？[[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] 提供了候选方向。
- [待验证] 统计势中稀有非经典相互作用的低估，能否通过物理势重标定而不损害粗粒化搜索效率？

## Connections

- 支持 :: [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] — 两者都显示长程约束能显著改善复杂 RNA 的全局拓扑。
- 矛盾 :: [[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]] — 这里的核心取舍是搜索覆盖而非原子精度；两者不是结论冲突，而是分辨率与可扩展性的张力。
- 延伸 :: [[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]] — ClaRNA 可直接评价 SimRNA 粗粒化模型中的接触类型，补足只看 RMSD 的不足。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] — 理解如何自动生成 SimRNA 最需要的长程约束。
- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 比较粗粒化全局搜索与全原子片段组装的边界。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
