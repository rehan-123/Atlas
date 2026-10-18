---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# VPN

> [!abstract] In plain words
> A VPN creates an encrypted tunnel over the internet, so a remote user or branch office can reach the office network safely.

Part of [[Networking]].

- [[WireGuard]]: A modern, simple and fast VPN.
- [[OpenVPN]]: A long-standing open-source VPN.
- [[Cisco Secure Client]]: Cisco's VPN app (formerly AnyConnect).
- [[GlobalProtect]]: Palo Alto's VPN app.
- [[FortiClient]]: Fortinet's VPN app for connecting to a FortiGate.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/VPN"
WHERE type = "tool"
SORT file.name ASC
```
