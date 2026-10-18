---
type: "moc"
level: "All"
tags:
  - "moc"
  - "virtualization"
created: "2026-10-18"
updated: "2026-10-18"
---

# VDI & app delivery

> [!abstract] In plain words
> VDI gives users a desktop that actually runs in the data center or cloud, which they reach over the network.

Part of [[Virtualization & Storage]].

- [[Citrix Virtual Apps and Desktops]]: Delivers Windows desktops and apps from the data center to any device.
- [[Azure Virtual Desktop]]: Windows desktops that run in Azure, which users connect to from anywhere.
- [[Windows 365]]: A personal Windows PC in the cloud for each user, for a monthly fee.
- [[Omnissa Horizon]]: Virtual desktops and apps, formerly VMware Horizon.
- [[Parallels RAS]]: Software for publishing Windows apps and desktops to users anywhere, often a simpler alternative to Citrix.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "11 Virtualization & Storage/VDI & app delivery"
WHERE type = "tool"
SORT file.name ASC
```
