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

## Federal workforce data: what it holds (checked 2026-11-09)

OPM's [Federal Workforce Data](https://data.opm.gov/) publishes three record-level monthly files from EHRI:
employment (month-end snapshot, about 2.1M rows), accessions and separations. The new format runs from about
2021, monthly, through a free Parquet API with no key; older FedScope files go back to 1998 (headcount) and
FY2005 (separations). Fields: agency and sub-agency, occupation, grade and pay plan, salary, age bracket,
education, years of service, supervisory status, appointment type, work schedule, duty station; separations add
a reason code (quit, retirement, RIF, termination, transfer) and a deferred-resignation flag.

Limits that shape the plan:

- **No person ID.** Records can't be linked across months, so no person-level attrition model from this data.
- **No sex, race, ethnicity or disability** (removed under 2025 executive orders); fairness checks only by age
  bracket and education.
- Some pay and about half of duty-station state values redacted; USPS and intelligence agencies excluded.
- 2025 is an outlier (about 125,000 separations in September 2025 against a typical 20,000 a month).

So the two datasets split the work:

- **Federal data**: the medallion pipeline, and group-level exit curves. Separations by years of service
  divided by headcount at the same tenure gives real hazard curves by agency, occupation, grade and age bracket,
  split by reason.
- **Midwestern State**: person-level prediction, planted causes, leakage traps and fairness checks.

## To resolve

- [ ] Simulator spec: org structure, variables, true causal drivers
- [ ] Group-level exit curves on the federal data (tenure hazard by agency, occupation, grade; quits vs retirements)
- [ ] Build the simulator and the model in Databricks Free Edition
- [ ] Write the case study
