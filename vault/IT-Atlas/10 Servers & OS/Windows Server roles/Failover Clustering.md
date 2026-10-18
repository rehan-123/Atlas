---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server feature"
status: "current"
agent_service: "ClusSvc"
aliases:
  - "WSFC"
  - "Windows Server Failover Clustering"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Failover Clustering

> [!abstract] In plain words
> Joins servers together so that if one fails, its work (VMs, SQL, file shares) moves to another automatically.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server feature · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **CSV**: In Hyper-V, a Cluster Shared Volume: storage that all servers in a cluster use at once. Elsewhere, a comma-separated spreadsheet file.
> **failover**: Automatically switching to a backup system when the main one fails.
> **quorum**: The majority vote a cluster needs to keep running, so two halves can't both think they're in charge.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## In more detail

Windows Server Failover Clustering: highly available roles (Hyper-V VMs, file servers, SQL) with quorum, cluster networks and Cluster Shared Volumes.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`ClusSvc`

## Alerts you'll see

- Node removed from membership (event 1135)
- Cluster resource failed (event 1069)
- Quorum lost (event 1177)
- CSV in redirected access

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Node dropped out | Check network heartbeats between nodes and generate the cluster log around the time |
| CSV redirected | Check storage paths (MPIO, iSCSI or FC) on the affected node |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-ClusterNode
Get-ClusterResource
Get-ClusterSharedVolume
Get-ClusterQuorum
Get-ClusterLog -TimeSpan 60 -Destination C:\Temp
Test-Cluster
```

## See also

[[Hyper-V]] · [[Storage Spaces Direct]] · [[Hypervisor host disconnected]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
