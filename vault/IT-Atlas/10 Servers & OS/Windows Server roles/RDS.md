---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server roles"
status: "current"
aliases:
  - "Remote Desktop Services"
  - "RDSH"
  - "Terminal Services"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# RDS

> [!abstract] In plain words
> Remote Desktop Services: many users log in to the same Windows server and work there, as if it were their own desktop.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server roles · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **CPU**: The processor, the part of a computer that does the calculations.
> **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
> **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Remote Desktop Services: Session Hosts, Connection Broker, Gateway, Web Access and Licensing, delivering shared desktops and RemoteApps.

## Main parts

- RD Session Host
- RD Connection Broker
- RD Gateway
- RD Web Access
- RD Licensing (per-user or per-device CALs)
- FSLogix or user profile disks for profiles

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 3389/TCP and UDP to session hosts
- 443/TCP to RD Gateway

## Alerts you'll see

- Session hosts not accepting connections
- High CPU or memory per host
- Profile load failures
- Licensing grace period expiring
- Gateway certificate expiring

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Users get temporary profiles | Check FSLogix or UPD logs; locked VHDX files are the usual cause |
| No licenses available | Check the licensing server is set on hosts and has CALs of the right mode |
| Slow logons | Check profile size, GPO processing time and antivirus exclusions for profile containers |

## Where to find its logs

- Event Viewer: TerminalServices-LocalSessionManager and RemoteConnectionManager operational logs

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
qwinsta
quser
Get-RDUserSession
Get-RDSessionHost -CollectionName COLLECTION
```

## See also

[[FSLogix]] · [[RD Gateway]] · [[RDP]] · [[Azure Virtual Desktop]] · [[FSLogix profile failed to load]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
