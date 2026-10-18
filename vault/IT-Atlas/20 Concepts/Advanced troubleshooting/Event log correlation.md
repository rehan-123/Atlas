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

# Event log correlation

> [!abstract] In one line
> Lining up events from several logs and systems by time to find the real cause rather than the loudest symptom.

> [!tip] Think of it like
> Investigating a car crash by lining up every witness statement by time.

> [!info]+ Words on this page
> **NTP**: Network Time Protocol, which keeps clocks in sync.
> **SIEM**: A system that collects security logs from everywhere and looks for attacks.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## How it works

- Start from the exact time of the failure and look at all relevant logs: System, Application, Security, app logs, firewall, hypervisor.
- The first error is usually the cause; later errors are consequences.
- Make sure clocks agree (NTP) or the timeline lies.
- A SIEM or `Get-WinEvent` with `-FilterHashtable` across servers saves hours.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Ten errors appear at 02:00. Which one do you investigate first?
> The earliest one: later errors are usually knock-on effects.

## See also

[[Windows Event Log]] · [[Windows Event ID reference]] · [[SIEM]] · [[NTP]]
