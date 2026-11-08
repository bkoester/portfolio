---
title: HR chatbot
bucket: um-hr
status: todo
visibility: description-only
repos: []
papers: []
next: Build a public demo over a public HR policy handbook
---

# HR chatbot

## How to describe it publicly

Shipped a retrieval-augmented assistant embedded on a large university's HR website: about 900 pages chunked from
HTML, a moderator that keeps questions in scope, traced conversations, nightly metrics, and golden-query
regression tests. Replaced dashboard-checking with generated reports for leadership.

## Public parallel

- [Ask Ben](../live/ask-ben.md) already shows retrieval, scoping and evaluation on public content.
- Add a small demo over a public HR policy handbook that declines out-of-scope questions, with a golden-query
  test set and a one-page report of its scores.

## Data for the parallel

Public policy documents only.

## To resolve

- [ ] Choose the public handbook
- [ ] Build the demo with its own golden queries
