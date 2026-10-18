---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "Active Directory"
status: "current"
aliases: []
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Group Policy

> [!abstract] In plain words
> Settings pushed from Active Directory to every domain computer and user: password rules, mapped drives, security settings and more.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** Active Directory · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **registry**: Windows' central settings database.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> *More in the [[Glossary]].*

## In more detail

Policy delivered from SYSVOL to domain-joined machines: security settings, scripts, drive maps, software and registry preferences.

## Alerts you'll see

- GPO processing failures (System log, source GroupPolicy)
- SYSVOL replication problems

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Policy not applying | gpresult /h report.html shows applied and denied GPOs and why; check security filtering and WMI filters |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
gpupdate /force
gpresult /h C:\Temp\gp.html
gpresult /r /scope computer
Get-GPO -All | Sort-Object ModificationTime -Descending | Select-Object -First 10
```

## See also

[[Active Directory]] · [[File Server & DFS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
