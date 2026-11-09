---
title: "Campus Connections: Student and Course Networks in Higher Education"
authors: Israel, U.; Koester, B. P.; McKay, T. A.
year: 2020
venue: Innovative Higher Education
doi: 10.1007/s10755-019-09497-3
url: https://doi.org/10.1007/s10755-019-09497-3
open_access: true
first_author: false
projects: [campus-networks]
source_read: full text
status: drafted
---

# Which courses and students hold a campus together

Treating enrollment as a network shows which courses connect otherwise separate parts of a university, and that
course size alone doesn't decide it: some small courses are among the strongest connectors.

## Question

How can network analysis of institutional records describe the way undergraduates and courses are linked through
shared enrollment?

## Data

- University of Michigan, more than 40,000 undergraduates
- 6,738 students who entered in fall 2011, followed through winter 2016 (90.9% had graduated)
- Full network: 68,946 students (the cohort plus everyone who shared a course with them) and 6,152 courses

## Approach

- A student-by-course enrollment network, projected into student-to-student and course-to-course networks
- Normalized degree centrality and local clustering coefficient for each node (Python, NetworkX); low clustering
  marks a node that bridges otherwise unlinked groups

## Findings

- The largest course on campus, STATS 250, had a clustering coefficient of 0.078: it links students who would
  otherwise never meet [The Course Networks]
- ASTRO 106, with about a fifth of STATS 250's enrollment, had nearly the same centrality; small courses such as
  DANCE 100 also stood out as connectors [The Course Networks]
- Size tracked centrality closely, with exceptions such as PHYSICS 240, which was fairly isolated for its size
  [The Course Networks]
- Students clustered by major: Neuroscience majors formed a tight cluster, Political Science majors were spread
  out [The Student Networks]
- The most central students were linked to almost a quarter of their entering cohort (about 1,500 people)
  [The Student Networks]

## Why it matters

Network measures show which courses and students bind a campus together, informing course choice, curriculum
design and equity work such as spotting isolation by background. The method can be repeated at other
institutions, though sharing a course doesn't guarantee real interaction.

## My role

Not stated in the paper. Ben to fill in.

## Cite

Israel, U., Koester, B. P., & McKay, T. A. (2020). Campus Connections: Student and Course Networks in Higher
Education. Innovative Higher Education. doi:10.1007/s10755-019-09497-3
