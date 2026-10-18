---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Storage arrays & NAS]]"
vendor: "[[Synology]]"
deployment: "Appliance"
status: "current"
aliases:
  - "DSM"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Synology NAS

> [!abstract] In plain words
> A popular network storage box for small businesses, also often used as a backup target.
>
> **What kind of tool is this?** Storage arrays and NAS boxes are dedicated machines full of disks that store data for servers and users.

**Made by:** [[Synology]] · **Runs:** Appliance · **Category:** [[Virtualization & Storage]] › [[Storage arrays & NAS]]

> [!info]+ Words on this page
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **SMB**: The Windows file-sharing protocol (port 445).
> **TCP**: A connection-based network protocol that confirms delivery.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **HTTPS**: Encrypted HTTP (port 443).
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> *More in the [[Glossary]].*

## In more detail

Popular SMB NAS running DSM: SMB shares, Hyper Backup, Snapshot Replication, Active Backup for Business and iSCSI.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5000/TCP DSM HTTP
- 5001/TCP DSM HTTPS

## Alerts you'll see

- Volume degraded or crashed
- Disk SMART warnings
- Backup task failures
- Volume nearly full

## Good to know

- Do not expose DSM to the internet; NAS boxes are routinely brute-forced and hit by ransomware.

## See also

[[Synology Active Backup for Business]] · [[RAID levels]] · [[RAID degraded]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
