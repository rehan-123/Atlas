---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# Infrastructure as code & config

> [!abstract] In plain words
> Infrastructure as code means writing servers, networks and settings down in files, so building them is a repeatable command instead of a checklist.

Part of [[DevOps & Containers]].

- [[Bicep]]: Microsoft's simple language for describing Azure resources in files and deploying them repeatably.
- [[Puppet]]: A configuration management tool that keeps many servers in a defined state.
- [[PowerShell DSC]]: PowerShell Desired State Configuration: write how a Windows server should look, and DSC makes it so.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers/Infrastructure as code & config"
WHERE type = "tool"
SORT file.name ASC
```
