---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# Privileged access & passwords

> [!abstract] In plain words
> These tools store passwords safely and control who can use admin accounts.

Part of [[Security]].

- [[Windows LAPS]]: Built into Windows: gives every computer a different local admin password, changes it regularly, and stores it in Active Directory or Entra ID.
- [[Keeper]]: A password manager for teams and MSPs.
- [[Bitwarden]]: An open-source password manager.
- [[N-able Passportal]]: A password manager and documentation tool for MSPs.
- [[CyberArk]]: Enterprise tool that locks away admin passwords and records admin sessions.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/Privileged access & passwords"
WHERE type = "tool"
SORT file.name ASC
```
