---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Backup storage targets]]"
vendor: "[[Wasabi]]"
deployment: "Cloud object storage"
status: "current"
aliases: []
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Wasabi

> [!abstract] In plain words
> Cheap cloud storage often used to hold backups, with an option to lock them so they can't be deleted.
>
> **What kind of tool is this?** These are the places backups get stored in the cloud. Many can lock a backup so nobody, not even an attacker with admin rights, can delete it early.

**Made by:** [[Wasabi]] · **Runs:** Cloud object storage · **Category:** [[Backup & DR]] › [[Backup storage targets]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> *More in the [[Glossary]].*

## In more detail

S3-compatible cloud object storage with no egress fees (under its fair-use policy) and Object Lock immutability. A common target for Veeam and other backup tools.

## See also

[[Backblaze B2]] · [[Amazon S3]] · [[Immutability & air gap]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
