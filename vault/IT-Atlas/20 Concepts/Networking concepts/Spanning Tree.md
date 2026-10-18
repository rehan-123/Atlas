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

# Spanning Tree

> [!abstract] In one line
> STP prevents layer 2 loops by blocking redundant paths.

> [!tip] Think of it like
> Spanning Tree closes extra roads that would make traffic drive in circles forever.

> [!info]+ Words on this page
> **LAN**: Local area network: the network inside a building.
> **CPU**: The processor, the part of a computer that does the calculations.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## How it works

- Without STP, a single looped cable causes a broadcast storm that takes down the whole LAN.
- Use RSTP or MSTP, set a deliberate root bridge, enable PortFast and BPDU Guard on edge ports.
- Symptom of a loop: switch CPU at 100%, MAC flapping logs, and many topology change notifications.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What happens on a network without Spanning Tree if someone plugs both ends of a cable into the same switch?
> A loop causes a broadcast storm: switch CPU hits 100% and the whole network slows down or stops.

## See also

[[Cisco Catalyst]] · [[VLAN]] · [[Interface errors and packet loss]]
