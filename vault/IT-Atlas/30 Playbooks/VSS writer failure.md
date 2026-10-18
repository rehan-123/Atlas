---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# VSS writer failure

> [!abstract] What this alert means
> Windows couldn't take the consistent snapshot that the backup needs.
>
> **Why it matters:** Backups fail, or capture apps such as SQL in a state that may not restore cleanly.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Backup fails with a VSS or snapshot error
- Events 8193, 8194 or 12289 from VSS

## First 5 minutes

1. Run `vssadmin list writers` as administrator and note any writer not in a Stable state with no error
2. Check `vssadmin list providers` for leftover third-party providers

## Find the cause

- Failed writer named in the output points to its service (SQL Writer, NTDS, Hyper-V VSS Writer, WMI Writer)
- Shadow storage too small: `vssadmin list shadowstorage`
- Two backup products running at the same time

## Fix it

- Restart the service that owns the failed writer (for example SQL Server VSS Writer, Cryptographic Services, WMI)
- Remove leftover providers from old backup software with the vendor's cleanup tool
- Increase shadow storage
- Reboot in a window if writers stay in a failed state

## Ask for help (escalate) when

- Writers fail again right after a reboot
- Database writers failing on SQL or Exchange

## Write it up

Copy this into the ticket and fill it in:

```
Host: 
Failed writer(s): 
Provider(s): 
Action: 
Backup re-run:
```

## See also

[[VSS]] · [[Backup job failed]] · [[Windows Event ID reference]]
