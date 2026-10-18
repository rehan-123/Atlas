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

# ARP

> [!abstract] In one line
> Address Resolution Protocol maps IP addresses to MAC addresses on a LAN.

> [!tip] Think of it like
> ARP asks the room 'Who has IP 10.0.0.5?' and the right device answers with its hardware (MAC) address.

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **LAN**: Local area network: the network inside a building.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> *More in the [[Glossary]].*

## How it works

- `arp -a` (Windows) or `ip neigh` (Linux) shows the cache.
- Duplicate IP conflicts show up as ARP flapping between two MACs.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What might ARP flapping between two MAC addresses indicate?
> Two devices are using the same IP address (an IP conflict).

## See also

[[VLAN]] · [[OSI model]]
