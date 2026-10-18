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

# NetFlow, sFlow & IPFIX

> [!abstract] In one line
> Flow telemetry: who talked to whom, on which port, and how much.

> [!tip] Think of it like
> If SNMP tells you how full the pipe is, flow data tells you who is using it.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **router**: Device that connects one network to another, such as the office to the internet.
> **bandwidth**: How much data a link can carry per second.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## How it works

- Routers and firewalls export flow records to a collector (often UDP 2055, 6343 for sFlow or 4739 for IPFIX; check the device).
- Answers "what is eating the bandwidth" in a way SNMP interface counters cannot.
- sFlow samples packets; NetFlow and IPFIX summarize flows.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- The internet link is maxed out. Which tells you which PC is responsible: SNMP or NetFlow?
> NetFlow (or sFlow or IPFIX). SNMP only shows total traffic on the interface.

## See also

[[PRTG Network Monitor]] · [[Auvik]] · [[SolarWinds NPM]] · [[High latency]]
