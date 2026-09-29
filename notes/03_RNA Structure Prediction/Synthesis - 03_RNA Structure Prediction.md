---
title: "Synthesis - 03_RNA Structure Prediction"
type: "synthesis"
topic: "03_RNA Structure Prediction"
created: "2026-08-03"
updated: "2026-08-03"
last_synthesized: "2026-08-03"
source_reference_count: 7
status: "current"
tags:
  - "synthesis"
  - "domain/rna-structure-prediction"
author: "Jason"
---
# 综合笔记：RNA 三级结构预测

返回 [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction MOC]] · 查看 [[00_Home/Idea Backlog|空白清单]]。

## Scope

本轮综合基于 7 篇已精读文献，覆盖原子级片段组装、粗粒化全局搜索、逐步 Monte Carlo、同源建模、学习式距离约束和接触评价。它不是对 22 篇馆藏的最终综述，而是一个可检验的第一版研究地图。

## Current consensus

1. **RNA 三级结构预测不是单一模型问题，而是约束、采样、评分三者的联合问题。** 二级结构、同源模板、协变接触或实验信息都会显著缩小搜索空间；完全从裸序列预测大 RNA 仍不稳定。
2. **全局拓扑与局部原子精度需要不同尺度的方法。** SimRNA 和 FARFAR2 更适合探索全局折叠；SWM 对困难非经典模体更精确但成本过高；实用路线应是分层组合。
3. **能量最低不等于最接近真实结构。** FARFAR2 和 SWM 都发现错误 decoy 可能获得更低能量；模型收敛度、接触恢复和外部约束必须共同用于置信度判断。
4. **模板仍是最高价值的信息源之一。** 当可信同源结构存在时，模板区 + 局部 de novo 通常比整条 RNA 从头折叠更准确；关键风险是错误模板和结构创新。
5. **评价不能只看 RMSD。** 非经典配对、堆叠和局部接触决定功能；ClaRNA 一类接触分类与 RMSD 应并列报告。

## Method map

- [[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]]：建立“片段组装 + 全原子精修”的原子级基线。
- [[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]]：以五伪原子表示扩大采样范围，并自然接收结构约束。
- [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]]：用可逆增删移动提升非经典局部模体的盲测精度。
- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]]：自动化 Rosetta 全局折叠流程，并用 RNA-Puzzles 系统量化瓶颈。
- [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]]：把 MSA 协变和二级结构转换为可供折叠器使用的长程距离约束。
- [[notes/03_RNA Structure Prediction/Using Rosetta for RNA homology modeling [NSPH62NF]|Rosetta homology modeling]]：给出模板选择、线程化、缺口重建与收敛检查的完整工作流。
- [[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]]：把模型评价从单一 RMSD 扩展到可解释的接触类型。

## Tensions and contradictions

- **片段组装 vs. 逐步采样**：FARFAR2 可处理更大尺度，但 SWM 在严格的非经典局部模体基准上显著更准；不存在一个方法在全部尺度占优。
- **粗粒化覆盖 vs. 原子级可信度**：SimRNA 能发现折叠路径和假结，但统计势与五点表示限制了稀有非经典接触的精度。
- **模板优先 vs. 结构创新**：同源建模在可靠模板下非常强，但假结、配体诱导变化和新拓扑会让序列同源产生误导。
- **距离约束 vs. 物理接触**：RNAcontact 的 8 Å 接近关系适合提供搜索约束，却不能直接解释为 ClaRNA 的具体相互作用类别。

## Open gaps

- 如何自动构建“全局搜索 → 低置信度定位 → SWM 局部精修”的多尺度调度器？
- 如何在浅 MSA 或人工设计序列上生成可靠长程约束？
- 如何把金属离子、配体、水和多构象状态纳入可扩展能量函数？
- 如何建立独立、可复现的 RNA 接触金标准与模型置信度校准？
- 如何对模板片段逐段给出可信度，并识别结构创新导致的模板失效？

## Next research direction

优先做一个小型、可复现实验：在同一组 RNA-Puzzles 目标上，把 RNAcontact 的 top-$L$ 约束分别加入 SimRNA 与 FARFAR2；用全局 RMSD、ClaRNA 接触恢复和 top-model 收敛度三轴评价。若某些局部区域接触冲突高且模型不收敛，再只对这些区域运行 SWM。这个实验能同时检验“学习式约束是否有效”和“多尺度自动路由是否值得继续”。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/Improved RNA homology detection and alignment by automatic iterative search in an expanded datab [YJ7ACSQ4]|Improved RNA homology detection and alignment]] — 补上远缘模板发现。
- [[notes/04_RNA Structure Assessment/RNA-Puzzles A CASP-like evaluation of RNA three-dimensional structure prediction [BYDKXBBT]|RNA-Puzzles]] — 补上跨方法的盲测框架。
- [[notes/04_RNA Structure Assessment/Geometric deep learning of RNA structure Science [Z6YXGQZJ]|Geometric deep learning of RNA structure]] — 追踪端到端几何学习的新路线。

## Synthesis trigger

当本主题新增 **5 篇已精读文献**，或本综合笔记距离最近一次更新超过 **30 天** 时，重新综合一次。
