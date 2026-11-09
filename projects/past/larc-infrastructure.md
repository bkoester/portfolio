---
title: Learning-analytics data architecture
bucket: past
status: todo
visibility: description-only
repos: [LARC, aws_larc_pipeline, aws_larc_cookbook, larc_redshift_load, LARC_lambda_process, larc_pure_python, larc-sql-test]
papers: [10.18608/jla.2019.62.8]
next: Make the public LARC repo private; let the paper carry this project
---

# Learning-analytics data architecture

Built and maintained a research-ready student data warehouse so faculty and staff could study teaching and
learning without each team rebuilding the data. The model is published in the Journal of Learning Analytics.

## How to describe it publicly

Designed a collaborative model for institutional learning-analytics data: a curated research dataset of
student records and course enrollments, its documentation and access process, and AWS pipelines (Lambda,
Redshift) that loaded and refreshed it.

## Results

- A cross-campus team designed the dataset around the researcher: a handful of flat tables, simple 0/1 coding,
  common calculations built in, and a deliberate target of the 80% of questions researchers ask most, with room to
  extend ([JLA 2019](../../papers/jla-2019-rearchitecting-data.md))
- Released in September 2016 as snapshots three times a year, a model borrowed from the Sloan Digital Sky
  Survey's data releases, the same survey behind the [MaxBCG catalog](maxbcg.md)
- More than 50 investigators had access by the time of publication, with about a week from request to data; the
  approach was reused for a later institutional enrollment dataset
- The paper closes with a six-point framework for other institutions, which reads as a consulting playbook

## Papers

- Lonn & Koester. Rearchitecting Data for Researchers: A Collaborative Model for Enabling Institutional Learning
  Analytics in Higher Education. Journal of Learning Analytics, 2019. doi:10.18608/jla.2019.62.8
  ([summary](../../papers/jla-2019-rearchitecting-data.md))

## Code

All repos stay private: they name internal tables and columns throughout.

## To resolve

- [ ] Make the public LARC repo private (one of its SQL files names internal tables)
- [ ] One paragraph on the AWS pipeline design, in general terms
