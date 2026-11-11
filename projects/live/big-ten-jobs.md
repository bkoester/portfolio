---
title: University job postings tracker
bucket: live
status: in-progress
publish: false
visibility: description-only
repos: [big-ten-jobs]
papers: []
next: Ben checks the write-up; re-run the findings script for the weekly counts
---

# University job postings tracker

What do large universities hire for, how long do postings stay open, and what do they pay? A daily scraper has
recorded 27,637 postings at eleven universities, with an explorer on top. The clearest finding so far: whether
a posting states its pay follows state law almost exactly.

## The problem

University hiring is spread across separate applicant-tracking systems with no shared view. Each site shows
what is open today and nothing about what opened last month, when it closed, or how one school compares with
another.

## Data

Public job postings from eleven universities: Michigan, Ohio State, Penn State, Maryland, USC, Purdue, UT
Austin, Texas A&M, Iowa State, Washington State and Louisville. One row per posting: title, location, full or
part time, posting dates, a salary range where the description states one, the description text, and three
fields the scraper adds itself: first seen, last seen, and whether the posting is still listed. Michigan
exposes more (department, work mode, pay class); the others do not.

## Approach

- **Survey first.** Before writing a second scraper, a scan of all 18 Big Ten career sites recorded each one's
  platform and robots.txt. Eighteen schools collapsed to about seven platforms, so the work is one extractor
  per platform, not one per school. Four schools whose robots.txt disallows crawlers were left out.
- **Three extractors.** Workday's JSON endpoint covers nine of the eleven schools, SuccessFactors covers
  Purdue, and Michigan's own site is crawled as HTML.
- **Two-phase crawl.** List every posting ID first, compare with the database, and fetch full details only for
  postings not seen before. A re-run on an unchanged school takes minutes instead of hours.
- **One table.** SQLite, keyed by posting, with first-seen, last-seen and active maintained by a daily diff.
  That is what turns a list of today's jobs into a history.
- **Salary parsing.** Pay is read from description text: only lines that mention salary, pay or wage, stray
  small dollar amounts dropped, hourly and annual figures kept apart.
- **Explorer.** A read-only FastAPI service and a SvelteKit front end over the same file: a filterable table
  with full-text search of descriptions, per-school activity, and what is new since the last crawl. The
  scraper is the only writer.
- **Operations.** Two containers and daily timers on the [EC2 host](ec2-platform.md).

## Results

From `tools/big_ten_findings.py`, run against the database on 11 November 2026 (output in
`data/big_ten_findings_2026-11-11.json`). 27,637 postings recorded; 6,333 open that day.

**Stated pay follows state law**

Share of open postings where the scraper found a pay figure:

| University | State | Postings with pay | State requires pay in postings |
| --- | --- | --- | --- |
| Washington State | WA | 93% | yes, since 2023 |
| USC | CA | 89% | yes, since 2023 |
| Maryland | MD | 85% | yes, since October 2024 |
| Michigan | MI | 45% | no |
| Penn State | PA | 26% | no |
| UT Austin | TX | 21% | no |
| Texas A&M | TX | 14% | no |
| Ohio State | OH | 11% | no |
| Louisville | KY | 6% | no |
| Iowa State | IA | 1% | no |
| Purdue | IN | 0% | no |

The three universities in states with a pay-transparency law state pay on 85 to 93% of postings. No other
school reaches half. Open question: Purdue's 0% across 476 postings may be the SuccessFactors extractor not
reading pay at all, not Purdue never stating it.

**Two posting styles**

Median days a posting stayed listed, closed postings only:

- Six schools close in about two weeks, with a narrow spread: Texas A&M 9, Michigan 11, Ohio State 11, Iowa
  State 12, Louisville 13, Washington State 14. Half of Michigan's 6,426 closed postings ran 7 to 15 days,
  which looks like a fixed posting window.
- Five run two to three times longer, with a wide spread: UT Austin 19, USC 24, Penn State 26, Purdue 31,
  Maryland 32.5 (a quarter of Maryland's ran past 71 days).

Postings still open are not counted, so the long-running ones are understated.

**Michigan's work modes**

Of 884 open postings, 70% are on-site, 26% hybrid and 3% remote.

**What the numbers exposed**

- Pay amounts are not yet comparable across schools. Washington State states monthly pay, which is stored as
  annual (median "annual" pay of $6,943); one Iowa State posting parsed as $3.5 million; Maryland's hourly
  median of $82.50 is not credible. Coverage holds up; amounts need the parser fixed first.
- Outside Michigan, no school shows more than three days in a row without a new or closed posting since May,
  and those runs fall on weekends and holidays. Michigan's history before May 2026 is sparse, not daily.
- Open question: new postings per week. The first run returned nothing for it (a date function the host's
  database lacks); the script is fixed and needs one more run.

## Running it

- **A retry storm of its own making.** In July 2026 Michigan's crawl failed every day for about nine days on
  truncated responses. The host's catch-up logic decided whether today's crawl had run by looking for a file
  written only after a fully successful Michigan crawl, so every Spot replacement re-ran the whole batch: 6 to
  16 times a day against a site that was already struggling. The fix was retries with backoff and a marker
  written after every attempt, success or failure. A week later the same flakiness came back in another shape
  (a completed response marked HTTP 520), which the first fix did not cover.
- **Two IDs for one job.** Purdue's listing page and detail page identified a posting by different numbers, so
  every daily diff saw nothing unchanged and re-inserted the whole listing.
- **Configuration that lived only on the server.** Five of the eleven schools had been added by editing the
  copy on the host and were never committed. The explorer, with six schools hardcoded, silently hid them. The
  registry was recovered into the repo and the explorer now reads its school list from the data.
- **Salary edge cases.** Bonus and raise amounts read as wages, and hourly and annual figures merged into one
  range.
- A daily digest email was tried and dropped; the explorer proved more useful
  ([what came and went](ec2-platform.md)).

## Code

- big-ten-jobs (private until cleaned up): extractors, diff and store, tests, the API and the explorer

## What I'd do differently

- Record every crawl attempt from day one, not only the successes. The retry storm came from treating "no
  success yet" as "not tried yet".
- Never edit configuration on the server. Five schools existed nowhere but one disk.

## To resolve

- [x] Findings script run on the host (2026-11-11); Results written from it
- [ ] Re-run the script for weekly counts (same command; the week calculation is fixed)
- [ ] Check whether the SuccessFactors extractor parses pay at all (Purdue 0%)
- [ ] Fix pay parsing: monthly pay (Washington State), implausible outliers, Maryland hourly
- [ ] Charts: pay coverage by state law; days listed by school
- [ ] Ben: check "What I'd do differently"
- [ ] Ben: decide how the public page names the sites. The repo's own survey notes that Workday's terms ask
      for written permission for automated access and that one school's robots.txt disallows its search path
- [ ] The repo also holds a personal job feed and fit scoring. They stay out of this write-up and need to come
      out of the repo (or onto a private branch) before it goes public
- [ ] Check history for any committed .env or API keys
