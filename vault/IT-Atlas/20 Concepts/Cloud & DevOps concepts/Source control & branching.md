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

# Source control & branching

> [!abstract] In one line
> Keeping every version of code and scripts in Git, and making changes on branches that are reviewed before merging.

> [!tip] Think of it like
> Track changes in Word, but for a whole folder, with every saved version kept forever.

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **repository**: Where backups are stored.
> **branch**: A separate line of changes in Git, merged back into main after review.
> **pull request**: A request to review and merge changes from one branch into another.
> *More in the [[Glossary]].*

## How it works

- A **repository** holds the files and their full history.
- A **branch** is a safe copy to work on; **main** is what's live.
- A **pull request** asks for review before a branch is merged into main.
- Put PowerShell scripts, RMM procedures and infrastructure code in Git: you get history, review and rollback for free.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A script change broke production. How does Git help?
> You can see exactly what changed and who changed it, and revert to the last good version.

## See also

[[Git]] · [[GitHub]] · [[Continuous integration and delivery]]
