---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Storage arrays & NAS]]"
vendor: "[[Lenovo]]"
deployment: "Appliance"
status: "current"
aliases:
  - "DE-Series"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Lenovo ThinkSystem DE-Series

> [!abstract] In plain words
> Lenovo's shared storage arrays. Replacement drives must be the exact supported part.
>
> **What kind of tool is this?** Storage arrays and NAS boxes are dedicated machines full of disks that store data for servers and users.

**Made by:** [[Lenovo]] · **Runs:** Appliance · **Category:** [[Virtualization & Storage]] › [[Storage arrays & NAS]]

> [!info]+ Words on this page
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> *More in the [[Glossary]].*

## In more detail

Lenovo's block storage arrays, based on NetApp E-Series and managed with ThinkSystem System Manager (SANtricity).

## Alerts you'll see

- Drive failed or predictive failure
- Controller or path failure
- Incompatible or unsupported replacement drive

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Replacement drive not accepted | Check the drive part number and firmware against the array's compatibility list before shipping |

## See also

[[NetApp ONTAP]] · [[Lenovo XClarity Controller]] · [[RAID degraded]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
