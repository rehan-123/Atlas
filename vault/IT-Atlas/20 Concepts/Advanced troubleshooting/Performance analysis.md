---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Performance analysis

> [!abstract] In one line
> Measuring where a slow system actually spends its time: CPU, memory, disk or network.

> [!tip] Think of it like
> A doctor's blood test instead of guessing from symptoms: numbers point to the real cause.

> [!info]+ Words on this page
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **CPU**: The processor, the part of a computer that does the calculations.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **datastore**: In VMware, the storage where virtual machines' disk files live.
> **latency**: Delay: how long data takes to get from A to B.
> *More in the [[Glossary]].*

## How it works

- Start with Resource Monitor and Task Manager; then Performance Monitor counters over time.
- Useful counters: `% Processor Time`, `Available MBytes`, `Avg. Disk sec/Read` and `/Write` (over 20-25 ms is slow), `Disk Queue Length`, `Network Interface Bytes Total/sec`.
- Windows Performance Recorder/Analyzer (WPR/WPA) show exactly which driver or process is slow.
- On VMs, check the host too: CPU ready, memory ballooning and datastore latency.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What disk latency value usually means storage is too slow?
> Average read or write latency consistently above about 20-25 ms.

## See also

[[High CPU]] · [[High memory]] · [[High disk latency]] · [[Monitoring thresholds and baselines]]
