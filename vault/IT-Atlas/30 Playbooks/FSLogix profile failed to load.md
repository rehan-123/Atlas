---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# FSLogix profile failed to load

> [!abstract] What this alert means
> A user's remote desktop profile couldn't be attached at login.
>
> **Why it matters:** The user gets a temporary profile: no files, settings or Outlook data.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
> **SMB**: The Windows file-sharing protocol (port 445).
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **latency**: Delay: how long data takes to get from A to B.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Users get temporary or local profiles
- FSLogix errors in the event log

## First 5 minutes

1. Check the FSLogix profile log for the user's attach attempt and its reason or status code
2. Check whether the user's VHDX is attached on another host

## Find the cause

- VHDX locked by another session or host
- Share permissions or SMB connectivity
- Container full
- Antivirus scanning the containers
- Storage latency causing attach timeouts

## Fix it

- Log the user off everywhere and release the lock
- Fix permissions
- Expand or clean the container
- Add AV exclusions for .vhd and .vhdx files

## Ask for help (escalate) when

- Many users affected
- Corrupt containers

## Write it up

Copy this into the ticket and fill it in:

```
User: 
Host: 
Log reason / status code: 
Cause: 
Action:
```

## See also

[[FSLogix]] · [[RDS]] · [[Azure Virtual Desktop]] · [[File Server & DFS]]
