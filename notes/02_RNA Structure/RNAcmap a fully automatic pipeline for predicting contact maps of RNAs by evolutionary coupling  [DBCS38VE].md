---
title: "RNAcmap: a fully automatic pipeline for predicting contact maps of RNAs by evolutionary coupling analysis"
created: "2022-11-30"
updated: "2022-11-30"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure"
author: "Tongchuan Zhang"
authors:
  - "Tongchuan Zhang"
  - "Jaswinder Singh"
  - "Thomas Litfin"
  - "Jian Zhan"
  - "Kuldip Paliwal"
  - "Yaoqi Zhou"
zotero_key: "DBCS38VE"
item_type: "journalArticle"
publication_date: "2021-10-15 2021-10-15"
doi: "10.1093/bioinformatics/btab391"
url: "https://doi.org/10.1093/bioinformatics/btab391"
collections:
  - "02_RNA Structure"
zotero_tags:
has_pdf: true
has_abstract: true
status: "unread"
---
# RNAcmap: a fully automatic pipeline for predicting contact maps of RNAs by evolutionary coupling analysis

## Source

- Zotero: [Open item](zotero://select/library/items/DBCS38VE)
- DOI: [10.1093/bioinformatics/btab391](https://doi.org/10.1093%2Fbioinformatics%2Fbtab391)
- Source: [Open source](https://doi.org/10.1093/bioinformatics/btab391)
- PDF attached: yes

## Authors

Tongchuan Zhang; Jaswinder Singh; Thomas Litfin; Jian Zhan; Kuldip Paliwal; Yaoqi Zhou

## Abstract

The accuracy of RNA secondary and tertiary structure prediction can be significantly improved by using structural restraints derived from evolutionary coupling or direct coupling analysis. Currently, these coupling analyses relied on manually curated multiple sequence alignments collected in the Rfam database, which contains 3016 families. By comparison, millions of non-coding RNA sequences are known. Here, we established RNAcmap, a fully automatic pipeline that enables evolutionary coupling analysis for any RNA sequences. The homology search was based on the covariance model built by INFERNAL according to two secondary structure predictors: a folding-based algorithm RNAfold and the latest deep-learning method SPOT-RNA.We showed that the performance of RNAcmap is less dependent on the specific evolutionary coupling tool but is more dependent on the accuracy of secondary structure predictor with the best performance given by RNAcmap (SPOT-RNA). The performance of RNAcmap (SPOT-RNA) is comparable to that based on Rfam-supplied alignment and consistent for those sequences that are not in Rfam collections. Further improvement can be made with a simple meta predictor RNAcmap (SPOT-RNA/RNAfold) depending on which secondary structure predictor can find more homologous sequences. Reliable base-pairing information generated from RNAcmap, for RNAs with high effective homologous sequences, in particular, will be useful for aiding RNA structure prediction.RNAcmap is available as a web server at https://sparks-lab.org/server/rnacmap/ and as a standalone application along with the datasets at https://github.com/sparks-lab-org/RNAcmap_standalone. A platform independent and fully configured docker image of RNAcmap is also provided at https://hub.docker.com/r/jaswindersingh2/rnacmap.Supplementary data are available at Bioinformatics online.

## Reading notes

_尚未精读。_

## Collections

- [[notes/02_RNA Structure/MOC - 02_RNA Structure|02_RNA Structure]]
