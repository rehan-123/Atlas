---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[BCDR appliances]]"
vendor: "[[Kaseya]]"
deployment: "On-site appliance plus Datto Cloud"
status: "current"
aliases:
  - "Datto SIRIS"
  - "Datto ALTO"
  - "SIRIS"
  - "ALTO"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Datto BCDR

> [!abstract] In plain words
> A Datto appliance at the client's site backs up servers, copies the backups to the Datto cloud, and test-boots them to prove they work. If a server dies, its backup can run as a virtual machine.
>
> **What kind of tool is this?** A BCDR appliance is a box at the client's office that backs up their servers, sends copies to the cloud, and can even run a failed server as a virtual machine until it's fixed.

**Made by:** [[Kaseya]] · **Runs:** On-site appliance plus Datto Cloud · **Category:** [[Backup & DR]] › [[BCDR appliances]]

> [!info]+ Words on this page
> **BCDR**: Business continuity and disaster recovery: keeping a business running, and getting it back after a disaster.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> *More in the [[Glossary]].*

## In more detail

Appliance-based business continuity: image backups to a local SIRIS or ALTO appliance, replication to the immutable Datto Cloud, screenshot verification, and local or cloud virtualization for instant recovery.

## Main parts

- SIRIS (business) and ALTO (small business) appliances
- Datto Windows Agent and Datto Linux Agent (ShadowSnap on legacy systems)
- Agentless backup for VMware
- Offsite replication to the Datto Cloud
- Screenshot verification and advanced verification
- Local and cloud virtualization
- Inverse Chain Technology (every snapshot is independently bootable)

## Alerts you'll see

- Backup failed
- Screenshot verification failed
- Offsite synchronization behind
- Appliance offline
- Local storage nearly full

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Screenshot verification failed | Open the screenshot: boot errors usually mean drivers, BitLocker, a pending CHKDSK or a failed update in the protected machine |
| Agent backup fails | Check VSS writers on the protected machine and the agent service |
| Offsite behind | Check appliance bandwidth throttling, internet uplink and retention settings |
| Storage nearly full | Review local retention and remove agents or old snapshots per policy |

## Where to find its logs

- Device and agent logs in the Datto partner portal and appliance web UI

## See also

[[Datto RMM]] · [[Autotask PSA]] · [[Datto Endpoint Backup]] · [[VSS]] · [[Backup verification]] · [[Backup job failed]] · [[Screenshot verification failed]] · [[Instant recovery]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
