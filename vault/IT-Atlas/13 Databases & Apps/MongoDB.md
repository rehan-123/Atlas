---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[MongoDB]]"
deployment:
status: "current"
agent_service: "mongod"
aliases: []
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# MongoDB

> [!abstract] In plain words
> A popular database that stores data as flexible JSON-like documents instead of tables.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[MongoDB]] · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Document database with replica sets for high availability and sharding for scale; Atlas is the managed cloud service.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`mongod`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 27017/TCP

## Good to know

- Never expose it to the internet without authentication: open MongoDB servers are routinely wiped by attackers.

## See also

[[PostgreSQL]] · [[Redis]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
