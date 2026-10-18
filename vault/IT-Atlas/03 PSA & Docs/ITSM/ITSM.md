---
type: "moc"
level: "All"
tags:
  - "moc"
  - "psa"
created: "2026-10-18"
updated: "2026-10-18"
---

# ITSM

> [!abstract] In plain words
> ITSM tools are the ticketing systems big internal IT departments use, built around formal processes for incidents and changes.

Part of [[PSA & Documentation]].

- [[ServiceNow ITSM]]: The ticketing platform most large companies use. You'll meet it when you work alongside a client's own IT team.
- [[Jira Service Management]]: Atlassian's ticketing system, built on Jira.
- [[Freshservice]]: A cloud ticketing system for mid-sized IT teams.
- [[Zendesk]]: A customer support ticketing system, sometimes used as an internal IT help desk.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "03 PSA & Docs/ITSM"
WHERE type = "tool"
SORT file.name ASC
```
