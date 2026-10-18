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

# Infrastructure as code

> [!abstract] In one line
> Describing servers, networks and settings in files, so they're built the same way every time by a tool.

> [!tip] Think of it like
> A recipe instead of cooking from memory: anyone can make the same dish again.

## How it works

- Tools: Terraform, Bicep, Ansible, PowerShell DSC.
- **Declarative**: you say what you want; the tool works out the steps.
- Benefits: repeatable builds, review before change, easy disaster recovery, documentation that can't go stale.
- Always run a **plan** or **what-if** first to see what will change.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why run terraform plan or a Bicep what-if before applying?
> It shows exactly what will be created, changed or destroyed, so a mistake is caught before it happens.

## See also

[[Terraform]] · [[Bicep]] · [[Ansible]] · [[PowerShell DSC]]
