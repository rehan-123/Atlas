---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Log management

> [!abstract] In plain words
> Log tools gather the logs from many systems into one searchable place, so you don't have to log in to each machine.

Part of [[Monitoring & Observability]].

- [[Elastic Stack]]: A set of tools (Elasticsearch, Kibana and others) for collecting and searching huge amounts of logs.
- [[Graylog]]: A tool that collects logs from many systems so you can search them in one place.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring/Log management"
WHERE type = "tool"
SORT file.name ASC
```
