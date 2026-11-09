---
title: Building a transcript of the future
authors: Koester, B. P.; Fogel, J.; Murdock, W.; Grom, G.; McKay, T. A.
year: 2017
venue: International Conference on Learning Analytics and Knowledge (LAK17)
doi: 10.1145/3027385.3027418
url: https://doi.org/10.1145/3027385.3027418
open_access: false
first_author: true
projects: [transcript-of-the-future]
source_read: not reached (ACM blocked); measures described from the authors' LAK19 follow-up draft and the ICPSR 38594 study page
status: todo
---

# Transcript of the Future

A transcript lists courses and grades but says nothing about how one student's education compares with others who
earned the same degree. This paper introduced measures, built only from transcript data, that put each student's
record in context.

## Question

Can routinely recorded transcript data be turned into contextual, comparable summaries of a student's education:
performance, difficulty, depth, breadth and the diversity of classmates and subjects?

## Data

Not reached. Ben to supply (institution, cohorts, number of students).

## Approach

The measures, as the follow-up draft describes those introduced here:

- **Student fixed effect**: performance relative to classmates in the same courses, in grade points, from a linear
  model of grades with student and course effects
- **Course grading difficulty**: the credit-weighted course effects from the same model; low means harder-graded
  courses
- **Major diversity**: how varied the eventual majors of a student's classmates were, using a diversity index
- **Subject diversity**: the same index applied to course subjects

The follow-up draft adds depth (credit-weighted course level) and range of experience (spread across lecture,
lab, discussion and other formats), and combines all six into a liberal-arts composite.

## Findings

Not reached. Ben to supply one or two headline findings.

- Four of the measures were later released to researchers as part of the College and Beyond II dataset, which asks
  users to cite this paper ([CBII summary](icpsr-2022-cbii-student-experience.md))

## Why it matters

Contextual measures make a transcript comparable across students, majors and institutions, and they scale to tens
of thousands of students.

## My role

First author. Ben to add specifics.

## Cite

Koester, B. P., Fogel, J., Murdock, W., Grom, G., & McKay, T. A. (2017). Building a transcript of the future.
Proceedings of LAK17. doi:10.1145/3027385.3027418
