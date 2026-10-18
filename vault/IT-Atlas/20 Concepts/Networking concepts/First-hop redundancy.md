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

# First-hop redundancy

> [!abstract] In one line
> VRRP, HSRP and similar protocols give hosts a gateway IP that survives a router or firewall failure.

> [!tip] Think of it like
> Two routers share one gateway address; if the main one dies, the spare takes over the address instantly.

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **cluster**: Several servers working together so one can take over if another fails.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- Two devices share a virtual IP; one is active. Firewall HA clusters do the same job for the firewall itself.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why do PCs need this?
> PCs only know one default gateway address. Without failover, a router failure cuts them off.

## See also

[[FortiGate]] · [[Cisco Catalyst]]
