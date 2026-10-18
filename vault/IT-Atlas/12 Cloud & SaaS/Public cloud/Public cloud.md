---
type: "moc"
level: "All"
tags:
  - "moc"
  - "cloud"
created: "2026-10-18"
updated: "2026-10-18"
---

# Public cloud

> [!abstract] In plain words
> Public clouds rent out servers, storage and networking by the hour from huge data centers.

Part of [[Cloud & SaaS]].

- [[Microsoft Azure]]: Microsoft's public cloud.
- [[Azure Arc]]: Lets you manage on-site servers from Azure, as if they were Azure VMs.
- [[Amazon Web Services]]: Amazon's public cloud, the largest one.
- [[Google Cloud]]: Google's public cloud.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "12 Cloud & SaaS/Public cloud"
WHERE type = "tool"
SORT file.name ASC
```
