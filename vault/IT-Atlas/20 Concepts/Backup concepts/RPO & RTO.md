---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# RPO & RTO

> [!abstract] In one line
> Recovery point objective and recovery time objective.

> [!tip] Think of it like
> RPO: how much work you can afford to lose. RTO: how long you can afford to be down.

> [!info]+ Words on this page
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> **RTO**: Recovery time objective: how long you can afford to be down.
> *More in the [[Glossary]].*

## How it works

- **RPO**: how much data loss is acceptable (time since the last good backup). Hourly backups give at best a 1-hour RPO.
- **RTO**: how long until the service is back.
- Agree both with the client per system and test against them. Backup copy lag and failed jobs silently push RPO out.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Backups run every 4 hours. What's the best possible RPO?
> 4 hours of lost data, and worse if a backup fails.

## See also

[[Replication vs backup]] · [[Instant recovery]] · [[Backup copy & replication lag]]
