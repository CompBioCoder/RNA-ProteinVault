---
title: "RNA inter-nucleotide 3D closeness prediction by deep residual neural networks"
created: "2022-10-28"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Saisai Sun"
authors:
  - "Saisai Sun"
  - "Wenkai Wang"
  - "Zhenling Peng"
  - "Jianyi Yang"
zotero_key: "M5Z4FRJF"
item_type: "journalArticle"
publication_date: "2021-05-23 2021-05-23"
doi: "10.1093/bioinformatics/btaa932"
url: ""
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
  - "Algorithms"
  - "Computational Biology"
  - "Neural Networks, Computer"
  - "Nucleotides"
  - "RNA"
  - "Sequence Alignment"
has_pdf: true
has_abstract: true
status: "read"
---
# RNA inter-nucleotide 3D closeness prediction by deep residual neural networks

## Source

- Zotero: [Open item](zotero://select/library/items/M5Z4FRJF)
- DOI: [10.1093/bioinformatics/btaa932](https://doi.org/10.1093%2Fbioinformatics%2Fbtaa932)
- Source: not recorded
- PDF attached: yes

## Authors

Saisai Sun; Wenkai Wang; Zhenling Peng; Jianyi Yang

## Abstract

MOTIVATION: Recent years have witnessed that the inter-residue contact/distance in proteins could be accurately predicted by deep neural networks, which significantly improve the accuracy of predicted protein structure models. In contrast, fewer studies have been done for the prediction of RNA inter-nucleotide 3D closeness.
RESULTS: We proposed a new algorithm named RNAcontact for the prediction of RNA inter-nucleotide 3D closeness. RNAcontact was built based on the deep residual neural networks. The covariance information from multiple sequence alignments and the predicted secondary structure were used as the input features of the networks. Experiments show that RNAcontact achieves the respective precisions of 0.8 and 0.6 for the top L/10 and L (where L is the length of an RNA) predictions on an independent test set, significantly higher than other evolutionary coupling methods. Analysis shows that about 1/3 of the correctly predicted 3D closenesses are not base pairings of secondary structure, which are critical to the determination of RNA structure. In addition, we demonstrated that the predicted 3D closeness could be used as distance restraints to guide RNA structure folding by the 3dRNA package. More accurate models could be built by using the predicted 3D closeness than the models without using 3D closeness.
AVAILABILITY AND IMPLEMENTATION: The webserver and a standalone package are available at: http://yanglab.nankai.edu.cn/RNAcontact/.
SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.

## Reading notes

### Research question

能否像蛋白质接触预测一样，利用多序列比对协变和二级结构信息学习 RNA 核苷酸对的长程三维接近关系，并把预测真正转化为折叠约束？

### Method

- RNAcontact 以序列为输入，用 Infernal 构建 MSA、PETfold 预测二级结构，再把协变与二级结构编码成 26 个 $L\times L$ 特征图。
- 网络由 3 个二维卷积层、5 个残差块和输出概率矩阵组成；“三维接近”定义为任意重原子距离小于 8 Å。
- 在独立集合 TE80 等数据上与 PLMC/DIRECT 比较，并把预测的前 $L$ 个长程接近关系转成 3dRNA 的距离约束。

### Evidence

- TE80 上协变 + 二级结构的长程精度，在 top $L/10$、$L/5$、$L/2$ 和 $L$ 分别为 0.89、0.88、0.81 和 0.66，明显高于单独特征。
- 正确预测中约 27% 不是二级结构碱基对，说明模型确实补充了三级信息。
- 在 168 nt 的 4r4v_A 上，约束把模型改善到 16.7 Å RMSD，优于无约束模型及当时 RNA-Puzzles 的 20.4 Å；6ol3_C 从 16.8 Å 改善到 13.5 Å，6fyy_1 从 5.9 Å 改善到 4.6 Å。

### Limitations

- 模型依赖足够深且质量可靠的 MSA，也依赖 PETfold 的二级结构；低同源序列问题未被充分验证。
- 下游折叠只测试 3 个 RNA 和 3dRNA，如何选择约束数量、置信度与权重尚未系统优化。
- 距离接近并不等同于明确的碱基配对、堆叠或配体介导相互作用，模型的结构解释力有限。

## Open questions / Gaps

- [待验证] 把 RNAcontact 约束接入 FARFAR2 或 SimRNA，是否比接入 3dRNA 获得更稳定的全局拓扑和原子精度？
- [待验证] 在浅 MSA、孤立 ncRNA 或人工设计序列上，如何用语言模型/单序列特征替代协变而不显著降低精度？
- [已有候选方向] 能否把“距离接近”进一步分解成 ClaRNA 风格的接触类型和方向，从而生成更可解释的约束？

## Connections

- 支持 :: [[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]] — 两篇论文都显示长程约束对复杂 RNA 的全局折叠至关重要。
- 延伸 :: [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — FARFAR2 明确把协变/神经网络接触推断列为改善评分的方向，RNAcontact 给出可操作实现。
- 矛盾 :: [[notes/03_RNA Structure Prediction/ClaRNA a classifier of contacts in RNA 3D structures based on a comparative analysis of various  [ANSXAPVD]|ClaRNA]] — RNAcontact 的 8 Å 距离关系比物理接触分类更宽，两个标签体系不能直接互换。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/FARFAR2 Improved De Novo Rosetta Prediction of Complex Global RNA Folds [P8RQAIT6]|FARFAR2]] — 判断学习式约束最可能插入哪一阶段。
- [[notes/04_RNA Structure Assessment/Geometric deep learning of RNA structure Science [Z6YXGQZJ]|Geometric deep learning of RNA structure]] — 继续追踪从二维距离图到端到端三维建模的路线。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
