---
title: Robust Optical Richness Estimation with Reduced Scatter
authors: Rykoff, E. S.; Koester, B. P.; Rozo, E.; Annis, J.; Evrard, A. E.; Hansen, S. M.; and 4 others
year: 2012
venue: The Astrophysical Journal
doi: 10.1088/0004-637x/746/2/178
url: https://doi.org/10.1088/0004-637x/746/2/178
open_access: true
first_author: false
author_position: 2 of 10
projects: []
source_read: full text
status: drafted
---

# A better way to count cluster galaxies

The paper tunes a matched-filter richness estimator, lambda, so that richness predicts cluster mass with less
scatter, tests that it holds up, and releases code plus an augmented maxBCG catalog.

## Question

Which choices in an optical richness estimator minimize the scatter between richness and cluster mass?

## Data

- SDSS DR7 imaging, about 10,000 square degrees; maxBCG area about 7,500 square degrees [Sec. 2]
- maxBCG catalog of 13,823 clusters at 0.1 to 0.3; analysis uses the top 2,000 [Sec. 2]
- ROSAT All-Sky Survey X-ray luminosities as the mass proxy [Abstract, Sec. 2]

## Approach

- Count galaxies with radial, luminosity and color filters and a background term [Sec. 3]
- Judge each variant by scatter in ln L_X at fixed richness, compared by bootstrap [Sec. 4.1]
- Vary luminosity cut, aperture, blue galaxies and luminosity weighting [Sec. 4]
- Robustness tests and Monte Carlo runs to explain the optimal cuts [Sec. 5, 6]

## Findings

- Scatter of 0.63 ± 0.02 in ln L_X at fixed lambda, versus 0.86 ± 0.02 for maxBCG N200 [Abstract, Sec. 1, Sec. 4.7]
- Implied mass scatter at fixed richness of about 0.2-0.3 [Abstract]
- Best luminosity cut is 0.2 L*; best aperture R0 = 1.0 Mpc/h with beta = 0.2 [Sec. 4.4, 4.7, Figs. 2-3]
- Adding blue galaxies or weighting by luminosity increases scatter [Sec. 4.2, 4.6]
- Robust to filters straddling the 4000 Angstrom break and to 50% background uncertainty [Abstract, Sec. 5]

## Why it matters

The authors expect residual scatter is dominated by miscentering, so better centering could cut it further.

## My role

Not stated in the paper (author 2 of 10). Ben to fill in.

## Cite

Rykoff, E. S., Koester, B. P., Rozo, E., et al. (2012). Robust Optical Richness Estimation with Reduced Scatter.
The Astrophysical Journal. doi:10.1088/0004-637x/746/2/178
