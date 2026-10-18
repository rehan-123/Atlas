---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# Encryption

> [!abstract] In plain words
> Disk encryption scrambles everything on a laptop's drive, so a lost or stolen device doesn't leak data.

Part of [[Security]].

- [[BitLocker]]: Windows' built-in disk encryption. Make sure every recovery key is saved somewhere you can find it.
- [[FileVault]]: The Mac's built-in disk encryption.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/Encryption"
WHERE type = "tool"
SORT file.name ASC
```
