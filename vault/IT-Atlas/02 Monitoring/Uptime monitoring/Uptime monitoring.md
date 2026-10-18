---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Uptime monitoring

> [!abstract] In plain words
> Uptime monitors check from the outside, like a customer would, that a website or service still answers.

Part of [[Monitoring & Observability]].

- [[Uptime Kuma]]: A free, self-hosted tool that checks websites and services are up and shows a status page.
- [[UptimeRobot]]: A cloud service that checks your websites every few minutes and alerts you when they're down.
- [[Pingdom]]: A website monitoring service that checks your sites from around the world and alerts when they're down or slow.
- [[Better Stack]]: Uptime monitoring, status pages and on-call alerts in one service.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring/Uptime monitoring"
WHERE type = "tool"
SORT file.name ASC
```
