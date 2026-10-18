---
type: "moc"
level: "All"
tags:
  - "moc"
  - "virtualization"
created: "2026-10-18"
updated: "2026-10-18"
---

# Hypervisors

> [!abstract] In plain words
> A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

Part of [[Virtualization & Storage]].

- [[VMware vSphere]]: VMware's virtualization: ESXi runs on each physical server and hosts the VMs, and vCenter manages them all. Now owned by Broadcom.
- [[Hyper-V]]: Microsoft's virtualization built into Windows Server.
- [[Proxmox VE]]: A free virtualization platform, popular as a VMware replacement.
- [[Nutanix AHV]]: Virtualization and storage in one system, managed through a web console called Prism.
- [[XenServer]]: A virtualization platform mostly used with Citrix.
- [[Azure Local]]: Hyper-V servers at the client's site, managed from Azure (formerly Azure Stack HCI).

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "11 Virtualization & Storage/Hypervisors"
WHERE type = "tool"
SORT file.name ASC
```
