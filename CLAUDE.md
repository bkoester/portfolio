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

## Writing case studies

- Every project file keeps its front matter current: `status` is one of `todo`, `in-progress`, `done`.
- Lead with the question and what came of it, then data, method, results, papers, repos.
- Cite papers by DOI. Results from restricted data are stated in general or relative terms only.
- Don't invent results. An unknown is written as an open question.
