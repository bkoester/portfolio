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

## Papers

- Lonn & Koester. Rearchitecting Data for Researchers: A Collaborative Model for Enabling Institutional Learning
  Analytics in Higher Education. Journal of Learning Analytics, 2019. doi:10.18608/jla.2019.62.8
  ([summary](../../papers/jla-2019-rearchitecting-data.md))

## Code

All repos stay private: they name internal tables and columns throughout.

## To resolve

- [ ] Make the public LARC repo private (it includes LARC_PII.sql, which names internal tables)
- [ ] One paragraph on the AWS pipeline design, in general terms
