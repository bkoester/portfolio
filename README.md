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
| Past | [Grade penalties and course pathways](projects/past/grade-penalties.md) | done | Ben approves it for the site |
| Past | [Transcript of the Future](projects/past/transcript-of-the-future.md) | done | Ben approves it for the site |
| Past | [SEISMIC STEM-equity collaboration](projects/past/seismic.md) | done | Ben approves it for the site |
| Past | [Campus networks](projects/past/campus-networks.md) | done | Ben approves it for the site |
| Past | [Learning-analytics data architecture](projects/past/larc-infrastructure.md) | done | Ben approves it for the site |
| Past | [Synthetic student transcripts (SSU)](projects/past/synthetic-transcripts.md) | todo | Refresh dependencies, add a worked example |
| Past | [Equity-analytics workshop (LASI 2019)](projects/past/lasi-equity-workshop.md) | todo | Rename columns; present as teaching |
| Past | [MaxBCG galaxy cluster finder and catalog](projects/past/maxbcg.md) | done | — |
| Live | [Self-healing EC2 host](projects/live/ec2-platform.md) | done | Make both repos public |
| Live | [Home solar and battery advisor](projects/live/solar.md) | in-progress | Ben checks the write-up |
| Live | [University job postings tracker](projects/live/big-ten-jobs.md) | in-progress | Ben runs the findings script |
| Live | [Ask Ben](projects/live/ask-ben.md) | todo | Ben writes the first published answers |
| Live | [WCC pathfinder](projects/live/wcc-pathfinder.md) | todo | Write the case study |
| Live | [Car search](projects/live/car-search.md) | todo | Make public; write the case study |
| Live | [College scraper](projects/live/college-scraper.md) | todo | Consolidate setup docs into one README |
| U-M HR | [HR chatbot](projects/um-hr/hr-chatbot.md) | todo | Public policy-handbook demo |
| U-M HR | [Attrition modeling](projects/um-hr/attrition.md) | todo | Build the Midwestern State simulator |
| U-M HR | [Databricks medallion pipeline](projects/um-hr/databricks-medallion.md) | todo | Pipeline on simulator data in Free Edition |
| U-M HR | [Report and data catalogue](projects/um-hr/data-catalogue.md) | todo | Open template for Midwestern State |
| U-M HR | [Leadership reporting](projects/um-hr/leadership-reporting.md) | todo | Description only |
| U-M HR | [Docs to GitHub knowledge-base sync](projects/um-hr/docs-kb-sync.md) | todo | Rewrite as a small open-source tool |
| U-M HR | [Small agents and staff upskilling](projects/um-hr/small-agents.md) | todo | Placeholder |

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
| 2019 | [Rearchitecting data for researchers](papers/jla-2019-rearchitecting-data.md) | full text | Data architecture |
| 2018 | [Categorization, intersectionality and learning analytics](papers/lak18-categorization-intersectionality.md) | abstract | LASI workshop |
| 2017 | [Gendered grade gaps at five universities](papers/aera-open-2017-gendered-performance.md) | full text | Grade penalties |
| 2017 | [Transcript of the Future](papers/lak17-transcript-of-the-future.md) | full text | Transcript of the Future |
| 2016 | [Grade penalties and gender gaps at Michigan](papers/arxiv-2016-gendered-performance.md) | full text | Grade penalties |
| 2016 | [What faculty need to use learning-analytics data](papers/perc-2016-supporting-faculty.md) | abstract | Grade penalties |
| 2007 | [The MaxBCG catalog](papers/apj-2007-maxbcg-catalog.md) | full text | MaxBCG |
| 2007 | [The MaxBCG cluster finder](papers/apj-2007-maxbcg-finder.md) | full text | MaxBCG |

### Astrophysics and earlier work

Summaries of every article from the PhD, postdoc and bioinformatics years. Position is Ben's place in the author
list. Abstracts, circulars and proposals are listed in [other outputs](papers/other-outputs.md).

