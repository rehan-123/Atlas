---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# Secrets management

> [!abstract] In plain words
> Secrets managers store passwords, API keys and certificates centrally, so they're never pasted into scripts.

Part of [[DevOps & Containers]].

- [[HashiCorp Vault]]: A secure vault for passwords, API keys and certificates that scripts and apps can request when they need them.
- [[Azure Key Vault]]: Azure's safe for secrets, encryption keys and certificates, with access controlled by Entra ID.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers/Secrets management"
WHERE type = "tool"
SORT file.name ASC
```
