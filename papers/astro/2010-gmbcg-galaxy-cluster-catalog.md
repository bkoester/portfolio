---
title: A GMBCG Galaxy Cluster Catalog of 55,424 Rich Clusters from SDSS DR7
authors: Hao, J.; McKay, T. A.; Koester, B. P.; Rykoff, E. S.; Rozo, E.; Annis, J.; and 8 others
year: 2010
venue: The Astrophysical Journal Supplement Series, 191, 254
doi: 10.1088/0067-0049/191/2/254
url: https://doi.org/10.1088/0067-0049/191/2/254
open_access: true
first_author: false
author_position: 3 of 14
projects: []
source_read: full text
status: drafted
---

# A catalog of 55,424 galaxy clusters

A new cluster-finding method that looks for a bright central galaxy plus a tight band of red galaxies produced
a catalog of more than 55,000 rich clusters from Sloan data, reaching to higher redshift than earlier catalogs.

## Question

Can a cluster finder built on a Gaussian mixture model of galaxy colors produce a large, pure and complete
cluster catalog from SDSS DR7 over a wide redshift range?

## Data

- 8240 square degrees of SDSS DR7 photometry, galaxies with i < 21.0 [Abstract; Sec. 4.1]
- Final catalog limited to 0.1 < z < 0.55 [Sec. 4.2.1]
- About 380,000 clusters before the richness cut; 55,424 with scaled richness of 8 or more [Sec. 4.2.2; title]

## Approach

- Fit galaxy colors around each candidate central galaxy with an error-corrected two-component mixture to find the red sequence [Sec. 3.1]
- Switched from g-r to r-i color at z = 0.43 to follow the red sequence to higher redshift [Table 2]
- Ranked candidates by a clustering strength and merged overlapping ones [Sec. 3.8]
- Tested against simulated clusters and cross-matched with maxBCG, WHL and X-ray catalogs [Sec. 5]

## Findings

- 13,374 of 13,823 maxBCG clusters (about 96.8%) have a GMBCG match; 8,818 of those share the same central galaxy [Sec. 5.4]
- 227 of 229 X-ray clusters match a GMBCG cluster [Sec. 5.6]
- Central-galaxy photometric redshifts have an rms error of about 0.015 against about 20,000 spectroscopic redshifts [Sec. 4.2.2; Fig. 13]
- Tests indicate high completeness and purity for clusters with 15 or more members [Abstract; Sec. 5.2]
- The full DR7 catalog ran within 23 hours on one desktop [Abstract; Sec. 6]

## Why it matters

The authors present it as a large, well-tested cluster sample for cosmology and galaxy-evolution work, and
point to deeper data such as SDSS co-adds and the Dark Energy Survey as next steps.

## My role

Not stated in the paper (author 3 of 14). Ben to fill in.

## Cite

Hao, J., McKay, T. A., Koester, B. P., et al. (2010). A GMBCG Galaxy Cluster Catalog of 55,424 Rich Clusters
from SDSS DR7. The Astrophysical Journal Supplement Series, 191, 254. doi:10.1088/0067-0049/191/2/254
