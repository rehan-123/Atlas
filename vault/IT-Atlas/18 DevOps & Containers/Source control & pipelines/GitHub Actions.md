---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Source control & pipelines]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# GitHub Actions

> [!abstract] In plain words
> GitHub's built-in automation: workflows run on every push or on a schedule to test, build and deploy.
>
> **What kind of tool is this?** Source control keeps every version of code and scripts. CI/CD pipelines test and deploy changes automatically when someone pushes.

**Made by:** [[Microsoft]] · **Category:** [[DevOps & Containers]] › [[Source control & pipelines]]

> [!info]+ Words on this page
> **CI/CD**: Continuous integration and delivery: automatic testing and deployment of every change.
> **YAML**: A plain-text format used for configuration files and pipeline definitions; indentation matters.
> **pipeline**: A series of automated steps (test, build, deploy) that run on every change.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **branch**: A separate line of changes in Git, merged back into main after review.
> *More in the [[Glossary]].*

## In more detail

CI/CD defined in YAML under .github/workflows: jobs run on GitHub-hosted or self-hosted runners, with secrets stored per repo or environment.

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Workflow didn't start | Check the on: trigger and branch filters in the YAML |
| Secret is empty | Secrets aren't passed to workflows from forks; check the secret name and environment |

## See also

[[GitHub]] · [[Continuous integration and delivery]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
