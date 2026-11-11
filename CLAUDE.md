# Ground rules for this repo

This repo describes Ben Koester's work for a public audience. Anything written here may end up on the open web.

## Never in this repo

- U-M table, column, schema, server or system names (LARC field names, warehouse schemas, internal hostnames)
- Any record, sample, screenshot or chart built from U-M student or HR data
- Code copied from U-M work repositories
- Credentials, API keys, account IDs, Terraform plan or state files

## U-M HR work (projects/um-hr/)

- Describe it at the level in each file's "How to describe it publicly" section, no deeper.
- Public parallels use data generated from Ben's own assumptions or from public sources. Never fit a
  synthesizer (CTGAN, SDV or similar) to U-M records; that output is still derived from U-M data.
- Parallel code is written fresh, on personal equipment and time.

## Writing paper summaries (papers/)

- Summaries are written in our own words from the paper's text. No copied sentences; at most one
  short quote (under 15 words) per paper, in quotation marks.
- Every number must appear in the paper; note where with the finding. If unsure, leave it out.
- `source_read` says whether the summary came from the full text or only the abstract.
- "My role" comes from the paper's author-contributions statement, or from Ben. Never guessed.
- `status: reviewed` only after Ben has checked the summary.

## Writing case studies

- Every project file keeps its front matter current: `status` is one of `todo`, `in-progress`, `done`.
- Lead with the question and what came of it, then data, method, results, papers, repos.
- Cite papers by DOI. Results from restricted data are stated in general or relative terms only.
- Don't invent results. An unknown is written as an open question.

## Publishing to benkoester.com

- A case study reaches the site only with `status: done` and `publish: true`. Set `publish: true` only when Ben
  says to publish that one.
- The site copy is generated: run `node scripts/sync-case-studies.mjs ../portfolio` in the site repo, then
  commit there. Never edit the generated files.
- The site allows no job-search or consulting-pitch language. The sync drops "To resolve" and "Why it reads
  well to a client"; keep pitch language out of every other section.
- Put `<!-- alt: ... -->` on the line above a mermaid block; it becomes the diagram's alt text.
