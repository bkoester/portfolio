---
title: A MaxBCG Catalog of 13,823 Galaxy Clusters from the Sloan Digital Sky Survey
authors: Koester, B. P.; McKay, T. A.; Annis, J.; Wechsler, R. H.; Evrard, A. E.; and others
year: 2007
venue: The Astrophysical Journal
doi: 10.1086/509599
url: https://doi.org/10.1086/509599
open_access: true
first_author: true
projects: [maxbcg]
source_read: full text
status: drafted
---

# The MaxBCG catalog: 13,823 galaxy clusters

The largest galaxy-cluster catalog assembled at the time: 13,823 clusters found in Sloan Digital Sky Survey
imaging, with measured purity and completeness, released for others to use.

## Question

Can a large, uniformly selected catalog of galaxy clusters be built from survey imaging and characterized well
enough for cosmology?

## Data

- SDSS five-band imaging of about 23 million galaxies, plus spectroscopy of 567,486 galaxies
- 7,500 square degrees of sky, redshifts 0.1 to 0.3
- Simulated (mock) galaxy catalogs and X-ray cluster catalogs for testing

## Approach

- Ran the maxBCG finder, which scores galaxies on how likely they are to be a cluster's brightest galaxy sitting
  in an overdensity of red-sequence galaxies
- Measured richness, assembled clusters by percolation, and measured purity and completeness on mock catalogs
- Checked redshifts, velocity dispersions and space density against spectroscopy and X-ray catalogs

## Findings

- 13,823 clusters holding 213,016 member galaxies; 5,413 have a spectroscopic redshift for the central galaxy
  [Sec. I, IV]
- More than 90% pure and more than 85% complete for clusters of at least 10^14 solar masses [Abstract]
- Photometric redshift scatter of about 0.01, flat across the redshift range [Sec. VI.1]
- 94 of 99 known X-ray clusters in the area were recovered [Sec. VII]
- Released publicly as FITS and ASCII tables [Sec. IV]

## Why it matters

A uniform, well-characterized catalog at this scale was the foundation for later work on cluster masses and
cosmological constraints, which the paper lays out as the next steps.

## My role

First author. The paper is adapted into Chapter 4 of Ben's PhD thesis
([thesis](astro/2006-maxbcg-systematic-discovery-characterization.md)).

## Cite

Koester, B. P., et al. (2007). A MaxBCG Catalog of 13,823 Galaxy Clusters from the Sloan Digital Sky Survey. The
Astrophysical Journal. doi:10.1086/509599
