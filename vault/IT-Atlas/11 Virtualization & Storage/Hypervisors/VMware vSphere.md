---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Hypervisors]]"
vendor: "[[Broadcom]]"
deployment: "On-prem"
status: "current"
aliases:
  - "ESXi"
  - "vCenter"
  - "VMware ESXi"
  - "vCenter Server"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# VMware vSphere

> [!abstract] In plain words
> VMware's virtualization: ESXi runs on each physical server and hosts the VMs, and vCenter manages them all. Now owned by Broadcom.
>
> **What kind of tool is this?** A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

**Made by:** [[Broadcom]] · **Runs:** On-prem · **Category:** [[Virtualization & Storage]] › [[Hypervisors]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **TCP**: A connection-based network protocol that confirms delivery.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## In more detail

ESXi hosts managed by vCenter Server: clusters, HA, DRS, vMotion and datastores. Broadcom bought VMware in November 2023 and moved to subscription bundles (VCF and VVF).

## Main parts

- ESXi hosts
- vCenter Server Appliance
- Clusters with HA and DRS
- Datastores (VMFS, NFS, vSAN)
- Distributed switches
- VMware Tools in guests

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP vSphere Client and API
- 902/TCP host console and NFC data transfer
- 5480/TCP vCenter appliance management (VAMI)

## Alerts you'll see

- Host disconnected or not responding
- Datastore usage above threshold
- Snapshots older than a few days
- HA failover events
- Hardware health alarms
- vCenter certificate expiry

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Host not responding | Check the management network and restart management agents (services.sh restart) from the console or SSH |
| Datastore full | Look for stale snapshots and thin-provisioned growth; consolidate snapshots first |
| VM needs consolidation | Run Consolidate; if it fails, check for a backup proxy still holding the disks |

## Where to find its logs

- `/var/log/vmkernel.log`
- `/var/log/hostd.log`
- `/var/log/vpxa.log`
- `/var/log/vobd.log`
- vCenter: /var/log/vmware/vpxd/vpxd.log

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
esxcli system version get
esxcli storage core device list
esxcli storage vmfs extent list
esxcli network nic list
vim-cmd vmsvc/getallvms
vim-cmd vmsvc/power.getstate VMID
esxtop
/etc/init.d/hostd restart
```

## Good to know

- Many MSPs moved small clients from vSphere to Hyper-V or Proxmox after the Broadcom licensing changes.

## See also

[[Veeam Backup & Replication]] · [[Hyper-V]] · [[Proxmox VE]] · [[Snapshot age]] · [[Hypervisor host disconnected]] · [[Datastore or CSV low space]] · [[ESXi and Hyper-V command cheat sheet]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
