---
type: "moc"
level: "All"
tags:
  - "moc"
  - "cloud"
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft 365 workloads

> [!abstract] In plain words
> The services inside Microsoft 365 (mail, files, Teams) and the API used to manage them.

Part of [[Cloud & SaaS]].

- [[Microsoft 365]]: Microsoft's online suite: email (Exchange Online), files (SharePoint and OneDrive), Teams and the Office apps.
- [[Exchange Online]]: Microsoft's hosted email service inside Microsoft 365.
- [[SharePoint & OneDrive]]: Where Microsoft 365 files live: SharePoint for shared team files, OneDrive for each person's own files.
- [[Microsoft Teams]]: Microsoft's chat, meetings and calling app. Each team stores its files in SharePoint.
- [[Microsoft Graph]]: The API (programmatic interface) scripts and tools use to read and change Microsoft 365 and Entra ID.
- [[Microsoft 365 admin center]]: The main admin website for Microsoft 365: users, licenses, groups, billing, service health and message center.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "12 Cloud & SaaS/Microsoft 365 workloads"
WHERE type = "tool"
SORT file.name ASC
```
