---
type: "playbook"
level: "Junior"
severity: "P4 (P3 for exploited CVEs)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Patch failure or pending reboot

> [!abstract] What this alert means
> Updates failed to install, or are waiting for a restart.
>
> **Why it matters:** The machine stays exposed to known security holes.

**How urgent:** P4 (P3 for exploited CVEs). See [[Severity levels]].

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **KB**: A Microsoft Knowledge Base number, which identifies a specific update (for example KB5034441).
> **CVE**: A public ID number for a specific security vulnerability.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Update install failed
- Machine pending reboot past the deadline

## First 5 minutes

1. Get the error code from the RMM or Windows Update history
2. Check free disk space on C:

## Find the cause

- 0x800f081f usually means missing or corrupt component store files
- 0x800f0922 often means the System Reserved partition is too small or the update could not reach its servers
- 0x80070070 means out of disk space
- Repeated rollback after reboot: a driver or third-party filter driver conflict

## Fix it

- DISM /RestoreHealth and SFC, then retry
- Reset the Windows Update cache
- Install the KB manually from the Microsoft Update Catalog
- Schedule the reboot with the user

## Ask for help (escalate) when

- Exploited CVE unpatched after the agreed window
- Same failure across many machines

## Write it up

Copy this into the ticket and fill it in:

```
Device: 
KB: 
Error code: 
Action: 
Result:
```

## See also

[[Windows Update]] · [[Patch Tuesday]] · [[Patch management]]
