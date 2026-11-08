---
title: Big Ten jobs
bucket: live
status: todo
visibility: public
repos: [big-ten-jobs]
papers: []
next: Remove the personal search page and fit scoring; check history for .env
---

# Big Ten jobs

A daily record of job postings across eleven large universities: what opens, what closes, and what it pays.
Higher-ed labor-market analytics from public data.

## The problem

University hiring is spread across different applicant-tracking systems with no shared view, so trends in what
universities hire for and pay are invisible.

## Data

Public job postings from University of Michigan, Ohio State, Penn State, Maryland, USC, Purdue, UT Austin,
Texas A&M, Iowa State, Washington State and Louisville. Michigan data goes back to 2023; the others since
May 2026.

## Approach

Scrapers per platform (Workday, SuccessFactors, Drupal) with retries; one SQLite table tracking first-seen,
last-seen and active status; salaries parsed from description text; a read-only FastAPI and SvelteKit explorer;
Docker on daily timers on the [EC2 host](ec2-platform.md).

## Results

Open question: two or three findings worth a chart — hiring volume by school over time, salary ranges by role
family, how long postings stay open.

## Code

- big-ten-jobs (private until cleaned up)

## To resolve

- [ ] Remove the personal "my search" page and LLM fit scoring, or move them to a private branch
- [ ] Check history for any committed .env or Adzuna keys
- [ ] Write findings with charts
