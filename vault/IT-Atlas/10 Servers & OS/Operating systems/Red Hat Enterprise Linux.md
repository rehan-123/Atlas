---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[Red Hat]]"
deployment:
status: "current"
aliases:
  - "RHEL"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Red Hat Enterprise Linux

> [!abstract] In plain words
> Red Hat's commercial Linux for businesses, with paid support and long life cycles. Rocky Linux and AlmaLinux are free rebuilds.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[Red Hat]] · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

## In more detail

Enterprise Linux with dnf packages, SELinux enforcing by default, firewalld and subscription management.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
cat /etc/redhat-release
sudo dnf update
getenforce
firewall-cmd --list-all
journalctl -xe
```

## Good to know

- SELinux denials look like 'permission denied' even for root; check with ausearch -m avc -ts recent.

## See also

[[Linux servers]] · [[Ubuntu Server]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
