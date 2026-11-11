---
title: SEISMIC STEM-equity collaboration
bucket: past
status: done
publish: false
visibility: description-only
repos: [SEISMIC]
papers: [10.1186/s40594-024-00474-7, 10.1187/cbe.24-02-0051, 10.3389/feduc.2023.1176876, 10.1187/cbe.21-06-0158]
next: Ben approves it for the site; the repo decision is tracked under To resolve
---

# SEISMIC STEM-equity collaboration

Shared code and standards for a multi-institution collaboration studying who succeeds in early STEM courses, and
why. Four journal papers from 2022 to 2024.

## The problem

Equity gaps in STEM courses look different at each university. Comparing them needs the same definitions,
samples and analyses everywhere.

## Data

Each institution ran the shared code on its own student-record and student-course tables. No data left any
campus.

## Approach

Shared R code for course performance, grade comparisons by gender, first-generation and underrepresented status,
pairwise student similarity, and replication of collaborators' analyses.

## Results

- At six universities and 227,413 students, each additional systemic advantage went with a smaller grade penalty
  in the largest introductory STEM courses, on every campus
  ([IJ STEM Ed 2024](../../papers/seismic-2024-systemic-advantage.md)); Ben co-led the project and supported data
  curation and analysis
- Across 3,207 course sections at five universities, about a third showed small or no opportunity gaps, evidence
  that equitable outcomes are achievable ([CBE—LSE 2024](../../papers/seismic-2024-opportunity-gaps.md))
- Process mining of biology curricula at two universities showed fewer than half of even the most advantaged
  students follow the intended sequence, and the least advantaged were far more likely to leave for non-STEM
  degrees ([Frontiers 2023](../../papers/seismic-2023-major-curricula.md)); Ben analyzed the data and managed the
  merged project data
- An essay on doing quantitative equity work without deficit framing
  ([CBE—LSE 2022](../../papers/seismic-2022-critical-approaches.md))

## Papers

- Castle, Byrd, Koester et al. Systemic advantage has a meaningful relationship with grade outcomes in students'
  early STEM courses at six research universities. International Journal of STEM Education, 2024.
  doi:10.1186/s40594-024-00474-7
- Denaro et al. A Multi-institutional Cluster Analysis to Identify Groups of Courses with Exemplary Opportunity
  Gaps for Undergraduate Students in the Biological Sciences. CBE—Life Sciences Education, 2024.
  doi:10.1187/cbe.24-02-0051
- Major curricula as structures for disciplinary acculturation that contribute to student minoritization.
  Frontiers in Education, 2023. doi:10.3389/feduc.2023.1176876
- Integrating Critical Approaches into Quantitative STEM Equity Work. CBE—Life Sciences Education, 2022.
  doi:10.1187/cbe.21-06-0158

## Code

- Shared analysis code in R, run separately at each institution. Not linked here yet.

## To resolve

- [ ] Ben: approve for the site (`publish: true`)
- [ ] Repos: SEISMIC is public today and contains SQL that names internal tables. Either delete those files and
      rename columns, or make the repo private and let the papers carry it
- [x] Fill in Results (from the papers; see papers/)
