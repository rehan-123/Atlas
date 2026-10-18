---
type: "moc"
level: "All"
tags:
  - "moc"
  - "cloud"
created: "2026-10-18"
updated: "2026-10-18"
---

# Productivity suites

> [!abstract] In plain words
> Office suites for mail, documents and calendars other than Microsoft 365.

Part of [[Cloud & SaaS]].

- [[Google Workspace]]: Google's office suite: Gmail, Drive, Calendar and Meet.
- [[Zoom Workplace]]: Zoom's meetings, chat and phone platform.
- [[Slack]]: A chat app for teams, organized into channels.
- [[Dropbox]]: Cloud file storage and sharing, popular with small businesses and creative teams.
- [[Box]]: Cloud content management used by businesses that need strong sharing controls and compliance.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "12 Cloud & SaaS/Productivity suites"
WHERE type = "tool"
SORT file.name ASC
```
