---
type: "moc"
level: "All"
tags:
  - "moc"
  - "virtualization"
created: "2026-10-18"
updated: "2026-10-18"
---

# Virtualization & Storage

Hypervisors, virtual desktops, storage arrays and the out-of-band management that tells you hardware is failing.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Size clusters for N+1: one host failure must not overload the rest.
> - Snapshots are not backups; alert on snapshots older than a few days.
> - Watch storage latency and capacity trends, not just free space; thin provisioning hides risk.
> - Keep firmware, drivers and hypervisor versions on the vendor's compatibility matrix.

## [[Hypervisors]]

A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

- [[VMware vSphere]]
- [[Hyper-V]]
- [[Proxmox VE]]
- [[Nutanix AHV]]
- [[XenServer]]
- [[Azure Local]]

## [[VDI & app delivery]]

VDI gives users a desktop that actually runs in the data center or cloud, which they reach over the network.

- [[Citrix Virtual Apps and Desktops]]
- [[Azure Virtual Desktop]]
- [[Windows 365]]
- [[Omnissa Horizon]]
- [[Parallels RAS]]

## [[Storage arrays & NAS]]

Storage arrays and NAS boxes are dedicated machines full of disks that store data for servers and users.

- [[Synology NAS]]
- [[QNAP NAS]]
- [[NetApp ONTAP]]
- [[Dell PowerVault ME]]
- [[Dell PowerStore]]
- [[HPE MSA]]
- [[HPE Alletra]]
- [[Lenovo ThinkSystem DE-Series]]
- [[Pure Storage FlashArray]]
- [[TrueNAS]]
- [[Storage Spaces Direct]]

## [[Server hardware management]]

Out-of-band controllers are tiny computers inside a server that let you see its health and console even when Windows is down.

- [[Dell iDRAC]]
- [[HPE iLO]]
- [[Lenovo XClarity Controller]]
- [[Supermicro IPMI]]
- [[Hardware RAID controllers]]

## Playbooks for this area

[[Datastore or CSV low space]] · [[FSLogix profile failed to load]] · [[Hypervisor host disconnected]] · [[RAID degraded]] · [[Server unreachable]] · [[Snapshot age]] · [[Temperature alarm]] · [[VM won't start]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "11 Virtualization & Storage"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
