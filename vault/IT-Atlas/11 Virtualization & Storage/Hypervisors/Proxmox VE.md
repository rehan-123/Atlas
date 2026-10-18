---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Hypervisors]]"
vendor: "[[Proxmox]]"
deployment: "On-prem (Debian-based)"
status: "current"
aliases: []
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Proxmox VE

> [!abstract] In plain words
> A free virtualization platform, popular as a VMware replacement.
>
> **What kind of tool is this?** A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

**Made by:** [[Proxmox]] · **Runs:** On-prem (Debian-based) · **Category:** [[Virtualization & Storage]] › [[Hypervisors]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **TCP**: A connection-based network protocol that confirms delivery.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Open-source virtualization on Debian: KVM VMs and LXC containers, clustering, ZFS and Ceph, with paid enterprise repositories.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8006/TCP web UI

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
qm list
pct list
pvecm status
pvesm status
zpool status
```

## See also

[[Proxmox Backup Server]] · [[VMware vSphere]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
