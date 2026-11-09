---
title: "MaxBCG: A Red-Sequence Galaxy Cluster Finder"
authors: Koester, B. P.; McKay, T. A.; Annis, J.; Wechsler, R. H.; Evrard, A. E.; Rozo, E.; Bleem, L.; Sheldon, E. S.; Johnston, D.
year: 2007
venue: The Astrophysical Journal
doi: 10.1086/512092
url: https://doi.org/10.1086/512092
open_access: true
first_author: true
projects: [maxbcg]
source_read: full text
status: drafted
---

# The MaxBCG cluster-finding algorithm

An algorithm that finds galaxy clusters in multi-band survey imaging by looking for a bright central galaxy
surrounded by red-sequence galaxies, tested against simulations to measure exactly how often it's right.

## Question

Can an algorithm reliably find galaxy clusters, down to small groups, in large imaging surveys, with errors
well enough understood for cosmology?

## Data

- SDSS imaging and spectroscopy, with the color model calibrated on known nearby clusters
- Three simulated galaxy catalogs built on dark-matter halos; shuffled catalogs and 15,000 artificially inserted
  clusters for false-positive and completeness tests

## Approach

- Gaussian color filters for the red sequence, a spatial filter, and a likelihood for the brightest cluster
  galaxy, combined into one score
- Richness as the count of red members, then percolation from the most to least likely candidates
- Matched recovered clusters to simulated halos to measure completeness, purity, splitting and merging

## Findings

- More than 90% pure for clusters with 10 or more red galaxies, and more than 90% complete for halos above
  2×10^14 h^-1 solar masses, at redshifts 0.1 to 0.3 [Abstract; Sec. IV.1]
- Photometric redshift errors below 0.015 [Sec. II.3.2]
- In shuffled catalogs, false detections were 7% at the lowest richness cut, falling below 1% for richer clusters
  [Sec. IV]
- Rarely splits clusters; sometimes merges neighbors along the line of sight [Sec. IV.2–IV.3]

## Why it matters

It produced the large, uniformly selected cluster samples cosmology needs, and was applied to SDSS to build the
13,823-cluster catalog in the companion paper.

## My role

First author. The paper is adapted into Chapter 3 of Ben's PhD thesis
([thesis](astro/2006-maxbcg-systematic-discovery-characterization.md)).

## Cite

Koester, B. P., et al. (2007). MaxBCG: A Red-Sequence Galaxy Cluster Finder. The Astrophysical Journal.
doi:10.1086/512092
