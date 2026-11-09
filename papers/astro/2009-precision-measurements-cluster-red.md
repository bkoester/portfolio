---
title: Precision Measurements of the Cluster Red Sequence Using an Error-Corrected Gaussian Mixture Model
authors: Hao, J.; Koester, B. P.; McKay, T. A.; Rykoff, E. S.; Rozo, E.; Evrard, A.; and 7 others
year: 2009
venue: The Astrophysical Journal
doi: 10.1088/0004-637x/702/1/745
url: https://doi.org/10.1088/0004-637x/702/1/745
open_access: true
first_author: false
author_position: 2 of 13
projects: []
source_read: full text
status: drafted
---

# Measuring the red sequence without error bias

A statistical method that accounts for each galaxy's measurement error separates a cluster's red galaxies from
the background, and shows ordinary methods overstate how much the red sequence spreads at higher redshift.

## Question

How do measurement errors bias the measured width and slope of the cluster red sequence, and can a corrected
mixture model remove that bias?

## Data

- 13,823 clusters from the maxBCG catalog, at 0.1 ≤ z ≤ 0.3 [Abstract; Sec. I]
- SDSS imaging over about 7500 deg², plus SDSS DR6 spectroscopy [Sec. III]
- About 7100 clusters remain after richness and fitting cuts [Sec. IV]

## Approach

- Fit g−r colors with a Gaussian mixture that includes per-galaxy errors (ECGMM), using
  expectation-maximization, choosing components by BIC [Sec. II; App. A]
- Bootstrap resampling (50 resamples) for uncertainties [Sec. II.3]
- Monte Carlo tests, 200 runs per richness, showed recovery for clusters with at least 10 galaxies [Sec. II.4]
- Fit per-cluster slopes and compared with a spectroscopic sample [Sec. V]

## Findings

- Ordinary mixture fits show width growing nearly 140% by z = 0.3; ECGMM gives 0.051 ± 0.003 at z = 0.1 and
  0.079 ± 0.005 at z = 0.3, about 55% [Sec. IV; Fig. 7]
- Mean slope steepens by a factor of 2.5 by z = 0.3 [Sec. V.1; Fig. 9]
- Slope at z ≈ 0.1 is −0.013 ± 0.0003 mag per mag, shallower than the −0.022 of Hogg et al. (2004) [Sec. VI]
- Slope shows little dependence on richness [Sec. V.1; Fig. 10]
- Photometric and spectroscopic slopes do not differ significantly [Sec. V.2; Fig. 12]

## Why it matters

The red sequence underpins cluster finding; the authors offer ECGMM as a general tool and caution that the
trends may partly reflect uncorrected observational effects.

## My role

Not stated in the paper (author 2 of 13). Ben to fill in.

## Cite

Hao, J., Koester, B. P., et al. (2009). Precision Measurements of the Cluster Red Sequence Using an
Error-Corrected Gaussian Mixture Model. The Astrophysical Journal. doi:10.1088/0004-637x/702/1/745;
arXiv:0907.4383
