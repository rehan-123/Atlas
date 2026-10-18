---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Bare-metal restore

> [!abstract] In one line
> Restoring a whole machine, OS included, to new or empty hardware.

> [!tip] Think of it like
> Rebuilding a whole machine from nothing: operating system, apps and data.

> [!info]+ Words on this page
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> *More in the [[Glossary]].*

## How it works

- Needs boot media with the right storage and network drivers.
- Restoring to different hardware may need driver injection (Hardware Independent Restore and similar features).

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What often goes wrong when restoring to different hardware?
> Missing storage or network drivers, so the restored system won't boot or can't see its disk.

## See also

[[Windows Server Backup]] · [[Veeam Agent for Microsoft Windows]] · [[Instant recovery]]
