---
type: "moc"
level: "All"
tags:
  - "moc"
  - "servers"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Server roles

> [!abstract] In plain words
> Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

Part of [[Servers & Operating Systems]].

- [[Windows DNS Server]]: The DNS service on Windows servers (usually the domain controllers). It turns names into IP addresses for every PC in the domain.
- [[Windows DHCP Server]]: The DHCP service on Windows servers. It hands out IP addresses automatically to devices on the network.
- [[IIS]]: Microsoft's web server: it runs websites and web apps on Windows Server.
- [[File Server & DFS]]: Shared folders on Windows servers. DFS gives them one tidy path and keeps copies in sync between servers.
- [[Print Server]]: A Windows server that shares printers with everyone.
- [[RDS]]: Remote Desktop Services: many users log in to the same Windows server and work there, as if it were their own desktop.
- [[RD Gateway]]: Lets users reach remote desktops safely over HTTPS from outside the office, instead of opening RDP to the internet.
- [[FSLogix]]: Keeps each user's profile in a single virtual disk file on a file share, attached when they log in to a remote desktop server.
- [[Failover Clustering]]: Joins servers together so that if one fails, its work (VMs, SQL, file shares) moves to another automatically.
- [[Windows Deployment Services]]: A Windows Server role that lets new PCs start from the network (PXE) and install Windows.
- [[RRAS]]: Routing and Remote Access Service: the Windows Server role that provides VPN, NAT and basic routing.
- [[Always On VPN]]: A Windows VPN that connects automatically before or after sign-in, so remote laptops act as if they're in the office.
- [[Storage Replica]]: A Windows Server feature that copies a volume block by block to another server for disaster recovery.
- [[Windows Event Forwarding]]: Built-in Windows feature that sends chosen events from many PCs to one collector server, without buying a log tool.
- [[Windows Defender Firewall]]: The firewall built into every Windows PC and server, with separate rules for domain, private and public networks.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "10 Servers & OS/Windows Server roles"
WHERE type = "tool"
SORT file.name ASC
```
