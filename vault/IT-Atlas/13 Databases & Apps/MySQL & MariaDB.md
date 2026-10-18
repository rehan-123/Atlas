---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor:
deployment: "Self-hosted or cloud"
status: "current"
aliases:
  - "MySQL"
  - "MariaDB"
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# MySQL & MariaDB

> [!abstract] In plain words
> Free databases behind many websites and apps.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Runs:** Self-hosted or cloud · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source relational databases behind many web apps (and ConnectWise Automate's backend).

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 3306/TCP

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
mysqladmin status
SHOW PROCESSLIST;
SHOW ENGINE INNODB STATUS\G
```

## See also

[[ConnectWise Automate]] · [[PostgreSQL]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
