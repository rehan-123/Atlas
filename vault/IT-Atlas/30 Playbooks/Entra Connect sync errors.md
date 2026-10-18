---
type: "playbook"
level: "Mid"
severity: "P2 if sync has stopped, P3 for single-object errors"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Entra Connect sync errors

> [!abstract] What this alert means
> Changes in on-premises Active Directory aren't reaching Microsoft Entra ID, or some objects fail to sync.
>
> **Why it matters:** New starters can't sign in, leavers keep cloud access and password changes don't take effect in Microsoft 365.

**How urgent:** P2 if sync has stopped, P3 for single-object errors. See [[Severity levels]].

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **UPN**: User principal name: the sign-in name that looks like an email address.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Entra admin center shows sync last ran hours ago
- Email alerts about export errors
- A user's change in AD doesn't show in Microsoft 365

## First 5 minutes

1. Check the Entra Connect server is up and the ADSync service is running
2. Open Synchronization Service Manager and look at the latest run profiles for errors
3. Get-ADSyncScheduler to see whether the scheduler is enabled and when it last ran

## Find the cause

- Duplicate attribute (same UPN or proxyAddress on two objects)
- Object outside the synced OUs
- Expired credentials for the AD connector account
- Server staging mode left on after a migration
- Outdated Entra Connect version no longer supported

## Fix it

- Fix the conflicting attribute in AD, then Start-ADSyncSyncCycle -PolicyType Delta
- Re-enable the scheduler (Set-ADSyncScheduler -SyncCycleEnabled $true)
- Update Entra Connect to a supported version

## Ask for help (escalate) when

- Sync stopped for more than 3 hours
- Hard-match or source-anchor problems that risk deleting cloud objects
- Plans to move to Entra Cloud Sync

## Write it up

Copy this into the ticket and fill it in:

```
Last successful sync: 
Errors found: 
Objects affected: 
Fix: 
Next sync verified:
```

## See also

[[Microsoft Entra Connect]] · [[Directory sync troubleshooting]] · [[Hybrid identity models]] · [[Entra Cloud Sync]]
