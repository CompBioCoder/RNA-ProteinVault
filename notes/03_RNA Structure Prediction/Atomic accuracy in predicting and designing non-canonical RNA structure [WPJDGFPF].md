---
title: "Atomic accuracy in predicting and designing non-canonical RNA structure"
created: "2022-09-26"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Rhiju Das"
authors:
  - "Rhiju Das"
  - "John Karanicolas"
  - "David Baker"
zotero_key: "WPJDGFPF"
item_type: "journalArticle"
publication_date: "2010-04-00 2010-4"
doi: "10.1038/nmeth.1433"
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2854559/"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# Atomic accuracy in predicting and designing non-canonical RNA structure

## Source

- Zotero: [Open item](zotero://select/library/items/WPJDGFPF)
- DOI: [10.1038/nmeth.1433](https://doi.org/10.1038%2Fnmeth.1433)
- Source: [Open source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2854559/)
- PDF attached: yes

## Authors

Rhiju Das; John Karanicolas; David Baker

## Abstract

We present a Rosetta full-atom framework for predicting and designing the non-canonical motifs that define RNA tertiary structure, called FARFAR (Fragment Assembly of RNA with Full Atom Refinement). For a test set of thirty-two 6-to-20-nucleotide motifs, the method recapitulated 50% of the experimental structures at near-atomic accuracy. Additionally, design calculations recovered the native sequence at the majority of RNA residues engaged in non-canonical interactions, and mutations predicted to stabilize a signal recognition particle domain were experimentally validated.

## Reading notes

### Research question

能否把片段组装与全原子能量函数结合，在不借用同源模体的条件下预测 RNA 非经典局部结构，并用同一套能量函数反向设计更稳定的序列？

### Method

- 先用 FARNA 做低分辨率片段组装，再用 Rosetta 全原子能量函数优化，形成 FARFAR。
- 在 32 个长度为 6–20 nt 的非经典模体上测试；相似或同源片段从片段库中剔除，并给定模体边界处的经典碱基对。
- 每个目标生成 50,000 个构象，按能量筛选和聚类后考察前 5 个簇中心。
- 另在 15 个高分辨率 RNA 结构上做固定骨架序列设计，并用 DMS 化学探测和 Mg²⁺ 滴定验证 SRP 模体的稳定化突变。

### Evidence

- 32 个目标中有 14 个在前 5 个模型里达到小于 2.0 Å 的全重原子 RMSD；计入完整恢复非经典碱基对的另外 2 例后，16/32 被判定为高精度。
- 14 个近原子精度案例中有 11 个恢复了全部非经典碱基对。
- 固定骨架设计的总体序列恢复率为 45%，非经典相互作用位点为 65%，均高于随机期望。
- SRP 双突变的实验折叠自由能变化为 −1.2 ± 0.5 kcal/mol，与预测的 −1.6 kcal/mol 一致。

### Limitations

- 模体超过约 12 nt 后采样和收敛明显变差；这项研究并未解决大尺度全局折叠。
- 预测预先知道边界经典碱基对，因此并非完全从裸序列恢复所有拓扑约束。
- 水、Mg²⁺ 等离子和溶剂效应只被近似处理；失败案例既可能来自采样不足，也可能来自能量函数排序错误。

## Open questions / Gaps

- [已被后续文献回答] 如何在未知非经典模体上减少片段库偏差并提高局部采样？后续 [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]] 给出了逐步增删采样方案。
- [待验证] 显式水、Mg²⁺ 和相关主链扭转势能否稳定提升非经典相互作用的能量排序，而不是只改善个别模体？
- [已有候选方向] 能否把全原子精修接到粗粒化全局搜索之后，形成“广搜—精修”的可扩展流程？

## Connections

- 延伸 :: [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 更新片段库、螺旋采样和能量函数，把局部 FARFAR 推向复杂全局折叠。
- 延伸 :: [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|Blind prediction / SWM]] — 用逐核苷酸采样处理 FARFAR 难以覆盖的非经典局部模体。
- 支持 :: [[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]] — 说明仅看 RMSD 不够，还需要稳定、可解释的非经典接触分类来评价模型。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|Blind prediction of noncanonical RNA structure at atomic accuracy]] — 直接追踪本文最明显的局部采样瓶颈。
- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 查看 Rosetta 路线如何扩展到更大 RNA 和真正盲测。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
