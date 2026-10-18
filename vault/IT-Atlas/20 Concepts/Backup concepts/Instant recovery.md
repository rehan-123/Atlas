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

# Instant recovery

> [!abstract] In one line
> Booting a machine directly from its backup as a VM to cut downtime, then migrating it back to production storage.

> [!tip] Think of it like
> Running a server straight from its backup like a spare tyre: it gets you moving, but don't drive on it for long.

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> *More in the [[Glossary]].*

## How it works

- Datto local and cloud virtualization, Veeam Instant Recovery and Axcient Virtual Office are examples.
- Performance runs from backup storage, so it is a bridge, not a home.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why is instant recovery a temporary fix?
> It runs from backup storage, which is slower, so you must move it back to production storage.

## See also

[[Datto BCDR]] · [[Veeam Backup & Replication]] · [[RPO & RTO]]
