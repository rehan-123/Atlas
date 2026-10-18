---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[BCDR appliances]]"
vendor: "[[Kaseya]]"
deployment: "Physical or virtual appliance plus Unitrends Cloud"
status: "current"
aliases:
  - "Unitrends Backup"
  - "Recovery Series"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Unitrends

> [!abstract] In plain words
> Kaseya's backup appliances (physical or virtual). They back up servers and VMs and can automatically test that recovery works.
>
> **What kind of tool is this?** A BCDR appliance is a box at the client's office that backs up their servers, sends copies to the cloud, and can even run a failed server as a virtual machine until it's fixed.

**Made by:** [[Kaseya]] · **Runs:** Physical or virtual appliance plus Unitrends Cloud · **Category:** [[Backup & DR]] › [[BCDR appliances]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **BCDR**: Business continuity and disaster recovery: keeping a business running, and getting it back after a disaster.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **WAN**: Wide area network: links between sites, or to the internet.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## In more detail

Unitrends Recovery Series physical appliances or the Unitrends Backup virtual appliance: agent and hypervisor backups, backup copies to Unitrends Cloud or a second appliance, and Recovery Assurance automated DR testing.

## Main parts

- Recovery Series appliance or Unitrends Backup virtual appliance
- Windows and Linux agents
- Host-level VMware and Hyper-V backups
- Backup copy (hot) to Unitrends Cloud or another appliance; cold copies to disk or tape
- Recovery Assurance automated recovery testing
- Unitrends portal for multi-appliance management

## Alerts you'll see

- Backup job failed
- Backup copy failed or behind
- Appliance storage full
- Appliance offline
- Recovery Assurance test failed

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent backup fails | Check the agent service on the client and VSS writers; confirm the appliance can reach the agent |
| Storage full | Check retention and purge settings; large unexpected change rates fill appliances fast |
| Backup copy behind | Check WAN bandwidth, throttling windows and the copy queue |

## Where to find its logs

- Jobs and system reports in the appliance UI

## See also

[[Datto BCDR]] · [[VSS]] · [[Backup job failed]] · [[Backup copy & replication lag]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
