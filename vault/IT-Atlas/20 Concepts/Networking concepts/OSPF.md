---
type: "concept"
level: "Mid"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# OSPF

> [!abstract] In one line
> Open Shortest Path First: link-state interior routing protocol inside an organization.

> [!tip] Think of it like
> OSPF is the sat-nav inside a company network: routers share a map and each works out the shortest path.

> [!info]+ Words on this page
> **MTU**: The largest packet size a link can carry without splitting it.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- Neighbours must match area, timers, MTU and authentication to form an adjacency.
- Stuck in EXSTART or EXCHANGE usually means an MTU mismatch.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Two OSPF routers are stuck and won't become neighbours. Name a common cause.
> A mismatch between them: area, timers, authentication or MTU.

## See also

[[BGP]] · [[MTU]]
