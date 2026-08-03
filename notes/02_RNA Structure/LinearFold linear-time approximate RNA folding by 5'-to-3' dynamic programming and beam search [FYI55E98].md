---
title: "LinearFold: linear-time approximate RNA folding by 5'-to-3' dynamic programming and beam search"
created: "2022-08-09"
updated: "2022-08-09"
tags:
  - "literature"
  - "zotero"
  - "domain/rna-structure"
author: "Liang Huang"
authors:
  - "Liang Huang"
  - "He Zhang"
  - "Dezhong Deng"
  - "Kai Zhao"
  - "Kaibo Liu"
  - "David A Hendrix"
  - "David H Mathews"
zotero_key: "FYI55E98"
item_type: "journalArticle"
publication_date: "2019-07-00 2019-7"
doi: "10.1093/bioinformatics/btz375"
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6681470/"
collections:
  - "02_RNA Structure"
zotero_tags:
has_pdf: true
has_abstract: true
status: "unread"
---
# LinearFold: linear-time approximate RNA folding by 5'-to-3' dynamic programming and beam search

## Source

- Zotero: [Open item](zotero://select/library/items/FYI55E98)
- DOI: [10.1093/bioinformatics/btz375](https://doi.org/10.1093%2Fbioinformatics%2Fbtz375)
- Source: [Open source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6681470/)
- PDF attached: yes

## Authors

Liang Huang; He Zhang; Dezhong Deng; Kai Zhao; Kaibo Liu; David A Hendrix; David H Mathews

## Abstract

Motivation
Predicting the secondary structure of an ribonucleic acid (RNA) sequence is useful in many applications. Existing algorithms [based on dynamic programming] suffer from a major limitation: their runtimes scale cubically with the RNA length, and this slowness limits their use in genome-wide applications.

Results
We present a novel alternative O(n3)-time dynamic programming algorithm for RNA folding that is amenable to heuristics that make it run in O(n) time and O(n) space, while producing a high-quality approximation to the optimal solution. Inspired by incremental parsing for context-free grammars in computational linguistics, our alternative dynamic programming algorithm scans the sequence in a left-to-right (5′-to-3′) direction rather than in a bottom-up fashion, which allows us to employ the effective beam pruning heuristic. Our work, though inexact, is the first RNA folding algorithm to achieve linear runtime (and linear space) without imposing constraints on the output structure. Surprisingly, our approximate search results in even higher overall accuracy on a diverse database of sequences with known structures. More interestingly, it leads to significantly more accurate predictions on the longest sequence families in that database (16S and 23S Ribosomal RNAs), as well as improved accuracies for long-range base pairs (500+ nucleotides apart), both of which are well known to be challenging for the current models.

Availability and implementation
Our source code is available at https://github.com/LinearFold/LinearFold, and our webserver is at http://linearfold.org (sequence limit: 100 000nt).

Supplementary information

 are available at Bioinformatics online.

## Reading notes

_尚未精读。_

## Collections

- [[notes/02_RNA Structure/MOC - 02_RNA Structure|02_RNA Structure]]
