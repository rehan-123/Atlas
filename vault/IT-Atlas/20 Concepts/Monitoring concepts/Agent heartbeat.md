---
type: "concept"
level: "Junior"
category: "[[Monitoring concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Agent heartbeat

> [!abstract] In one line
> Agents check in on a schedule; a missed check-in raises an offline alert.

> [!tip] Think of it like
> The agent checks in like a guard on patrol. A missed check-in means 'go and look', not 'definitely down'.

> [!info]+ Words on this page
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **ping**: A quick test that sends a small message to a device and waits for a reply.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## How it works

- Offline does not always mean down: the machine may be off, asleep, on a blocked network or have a broken agent.
- Before escalating, check a second signal: ping, the hypervisor console, another tool's agent, or a user.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A laptop's agent is offline. Name two harmless reasons.
> The laptop is off or asleep, or it's on a network that blocks the agent.

## See also

[[Agent offline]] · [[RMM]]
