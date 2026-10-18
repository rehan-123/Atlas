---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "On-prem server"
status: "current"
agent_service: "ADSync (miiserver.exe)"
aliases:
  - "Azure AD Connect"
  - "AAD Connect"
  - "Entra Connect"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Entra Connect

> [!abstract] In plain words
> Copies users and passwords from on-site Active Directory to Entra ID every 30 minutes, so people have one account for both (formerly Azure AD Connect).
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** On-prem server · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **UPN**: User principal name: the sign-in name that looks like an email address.
> *More in the [[Glossary]].*

## In more detail

Syncs on-prem Active Directory to Entra ID (formerly Azure AD Connect) with password hash sync, pass-through authentication or federation. Runs a delta sync every 30 minutes by default.

## Main parts

- ADSync service (miiserver.exe) and its database
- Synchronization Service Manager (miisclient.exe)
- Connectors for AD and Entra ID
- Password hash sync, pass-through authentication or federation

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`ADSync (miiserver.exe)`

## Alerts you'll see

- Sync errors (duplicate attributes, invalid characters)
- Sync not run in more than 3 hours
- Password hash sync heartbeat errors
- Version nearing end of support

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Sync stopped | Check the ADSync service and run a delta sync; review Synchronization Service Manager for the failed run profile |
| Duplicate attribute errors | Find the conflicting proxyAddresses or UPN in Entra ID and fix the source object in AD |
| High memory on the sync server | miiserver.exe memory grows with object count; size the server rather than killing the process |

## Where to find its logs

- Synchronization Service Manager operations tab
- Application log, sources ADSync and Directory Synchronization

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-ADSyncScheduler
Start-ADSyncSyncCycle -PolicyType Delta
Start-ADSyncSyncCycle -PolicyType Initial
```

## See also

[[Active Directory]] · [[Microsoft Entra ID]] · [[Entra Cloud Sync]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
