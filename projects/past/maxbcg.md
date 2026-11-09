---
title: MaxBCG galaxy cluster finder and catalog
bucket: past
status: todo
visibility: description-only
repos: []
papers: [10.1086/512092, 10.1086/509599]
next: Ben adds his role
---

# MaxBCG galaxy cluster finder and catalog

Built an algorithm that finds galaxy clusters in survey imaging and used it to produce the largest cluster catalog
of its time: 13,823 clusters from the Sloan Digital Sky Survey, with measured accuracy, released for others to use.
This is large-scale data work, years before "data science" was a job title.

## The problem

Galaxy clusters are a sensitive probe of cosmology, but only if you can find them uniformly across a huge survey
and know exactly how often your finder is wrong.

## Data

SDSS five-band imaging of about 23 million galaxies plus spectroscopy of 567,486, over 7,500 square degrees;
simulated galaxy catalogs for testing.

## Approach

A scoring method that looks for a bright central galaxy surrounded by red-sequence galaxies, with purity and
completeness measured against simulations, shuffled data and inserted fake clusters. See the
[finder paper](../../papers/apj-2007-maxbcg-finder.md).

## Results

- 13,823 clusters holding 213,016 member galaxies, more than 90% pure and more than 85% complete above 10^14 solar
  masses ([catalog paper](../../papers/apj-2007-maxbcg-catalog.md))
- Photometric redshifts accurate to about 0.01; 94 of 99 known X-ray clusters in the area recovered
- False detections below 1% for richer clusters ([finder paper](../../papers/apj-2007-maxbcg-finder.md))

## What it went on to support

The catalog became the basis for a run of collaboration papers, several with Ben as co-author:

- Weak-lensing mass calibration of the clusters, stacking background galaxy shapes around them
  ([2007](../../papers/astro/2007-crosscorrelation-weak-lensing-sdss.md))
- Cosmological constraints from cluster counts: an early result of σ8 = 0.92 ± 0.10
  ([2007](../../papers/astro/2007-cosmological-constraints-sdss-maxbcg.md)), refined to σ8 = 0.807 ± 0.020 when
  combined with WMAP5, about twice as tight as WMAP5 alone
  ([2010](../../papers/astro/2010-cosmological-constraints-sloan-digital.md))
- Successor cluster finders and catalogs: GMBCG, which recovers 13,374 of the 13,823 maxBCG clusters
  ([2010](../../papers/astro/2010-gmbcg-galaxy-cluster-catalog.md)), and redMaPPer, about 25,000 clusters from the
  later SDSS data release ([2014](../../papers/astro/2014-redmapper-i-algorithm-sdss.md))
- The thesis behind it all ([2006](../../papers/astro/2006-maxbcg-systematic-discovery-characterization.md))

## Why it reads well to a client

Validating a detection algorithm against simulated ground truth, quantifying false positives and false negatives,
and shipping a documented dataset other teams build on: the same discipline applies to any model put into
production.

## Papers

- Koester et al. (2007). MaxBCG: A Red-Sequence Galaxy Cluster Finder. ApJ. doi:10.1086/512092
- Koester et al. (2007). A MaxBCG Catalog of 13,823 Galaxy Clusters from the Sloan Digital Sky Survey. ApJ.
  doi:10.1086/509599

## To resolve

- [x] What the catalog went on to support (from the papers)
- [ ] Ben: his role on the finder and catalog papers
