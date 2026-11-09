---
title: Improvement of the Richness Estimates of maxBCG Clusters
authors: Rozo, E.; Rykoff, E. S.; Koester, B. P.; McKay, T.; Hao, J.; Evrard, A.; and 8 others
year: 2009
venue: The Astrophysical Journal
doi: 10.1088/0004-637x/703/1/601
url: https://doi.org/10.1088/0004-637x/703/1/601
open_access: true
first_author: false
author_position: 3 of 14
projects: []
source_read: full text
status: drafted
---

# A better galaxy count for cluster mass

A new way of counting a cluster's member galaxies (its richness) tracks X-ray brightness, and so mass, more
closely than the original maxBCG count. Better richness means tighter mass estimates for cluster cosmology.

## Question

Can a matched-filter richness estimator, with an aperture tuned to minimize scatter, reduce the spread in
X-ray luminosity at fixed richness for maxBCG clusters?

## Data

- maxBCG catalog: 13,823 clusters with N200 ≥ 10 at 0.1 ≤ z ≤ 0.3. The analysis uses the 2,000 richest clusters
  by the new measure, plus a "clean" subsample [Sec. 2.2, 2.4]
- SDSS imaging for the galaxy catalogs, in an area close to the DR4 footprint [Sec. 2.1]
- ROSAT All-Sky Survey X-ray luminosities [Sec. 2.3]

## Approach

- Built a richness estimator, λ, that weights galaxies by distance from the center, brightness and red-sequence
  color [Sec. 3]
- Let the counting radius grow with richness, and searched for the radius parameters that minimize scatter in
  ln L_X at fixed richness [Sec. 4, Eq. 3]
- Checked significance with bootstrap resampling [Sec. 4; Sec. 5.3]

## Findings

- For the clean sample, scatter in ln L_X at fixed richness fell from 0.86 ± 0.02 to 0.69 ± 0.02 [Abstract;
  Table 1]
- The improvement is significant at 9σ for the full sample and 11σ for the clean one [Sec. 5.3]
- Best aperture: R0 = 1.27 h^-1 Mpc with slope α = 1/3 [Sec. 5.2]
- Implied mass scatter at fixed richness is about 0.43 for λ, against 0.54 for N200 [Sec. 7]
- The new richness shows no sign of redshift evolution: γ = 0.7 ± 0.8, versus 6.0 ± 0.8 for N200 [Sec. 6;
  Table 2]

## Why it matters

The authors say lower mass–observable scatter is a key goal for cluster cosmology. They credit the improvement
mainly to better handling of galaxy color, and note that the aperture-tuning method works for any mass tracer.

## My role

Not stated in the paper (author 3 of 14). Ben to fill in.

## Cite

Rozo, E., et al. (2009). Improvement of the Richness Estimates of maxBCG Clusters. The Astrophysical Journal.
doi:10.1088/0004-637x/703/1/601
