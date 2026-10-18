---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[Canonical]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Ubuntu Server

> [!abstract] In plain words
> A very common free Linux server operating system, with long-term support releases every two years.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[Canonical]] · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

## In more detail

Debian-based Linux distribution; LTS releases get five years of standard support; apt for packages, netplan for networking, systemd for services.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
lsb_release -a
sudo apt update && sudo apt upgrade
systemctl status SERVICE
journalctl -u SERVICE --since today
ip a
df -h
```

## See also

[[Linux servers]] · [[Linux command cheat sheet]] · [[Red Hat Enterprise Linux]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
