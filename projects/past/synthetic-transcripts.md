---
title: Synthetic student transcripts (SSU)
bucket: past
status: todo
visibility: public
repos: [SSU, calibrated-GPA]
papers: []
next: Refresh dependencies and add a worked example
---

# Synthetic student transcripts (SSU)

A generator for realistic synthetic student records, course enrollments and terms, so learning-analytics code can
be shared, taught and tested without restricted data.

## The problem

Analytics code built on student records can't be shared with the records. Without data, nobody can run it.

## Approach

Python generator (`make_data.create_student_struct(n)`) producing student, course and term tables; CI on GitHub
Actions across Python 3.7 to 3.10; runs on EC2. calibrated-GPA holds related notebooks on synthetic GPA
calibration (linear and logistic).

## Why it matters now

This is the precedent for the Midwestern State simulator in [um-hr/attrition](../um-hr/attrition.md): the same
idea, applied to a workforce instead of a student body.

## Code

- [SSU](https://github.com/bkoester/SSU)
- [calibrated-GPA](https://github.com/bkoester/calibrated-GPA)

## To resolve

- [ ] Refresh dependencies for current Python
- [ ] Add a worked example: generate data, run one TOF or PLA analysis on it
- [ ] Give calibrated-GPA a README or archive it
