---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[Samba team]]"
deployment:
status: "current"
agent_service: "smbd, nmbd, winbind"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Samba

> [!abstract] In plain words
> Software that lets Linux share files with Windows (SMB) and can even act as an Active Directory domain controller.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[Samba team]] · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

> [!info]+ Words on this page
> **SMB**: The Windows file-sharing protocol (port 445).
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **DC**: Domain controller: a server running Active Directory.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## In more detail

SMB file and print server for Linux/Unix; can join AD as a member or run as an AD-compatible DC.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`smbd, nmbd, winbind`

## Where to find its logs

- `/var/log/samba/`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
smbstatus
testparm
wbinfo -u
```

## See also

[[File Server & DFS]] · [[Linux servers]] · [[SMB signing and versions]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
