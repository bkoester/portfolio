---
title: MaxBCG galaxy cluster finder and catalog
bucket: past
status: todo
visibility: description-only
repos: []
papers: [10.1086/512092, 10.1086/509599]
next: Ben adds his role and one line on what the catalog was later used for
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

## Why it reads well to a client

Validating a detection algorithm against simulated ground truth, quantifying false positives and false negatives,
and shipping a documented dataset other teams build on: the same discipline applies to any model put into
production.

## Papers

- Koester et al. (2007). MaxBCG: A Red-Sequence Galaxy Cluster Finder. ApJ. doi:10.1086/512092
- Koester et al. (2007). A MaxBCG Catalog of 13,823 Galaxy Clusters from the Sloan Digital Sky Survey. ApJ.
  doi:10.1086/509599

## To resolve

- [ ] Ben: his role and one line on what the catalog went on to support
