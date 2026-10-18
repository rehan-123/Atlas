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

# SaaS shared responsibility

> [!abstract] In one line
> Microsoft and Google keep their services running; protecting your data from deletion, attack and retention gaps is your job.

> [!tip] Think of it like
> Microsoft looks after the building; you look after what's in your filing cabinet.

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **retention**: How long backups or logs are kept.
> *More in the [[Glossary]].*

## How it works

- Recycle bins and version history are time-limited and can be purged by an attacker or an admin.
- Hence SaaS backup products: Spanning, Datto SaaS Protection, Veeam Backup for Microsoft 365, Microsoft 365 Backup and others.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Does Microsoft back up deleted Microsoft 365 data for you forever?
> No. Recycle bins and retention are time-limited, which is why SaaS backup exists.

## See also

[[SaaS backup]] · [[Microsoft 365]] · [[Spanning Backup]]
