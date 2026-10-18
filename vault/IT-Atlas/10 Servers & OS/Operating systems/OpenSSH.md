---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[OpenBSD project]]"
deployment:
status: "current"
agent_service: "sshd"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# OpenSSH

> [!abstract] In plain words
> The standard tool for securely logging in to Linux servers and network devices, now built into Windows too.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[OpenBSD project]] · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

> [!info]+ Words on this page
> **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

SSH client and server: key-based authentication, port forwarding, SCP/SFTP; included in Windows as an optional feature.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`sshd`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 22/TCP

## Where to find its logs

- `/var/log/auth.log (Ubuntu)`
- `/var/log/secure (RHEL)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
ssh USER@HOST
ssh-keygen -t ed25519
ssh-copy-id USER@HOST
sudo sshd -t
```

## Good to know

- Disable password login and use keys on internet-facing servers.

## See also

[[Linux servers]] · [[Remote Access]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
