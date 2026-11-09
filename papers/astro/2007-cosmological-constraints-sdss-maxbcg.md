---
title: Cosmological Constraints from SDSS maxBCG Cluster Abundances
authors: Rozo, E.; Wechsler, R. H.; Koester, B. P.; McKay, T. A.; Evrard, A. E.; Johnston, D.; and 3 others
year: 2007
venue: arXiv e-prints
doi:
url: https://arxiv.org/abs/astro-ph/0703571
open_access: true
first_author: false
author_position: 3 of 9
projects: []
source_read: full text
status: drafted
---

# Counting clusters to weigh the universe

Counting how many galaxy clusters of each size appear in the SDSS maxBCG catalog gives a measure of how clumpy matter in the universe is. The result is a value of the clumpiness parameter sigma_8 with a firm lower limit, even after allowing for uncertainty in how clusters were selected.

## Question

What value of the matter power spectrum normalization (sigma_8) is implied by the number of maxBCG clusters as a function of richness, once selection systematics are marginalized over?

## Data

- SDSS maxBCG cluster sample (Koester et al. 2007a), clusters at redshift 0.1 to 0.3 [Sec. IV].
- Clusters split into nine log-spaced richness bins for 10 ≤ N_obs < 100 plus one bin for N_obs ≥ 100 [Sec. IV; Fig. 1].
- External priors: CMB prior on Omega_m h^2 = 0.128 ± 0.01 and a supernova prior on h [Sec. III.4].

## Approach

- Model expected cluster counts as the halo mass function convolved with a detection model: a halo occupation (HOD) relation, completeness and purity [Sec. III.1–III.3].
- Gaussian likelihood whose covariance includes Poisson noise, sample variance, photo-z errors and selection scatter [Sec. III.2].
- Assume flat cosmologies, scale-invariant spectrum and massless neutrinos; explore parameters with MCMC chains [Abstract; Sec. IV].
- Test robustness by cutting the richness range and swapping mass functions [Sec. IV; Sec. V.2].

## Findings

- sigma_8 = 0.92 ± 0.10 (1 sigma) [Abstract; Sec. IV; Fig. 5].
- Lower limits of sigma_8 > 0.76 at 95% and > 0.68 at 99% confidence [Abstract; Sec. IV].
- The HOD slope comes out low, alpha = 0.83 ± 0.06, mildly below the usual value of one [Abstract; Sec. V.1].
- Using the Sheth & Tormen or Warren et al. mass functions instead moves parameters by less than 1 sigma [Sec. V.2].
- The poorly known maxBCG selection function is the main limit on precision [Sec. V].

## Why it matters

The authors show cluster counts from a large optical catalog can constrain cosmology, and expect tighter results once weak lensing, X-ray and dynamical masses are added.

## My role

Not stated in the paper (author 3 of 9). Ben to fill in. The analysis uses the maxBCG catalog and algorithm of Koester et al. (2007a,b).

## Cite

Rozo, E., Wechsler, R. H., Koester, B. P., et al. (2007). Cosmological Constraints from SDSS maxBCG Cluster Abundances. arXiv e-prints. arXiv:astro-ph/0703571
