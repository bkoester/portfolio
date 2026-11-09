---
title: Transcript of the Future
bucket: past
status: todo
visibility: public
repos: [TOF, TOF2Paper]
papers: [10.1145/3027385.3027418, 10.3886/icpsr38594.v1]
next: Rename LARC column names in TOF to generic ones
---

# Transcript of the Future

A traditional transcript lists courses and grades but says nothing about how one student's path compares with
others who earned the same degree. This work builds measures that put each student's experience in context.

## The problem

Transcripts are rich but flat. They can't show breadth, depth, or how typical a student's path was for their
major.

## Data

Two institution-generated tables: student-course (one row per student-course) and student-record. The toolkit
documents the columns it needs so other institutions can build their own.

## Approach

Pairwise student similarity and clustering; a liberal-arts index; disciplinary depth and breadth; division
credit intensity; course and demographic diversity; student-course fixed effects. All in R with the tidyverse.

## Results

- The measures became research infrastructure: computed for the undergraduate population of 19 public universities
  in the College and Beyond II study (1.3 million students, 46.9 million enrollments) and released through ICPSR,
  with four variables credited to the LAK17 paper ([CBII summary](../../papers/icpsr-2022-cbii-student-experience.md))
- Open question for Ben: one or two headline findings from LAK17 itself
  ([paper summary](../../papers/lak17-transcript-of-the-future.md); the full text wasn't reachable)

## Papers

- Koester, Fogel, Murdock, Grom & McKay. Building a transcript of the future. LAK17.
  doi:10.1145/3027385.3027418 (first author)
- Koester et al. College and Beyond II (CBII) Student Experience Analytics, 2000–2021. ICPSR 38594, 2022.
  doi:10.3886/icpsr38594.v1 (first author)
- Data-Driven Representation of Student Experience with the Transcript of the Future: draft prepared for LAK19
  (TOF2Paper). Open question: accepted, or unpublished?

## Code

- [TOF](https://github.com/bkoester/TOF): the toolkit

## To resolve

- [ ] Rename LARC column names (STDNT_ID, SBJCT_CD, CATLG_NBR and the rest) to generic names in code and README
- [ ] Decide on the LAK19 draft: post as a preprint, or retire it
- [ ] Add a small synthetic sample so the toolkit runs end to end
- [ ] Fill in Results
