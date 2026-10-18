---
type: "concept"
level: "Mid"
category: "[[Monitoring concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# WMI

> [!abstract] In one line
> Windows Management Instrumentation: how agentless tools query Windows performance and configuration.

> [!tip] Think of it like
> WMI is a question-and-answer window into Windows: monitoring tools ask it for disk space, services and more.

> [!info]+ Words on this page
> **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **repository**: Where backups are stored.
> *More in the [[Glossary]].*

## How it works

- Uses DCOM/RPC (135 plus dynamic ports) or WinRM (5985 and 5986) via CIM.
- Failures are usually credentials, firewall rules or a corrupt repository.
- Test: `Get-CimInstance Win32_OperatingSystem -ComputerName HOST`. Repair check: `winmgmt /verifyrepository`.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- PRTG's WMI sensors fail on one server. Name two things to check.
> The credentials, and whether the Windows Firewall allows WMI/RPC from the probe.

## See also

[[PRTG Network Monitor]] · [[N-able N-central]] · [[PowerShell]]
