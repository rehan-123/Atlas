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

# Link aggregation

> [!abstract] In one line
> Bundling several physical links into one logical link (LACP, 802.3ad).

> [!tip] Think of it like
> Several lanes joined into one wider road between two switches.

> [!info]+ Words on this page
> **bandwidth**: How much data a link can carry per second.
> *More in the [[Glossary]].*

## How it works

- Adds bandwidth and redundancy between switches, servers and storage.
- Both ends must agree on mode (LACP active or passive vs static).
- A single flow uses only one member link; aggregation does not make one file copy faster.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Will a single file copy go faster over a 2 x 1 Gb link aggregation?
> Usually not. One conversation uses one link; aggregation helps when there are many conversations at once.

## See also

[[Cisco Catalyst]] · [[VLAN]]
