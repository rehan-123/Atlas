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

# Disaster recovery planning

> [!abstract] In one line
> A written, tested plan for bringing the business back after losing a site, a system or the whole network.

> [!tip] Think of it like
> A fire evacuation plan: useless if nobody has practised it or the plan is inside the burning building.

> [!info]+ Words on this page
> **RTO**: Recovery time objective: how long you can afford to be down.
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> *More in the [[Glossary]].*

## How it works

- Lists critical systems in recovery order, their RTO/RPO, where backups are and who does what.
- Includes contact details, vendor support numbers and how to communicate if email is down.
- Store a copy outside the systems it protects (offline or a separate cloud).
- Test it: tabletop exercises yearly, technical restore tests regularly.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Where should the DR plan be kept?
> Somewhere available when the main systems are down: printed, offline, or in a separate system.

## See also

[[High availability vs disaster recovery]] · [[RPO & RTO]] · [[Backup architecture]] · [[Suspected ransomware]]
