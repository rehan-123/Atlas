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

# Retention & GFS

> [!abstract] In one line
> How long restore points are kept. GFS = grandfather-father-son: daily, weekly, monthly and yearly points.

> [!tip] Think of it like
> Keep daily photos for a week, weekly ones for a month, monthly ones for a year.

> [!info]+ Words on this page
> **GFS**: Grandfather-father-son: keeping daily, weekly and monthly backups for different lengths of time.
> **retention**: How long backups or logs are kept.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> *More in the [[Glossary]].*

## How it works

- Match retention to business, legal and insurance requirements, and to likely attacker dwell time.
- Longer retention on cheaper or immutable storage tiers.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why keep backups longer than attackers usually stay hidden?
> So you can restore from a point before they got in.

## See also

[[Immutability & air gap]] · [[3-2-1-1-0 rule]]
