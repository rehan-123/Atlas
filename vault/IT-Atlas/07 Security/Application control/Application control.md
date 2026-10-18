---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# Application control

> [!abstract] In plain words
> Application control only lets approved programs run, so unknown or malicious software is blocked by default.

Part of [[Security]].

- [[ThreatLocker]]: Only lets approved software run, and limits what that software can touch.
- [[App Control for Business]]: Windows' built-in way to allow only approved apps (formerly WDAC; AppLocker is the older version).
- [[AppLocker]]: A Windows feature that only lets approved programs run, using rules by publisher, path or file hash.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/Application control"
WHERE type = "tool"
SORT file.name ASC
```
