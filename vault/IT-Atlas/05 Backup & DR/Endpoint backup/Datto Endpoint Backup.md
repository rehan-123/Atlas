---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Endpoint backup]]"
vendor: "[[Kaseya]]"
deployment: "Direct-to-cloud agent"
status: "current"
aliases:
  - "KEBv2"
  - "Datto Endpoint Backup v2"
  - "DEB"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Datto Endpoint Backup

> [!abstract] In plain words
> Backs up PCs and servers straight to the Datto cloud, with no appliance on site.
>
> **What kind of tool is this?** Endpoint backup protects laptops and desktops, usually by sending copies straight to the cloud.

**Made by:** [[Kaseya]] · **Runs:** Direct-to-cloud agent · **Category:** [[Backup & DR]] › [[Endpoint backup]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> *More in the [[Glossary]].*

## In more detail

Appliance-free image backup of PCs and servers straight to the Datto Cloud, managed in the Datto partner portal, with cloud virtualization for recovery on server editions.

## Main parts

- Endpoint agent
- Datto Cloud storage
- Partner portal management
- Cloud virtualization (server editions)

## Alerts you'll see

- Backup failed
- Agent not checking in
- Backup overdue

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Backup failing after migration from another product | Remove the old backup agent fully and check for leftover VSS providers or filter drivers |
| Agent not checking in | Check the agent service and outbound 443 |

## See also

[[Datto BCDR]] · [[Acronis Cyber Protect]] · [[VSS]] · [[Backup job failed]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
