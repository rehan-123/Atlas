---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Agent on RDS, AVD and VDI hosts"
status: "current"
agent_service: "frxsvc, frxccds"
aliases:
  - "FSLogix Profile Containers"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# FSLogix

> [!abstract] In plain words
> Keeps each user's profile in a single virtual disk file on a file share, attached when they log in to a remote desktop server.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Agent on RDS, AVD and VDI hosts · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **RDS**: Remote Desktop Services: many users working on one shared Windows server.
> **VDI**: Virtual desktop infrastructure: desktops that run on servers and are used remotely.
> **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
> **SMB**: The Windows file-sharing protocol (port 445).
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> *More in the [[Glossary]].*

## In more detail

Microsoft's profile container technology: each user's profile lives in a VHD(X) on a file share and is attached at logon. Includes Office Containers and Cloud Cache.

## Main parts

- Profile Containers
- ODFC (Office) Containers
- Cloud Cache for multiple storage locations
- frx.exe command-line tool
- Registry settings under HKLM\SOFTWARE\FSLogix

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`frxsvc, frxccds`

## Alerts you'll see

- Profile failed to attach (user gets a temporary or local profile)
- Container share low on space
- VHDX locked by another session
- Slow logons

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Profile fails to load | Read the FSLogix Profile log for the reason code; check share permissions and whether another host holds the VHDX lock |
| Containers filling the share | Check container sizes and redirect or exclude browser caches |
| Intermittent attach timeouts | Check SMB latency to the share and antivirus exclusions for .vhd and .vhdx files |

## Where to find its logs

- `C:\ProgramData\FSLogix\Logs`
- Event Viewer: Microsoft > FSLogix > Apps > Operational and Admin

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
& "C:\Program Files\FSLogix\Apps\frx.exe" version
Get-ItemProperty HKLM:\SOFTWARE\FSLogix\Profiles
```

## Good to know

- Event ID 26 with FrxStatus 31 has been seen with semaphore timeouts when attaching containers on RDS farms (field note).

## See also

[[RDS]] · [[Azure Virtual Desktop]] · [[FSLogix profile failed to load]] · [[File Server & DFS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
