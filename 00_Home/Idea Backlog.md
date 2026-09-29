---
title: "Idea backlog"
created: "2026-08-03"
updated: "2026-08-03"
tags:
  - "research-gaps"
  - "idea-backlog"
author: "Jason"
---
# 空白清单 / Idea backlog

返回 [[00_Home/RNA-Protein Research Hub|Research Hub]]。

本页是当前已精读文献中 `## Open questions / Gaps` 的人工校对快照；Dashboard 会实时扫描所有文献笔记，因此新增问题不必手动登记才能显示。

状态含义：**待验证** = 尚无明确解法；**已有候选方向** = 已出现可测试路线；**已被后续文献回答** = 后续工作至少部分解决。

## 能量函数与物理真实性

- [待验证] 显式水、Mg²⁺ 与相关主链扭转势，能否在跨模体基准上稳定改善非经典接触排序？来源：[[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]]、[[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]]
- [待验证] 配体、金属离子和多构象状态存在时，“最低能量 + 聚类”是否仍可作为可靠置信度？来源：[[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]]
- [已有候选方向] 用高分辨率物理势重标定 SimRNA 的稀有非经典相互作用，同时保留粗粒化效率。来源：[[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]]

## 多尺度采样与自动路由

- [已有候选方向] 让 SimRNA/FARFAR2 负责全局拓扑，只对低置信度局部模体调用 SWM。来源：[[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]]、[[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]]
- [待验证] 如何自动判断区域应使用片段组装还是逐核苷酸精修，并把局部置信度传递到完整模型？来源：[[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]]、[[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]]
- [已被后续文献回答] 未知非经典模体的局部采样可以由 SWM 的可逆增删移动显著改善，但大 RNA 的计算扩展仍未解决。来源：[[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]] → [[notes/03_RNA Structure Prediction/Blind prediction of noncanonical RNA structure at atomic accuracy [7CU6NKZJ]|SWM]]

## 学习式约束

- [待验证] RNAcontact 约束接入 FARFAR2/SimRNA 是否比接入 3dRNA 更稳定？来源：[[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]]
- [待验证] 浅 MSA、人工设计 RNA 和孤立 ncRNA 如何获得可靠的单序列三级约束？来源：[[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]]
- [已有候选方向] 把 8 Å 距离预测细化成配对、堆叠和方向性接触类型。来源：[[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]]、[[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]]

## 模板、同源与置信度

- [已有候选方向] 用迭代同源检测和协变模型自动发现远缘 RNA 模板。来源：[[notes/03_RNA Structure Prediction/Using Rosetta for RNA homology modeling [NSPH62NF]|Rosetta homology modeling]]
- [待验证] 如何为每个模板片段输出可信度与 de novo 缺口风险，并在构象切换或新假结出现时拒绝错误模板？来源：[[notes/03_RNA Structure Prediction/Using Rosetta for RNA homology modeling [NSPH62NF]|Rosetta homology modeling]]

## 评价与可解释性

- [待验证] 如何建立不依赖现有分类器共识的 RNA 接触金标准？来源：[[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]]
- [待验证] 配体、金属和蛋白介导接触如何进入可扩展、可比较的接触分类体系？来源：[[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]]

## 本轮优先级

1. **先验证约束价值**：把 RNAcontact 的 top-$L$ 约束分别接入 SimRNA、FARFAR2，在同一 RNA-Puzzles 子集比较。
2. **再做自动路由**：用全局收敛度和局部接触冲突标出需要 SWM 精修的区域。
3. **最后补物理项**：只在路由后的困难模体上测试金属/水/扭转势，避免计算成本失控。
