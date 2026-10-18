---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor:
deployment: "On-prem or cloud"
status: "current"
aliases:
  - "Linux"
  - "Ubuntu"
  - "RHEL"
  - "Debian"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Linux servers

> [!abstract] In plain words
> Linux servers such as Ubuntu or Red Hat. Mostly managed by typing commands in a terminal.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Runs:** On-prem or cloud · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

> [!info]+ Words on this page
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> *More in the [[Glossary]].*

## In more detail

Linux servers (Ubuntu, Debian, RHEL and derivatives). systemd, journald and the package manager are where most NOC checks start.

## Alerts you'll see

- Disk and inode usage
- Load average and memory
- Failed systemd units
- Pending security updates

## Where to find its logs

- journalctl
- `/var/log/syslog (Debian, Ubuntu) or /var/log/messages (RHEL)`
- `/var/log/auth.log or /var/log/secure`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
systemctl --failed
journalctl -p err -b
df -h && df -i
free -m
top
ss -tulpn
apt list --upgradable
dnf check-update
```

## See also

[[Bash]] · [[Linux command cheat sheet]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
