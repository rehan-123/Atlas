---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# Web servers & proxies

> [!abstract] In plain words
> Web servers answer browser requests; reverse proxies sit in front of apps to add HTTPS, routing and caching.

Part of [[DevOps & Containers]].

- [[Nginx]]: A fast web server and reverse proxy that sits in front of many websites and apps.
- [[Apache HTTP Server]]: One of the oldest and most common web servers, especially on Linux.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers/Web servers & proxies"
WHERE type = "tool"
SORT file.name ASC
```
