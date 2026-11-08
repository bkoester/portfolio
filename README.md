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
inventory/
  repos.md  Every repo in the account, its bucket, and what to do with it
publications.md   Which papers anchor which projects
templates/
  case-study.md   Skeleton for a new project file
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

## Order of work

1. Consolidate the grade-penalty repos and archive the tutorial clutter
2. Rename LARC column names in TOF and LASI_2019_equity
3. Publications page on benkoester.com, generated from the publications JSON
4. Clean up big-ten-jobs and ec2-infra and make them public
5. Build the Midwestern State simulator
6. Attrition case study on the simulator
7. Databricks medallion pipeline and catalogue on the same data
8. File the M-Inform outside-activity disclosure before the first paid engagement
