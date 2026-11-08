---
title: Ask Ben
bucket: live
status: todo
visibility: public
repos: [ask-ben, site]
papers: []
next: Review the eval results before pointing people at it
---

# Ask Ben

benkoester.com with an ask-me-anything chat that answers from Ben's own writing and project notes. It is also
the public twin of the [HR chatbot](../um-hr/hr-chatbot.md): the same retrieval, scoping and evaluation craft,
on content anyone can see.

## Approach

Retrieval over a personal corpus with a database, an API and an evaluation service, running as containers on
the [EC2 host](ec2-platform.md) behind a tunnel.

## Results

Open question: what the eval measures and how it scores today.

## Code

- [ask-ben](https://github.com/bkoester/ask-ben)
- [site](https://github.com/bkoester/site)

## To resolve

- [ ] Review the ask-ben code and eval results
- [ ] Add projects and publications pages to the site, fed from this repo and bkoester/publications
