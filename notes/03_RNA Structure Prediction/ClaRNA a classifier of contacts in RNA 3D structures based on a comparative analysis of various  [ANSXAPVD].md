---
title: "ClaRNA: a classifier of contacts in RNA 3D structures based on a comparative analysis of various classification schemes"
created: "2022-09-07"
updated: "2026-08-03"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure-prediction"
author: "Tomasz Waleń"
authors:
  - "Tomasz Waleń"
  - "Grzegorz Chojnowski"
  - "Przemysław Gierski"
  - "Janusz M. Bujnicki"
zotero_key: "ANSXAPVD"
item_type: "journalArticle"
publication_date: "2014-10-29 2014-10-29"
doi: "10.1093/nar/gku765"
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4231730/"
collections:
  - "03_RNA Structure Prediction"
zotero_tags:
has_pdf: true
has_abstract: true
status: "read"
---
# ClaRNA: a classifier of contacts in RNA 3D structures based on a comparative analysis of various classification schemes

## Source

- Zotero: [Open item](zotero://select/library/items/ANSXAPVD)
- DOI: [10.1093/nar/gku765](https://doi.org/10.1093%2Fnar%2Fgku765)
- Source: [Open source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4231730/)
- PDF attached: yes

## Authors

Tomasz Waleń; Grzegorz Chojnowski; Przemysław Gierski; Janusz M. Bujnicki

## Abstract

The understanding of folding and function of RNA molecules depends on the identification and classification of interactions between ribonucleotide residues. We developed a new method named ClaRNA for computational classification of contacts in RNA 3D structures. Unique features of the program are the ability to identify imperfect contacts and to process coarse-grained models. Each doublet of spatially close ribonucleotide residues in a query structure is compared to clusters of reference doublets obtained by analysis of a large number of experimentally determined RNA structures, and assigned a score that describes its similarity to one or more known types of contacts, including pairing, stacking, base–phosphate and base–ribose interactions. The accuracy of ClaRNA is 0.997 for canonical base pairs, 0.983 for non-canonical pairs and 0.961 for stacking interactions. The generalized squared correlation coefficient (GC2) for ClaRNA is 0.969 for canonical base pairs, 0.638 for non-canonical pairs and 0.824 for stacking interactions. The classifier can be easily extended to include new types of spatial relationships between pairs or larger assemblies of nucleotide residues. ClaRNA is freely available via a web server that includes an extensive set of tools for processing and visualizing structural information about RNA molecules.

## Reading notes

### Research question

能否建立一个对低分辨率、粗粒化和轻度扭曲模型仍稳健的 RNA 接触分类器，同时给出“近似匹配”的连续分数，而不是只做有/无接触判断？

### Method

- 以 RNAView、MC-Annotate、FR3D 和 ModeRNA 的共识加人工校正构建参考双核苷酸集合。
- 对 PDB 中空间接近的核苷酸双体做几何匹配，分类碱基配对、堆叠、碱基–磷酸和碱基–核糖相互作用，并输出 0–1 相似分数。
- 算法先修复缺失/非平面碱基，再用 KD-tree 找近邻，最后与每个接触类别的代表几何比较；另在 SimRNA 粗粒化表示上测试。

### Evidence

- 全原子测试中，经典配对、非经典配对和堆叠的准确率分别约 0.997、0.983 和 0.962。
- 在 SimRNA 粗粒化表示上，经典/非经典配对与堆叠准确率仍约 0.997、0.980 和 0.961，说明其对降分辨率模型较稳健。
- 连续相似分数能把轻微扭曲的 near match 与完全不匹配区分开，适合模型检查和精修反馈。

### Limitations

- 训练真值来自其他分类器的共识，存在循环验证；碱基–磷酸和碱基–核糖类别尤其依赖 FR3D 单一来源。
- 几何相似并不直接证明真实氢键、溶剂或离子介导作用，罕见新型接触仍可能被现有类别漏掉。
- 在粗粒化输入上，碱基–核糖和碱基–磷酸的相关性明显下降，不能把所有接触类型视为同等可靠。

## Open questions / Gaps

- [待验证] 如何用独立实验或高分辨率量化计算建立不依赖现有分类器共识的接触金标准？
- [已有候选方向] 能否把 ClaRNA 的接触类型作为深度模型训练目标，使 RNAcontact 不只预测“8 Å 内”，还预测方向和相互作用类别？
- [待验证] 新型配体、金属和蛋白介导接触应如何扩展到同一套可比较的分类体系？

## Connections

- 支持 :: [[notes/03_RNA Structure Prediction/SimRNA a coarse-grained method for RNA folding simulations and 3D structure prediction [EPFWC7C2]|SimRNA]] — 在五伪原子表示上仍能稳定识别主要接触，可作为粗粒化轨迹的解释层。
- 延伸 :: [[notes/03_RNA Structure Prediction/Atomic accuracy in predicting and designing non-canonical RNA structure [WPJDGFPF]|FARFAR]] — 把“是否接近实验结构”拆成可解释的非经典配对、堆叠等局部指标。
- 矛盾 :: [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] — 8 Å 距离阈值包含大量不属于明确物理接触的核苷酸对，不能直接当作 ClaRNA 接触标签。

## Suggested next reading

- [[notes/03_RNA Structure Prediction/Geometric nomenclature and classification of RNA base pairs [XB9S8JAM]|Geometric nomenclature and classification of RNA base pairs]] — 补足 ClaRNA 分类体系的几何基础。
- [[notes/03_RNA Structure Prediction/RNA inter-nucleotide 3D closeness prediction by deep residual neural networks [M5Z4FRJF]|RNAcontact]] — 比较“距离接近”与“接触类型”两种学习目标。

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
