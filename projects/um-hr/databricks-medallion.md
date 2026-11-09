---
title: Databricks medallion pipeline
bucket: um-hr
status: todo
visibility: description-only
repos: []
papers: []
next: Build bronze, silver and gold layers for Midwestern State in Databricks Free Edition
---

# Databricks medallion pipeline

## How to describe it publicly

Leading the move of HR analytics from Oracle and BigQuery to a Databricks medallion architecture, including tables
refreshed faster than daily, and the workspace layout for dev, staging and production.

## Public parallel

Bronze, silver and gold pipeline for the Midwestern State workforce in Databricks Free Edition: raw extracts,
cleaned and conformed tables, then metrics tables that feed the [attrition model](attrition.md). Dev and test
schemas, all code in GitHub.

## Data for the parallel

- **OPM Federal Workforce Data**: monthly employment, accessions and separations Parquet files from a free API
  (see [attrition](attrition.md) for what the files hold and their limits). Real-world mess to handle: monthly
  versioned releases with revisions, "REDACTED" values, code-and-label pairs, and the format change from the
  older FedScope files.
- **The Midwestern State simulator**, for person-level tables.

## To resolve

- [ ] Check whether Free Edition serverless compute can reach the OPM API; if not, pull files on the EC2 host and upload
- [ ] Pipeline design note: layers, tables, refresh cadence
- [ ] Build it
- [ ] Databricks certification
