---
title: Long-Range Autocorrelations of CpG Islands in the Human Genome
authors: Koester, B.; Rea, T. J.; Templeton, A. R.; Szalay, A. S.; Sing, C. F.
year: 2012
venue: PLoS ONE
doi: 10.1371/journal.pone.0029889
url: https://doi.org/10.1371/journal.pone.0029889
open_access: true
first_author: true
author_position: 1 of 5
projects: []
source_read: full text
status: drafted
---

# Astronomy's clustering statistic applied to the genome

A tool astronomers use to measure how galaxies cluster was applied to CpG islands, short DNA stretches that often
mark gene promoters. Their placement along human chromosomes turns out to be far from random, with clustering
reaching millions of base pairs and differing strongly from one chromosome to the next.

## Question

Is the large-scale arrangement of CpG islands along human chromosomes non-random? If so, how far does the
clustering extend, and does it vary between chromosomes?

## Data

- Human reference sequence GRCh37, with all 22 autosomes plus X and Y [Results; Table 1]
- CpG islands found with the Takai and Jones (2002) algorithm, which is tuned for promoter regions and avoids Alu
  repeats. Per-chromosome counts run from 311 (Y) to 3,430 (chromosome 1) [Table 1]
- Two other island definitions for comparison: a hidden Markov model set (Irizarry et al.) and a CAP-seq set
  (Illingworth et al.) [Fig. 2; Text S2]

## Approach

- Measured the two-point correlation function with the Landy–Szalay estimator. It counts island pairs at each
  separation and compares them with random positions that respect sequence gaps and chromosome ends [Methods, Eq. 5]
- Used 15 logarithmic distance bins from 1,000 bp to 249 Mb, the same for every chromosome [Results]
- Estimated uncertainties from 250 bootstrap resamples. Fitted power laws at intermediate scales, with confidence
  bands from Monte Carlo realizations [Methods]

## Findings

- CpG islands cluster well above random expectation out to nearly 10 Mb [Results, Two-Point Statistics; Abstract]
- Clustering strength differs between chromosomes by 5-fold or more at separations of about 0.1 Mb or less
  [Discussion]
- Chromosome 4 is the most strongly clustered and chromosome 19 the least [Fig. 3]
- Some chromosomes are also clustered at scales close to their full length, which the authors attribute to dense
  islands near the telomeres [Results; Fig. 3]
- Average island density ranges from 9.0 to 55.9 per Mb across chromosomes, and the distributions are skewed
  [Table 1]

## Why it matters

The authors present this as a global, chromosome-level summary of how a functional sequence feature is
organized, which single-site measures of variation do not capture. They suggest uses in studying methylation and
in future genotype-phenotype studies.

## My role

Per the paper's author-contributions statement: B. Koester ran the experiments together with C. F. Sing, did
all of the data analysis, and co-wrote the paper with the other four authors.

## Cite

Koester, B., Rea, T. J., Templeton, A. R., Szalay, A. S., & Sing, C. F. (2012). Long-Range Autocorrelations of
CpG Islands in the Human Genome. PLoS ONE. doi:10.1371/journal.pone.0029889
