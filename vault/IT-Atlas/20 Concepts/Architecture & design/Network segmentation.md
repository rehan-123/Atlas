---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Network segmentation

> [!abstract] In one line
> Splitting a network into zones with firewall rules between them, so one infected device can't reach everything.

> [!tip] Think of it like
> Fire doors in a building: a fire in one room doesn't spread through the whole floor.

> [!info]+ Words on this page
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## How it works

- Typical zones: users, servers, management, guest, IoT/printers, voice, DMZ.
- Use VLANs plus firewall rules between them; default deny and allow what's needed.
- Management interfaces (iDRAC/iLO, switches, hypervisors) belong on their own restricted network.
- Micro-segmentation applies the same idea per workload, in the cloud or with host firewalls.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why put printers and IoT devices on their own VLAN?
> They're rarely patched and easy to compromise; isolating them stops an attacker using them to reach servers.

## See also

[[VLAN]] · [[Firewalls]] · [[Zero Trust]] · [[Windows Defender Firewall]]
