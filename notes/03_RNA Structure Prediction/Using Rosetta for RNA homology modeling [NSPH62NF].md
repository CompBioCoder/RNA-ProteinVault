---
title: "Using Rosetta for RNA homology modeling"
created: "2022-11-09"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Andrew M. Watkins"
authors:
  - "Andrew M. Watkins"
  - "Ramya Rangan"
  - "Rhiju Das"
zotero_key: "NSPH62NF"
item_type: "journalArticle"
publication_date: "2019-00-00 2019"
doi: "10.1016/bs.mie.2019.05.026"
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7932369/"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# Using Rosetta for RNA homology modeling

## Source

- Zotero: [Open item](zotero://select/library/items/NSPH62NF)
- DOI: [10.1016/bs.mie.2019.05.026](https://doi.org/10.1016%2Fbs.mie.2019.05.026)
- Source: [Open source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7932369/)
- PDF attached: yes

## Authors

Andrew M. Watkins; Ramya Rangan; Rhiju Das

## Abstract

The three-dimensional structures of RNA molecules provide rich and often critical information for understanding their functions, including how they recognize small molecule and protein partners. Computational modeling of RNA 3D structure is becoming increasingly accurate, particularly with the availability of growing numbers of template structures already solved experimentally and the development of sequence alignment and 3D modeling tools to take advantage of this database. For several recent “RNA puzzle” blind modeling challenges, we have successfully identified useful template structures and achieved accurate structure predictions through homology modeling tools developed in the Rosetta software suite. We describe our semi-automated methodology here and walk through two illustrative examples: an adenine riboswitch aptamer, modeled from a template guanine riboswitch structure, and a SAM I/IV riboswitch aptamer, modeled from a template SAM I riboswitch structure.

## Reading notes

### Research question

当目标 RNA 只有部分区域能找到可靠模板时，如何系统选择、清理和线程化模板，再用 FARFAR 或 SWM 重建差异区域，并估计最终模型是否可信？

### Method

- 工作流包括：寻找同源结构、ERRASER–Phenix 清理模板、确定目标二级结构、选择可信模板片段、把目标序列线程化到模板、用 FARFAR/SWM 重建缺口、按能量与模型收敛度选择结果。
- 以鸟嘌呤核糖开关为模板重建腺嘌呤核糖开关；再以 SAM-I 的配体结合核心跨家族重建 SAM-I/IV 核糖开关。
- 用 top 模型之间的 mutual RMSD 作为采样收敛和预期准确度的实用指标。

### Evidence

- 腺嘌呤核糖开关的 top 10 模型 mutual RMSD 小于 0.5 Å；相对未知于建模过程的晶体结构，最终模型约为 1.4 Å RMSD。
- SAM-I/IV 的大范围差异区域需要 de novo 重建；在约 6,000 CPU-hour 条件下，FARFAR 与 SWM 均恢复正确全局折叠，top 5 低能模型中的最佳 RMSD 小于 5 Å。
- 既往 RNA-Puzzles 的 GIR1、AdoCbl、谷氨酰胺、Zika xrRNA 和 SAM-I/IV 案例证明，远缘模板也能带来可验证的结构收益。

### Limitations

- 模板选择、家族比对和保留区域判断仍高度依赖专家；错误模板可能把整个全局折叠锁定在错误拓扑。
- 当模板只覆盖小部分目标时，需要约 100 CPU 的计算集群；非常大或同源关系不清的 RNA 仍不可达。
- 常用二级结构工具对假结支持不足，序列相似并不保证非螺旋区域保留相同构象。

## Open questions / Gaps

- [待验证] 能否自动输出“模板片段可信度 + de novo 缺口风险”，而不是只给一个最终模型？
- [已有候选方向] 用更强的同源检测与协变模型自动发现远缘 RNA 模板，减少人工文献检索。
- [待验证] 如何在模板与目标可能存在构象切换、配体诱导或新假结时，自动拒绝错误模板拓扑？

## Connections

- 支持 :: [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 盲测表明“可靠模板 + 局部 de novo”通常优于整条 RNA 从头搜索。
- 延伸 :: [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]] — 把 SWM 从孤立模体预测嵌入真实同源模型的缺口重建。
- 矛盾 :: [[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]] — 当可靠模板存在时，模板优先往往以更小搜索空间获得更高精度；但它无法覆盖无同源或发生拓扑创新的目标。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/Improved RNA homology detection and alignment by automatic iterative search in an expanded datab [YJ7ACSQ4]|Improved RNA homology detection and alignment]] — 直接针对模板发现这一步的自动化瓶颈。
- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 了解当前模板区与新建区如何被统一处理。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
