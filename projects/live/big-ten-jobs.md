---
title: University job postings tracker
bucket: live
status: in-progress
publish: false
visibility: description-only
repos: [big-ten-jobs]
papers: []
next: Ben runs tools/big_ten_findings.py against the database so the Results can be written
---

# University job postings tracker

What do large universities hire for, how long do postings stay open, and what do they pay? A daily scraper has
recorded every posting at eleven universities since May 2026, with an explorer on top; the findings are still
to be pulled from the data.

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
- **Salary parsing.** Pay is read from description text: only lines that mention salary, pay or wage, small
  amounts such as bonuses dropped, hourly and annual figures kept apart.
- **Explorer.** A read-only FastAPI service and a SvelteKit front end over the same file: a filterable table
  with full-text search of descriptions, per-school activity, and what is new since the last crawl. The
  scraper is the only writer.
- **Operations.** Two containers and daily timers on the [EC2 host](ec2-platform.md).

## Results

Open question: the findings. `tools/big_ten_findings.py` in this repo produces them from the database as
counts and medians by school:

- Postings and active postings per school
- New postings per week, per school
- How long postings stay open
- Salary coverage and median pay, hourly and annual
- Michigan's split between on-site, hybrid and remote

## Running it

- **A retry storm of its own making.** In July 2026 Michigan's crawl failed every day for about two weeks on
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
- **Salary edge cases.** Sign-on bonuses read as wages, and hourly and annual figures merged into one range.
- A daily digest email was tried and dropped; the explorer proved more useful
  ([what came and went](ec2-platform.md)).

## Code

- big-ten-jobs (private until cleaned up): extractors, diff and store, tests, the API and the explorer

## What I'd do differently

- Record every crawl attempt from day one, not only the successes. The retry storm came from treating "no
  success yet" as "not tried yet".
- Never edit configuration on the server. Five schools existed nowhere but one disk.

## To resolve

- [ ] Ben: run `python3 tools/big_ten_findings.py <path to um_careers.db> > big_ten_findings.json` and send the
      file; then write Results with two or three charts
- [ ] Ben: check "What I'd do differently"
- [ ] Ben: decide how the public page names the sites. The repo's own survey notes that Workday's terms ask
      for written permission for automated access and that one school's robots.txt disallows its search path
- [ ] The repo also holds a personal job feed and fit scoring. They stay out of this write-up and need to come
      out of the repo (or onto a private branch) before it goes public
- [ ] Check history for any committed .env or API keys
