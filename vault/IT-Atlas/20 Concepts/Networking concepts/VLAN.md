---
type: "concept"
level: "Junior"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# VLAN

> [!abstract] In one line
> Virtual LANs split one physical switch into separate layer 2 networks.

> [!tip] Think of it like
> A VLAN splits one physical switch into separate virtual switches, like putting walls inside one big office.

> [!info]+ Words on this page
> **LAN**: Local area network: the network inside a building.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **trunk**: A switch port that carries several VLANs at once.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- Access ports carry one untagged VLAN; trunk ports carry many tagged VLANs (802.1Q).
- Inter-VLAN traffic must go through a router or firewall, which is where you apply policy.
- Common faults: a VLAN missing from a trunk's allowed list, a native VLAN mismatch, or an AP or phone port configured as access instead of trunk.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What's the difference between an access port and a trunk port?
> An access port carries one VLAN, for a PC or printer. A trunk carries many tagged VLANs, between switches or to an access point.

## See also

[[Cisco Catalyst]] · [[DHCP]] · [[Spanning Tree]]
