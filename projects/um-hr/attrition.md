---
title: Attrition modeling
bucket: um-hr
status: todo
visibility: description-only
repos: []
papers: []
next: Write the Midwestern State simulator spec
---

# Attrition modeling

## How to describe it publicly

Built an employee attrition model for a large university workforce.

## Public parallel: Midwestern State

A fictional university whose workforce is simulated from stated assumptions, with known true drivers of exit.
The same simulated workforce also feeds the [Databricks pipeline](databricks-medallion.md) and the
[catalogue](data-catalogue.md).

The case study shows:

- the model recovering the true drivers, or failing to
- leakage traps, such as features that exist only because someone already gave notice
- why time-to-exit (survival) framing beats a yes/no classifier
- fairness checks across groups
- what HR should and shouldn't do with a risk score: fix systemic causes, never target individuals

## Data for the parallel

Hand-built simulator: departments, job families, tenure, pay against market, time since promotion, manager
changes, remote eligibility. Rates and tenure curves tuned to public sources:

- [OPM Federal Workforce Data](https://data.opm.gov/explore-data/data/data-downloads): record-level monthly
  separations and accessions
- BLS JOLTS quit rates by industry

Builds on [SSU](../past/synthetic-transcripts.md), the earlier synthetic-transcript generator.

## To resolve

- [ ] Simulator spec: org structure, variables, true causal drivers
- [ ] Build the simulator and the model in Databricks Free Edition
- [ ] Write the case study
