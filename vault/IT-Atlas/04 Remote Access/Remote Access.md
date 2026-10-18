---
type: "moc"
level: "All"
tags:
  - "moc"
  - "remote-access"
created: "2026-10-18"
updated: "2026-10-18"
---

# Remote Access

> [!abstract] In plain words
> Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

Tools to get onto a machine: attended support, unattended access and gateways. A favourite attack path, so access control and fast patching matter.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Remote access tools are a top attack path; patch them fast, enforce MFA and restrict who can use them.
> - Prefer one approved tool per purpose and remove the rest from endpoints.
> - Log and review sessions, especially unattended access to servers.

## Tools

- [[ScreenConnect]]: ConnectWise's remote control tool. You can join a user's session while they watch, or connect to unattended machines.
- [[TeamViewer]]: A very common remote control tool. Scammers use it too, so be careful with unknown requests.
- [[AnyDesk]]: A lightweight remote control tool, also often abused by scammers.
- [[Splashtop]]: A remote control tool built into several RMMs.
- [[N-able Take Control]]: N-able's remote control tool.
- [[BeyondTrust Remote Support]]: An enterprise remote support tool (formerly Bomgar) that records every session.
- [[MeshCentral]]: A free, self-hosted tool for remote desktop and command line access.
- [[RustDesk]]: A free, open-source remote desktop tool you can host yourself.
- [[Apache Guacamole]]: Lets you open RDP or SSH sessions in a web browser, with nothing installed on your computer.
- [[RDP]]: Remote Desktop Protocol: Windows' built-in way to log in to another machine's desktop. It should never be open to the internet.

## Playbooks for this area

[[Account lockout storm]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "04 Remote Access"
WHERE type = "tool"
SORT file.name ASC
```