| Year | Paper | Venue | Position | Read from |
| --- | --- | --- | --- | --- |
| 2020 | [Public lens models for 37 clusters](papers/astro/2020-strong-lens-models-37.md) | The Astrophysical Journal Supplement Ser | 13/16 | partial full text |
| 2014 | [redMaPPer: a cluster finder for big surveys](papers/astro/2014-redmapper-i-algorithm-sdss.md) | The Astrophysical Journal | 8/15 | full text |
| 2013 | [A magnified dusty starburst galaxy](papers/astro/2013-sgas-1438451145407-big-cool.md) | The Astrophysical Journal | 14/17 | full text |
| 2013 | [A quasar split six ways by a cluster](papers/astro/2013-sdss-j22222745-gravitationally-lensed.md) | The Astrophysical Journal | 7/14 | full text |
| 2012 | [A better way to count cluster galaxies](papers/astro/2012-robust-optical-richness-estimation.md) | The Astrophysical Journal | 2/10 | full text |
| 2012 | [Confirming fossil groups in X-rays](papers/astro/2012-finding-fossil-groups-optical.md) | The Astrophysical Journal | 8/9 | full text |
| 2012 | [Cosmology from cluster mass per galaxy](papers/astro/2012-cosmological-constraints-galaxy-clustering.md) | The Astrophysical Journal | 11/11 | full text |
| 2012 | [Distant supernovae in old, dust-poor galaxies](papers/astro/2012-hubble-space-telescope-cluster-4.md) | The Astrophysical Journal, 750, 1 | 21/39 | partial full text |
| 2012 | [Distant supernovae sharpen dark-energy limits](papers/astro/2012-hubble-space-telescope-cluster-1.md) | The Astrophysical Journal | 36/66 | full text |
| 2012 | [How often stars explode as Type Ia supernovae](papers/astro/2012-hubble-space-telescope-cluster-2.md) | The Astrophysical Journal | 22/43 | full text |
| 2012 | [Mass profiles of 28 lensing clusters](papers/astro/2012-combined-strong-weak-lensing.md) | Monthly Notices of the Royal Astronomica | 8/8 | partial full text |
| 2012 | [Supernova rates in distant galaxy clusters](papers/astro/2012-hubble-space-telescope-cluster-3.md) | The Astrophysical Journal | 22/43 | full text |
| 2012 | [Un-stretching a magnified distant galaxy](papers/astro/2012-sourceplane-reconstruction-bright-lensed.md) | The Astrophysical Journal | 5/7 | full text |
| 2011 | [Are strong-lensing clusters too concentrated?](papers/astro/2011-sunyaevzeldovich-effect-observations-strong.md) | The Astrophysical Journal | 17/26 | full text |
| 2011 | [How far away are giant lensed arcs?](papers/astro/2011-redshift-distribution-giant-arcs.md) | The Astrophysical Journal Letters | 6/7 | full text |
| 2011 | [Spectra of clusters that bend light](papers/astro/2011-geminigmos-spectroscopy-26-stronglensingselected.md) | The Astrophysical Journal Supplement Ser | 4/7 | full text |
| 2011 | [Too many massive clusters, too early?](papers/astro/2011-scaling-relations-overabundance-massive.md) | The Astrophysical Journal | 8/25 | full text |
| 2011 | [What blurs cluster galaxy counts](papers/astro/2011-extrinsic-sources-scatter-richnessmass.md) | The Astrophysical Journal | 3/7 | full text |
| 2010 | [A catalog of 55,424 galaxy clusters](papers/astro/2010-gmbcg-galaxy-cluster-catalog.md) | The Astrophysical Journal Supplement Ser | 3/14 | full text |
| 2010 | [A very bright lensed galaxy at z = 1.7](papers/astro/2010-bright-spatially-extended-lensed.md) | The Astrophysical Journal | 9/10 | full text |
| 2010 | [Central galaxies line up with clusters](papers/astro/2010-alignment-brightest-cluster-galaxies.md) | Monthly Notices of the Royal Astronomica | 4/5 | full text |
| 2010 | [Cosmology from counting maxBCG clusters](papers/astro/2010-cosmological-constraints-sloan-digital.md) | The Astrophysical Journal | 11/14 | full text |
| 2010 | [Faint red cluster galaxies arrived late](papers/astro/2010-growth-redsequence-clusters-since.md) | Highlights of Astronomy (Vol. 15, XXVIIt | 3/6 | full text |
| 2010 | [Two magnified galaxies at redshift 3](papers/astro/2010-two-lensed-z-3.md) | The Astrophysical Journal Letters, 723,  | first | full text |
| 2010 | [Two magnified galaxies from the early universe](papers/astro/2010-two-lensed-lyman-emitting.md) | The Astrophysical Journal | 6/7 | full text |
| 2010 | [X-ray checks on fossil galaxy groups](papers/astro/2010-large-xray-sample-fossil.md) | Highlights of Astronomy | 6/6 | full text |
| 2009 | [A better galaxy count for cluster mass](papers/astro/2009-improvement-richness-estimates-maxbcg.md) | The Astrophysical Journal | 3/14 | full text |
| 2009 | [Are lensing clusters too concentrated?](papers/astro/2009-subaru-weak-lensing-measurements.md) | The Astrophysical Journal | 7/9 | full text |
| 2009 | [Catching a supernova in its first days](papers/astro/2009-early-spectroscopic-identification-sn.md) | The Astrophysical Journal Letters | 27/30 | full text |
| 2009 | [Finding distant supernovae by watching clusters](papers/astro/2009-intensive-hubble-space-telescope.md) | The Astronomical Journal | 30/61 | full text |
| 2009 | [How much mass per unit light in clusters](papers/astro/2009-crosscorrelation-weak-lensing-sdss-2.md) | The Astrophysical Journal | 8/11 | full text |
| 2009 | [How well galaxy counts track cluster mass](papers/astro/2009-constraining-scatter-massrichness-relation.md) | The Astrophysical Journal | 7/13 | full text |
| 2009 | [Measuring the red sequence without error bias](papers/astro/2009-precision-measurements-cluster-red.md) | The Astrophysical Journal | 2/13 | full text |
| 2009 | [Optically found clusters have younger galaxies](papers/astro/2009-galaxy-clusters-formation-determining.md) | arXiv e-prints | first | full text |
| 2009 | [Weighing SDSS clusters with weak lensing](papers/astro/2009-crosscorrelation-weak-lensing-sdss-1.md) | The Astrophysical Journal | 4/15 | full text |
| 2009 | [What galaxies live in clusters](papers/astro/2009-galaxy-content-sdss-clusters.md) | The Astrophysical Journal | 4/4 | full text |
| 2008 | [Finding new giant gravitational arcs](papers/astro/2008-new-survey-giant-arcs.md) | The Astronomical Journal | 5/14 | full text |
| 2008 | [How X-ray bright are optically found clusters?](papers/astro/2008-measuring-mean-scatter-xray.md) | The Astrophysical Journal | 6/9 | full text |
| 2008 | [How cluster X-ray brightness tracks mass](papers/astro/2008-lsubxsubm-relation-clusters-galaxies.md) | Monthly Notices of the Royal Astronomica | 6/11 | full text |
| 2007 | [Counting clusters to weigh the universe](papers/astro/2007-cosmological-constraints-sdss-maxbcg.md) | arXiv e-prints | 3/9 | full text |
| 2007 | [Detecting dust inside galaxy clusters](papers/astro/2007-dust-content-galaxy-clusters.md) | The Astrophysical Journal Letters | 2/3 | full text |
| 2007 | [How fast galaxies move in maxBCG clusters](papers/astro/2007-mean-scatter-velocity-dispersionoptical.md) | The Astrophysical Journal | 3/12 | full text |
| 2007 | [Turning cluster catalogs into cosmology measurements](papers/astro/2007-opticallyselected-cluster-catalogs-precision.md) | arXiv e-prints | 3/5 | full text |
| 2007 | [Weighing SDSS clusters by stacking lensing](papers/astro/2007-crosscorrelation-weak-lensing-sdss.md) | arXiv e-prints | 5/10 | full text |
| 2006 | [Finding galaxy clusters in Sloan imaging](papers/astro/2006-maxbcg-systematic-discovery-characterization.md) | Ph.D. dissertation (Physics), University | first | full text |
| 2006 | [Hunting the host of a short burst](papers/astro/2006-closing-shorthard-burst-progenitor.md) | The Astrophysical Journal | 22/28 | full text |
| 2012 | [Astronomy's clustering statistic applied to the genome](papers/bio/2012-longrange-autocorrelations-cpg-islands.md) | PLoS ONE | first | full text |
| 2001 | [A short receptor variant doesn't explain drug response](papers/bio/2001-expression-mrna-encoding-truncated.md) | Molecular and Cellular Biochemistry, 217 | 3/7 | abstract only |

## Order of work

1. Consolidate the grade-penalty repos and archive the tutorial clutter
2. Rename LARC column names in TOF and LASI_2019_equity
3. Publications page on benkoester.com, generated from the publications JSON
4. Clean up big-ten-jobs and ec2-infra and make them public
5. Build the Midwestern State simulator
6. Attrition case study on the simulator
7. Databricks medallion pipeline and catalogue on the same data
8. File the M-Inform outside-activity disclosure before the first paid engagement
