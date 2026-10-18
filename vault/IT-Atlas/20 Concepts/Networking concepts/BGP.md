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

# BGP

> [!abstract] In one line
> Border Gateway Protocol: routing between autonomous systems, the routing protocol of the internet.

> [!tip] Think of it like
> BGP is how internet providers tell each other which addresses they can reach, the internet's road map between companies.

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **ISP**: Internet service provider.
> **SD-WAN**: Smart use of several internet links, automatically picking the best one.
> *More in the [[Glossary]].*

## How it works

- TCP 179. Neighbours must be explicitly configured.
- Used by ISPs, multi-homed sites, SD-WAN and cloud interconnects (Azure ExpressRoute, AWS Direct Connect).
- Alerts to watch: neighbour down, prefix count changes and route flapping.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Where might an MSP engineer see BGP?
> On ISP links, SD-WAN, multi-site firewalls and cloud connections such as Azure ExpressRoute.

## See also

[[OSPF]] · [[SD-WAN]] · [[MikroTik]]
