---
title: "FARFAR2: Improved De Novo Rosetta Prediction of Complex Global RNA Folds"
created: "2022-07-07"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Andrew Martin Watkins"
authors:
  - "Andrew Martin Watkins"
  - "Ramya Rangan"
  - "Rhiju Das"
zotero_key: "P8RQAIT6"
item_type: "journalArticle"
publication_date: "2020-08-00 08/2020"
doi: "10.1016/j.str.2020.05.011"
url: "https://linkinghub.elsevier.com/retrieve/pii/S0969212620301805"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# FARFAR2: Improved De Novo Rosetta Prediction of Complex Global RNA Folds

## Source

- Zotero: [Open item](zotero://select/library/items/P8RQAIT6)
- DOI: [10.1016/j.str.2020.05.011](https://doi.org/10.1016%2Fj.str.2020.05.011)
- Source: [Open source](https://linkinghub.elsevier.com/retrieve/pii/S0969212620301805)
- PDF attached: yes

## Authors

Andrew Martin Watkins; Ramya Rangan; Rhiju Das

## Abstract

Predicting RNA three-dimensional structures from sequence could accelerate understanding of the growing number of RNA molecules being discovered across biology. Rosetta’s Fragment Assembly of RNA with FullAtom Reﬁnement (FARFAR) has shown promise in community-wide blind RNA-Puzzle trials, but lack of a systematic and automated benchmark has left unclear what limits FARFAR performance. Here, we benchmark FARFAR2, an algorithm integrating RNA-Puzzle-inspired innovations with updated fragment libraries and helix modeling. In 16 of 21 RNA-Puzzles revisited without experimental data or expert intervention, FARFAR2 recovers native-like structures more accurate than models submitted during the RNA-Puzzles trials. Remaining bottlenecks include conformational sampling for >80-nucleotide problems and scoring function limitations more generally. Supporting these conclusions, preregistered blind models for adenovirus VA-I RNA and ﬁve riboswitch complexes predicted native-like folds with 3- to 14 A˚ root-mean-square deviation accuracies. We present a FARFAR2 webserver and three large model archives (FARFAR2-Classics, FARFAR2Motifs, and FARFAR2-Puzzles) to guide future applications and advances.

## Reading notes

### Research question

能否把过去 RNA-Puzzles 中依赖专家临场调整的 Rosetta 流程，整合成一个可自动运行、可系统基准的大型 RNA 三级结构预测协议？

### Method

- FARFAR2 整合四项关键改进：基于 657 个非冗余 RNA 结构的新片段库、低分辨率阶段的评分过滤、保持 Watson–Crick 几何的 base-pair-step 移动，以及更新的全原子能量函数。
- 先在 18 个小 RNA、82 个非经典模体上回顾性测试，再重跑 21 个 RNA-Puzzles；每个复杂问题生成约 3,000–30,000 个模型。
- 用 Rosetta 能量前 1% 的模型衡量可发现性，再用低能聚类做最终选择；另进行 6 个预注册盲测。

### Evidence

- 21 个 RNA-Puzzles 中，19 个在能量前 1% 内采样到 native-like 模型；16 个比当年所有参赛提交中的最佳模型更接近真实结构。
- 6 个盲测的最佳提交覆盖 3.0–14.3 Å RMSD，包括糖胺酸、SAM-IV、T-box 核糖开关和 VA RNA I。
- 顶部 10 个簇中心之间的平均 RMSD 与真实误差相关，$R^2=0.84$，说明“收敛度”可以作为模型可信度的近似。

### Limitations

- 当需要从头构建超过约 80 nt 时，独立运行很难收敛，构象采样成为明显瓶颈。
- 21 个问题中有 11 个出现非天然 decoy 能量低于近天然模型，说明能量函数排序仍不可靠。
- 配体结合位点和某些局部非经典模体仍依赖人工假设或 SWM；常规运行消耗数百 CPU 和大量模型。

## Open questions / Gaps

- [已有候选方向] 能否把协变或神经网络预测的残基接触直接纳入 FARFAR2 评分与约束？[[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] 是现成候选。
- [待验证] 如何自动判断一个区域该交给 FARFAR2 广泛片段采样，还是交给 SWM 做昂贵的逐核苷酸精修？
- [待验证] 配体、金属离子和多构象状态加入后，现有“最低能量 + 聚类”置信度估计是否仍然成立？

## Connections

- 延伸 :: [[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]] — 把原始局部片段组装更新为更自动化的全局折叠协议。
- 矛盾 :: [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]] — 在精细非经典局部模体上，SWM 的逐步采样显著优于传统 FARFAR；FARFAR2 的优势则是更大的搜索尺度。
- 支持 :: [[notes/03_RNA Structure Prediction/Using Rosetta for RNA homology modeling [NSPH62NF]|Rosetta homology modeling]] — 盲测中模板区域与 de novo 区域的混合建模验证了模板优先策略。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] — 论文讨论中明确指向的学习式接触约束路线。
- [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|Blind prediction / SWM]] — 了解 FARFAR2 在局部原子精度上的互补方法。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
