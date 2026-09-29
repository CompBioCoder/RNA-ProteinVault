---
title: "Blind prediction of noncanonical RNA structure at atomic accuracy"
created: "2022-11-16"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Andrew M. Watkins"
authors:
  - "Andrew M. Watkins"
  - "Caleb Geniesse"
  - "Wipapat Kladwang"
  - "Paul Zakrevsky"
  - "Luc Jaeger"
  - "Rhiju Das"
zotero_key: "7CU6NKZJ"
item_type: "journalArticle"
publication_date: "2018-05-00 2018-05"
doi: "10.1126/sciadv.aar5316"
url: "https://www.science.org/doi/10.1126/sciadv.aar5316"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# Blind prediction of noncanonical RNA structure at atomic accuracy

## Source

- Zotero: [Open item](zotero://select/library/items/7CU6NKZJ)
- DOI: [10.1126/sciadv.aar5316](https://doi.org/10.1126%2Fsciadv.aar5316)
- Source: [Open source](https://www.science.org/doi/10.1126/sciadv.aar5316)
- PDF attached: yes

## Authors

Andrew M. Watkins; Caleb Geniesse; Wipapat Kladwang; Paul Zakrevsky; Luc Jaeger; Rhiju Das

## Abstract

We report a new algorithm and a battery of blind challenges for the prediction of complex RNA structures at atomic accuracy.

## Reading notes

### Research question

在不依赖已知同源片段的真正盲测中，能否以原子精度恢复复杂 RNA 模体的非经典碱基对，并让预测产生可实验验证的新结构假说？

### Method

- 把原先确定性枚举的 stepwise assembly 改成 stepwise Monte Carlo（SWM），核心是可逆的逐核苷酸“添加—删除”移动。
- 在 82 个多样化模体上与排除同源片段的 FARFAR 比较，重点评价 RMSD 和非经典碱基对恢复。
- 对三个未知 tetraloop/receptor 做事前预测，用单核苷酸化学探测和补偿突变验证；再参与 Zika 病毒双假结的 RNA-Puzzle 盲测。

### Evidence

- 在 82 个模体上，SWM 的非经典碱基对恢复和 RMSD 均显著优于 FARFAR（分别 $P<5\times10^{-5}$ 与 $P<2\times10^{-4}$）。
- 多螺旋连接、锤头核酶三级接触和 GAAA/11-nt receptor 分别达到约 1.13、1.16 和 0.64 Å RMSD。
- R1 receptor 的 G4–C9、G4–U5–C9 三联体和 G6–A7 相互作用经补偿突变得到支持。
- Zika 病毒双假结盲测正确预测了全部非经典碱基对。

### Limitations

- SWM 对同时含多个模体和螺旋的大 RNA 仍过于昂贵，不能直接取代低分辨率全局方法。
- 14 个 RMSD 大于 3 Å 的失败案例中有 9 个把错误模型评为比实验结构更低能，核心问题仍是能量函数。
- 现有扭转势没有充分描述主链扭转角相关性，也缺少金属离子和完整静电效应。

## Open questions / Gaps

- [已有候选方向] 是否可以在 SimRNA/FARFAR2 给出的全局拓扑上，只对低置信度非经典模体触发 SWM 精修？
- [待验证] 改进相关扭转势并显式加入金属离子后，能否同时修复能量排序错误和主链几何错误？
- [待验证] 如何把 SWM 的局部置信度传递到完整 RNA 模型，而不是只报告单个最优构象？

## Connections

- 矛盾 :: [[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]] — 在严格排除同源片段的局部模体基准上，SWM 显著优于片段组装。
- 延伸 :: [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 两者形成局部精修与全局折叠的互补尺度。
- 支持 :: [[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]] — 非经典接触恢复率是比单一 RMSD 更能解释结构正确性的评价轴。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 了解如何把局部原子精度嵌入更大的 RNA 折叠问题。
- [[notes/03_RNA Structure Prediction/Using Rosetta for RNA homology modeling [NSPH62NF]|Using Rosetta for RNA homology modeling]] — 查看 SWM 在模板缺口和局部重建中的实际定位。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
