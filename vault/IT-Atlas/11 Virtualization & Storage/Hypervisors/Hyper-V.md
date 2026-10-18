---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Hypervisors]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
agent_service: "vmms"
aliases:
  - "Microsoft Hyper-V"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Hyper-V

> [!abstract] In plain words
> Microsoft's virtualization built into Windows Server.
>
> **What kind of tool is this?** A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Virtualization & Storage]] › [[Hypervisors]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **CSV**: In Hyper-V, a Cluster Shared Volume: storage that all servers in a cluster use at once. Elsewhere, a comma-separated spreadsheet file.
> **VHDX**: A virtual hard disk file used by Hyper-V and FSLogix.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **failover**: Automatically switching to a backup system when the main one fails.
> **checkpoint**: Hyper-V's name for a snapshot: a saved point in time of a VM.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## In more detail

Microsoft's hypervisor built into Windows Server, clustered with Failover Clustering and managed with Hyper-V Manager, Windows Admin Center or SCVMM.

## Main parts

- Virtual Machine Management Service (vmms)
- Checkpoints (AVHDX differencing disks)
- Virtual switches
- Hyper-V Replica
- Cluster Shared Volumes with Failover Clustering

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`vmms`

## Alerts you'll see

- VM in a critical or saved state
- Old checkpoints (AVHDX chains)
- CSV or volume low on space
- Replica health warning
- Host node down

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| VM won't start | Read Hyper-V-VMMS and Hyper-V-Worker admin logs; disk space and permissions on VHDX files are common |
| Leftover AVHDX files | A backup left a checkpoint; merge it with Get-VMSnapshot and Remove-VMSnapshot, never by deleting files |

## Where to find its logs

- Event Viewer: Microsoft > Windows > Hyper-V-VMMS > Admin
- Event Viewer: Microsoft > Windows > Hyper-V-Worker > Admin

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-VM | Select-Object Name, State, Uptime, Status
Get-VMSnapshot -VMName VM
Get-VMReplication
Get-VMHardDiskDrive -VMName VM | Get-VHD
Get-VMSwitch
```

## See also

[[Failover Clustering]] · [[VMware vSphere]] · [[Veeam Backup & Replication]] · [[Snapshot age]] · [[ESXi and Hyper-V command cheat sheet]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
