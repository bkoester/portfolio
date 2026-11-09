---
title: Optically-Selected Cluster Catalogs as a Precision Cosmology Tool
authors: Rozo, E.; Wechsler, R. H.; Koester, B. P.; Evrard, A. E.; McKay, T. A.
year: 2007
venue: arXiv e-prints
doi:
url: https://arxiv.org/abs/astro-ph/0703574
open_access: true
first_author: false
author_position: 3 of 5
projects: []
source_read: full text
status: drafted
---

# Turning cluster catalogs into cosmology measurements

Counting galaxy clusters by richness can pin down cosmology, but only if you model how the cluster finder picks
clusters out of the sky. This paper builds that model for maxBCG and tests it on simulated skies.

## Question

How do you link clusters found in optical imaging to the dark-matter halos theory predicts, carefully enough to
get precise cosmological constraints?

## Data

- Three mock galaxy catalogs (A, B, C) built on the Hubble Volume light-cone simulation, each with a different
  galaxy-population scheme [Sec. I, III.1]
- The maxBCG cluster finder run on those mocks [Sec. III.2]
- Nine logarithmic richness bins from N_obs = 10 to 100 for the cosmology test [Sec. IV.2]

## Approach

- Split the selection into two parts: how many galaxies a halo of a given mass holds (the halo occupation
  distribution), and how the finder's projection and detection effects distort that count [Abstract; Sec. II]
- Describe the finder through completeness, purity, a signal matrix and photo-z errors [Sec. II.3-II.5]
- Calibrate those pieces on the mocks by matching clusters to halos [Sec. III]
- Fit cosmology and halo-occupation parameters with MCMC, with and without marginalizing over the selection
  parameters [Sec. IV]

## Findings

- The matching cost function stays under 20% at all richnesses, implying purity and completeness above 80%
  [Sec. III.3, Fig. 1]
- The slope of the observed-to-true richness relation is robust across mocks at 1.18 ± 5% [Sec. III.6, Fig. 5]
- Photo-z bias of 1.00, 1.02 and 1.03, with scatter 0.04, 0.03 and 0.05, for mocks A, B and C [Sec. III.8]
- With a known selection function, the two best-constrained parameter combinations come out at about 1% and 4%
  [Sec. IV.2, Fig. 10]
- Percent-level accuracy holds if the selection function is known to about 15%; at 20% the top mode is still
  better than 5% [Abstract; Sec. IV.3, Fig. 11]

## Why it matters

Optical cluster catalogs had a reputation for being riddled with systematics; the authors argue they can deliver
precision cosmology once the selection function is calibrated well.

## My role

Not stated in the paper (author 3 of 5). Ben to fill in.

## Cite

Rozo, E., Wechsler, R. H., Koester, B. P., Evrard, A. E., & McKay, T. A. (2007). Optically-Selected Cluster
Catalogs as a Precision Cosmology Tool. arXiv e-prints. arXiv:astro-ph/0703574
