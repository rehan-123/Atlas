---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[Redis]]"
deployment:
status: "current"
agent_service: "redis-server"
aliases: []
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Redis

> [!abstract] In plain words
> A very fast in-memory data store, often used as a cache in front of a database.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[Redis]] · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **TCP**: A connection-based network protocol that confirms delivery.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **cluster**: Several servers working together so one can take over if another fails.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

In-memory key-value store used for caching, sessions and queues; persistence via RDB/AOF; replicas and Sentinel/Cluster for HA.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`redis-server`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 6379/TCP

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
redis-cli ping
redis-cli info memory
```

## See also

[[MongoDB]] · [[MySQL & MariaDB]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
