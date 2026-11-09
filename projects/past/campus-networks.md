---
title: Campus networks
bucket: past
status: todo
visibility: public
repos: [acad_network, unizin, NetworkWeightingManuscript]
papers: [10.1007/s10755-019-09497-3]
next: Merge the network code into one repo
---

# Campus networks

Students who share courses form a network; so do courses that share students. Mapping those networks shows how
a campus actually connects, beyond the org chart of departments.

## The problem

Universities organize by department, but students move across them. Who actually shares classrooms, and how
does that differ by major and term?

## Data

Student-course enrollments turned into bipartite student-course networks, then projected onto students or
courses.

## Approach

Network construction and reduction (C++ and Python in acad_network, R in unizin); weighting schemes for
projected networks; degree, clustering, eigenvector and triangle measures; Gephi visualizations.

## Results

- For 6,738 students entering in 2011 and the 68,946 students they shared classes with, a few courses act as the
  campus's bridges: the largest course links students who would otherwise never meet, and some small courses
  connect as many people as courses five times their size
  ([Campus Connections, 2020](../../papers/ihe-2020-campus-connections.md))
- Students cluster by major, some tightly (Neuroscience) and some loosely (Political Science); the most central
  students were linked to nearly a quarter of their entering class

## Papers

- Israel, Koester & McKay. Campus Connections: Student and Course Networks in Higher Education. Innovative Higher
  Education, 2020. doi:10.1007/s10755-019-09497-3
- Weighted Networks: manuscript draft for the Journal of Learning Analytics (NetworkWeightingManuscript). Open
  question: the methods side of Campus Connections, or a separate paper?

## Code

- acad_network (fork, with collaborator code), unizin: to be merged into one networks repo

## To resolve

- [ ] Merge into one networks repo with a synthetic example
- [ ] Settle the weighted-networks draft: blog post, preprint, or retire
- [x] Fill in Results (from the paper; see papers/)
- [ ] Ben: his role on Campus Connections
