# Portfolio — Ben Koester

Higher-ed and workforce analytics, with a research record behind it: 98 publications, 50 refereed journal
articles, 14 first-author. The work runs from building the MaxBCG galaxy-cluster catalog on Sloan Digital Sky
Survey data, through a decade of student-success and STEM-equity analytics at the University of Michigan, to HR
workforce analytics, AI assistants and a Databricks migration today.

This repo organizes that work into case studies. It is the source for the projects section of
[benkoester.com](https://benkoester.com); the full publication list lives in
[bkoester/publications](https://github.com/bkoester/publications).

## Layout

```
projects/
  past/     Past projects with papers behind them; repos need finishing, consolidating or scrubbing
  live/     Current projects on GitHub, most running on the self-healing EC2 host
  um-hr/    Current U-M HR work: described at a public level, shown through synthetic-data parallels
papers/     One summary per anchor paper: question, data, approach, findings, my role
inventory/
  repos.md  Every repo in the account, its bucket, and what to do with it
publications.md   Which papers anchor which projects
templates/
  case-study.md   Skeleton for a new project file
  paper.md        Skeleton for a new paper summary
CLAUDE.md         Ground rules for anyone (or any agent) editing this repo
```

Each project file starts with front matter (`status`, `repos`, `papers`, `visibility`, `next`) so the status
board below, and later the website, can be generated from it.

## Status board

| Bucket | Project | Status | Next step |
| --- | --- | --- | --- |
| Past | [Grade penalties and course pathways](projects/past/grade-penalties.md) | todo | Fold PLA, pla-devel, aim-analytics, cic-gp into one repo |
| Past | [Transcript of the Future](projects/past/transcript-of-the-future.md) | todo | Rename LARC column names; decide on the LAK19 draft |
| Past | [SEISMIC STEM-equity collaboration](projects/past/seismic.md) | todo | Scrub LARC SQL or keep private and let the papers speak |
| Past | [Campus networks](projects/past/campus-networks.md) | todo | Merge network repos; settle the weighted-networks draft |
| Past | [Learning-analytics data architecture](projects/past/larc-infrastructure.md) | todo | Paper only; repos stay private |
| Past | [Synthetic student transcripts (SSU)](projects/past/synthetic-transcripts.md) | todo | Refresh dependencies, add a worked example |
| Past | [Equity-analytics workshop (LASI 2019)](projects/past/lasi-equity-workshop.md) | todo | Rename columns; present as teaching |
| Past | [MaxBCG galaxy cluster finder and catalog](projects/past/maxbcg.md) | todo | Ben: role, and what the catalog went on to support |
| Live | [Self-healing EC2 host](projects/live/ec2-platform.md) | todo | Delete committed Terraform plan; write it up |
| Live | [Big Ten jobs](projects/live/big-ten-jobs.md) | todo | Remove personal search pages; check history; make public |
| Live | [Ask Ben](projects/live/ask-ben.md) | todo | Review eval results |
| Live | [WCC pathfinder](projects/live/wcc-pathfinder.md) | todo | Write the case study |
| Live | [Car search](projects/live/car-search.md) | todo | Make public; write the case study |
| Live | [College scraper](projects/live/college-scraper.md) | todo | Consolidate setup docs into one README |
| U-M HR | [HR chatbot](projects/um-hr/hr-chatbot.md) | todo | Public policy-handbook demo |
| U-M HR | [Attrition modeling](projects/um-hr/attrition.md) | todo | Build the Midwestern State simulator |
| U-M HR | [Databricks medallion pipeline](projects/um-hr/databricks-medallion.md) | todo | Pipeline on simulator data in Free Edition |
| U-M HR | [Report and data catalogue](projects/um-hr/data-catalogue.md) | todo | Open template for Midwestern State |
| U-M HR | [Leadership reporting](projects/um-hr/leadership-reporting.md) | todo | Description only |
| U-M HR | [Docs to GitHub knowledge-base sync](projects/um-hr/docs-kb-sync.md) | todo | Rewrite as a small open-source tool |

## Papers

Summaries written from each paper's text. `drafted` means not yet checked by Ben; "My role" stays open until he
fills it in.

| Year | Paper | Read from | Project |
| --- | --- | --- | --- |
| 2024 | [Systemic advantage and grade penalties at six universities](papers/seismic-2024-systemic-advantage.md) | full text | SEISMIC, grade penalties |
| 2024 | [Opportunity gaps across 3,207 course sections](papers/seismic-2024-opportunity-gaps.md) | full text | SEISMIC |
| 2023 | [The biology curriculum students actually take](papers/seismic-2023-major-curricula.md) | full text | SEISMIC |
| 2022 | [Quantitative equity work without deficit framing](papers/seismic-2022-critical-approaches.md) | full text | SEISMIC, LASI workshop |
| 2022 | [CBII Student Experience Analytics (dataset)](papers/icpsr-2022-cbii-student-experience.md) | study page, user guide | Transcript of the Future |
| 2021 | [ECoach in gateway courses](papers/lak21-ecoach.md) | abstract | — |
| 2020 | [Campus Connections](papers/ihe-2020-campus-connections.md) | full text | Campus networks |
| 2019 | [Rearchitecting data for researchers](papers/jla-2019-rearchitecting-data.md) | abstract | Data architecture |
| 2018 | [Categorization, intersectionality and learning analytics](papers/lak18-categorization-intersectionality.md) | abstract | LASI workshop |
| 2017 | [Gendered grade gaps at five universities](papers/aera-open-2017-gendered-performance.md) | full text | Grade penalties |
| 2017 | [Transcript of the Future](papers/lak17-transcript-of-the-future.md) | not reached; draft and dataset pages | Transcript of the Future |
| 2016 | [Grade penalties and gender gaps at Michigan](papers/arxiv-2016-gendered-performance.md) | full text | Grade penalties |
| 2016 | [What faculty need to use learning-analytics data](papers/perc-2016-supporting-faculty.md) | abstract | Grade penalties |
| 2007 | [The MaxBCG catalog](papers/apj-2007-maxbcg-catalog.md) | full text | MaxBCG |
| 2007 | [The MaxBCG cluster finder](papers/apj-2007-maxbcg-finder.md) | full text | MaxBCG |

## Order of work

1. Consolidate the grade-penalty repos and archive the tutorial clutter
2. Rename LARC column names in TOF and LASI_2019_equity
3. Publications page on benkoester.com, generated from the publications JSON
4. Clean up big-ten-jobs and ec2-infra and make them public
5. Build the Midwestern State simulator
6. Attrition case study on the simulator
7. Databricks medallion pipeline and catalogue on the same data
8. File the M-Inform outside-activity disclosure before the first paid engagement
