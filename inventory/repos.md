# Repo inventory

Every repo under `bkoester`, as of 2026-11-08. Visibility is current GitHub visibility; Action is what the
portfolio needs from it.

| Repo | Visibility | Bucket | Project | Action |
| --- | --- | --- | --- | --- |
| ec2-infra | private | live | [ec2-platform](../projects/live/ec2-platform.md) | Strip account IDs and the default subnet ID; then public |
| ec2-apps | private | live | [ec2-platform](../projects/live/ec2-platform.md) | Review for secrets; then public alongside ec2-infra |
| big-ten-jobs | private | live | [big-ten-jobs](../projects/live/big-ten-jobs.md) | Remove personal search and fit scoring; check history for .env; then public |
| ask-ben | public | live | [ask-ben](../projects/live/ask-ben.md) | Review eval results |
| site | public | live | [ask-ben](../projects/live/ask-ben.md) | Add projects and publications pages |
| wcc-pathfinder | private | live | [wcc-pathfinder](../projects/live/wcc-pathfinder.md) | Write case study; then public |
| college-scraper | public | live | [college-scraper](../projects/live/college-scraper.md) | Fold setup docs into one README |
| workspace | private | live | [ec2-platform](../projects/live/ec2-platform.md) | Keep private; mention as an app on the host |
| pages | private | live | [ec2-platform](../projects/live/ec2-platform.md) | Keep private |
| solar | private | live | [solar](../projects/live/solar.md) | Keep private (site location, station ID); case study written from it |
| solar_docker | private | live | [solar](../projects/live/solar.md) | Empty; superseded by solar; archive |
| cloud9solar | private | live | [solar](../projects/live/solar.md) | Earliest version; superseded by solar; archive |
| journal-dashboard | private | live | [ec2-platform](../projects/live/ec2-platform.md) | Keep private; mention as an app on the host |
| fantrax | private | personal | — | Keep private |
| whatsapp-nick-bot | private | personal | — | Keep private |
| claude-code-prompts | private | personal | — | Keep private |
| car-search | private, archived | live | [car-search](../projects/live/car-search.md) | History clean (no keys, VINs or personal notes); optional scrub of S3 bucket and laptop paths; then public |
| wod-search-firestore | private | personal | — | Keep private |
| publications | ? | past | [publications.md](../publications.md) | Add a site-page output to generate_outputs.py |
| PLA | public | past | [grade-penalties](../projects/past/grade-penalties.md) | Becomes the consolidated home; README states data is synthetic |
| pla-devel | public | past | [grade-penalties](../projects/past/grade-penalties.md) | Archive after folding into PLA |
| aim-analytics | public | past | [grade-penalties](../projects/past/grade-penalties.md) | Archive after folding into PLA |
| cic-gp | public | past | [grade-penalties](../projects/past/grade-penalties.md) | Archive after folding into PLA |
| TOF | public | past | [transcript-of-the-future](../projects/past/transcript-of-the-future.md) | Rename LARC column names to generic ones |
| TOF2Paper | private | past | [transcript-of-the-future](../projects/past/transcript-of-the-future.md) | Decide: preprint or retire |
| SEISMIC | public | past | [seismic](../projects/past/seismic.md) | Delete LARC SQL and rename columns, or make private |
| LASI_2019_equity | public | past | [lasi-equity-workshop](../projects/past/lasi-equity-workshop.md) | Rename columns |
| acad_network | public, fork | past | [campus-networks](../projects/past/campus-networks.md) | Merge into one networks repo |
| unizin | public | past | [campus-networks](../projects/past/campus-networks.md) | Merge into one networks repo |
| NetworkWeightingManuscript | private | past | [campus-networks](../projects/past/campus-networks.md) | Settle: blog post, preprint, or retire |
| SSU | public | past | [synthetic-transcripts](../projects/past/synthetic-transcripts.md) | Refresh dependencies; add worked example |
| calibrated-GPA | public, fork | past | [synthetic-transcripts](../projects/past/synthetic-transcripts.md) | Add a README or archive |
| LARC | public | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Contains internal table and column names; make private |
| aws_larc_pipeline | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| aws_larc_cookbook | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| larc_redshift_load | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| LARC_lambda_process | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| larc_pure_python | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| larc-sql-test | private | past | [larc-infrastructure](../projects/past/larc-infrastructure.md) | Keep private |
| sql_redshift_queries | private | past | — | Not yet reviewed |
| lsa_restricted | private | past | — | Not reviewed (access declined); keep private |
| enrollment-predictor | private, fork | past | — | Not reviewed (access declined) |
| sythetic_resume | private | — | — | Stub; archive |
| CCF_module2 | public | — | — | Course exercise; archive |
| scaffold | public | — | — | Course exercise; archive |
| sagemaker_ops | public | — | — | Stub; archive |
| hugotest | public | — | — | Archive |
| bkoester.github.io | public | — | — | Old site; archive or redirect to benkoester.com |
| learning_docker | public, fork | — | — | Archive |
| Python-MLOps-Cookbook | public, fork | — | — | Archive |
| github-actions-demo | public, fork | — | — | Archive |
| gcp-flask-ml-deploy | public, fork | — | — | Archive |
| Flask-Elastic-Beanstalk | public, fork | — | — | Archive |
| PRIMsrc | public, fork | — | — | Archive |
| so-simple-theme | public, fork | — | — | Archive |
| rfortraders | public, fork | — | — | Archive |
| coursera-android-labs | public, fork | — | — | Archive |
| frontend-nanodegree-resume | public, fork | — | — | Archive |

Security notes from the review: no credentials, keys or connection strings were found in the full history of
any public repo. The PLA, pla-devel and aim-analytics student tables are synthetic. One SQL file in the public
LARC repo names internal warehouse tables and columns.
