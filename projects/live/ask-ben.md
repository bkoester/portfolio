---
title: Ask Ben
bucket: live
status: todo
visibility: public
repos: [ask-ben, site]
papers: []
next: Ben writes the first published answers; the bot has nothing to answer from yet
---

# Ask Ben

benkoester.com with an ask-me-anything chat that answers from Ben's own writing and project notes. It is also
the public twin of the [HR chatbot](../um-hr/hr-chatbot.md): the same retrieval, scoping and evaluation craft,
on content anyone can see.

## Approach

Retrieval over a personal corpus with a database, an API and an evaluation service, running as containers on
the [EC2 host](ec2-platform.md) behind a tunnel.

## Where it stands (November 2026)

Built and wired in September 2026, not launched. The design is complete: answers Ben wrote for publication are
embedded into Postgres with pgvector; a question first meets a deterministic off-limits check that never calls
a model, then a similarity threshold that declines when nothing relevant is found, and only then a model that
must cite its sources. A daily spend cap takes the bot offline, and a ten-question golden set with an LLM judge
is ready to run.

What is missing is content. The corpus is empty, the golden set points at answers not yet written, no
evaluation has run, and the off-limits wording is a placeholder.

## Results

Open question: none yet. The first evaluation run needs the first published answers.

## Code

- [ask-ben](https://github.com/bkoester/ask-ben)
- [site](https://github.com/bkoester/site)

## To resolve

- [x] Review the ask-ben code and eval state (scaffold complete; corpus and eval history empty)
- [x] Projects and publications pages on the site
- [ ] Ben: write the first batch of published answers for the corpus
- [ ] Ben: confirm the off-limits wording
- [ ] Run the first evaluation and hand-label about 30 answers to check the judge
