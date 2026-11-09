---
title: redMaPPer. I. Algorithm and SDSS DR8 Catalog
authors: Rykoff, E. S.; Rozo, E.; Busha, M. T.; Cunha, C. E.; Finoguenov, A.; Evrard, A.; and 9 others
year: 2014
venue: The Astrophysical Journal
doi: 10.1088/0004-637x/785/2/104
url: https://doi.org/10.1088/0004-637x/785/2/104
open_access: true
first_author: false
author_position: 8 of 15
projects: []
source_read: full text
status: drafted
---

# redMaPPer: a cluster finder for big surveys

A new red-sequence cluster finder, built to train itself and to scale to surveys like DES and LSST, is run on
SDSS to produce a catalog of about 25,000 galaxy clusters with precise distances.

## Question

Can a cluster finder be built that calibrates itself, handles complex survey masks, gives full redshift and
centering probabilities, and keeps richness scatter at fixed mass low?

## Data

- SDSS DR8 photometry: an input footprint of 10,400 deg² and 56.5 million galaxies with i < 21.0 [Sec. II.1]
- SDSS DR9 spectroscopy, over 1.3 million spectra, about 20% used for training [Sec. II.2]

## Approach

- Alternate between calibrating the red sequence and finding clusters, iterating before a final run [Sec. III]
- Estimate richness from multi-color membership probabilities, counting galaxies down to 0.2 L* [Sec. IV]
- Compute cluster photometric redshifts and probabilistic central-galaxy assignments [Sec. VII-VIII]

## Findings

- About 25,000 clusters at 0.08 < z < 0.55 from about 10,000 deg² [Abstract]
- Redshift scatter about 0.006 at z ≈ 0.1, rising to about 0.02 at z ≈ 0.5 [Abstract]
- Median |Δz|/(1+z) of 0.006 for the full sample [Abstract]
- Projection effects at or below 5% [Abstract]
- A DES-like catalog takes about 500 CPU hours [Abstract]

## Why it matters

The authors designed it for current and upcoming photometric surveys (DES, LSST, HSC, Pan-STARRS), where cluster
counts are a cosmological probe.

## My role

Not stated in the paper (author 8 of 15). Ben to fill in.

## Cite

Rykoff, E. S., Rozo, E., Busha, M. T., et al. (2014). redMaPPer. I. Algorithm and SDSS DR8 Catalog. The
Astrophysical Journal, 785, 104. doi:10.1088/0004-637x/785/2/104
