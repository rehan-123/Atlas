---
type: "concept"
level: "Mid"
category: "[[Cloud & DevOps concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Continuous integration and delivery

> [!abstract] In one line
> Automatic steps that test and deploy every change: continuous integration (test it) and continuous delivery (ship it).

> [!tip] Think of it like
> A factory line with quality checks at each station; a faulty part never reaches the shop.

> [!info]+ Words on this page
> **YAML**: A plain-text format used for configuration files and pipeline definitions; indentation matters.
> **pipeline**: A series of automated steps (test, build, deploy) that run on every change.
> *More in the [[Glossary]].*

## How it works

- **CI**: every push runs linting and tests, so mistakes are caught before they reach anyone.
- **CD**: a passing change is deployed automatically or with one approval.
- Pipelines are defined in YAML files stored with the code.
- For IT teams: pipelines can test PowerShell with Pester and deploy Bicep or Terraform.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What's the difference between CI and CD?
> CI tests and builds every change automatically; CD takes a tested change and deploys it.

## See also

[[GitHub Actions]] · [[Azure DevOps]] · [[Infrastructure as code]]
