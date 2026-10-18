---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Time drift

> [!abstract] What this alert means
> A machine's clock is wrong.
>
> **Why it matters:** Logins can fail (Kerberos) and logs become hard to trust.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **NTP**: Network Time Protocol, which keeps clocks in sync.
> **DC**: Domain controller: a server running Active Directory.
> **threshold**: The value that triggers an alert.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Clock offset above threshold
- Kerberos errors

## First 5 minutes

1. Run `w32tm /query /status` on the affected machine and the PDC emulator

## Find the cause

- VM taking time from the host
- PDC emulator using a bad source
- UDP 123 blocked

## Fix it

- Point the PDC emulator at reliable NTP sources
- Disable host time sync for virtual DCs
- Resync with `w32tm /resync`

## Ask for help (escalate) when

- Domain-wide authentication failures

## Write it up

Copy this into the ticket and fill it in:

```
Machine: 
Offset: 
Source: 
Action:
```

## See also

[[NTP]] · [[Kerberos]] · [[FSMO roles]]
