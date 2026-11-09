---
title: Building a transcript of the future
authors: Koester, B. P.; Fogel, J.; Murdock, W., III; Grom, G.; McKay, T. A.
year: 2017
venue: International Conference on Learning Analytics and Knowledge (LAK17)
doi: 10.1145/3027385.3027418
url: https://doi.org/10.1145/3027385.3027418
open_access: true   # CC BY 4.0
first_author: true
projects: [transcript-of-the-future]
source_read: full text
status: drafted
---

# Transcript of the Future

GPA treats an A in a generously graded course the same as an A in a tough one, and says nothing about how broad a
student's education was. Using 16 years of Michigan transcripts, this paper built measures that put each student's
record in context, and showed they would change who gets honors.

## Question

Can routinely recorded transcript data give fairer measures of performance, plus measures of intellectual breadth
and of the diversity of a student's classmates?

## Data

- University of Michigan, Ann Arbor: fall 1998 to winter 2014
- 4,384,169 grades for 192,987 students in 15,571 courses across 318 subjects [Sec. 2]

## Approach

- Four performance measures compared: GPA; two "grade points above replacement" measures, loosely modeled on
  baseball's wins above replacement, that compare each grade with the course's grade distribution; and a new
  student fixed-effects model estimating student and course effects jointly from all grades [Sec. 2.2]
- Diversity indices (from ecology's family of diversity measures) for the subjects a student studied and the
  eventual majors of their classmates [Sec. 2.3]
- Bootstrap resampling of each student's courses to estimate the uncertainty in GPA [Sec. 4.2]

## Findings

- Average grades differ by more than 25% across disciplines, so GPA sends false signals about where students
  excel [Sec. 1.1]
- Over their careers, students share classes with anywhere from a dozen to nearly 25,000 classmates, typically
  7,500 to 12,500 [Sec. 2.1, Fig. 1]
- At the same GPA, majors differ in how strong students are relative to classmates: mathematics students ranked
  higher on the fixed-effects measure, English and psychology lower [Sec. 3.1, Fig. 4]
- The median standard error on a graduate's GPA is 0.058, so GPAs within 0.05 are statistically
  indistinguishable [Sec. 4.2]
- Ranking honors by the fixed-effects measure instead of GPA reshuffles them: in English, the three distinction
  levels go from 30, 9 and 9 students to 20, 8 and 0; in mathematics, from 13, 10 and 4 to 22, 11 and 15
  [Sec. 4.3]
- Breadth measures are nearly independent of performance (correlation of −0.14 with GPA, none with the
  fixed-effects measure), so they add new information [Sec. 4.4.2]

## Why it matters

Registrars already hold the data to give every transcript context. The authors argue for the idea of enriched
transcripts more than for any single measure, and invite institutions to build their own [Sec. 4.5].

## My role

First author. Ben to add specifics.

## Cite

Koester, B. P., Fogel, J., Murdock, W., III, Grom, G., & McKay, T. A. (2017). Building a transcript of the future.
Proceedings of LAK17. doi:10.1145/3027385.3027418
