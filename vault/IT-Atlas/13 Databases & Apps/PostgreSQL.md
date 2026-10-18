---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor:
deployment: "Self-hosted or cloud"
status: "current"
aliases:
  - "Postgres"
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# PostgreSQL

> [!abstract] In plain words
> A free, powerful database used by many apps.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Runs:** Self-hosted or cloud · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source relational database; also the default configuration database for newer Veeam installs.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5432/TCP

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
SELECT pid, state, query FROM pg_stat_activity;
pg_isready
```

## See also

[[Veeam Backup & Replication]] · [[MySQL & MariaDB]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
