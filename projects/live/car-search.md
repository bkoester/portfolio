---
title: Car search
bucket: live
status: todo
visibility: public
repos: [car-search]
papers: []
next: Make the repo public; write the case study
---

# Car search

A data-backed used-car decision tool: every hybrid and plug-in hybrid listing within 100 miles of Ann Arbor,
joined to federal safety, recall, complaint, fuel-economy and insurance-loss data, with AI digests and research
dossiers per model-year. Built for one real purchase, used to completion, and archived on 2026-11-07.

## The problem

Car listings show price and miles. Whether a given model-year has a known hybrid-system problem, what owners
complain about, and whether a price is good for that exact car are scattered across a dozen government and
industry sources.

## Data

- Listings and private-seller ads from the Marketcheck API, kept to a 450-call monthly budget with a ledger
- NHTSA safety ratings, recalls, owner complaints, and manufacturer service bulletins (flat files, five-year
  spans)
- EPA fuel economy, electric range and charge times
- IIHS-HLDI insurance-loss indexes by model

## Approach

- Python ingestion with deduplication rules (dealer groups that re-list national inventory, placeholder VINs)
- SQLite with full price history; delisted cars kept as a "gone" view, the closest free proxy for sold prices
- FastAPI back end and SvelteKit front end: sortable table, price map coloured against the median of comparable
  cars, histograms by price, miles and days on market
- Claude Haiku on Bedrock digests owner complaints per model-year on demand, told to count honestly and add no
  outside knowledge
- A Claude Code worker on the [EC2 host](ec2-platform.md) writes cited research dossiers and ranks a shortlist
  against an editable preference text; it sees model-year facts only, never a VIN or dealer
- Every metered or paid action is password-gated and fails closed

## Results

Open question: how many listings and model-years it tracked, and how the ranking held up against the car
actually bought.

## Code

- [car-search](https://github.com/bkoester/car-search)

## To resolve

- [ ] Make the repo public (it is archived; if GitHub won't change visibility while archived, unarchive, flip, re-archive)
- [ ] Optional scrub before flipping: ARCHIVED.md names the S3 backup bucket and SSM parameter paths, and
      CLAUDE.md has laptop paths. None are secrets, but there's no reason to publish them
- [ ] Two or three screenshots for the case study
