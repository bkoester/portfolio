---
title: College scraper
bucket: live
status: todo
visibility: public
repos: [college-scraper]
papers: []
next: Fold the 15 setup documents into one README
---

# College scraper

An agent that reads university websites and pulls out structured facts, using a local language model (Ollama) to
decide where to go and Microsoft's Playwright MCP server to drive the browser.

## Approach

Config-driven targets; robots.txt checks; IPEDS and Wikipedia as supporting sources; results as JSON with
confidence scores; optional Excel input and output; Docker Compose for the model and browser.

## Results

Open question: which schools it was run on, and how accurate the extracted fields were.

## Code

- [college-scraper](https://github.com/bkoester/college-scraper)

## To resolve

- [ ] Fold ARCHITECTURE, QUICKSTART, TESTING and the other setup docs into one README
- [ ] Add one example run with output
