---
type: "moc"
level: "All"
tags:
  - "moc"
  - "servers"
created: "2026-10-18"
updated: "2026-10-18"
---

# Operating systems

> [!abstract] In plain words
> The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

Part of [[Servers & Operating Systems]].

- [[Windows Server]]: Microsoft's server operating system. Always check whether a server's version is still supported.
- [[Windows client]]: Windows 10 and 11 on users' PCs. Windows 10 support ended in October 2025.
- [[Linux servers]]: Linux servers such as Ubuntu or Red Hat. Mostly managed by typing commands in a terminal.
- [[macOS]]: Apple's operating system for Macs, usually managed with Jamf or Intune.
- [[Ubuntu Server]]: A very common free Linux server operating system, with long-term support releases every two years.
- [[Red Hat Enterprise Linux]]: Red Hat's commercial Linux for businesses, with paid support and long life cycles. Rocky Linux and AlmaLinux are free rebuilds.
- [[Samba]]: Software that lets Linux share files with Windows (SMB) and can even act as an Active Directory domain controller.
- [[OpenSSH]]: The standard tool for securely logging in to Linux servers and network devices, now built into Windows too.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "10 Servers & OS/Operating systems"
WHERE type = "tool"
SORT file.name ASC
```
