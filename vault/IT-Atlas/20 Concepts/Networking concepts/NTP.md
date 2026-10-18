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

# NTP

> [!abstract] In one line
> Network Time Protocol keeps clocks in sync.

> [!tip] Think of it like
> NTP keeps every clock agreeing with a trusted master clock, like synchronizing watches before a mission.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **DC**: Domain controller: a server running Active Directory.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## How it works

- UDP 123.
- Kerberos fails when clocks drift more than 5 minutes apart by default.
- In AD, the PDC emulator syncs from an external source and everything else follows the domain hierarchy. Do not point domain members at internet time.
- Virtual DCs must not also take time from the hypervisor host.
- Commands: `w32tm /query /status`, `w32tm /query /source`, `w32tm /resync`.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What breaks in Active Directory if clocks drift more than 5 minutes?
> Kerberos authentication, so users and computers can't log in or reach resources.

> [!question]- Which domain controller should get time from the internet?
> Only the one holding the PDC emulator role; everyone else follows the domain.

## See also

[[Kerberos]] · [[FSMO roles]] · [[Time drift]]
