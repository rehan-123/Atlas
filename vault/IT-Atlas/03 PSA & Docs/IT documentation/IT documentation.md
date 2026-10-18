---
type: "moc"
level: "All"
tags:
  - "moc"
  - "psa"
created: "2026-10-18"
updated: "2026-10-18"
---

# IT documentation

> [!abstract] In plain words
> Documentation tools hold everything you need to know about each client: devices, passwords, network details and how-to guides.

Part of [[PSA & Documentation]].

- [[IT Glue]]: Where many MSPs keep client documentation: devices, passwords, network details and how-to guides.
- [[Hudu]]: A documentation platform for MSPs, similar to IT Glue, which you can also host yourself.
- [[Liongard]]: Automatically records the settings of firewalls, Microsoft 365, servers and more, and tells you when something changes.
- [[Confluence]]: Atlassian's wiki for team documentation, often used for internal runbooks and how-to pages.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "03 PSA & Docs/IT documentation"
WHERE type = "tool"
SORT file.name ASC
```
