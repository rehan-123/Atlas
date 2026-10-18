---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[VM backup]]"
vendor: "[[Proxmox]]"
deployment: "Self-hosted"
status: "current"
aliases:
  - "PBS"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Proxmox Backup Server

> [!abstract] In plain words
> The backup server for Proxmox virtual machines.
>
> **What kind of tool is this?** VM backup protects virtual machines from the host level, without installing software inside each one.

**Made by:** [[Proxmox]] · **Runs:** Self-hosted · **Category:** [[Backup & DR]] › [[VM backup]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **TCP**: A connection-based network protocol that confirms delivery.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **incremental**: A backup of only what changed since the last backup.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Deduplicating, incremental backup server for Proxmox VE VMs and containers, plus Linux hosts.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8007/TCP web UI and API

## See also

[[Proxmox VE]] · [[Deduplication]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
