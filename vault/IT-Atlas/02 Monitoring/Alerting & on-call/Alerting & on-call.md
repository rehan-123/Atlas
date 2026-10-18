---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Alerting & on-call

> [!abstract] In plain words
> On-call tools decide who gets woken up for an alert, and keep paging until someone responds.

Part of [[Monitoring & Observability]].

- [[PagerDuty]]: Sends alerts to whoever is on call, by app, SMS or phone call, and escalates if nobody answers.
- [[Opsgenie]]: Atlassian's on-call alerting tool. It is being retired, so customers are moving elsewhere.
- [[Splunk On-Call]]: An on-call and alert routing service, formerly VictorOps.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring/Alerting & on-call"
WHERE type = "tool"
SORT file.name ASC
```
