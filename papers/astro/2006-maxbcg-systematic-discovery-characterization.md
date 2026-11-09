---
title: "MaxBCG: Systematic Discovery, Characterization and Calibration of Galaxy Clusters from Large Optical Surveys"
authors: Koester, B. P.
year: 2006
venue: Ph.D. dissertation (Physics), University of Michigan
doi:
url: https://hdl.handle.net/2027.42/126198
open_access: false
first_author: true
author_position: 1 of 1
projects: [maxbcg]
source_read: full text
status: drafted
---

# Finding galaxy clusters in Sloan imaging

The dissertation behind MaxBCG: a cluster-finding algorithm, the largest and best-understood cluster catalog
assembled at the time, and a new way to estimate cluster mass from galaxy counts, all tested against detailed
simulations.

## Question

Can galaxy clusters be found systematically in large CCD imaging surveys, with purity, completeness, redshifts and
mass estimates understood well enough for cosmology?

## Data

- Sloan Digital Sky Survey imaging and spectroscopy (Ch. 2)
- Detailed mock galaxy catalogs built on dark-matter simulations, used to test the finder (Ch. 3–4)
- ROSAT All-Sky Survey X-ray clusters for comparison (Ch. 4)

## Approach

- Ch. 1: review of cluster detection methods (optical, X-ray, Sunyaev-Zeldovich, radio, weak lensing) and their
  uncertainties
- Ch. 3: the maxBCG algorithm, a likelihood combining the red-sequence "ridgeline" of cluster galaxies with a
  likelihood for the brightest cluster galaxy; completeness, purity, fragmentation and over-merging measured on
  mocks
- Ch. 4: the resulting SDSS catalog, tested against spectroscopy and X-ray clusters
- Ch. 5: mass proxies, checked against stacked weak lensing and velocity dispersions, and a new
  background-corrected richness ("Ngals") built from filters calibrated on the survey itself

## Findings

- Reliably recovers clusters with as few as 10 bright red galaxies, down to about 10^14 solar masses, which the
  thesis describes as unprecedented for imaging surveys [6.1]
- About 90% pure and complete at redshifts 0.1 to 0.3 for those masses and richnesses [6.1]
- Photometric redshift errors of 0.015, the most accurate of their kind at the time [6.1]
- Lensing and velocity measurements show richness scales well with mass, and the finder also detects smaller
  groups [6.1]
- The new background-corrected richness carries additional mass information beyond earlier estimates [5.5, Fig.
  5.15]

## Why it matters

The thesis describes it as the first use of large CCD imaging surveys together with next-generation simulations to
test a cluster finder and understand what it selects. It laid the groundwork for the weak-lensing, dynamical and
cosmological analyses that followed [6.2].

## My role

Sole author; doctoral committee chaired by Timothy A. McKay. Chapters 3 and 4 are adapted from the two 2007 ApJ
MaxBCG papers ([finder](../apj-2007-maxbcg-finder.md), [catalog](../apj-2007-maxbcg-catalog.md)).

## Cite

Koester, B. P. (2006). MaxBCG: Systematic Discovery, Characterization and Calibration of Galaxy Clusters from Large
Optical Surveys. Ph.D. dissertation, University of Michigan. hdl:2027.42/126198
