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

# Capacity planning

> [!abstract] In one line
> Watching growth trends so you buy or scale before you run out of disk, CPU, licences or bandwidth.

> [!tip] Think of it like
> Watching the fuel gauge on a long drive and stopping before the light comes on.

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **bandwidth**: How much data a link can carry per second.
> **failover**: Automatically switching to a backup system when the main one fails.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## How it works

- Track trends, not snapshots: disk growth per month, peak CPU, memory pressure, bandwidth at peak hours.
- Plan for headroom (for example, keep 20-30% free) and for failover: a cluster must run on one fewer node.
- Lead times matter: hardware and budget approvals take weeks.
- Review quarterly with the client; it's a sales conversation, not a surprise outage.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why must a two-node cluster's hosts each stay under about 50% load?
> If one node fails, the other has to run everything.

## See also

[[Monitoring thresholds and baselines]] · [[Low disk space]] · [[Cloud cost management]]
