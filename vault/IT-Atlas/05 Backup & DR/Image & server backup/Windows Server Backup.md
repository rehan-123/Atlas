---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Image & server backup]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows Server"
status: "current"
aliases:
  - "wbadmin"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Server Backup

> [!abstract] In plain words
> The basic backup tool built into Windows Server.
>
> **What kind of tool is this?** Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows Server · **Category:** [[Backup & DR]] › [[Image & server backup]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> *More in the [[Glossary]].*

## In more detail

The backup feature built into Windows Server: VSS-based full server, bare-metal, system state and volume backups, managed with wbadmin.

## Alerts you'll see

- Backup failed (Microsoft-Windows-Backup events)

## Where to find its logs

- Event Viewer: Applications and Services Logs > Microsoft > Windows > Backup

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
wbadmin get versions
wbadmin start backup -backupTarget:E: -include:C: -allCritical -quiet
wbadmin get status
```

## See also

[[VSS]] · [[Bare-metal restore]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
