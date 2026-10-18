---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[VM backup]]"
vendor: "[[Veeam]]"
deployment: "On-prem (Windows server plus proxies and repositories)"
status: "current"
agent_service: "Veeam Backup Service"
aliases:
  - "VBR"
  - "Veeam B&R"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Veeam Backup & Replication

> [!abstract] In plain words
> The most common tool for backing up virtual machines (VMware and Hyper-V). It can also test-boot backups and start a VM straight from its backup.
>
> **What kind of tool is this?** VM backup protects virtual machines from the host level, without installing software inside each one.

**Made by:** [[Veeam]] · **Runs:** On-prem (Windows server plus proxies and repositories) · **Category:** [[Backup & DR]] › [[VM backup]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **TCP**: A connection-based network protocol that confirms delivery.
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

The most common VM backup platform: VMware, Hyper-V, physical agents, NAS and cloud workloads, with backup copy jobs, SureBackup verification and Instant Recovery.

## Main parts

- Backup server and console
- Backup proxies (data movers)
- Repositories: Windows, hardened Linux (immutable) and scale-out backup repositories with object storage tiers
- Backup copy jobs for the offsite copy
- SureBackup automated recovery verification
- Instant Recovery
- Veeam Cloud Connect for service providers

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Veeam Backup Service`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 9392/TCP console to backup server
- 2500-3300/TCP data mover traffic between components

## Alerts you'll see

- Job failed or finished with warning
- Repository low on space
- Backup copy out of RPO
- SureBackup failed
- License or support expiring

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Failed to create VM snapshot | Check the hypervisor: datastore free space, stale snapshots needing consolidation, VMware Tools or Integration Services |
| VSS or guest processing error | Check guest credentials and vssadmin list writers inside the VM |
| Repository full | Check retention, orphaned backups and scale-out offload; never delete backup files by hand |
| Slow jobs | Look at the bottleneck statistic in the job session (source, proxy, network or target) |

## Where to find its logs

- `C:\ProgramData\Veeam\Backup (server and job logs)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-VBRJob | Select-Object Name, JobType
Get-VBRBackupSession | Sort-Object CreationTime -Descending | Select-Object -First 10 Name, Result, CreationTime
```

## See also

[[Veeam ONE]] · [[Veeam Backup for Microsoft 365]] · [[Veeam Agent for Microsoft Windows]] · [[VMware vSphere]] · [[Hyper-V]] · [[VSS]] · [[Changed block tracking]] · [[Immutability & air gap]] · [[3-2-1-1-0 rule]] · [[Backup job failed]] · [[Snapshot age]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
