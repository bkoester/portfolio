---
title: Home solar and battery advisor
bucket: live
status: in-progress
visibility: description-only
repos: [solar, cloud9solar, solar_docker]
papers: []
next: Ben checks the write-up and decides whether the dollar figures go public
---

# Home solar and battery advisor

Can a home battery be charged smarter by forecasting tomorrow's sun? Somewhat: a year of 15-minute data showed
that a plain monthly average predicts generation as well as anything fancier, that the money at stake in the
recommendation is small, and that keeping the pipeline alive and its alerts quiet was the harder problem.

## The problem

A house with rooftop solar and a battery, on a time-of-day electricity rate with a 3 to 7 PM peak. Each night
the battery needs a charge target: leave room for tomorrow's sun, or fill from the grid because tomorrow will
be dark. Getting it right needs a forecast of tomorrow's generation, and the panels are partly shaded by trees,
which generic forecast services know nothing about.

## Data

Four sources on a shared 15-minute grid, January 2025 to April 2026 (467 days, about 45,000 rows):

- Inverter readings: production, consumption, grid purchase and export
- Battery state: charge level, power, temperature
- A rooftop weather station: temperature, humidity, wind, solar radiation, rain
- A commercial solar forecast, snapshotted about 96 times a day, so each forecast can be compared with the
  ones made before and after it

All of it lands in S3 as daily Parquet files written by scheduled Lambda functions. The location and the
household's consumption patterns stay out of this write-up.

## Approach

**The analysis**, in four notebooks:

1. **Checks and a shading model.** Energy-balance checks on the raw readings, then a Fourier model of how much
   of the clear-sky sun reaches the panels by day of year and hour, fitted on 75 clear days.
2. **Backtest.** The commercial forecast, raw and shade-corrected, against what the panels produced on 453
   days. Then the decision it feeds: would each version have called the battery filling early, and what does a
   wrong call cost?
3. **Forecast inspection.** How the commercial forecast for one afternoon hour changes through the day.
4. **A clean model.** Drop the commercial forecast and the shading model. Predict tomorrow from the monthly
   average scaled by how yesterday went, and shape the day with the average 15-minute profile for that month,
   which has the tree shading built in.

**The live system** built from notebook 4:

- A dozen Lambda functions (AWS SAM): nightly data pulls, the nightly charge recommendation, an hourly storm
  check against the National Weather Service, intraday checks every 30 minutes, and a daily evaluation that
  scores yesterday's prediction against what happened.
- A Streamlit dashboard on the [EC2 host](ec2-platform.md): tomorrow's forecast, alerts, and accuracy and
  savings over time.
- An alert layer where Claude Haiku on Bedrock reads each new signal and decides whether it is worth sending
  and how to word it.
- A Discord bot with twelve tools for live status, history, weather and forecasts, plus Athena queries over
  the same Parquet files for questions the fixed tools could not answer.

## Results

**Forecasting**

- The commercial forecast missed daily generation by 8.4 kWh on average and ran 7.3 kWh high. The shading
  correction cut the miss to 4.4 kWh, though it then ran 3.4 kWh low (shading model R² 0.81).
- The simplest model did as well. The monthly average alone missed by 4.4 kWh; adjusting it by yesterday's
  output made it slightly worse (4.9 kWh).
- The commercial forecast's intraday updates swung by thousands of watts for the same hour, in both
  directions.

**The decision**

- When the raw and corrected forecasts disagreed about an afternoon export window, the corrected one was right
  64% of the time. Precision rose from 0.46 to 0.75, at the cost of recall falling from 0.98 to 0.40.
- The money is small. Acting on a wrong recommendation cost about $52 a year with the raw forecast and $23 with
  the corrected one. The shading model only pays off when more than about 1.9 kWh of load is being shifted at a
  time.
- Moving heavy loads into sunny peak hours was worth at most about $52 over the whole period.

**What the system is worth**

- Solar plus battery cut the bill by 64.5% against buying everything from the grid: $842 over 467 days, about
  $659 a year, with 52% of consumption covered without the grid.

**Open questions**

- How the live model has done since April 2026. The daily evaluation log has the answer.
- Why the dashboard was changed in June 2026 from an advisor that told you what to do into a reporting page.

## Running it

Most of the work after the notebooks went into operations, and the history records what broke:

- **Alert fatigue.** The storm check alone was sending about 176 emails a month. The Haiku layer now passes
  only what has materially changed, and routine messages moved from email to Discord. In simulation the
  intraday battery alert would have fired on 77% of days.
- **An eight-week silent outage.** A library upgrade (pyarrow 25) misread the system's own Parquet files, but
  only on ARM processors, so it could not be reproduced on a laptop. The nightly recommendation, intraday
  checks and daily evaluation all died from mid-July to early September 2026 while storm alerts kept flowing
  and hid the failure. The fix was a version pin and a dead-man check that reports when an expected file has
  not landed, kept separate from the alert layer it guards.
- **A bot that sounded right and was wrong.** Monthly rainfall totals ran 40 to 80% high because a daily
  counter that resets at local midnight was being grouped by UTC day, so rainy days were counted twice. The
  bot was also adding a month of daily values in its head; the query now returns the total. Separately, a
  300-token output cap was cutting off its tool calls, so it kept replying "let me pull that" and never did.
- **Mixed column types.** Letting each day's file infer its own types meant a dry day stored rainfall as an
  integer and a wet day as a decimal, which broke every Athena query that touched both. All writers now share
  one explicit schema.
- **Data that was never pulled.** The nightly job only ever fetched yesterday, so "how does this August compare
  with the last four?" could not be answered until a backfill recovered about six years of weather history.

The bot is one of the cases behind the lesson in the [EC2 write-up](ec2-platform.md): fixed tools answer the
questions you thought of, and the ad hoc query tools only became reliable once the queries themselves handled
local days and returned totals, instead of leaving that to the model.

## Code

- solar (private): notebooks, the recommender package, the SAM project, the dashboard and the bot
- cloud9solar and solar_docker (private): earlier versions, superseded

## What I'd do differently

- Start with the dumbest baseline. The monthly average was available on day one and nothing beat it.
- Put the dead-man check in before the first alert. The outage ran eight weeks because nothing was watching
  for silence.

## To resolve

- [ ] Ben: check the write-up, and whether the dollar figures go public
- [ ] Ben: check "What I'd do differently"
- [ ] Notebook 4's closing summary quotes errors of about 4.5 and 6.65 kWh; its own outputs say 4.85 and 8.43
- [ ] Pull the live evaluation log and report accuracy since April 2026
- [ ] Why the dashboard pivoted from advisor to reporting
- [ ] Before the repo could go public: remove the site location and station ID, and a code comment that names
      a utility bill file
- [ ] One or two figures: forecast against actual, and the shading surface
