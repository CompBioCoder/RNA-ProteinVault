---
title: "RNA inter-nucleotide 3D closeness prediction by deep residual neural networks"
created: "2022-10-28"
updated: "2022-10-28"
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
status: "unread"
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

_尚未精读。_

## Collections

- [[notes/03_RNA Structure Prediction/MOC - 03_RNA Structure Prediction|03_RNA Structure Prediction]]
