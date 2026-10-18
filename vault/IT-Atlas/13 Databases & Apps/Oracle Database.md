---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[Oracle]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Oracle Database

> [!abstract] In plain words
> A large commercial database used by big business applications.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[Oracle]] · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **CPU**: The processor, the part of a computer that does the calculations.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Enterprise relational database: instances, listeners, tablespaces, RMAN backups and Data Guard replication.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 1521/TCP listener

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
lsnrctl status
sqlplus / as sysdba
```

## Good to know

- Licensing is complex and tied to CPU cores; check before moving it to a different VM host.

## See also

[[Microsoft SQL Server]] · [[PostgreSQL]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
