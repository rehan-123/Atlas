---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Patch rings

> [!abstract] In one line
> Rolling out updates in waves: a small test group first, then pilot users, then everyone, with time to catch problems.

> [!tip] Think of it like
> Tasting a new dish on a few guests before serving it to the whole wedding.

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> *More in the [[Glossary]].*

## How it works

- Typical rings: IT/test devices (day 0), pilot users (day 2-3), broad (day 7), servers and critical systems in maintenance windows.
- Watch the first ring for failures before the next one starts.
- Critical, actively exploited vulnerabilities may skip ahead after a quick test.
- Same idea in Windows Update for Business, Intune update rings, WSUS groups and RMM patch policies.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A Patch Tuesday update breaks printing in the first ring. What does the ring model let you do?
> Pause the rollout before it reaches everyone, and remove or work around the update on the few affected devices.

## See also

[[Patch Tuesday]] · [[Windows Update for Business]] · [[Maintenance windows]] · [[Bad patch rollout]]
