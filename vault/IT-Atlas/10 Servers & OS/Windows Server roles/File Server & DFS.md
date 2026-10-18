---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server roles"
status: "current"
aliases:
  - "DFS"
  - "DFS-R"
  - "DFS Namespaces"
  - "DFS Replication"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# File Server & DFS

> [!abstract] In plain words
> Shared folders on Windows servers. DFS gives them one tidy path and keeps copies in sync between servers.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server roles · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **SMB**: The Windows file-sharing protocol (port 445).
> **TCP**: A connection-based network protocol that confirms delivery.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Windows file serving over SMB, with DFS Namespaces to present shares under one path and DFS Replication to keep folders in sync (also used for SYSVOL).

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 445/TCP SMB

## Alerts you'll see

- DFS-R backlog growing
- DFS-R event 2213 (dirty shutdown, replication paused)
- DFS-R event 4012 (stopped replicating: past MaxOfflineTimeInDays)
- Share or volume nearly full

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Event 2213 | Replication paused after an unexpected shutdown; resume per the event text once the database is checked |
| Backlog not clearing | Get-DfsrBacklog between partners; check the staging quota and conflicts |
| Users cannot reach the namespace | dfsutil diag; check the namespace servers and referral order |

## Where to find its logs

- Event Viewer: DFS Replication log
- `C:\Windows\debug (DFSR debug logs)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-DfsrBacklog -SourceComputerName FS01 -DestinationComputerName FS02 -GroupName GROUP -FolderName FOLDER
dfsrdiag replicationstate
Get-SmbShare
Get-SmbOpenFile | Where-Object Path -like '*FILE*'
Get-SmbSession
```

## See also

[[Active Directory]] · [[Group Policy]] · [[Low disk space]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
