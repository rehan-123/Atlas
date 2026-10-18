---
type: "moc"
level: "All"
tags:
  - "moc"
  - "servers"
created: "2026-10-18"
updated: "2026-10-18"
---

# Servers & Operating Systems

Windows Server roles the NOC monitors every day, and the operating systems underneath.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Track OS lifecycles; plan upgrades a year before end of support.
> - Use Server Core and minimal roles where possible; fewer features means fewer patches and less attack surface.
> - Separate roles: don't run apps on domain controllers.
> - Baseline performance so you can tell 'slow' from 'normal for month-end'.

## [[Windows Server roles]]

Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

- [[Windows DNS Server]]
- [[Windows DHCP Server]]
- [[IIS]]
- [[File Server & DFS]]
- [[Print Server]]
- [[RDS]]
- [[RD Gateway]]
- [[FSLogix]]
- [[Failover Clustering]]
- [[Windows Deployment Services]]
- [[RRAS]]
- [[Always On VPN]]
- [[Storage Replica]]
- [[Windows Event Forwarding]]
- [[Windows Defender Firewall]]

## [[Operating systems]]

The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

- [[Windows Server]]
- [[Windows client]]
- [[Linux servers]]
- [[macOS]]
- [[Ubuntu Server]]
- [[Red Hat Enterprise Linux]]
- [[Samba]]
- [[OpenSSH]]

## Playbooks for this area

[[Certificate expiring]] · [[DHCP scope exhausted]] · [[DNS resolution failure]] · [[FSLogix profile failed to load]] · [[Hypervisor host disconnected]] · [[Low disk space]] · [[Website down]] · [[Windows service stopped]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "10 Servers & OS"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
