---
type: "moc"
level: "All"
tags:
  - "moc"
  - "monitoring"
created: "2026-10-18"
updated: "2026-10-18"
---

# Infrastructure & APM

> [!abstract] In plain words
> These tools collect numbers (CPU, memory, response times) from servers, apps and cloud services and draw them as graphs, so you can spot trouble before users notice.

Part of [[Monitoring & Observability]].

- [[LogicMonitor]]: A cloud monitoring service: small 'collectors' at each site gather data and send it to the LogicMonitor portal.
- [[Datadog]]: A cloud monitoring service used by many software companies for servers, apps and logs.
- [[Prometheus]]: A free tool that collects numbers (metrics) from servers and apps over time. Usually paired with Grafana for graphs.
- [[Grafana]]: Makes dashboards and graphs from many data sources. Often the big screen on a NOC wall.
- [[New Relic]]: A cloud service mainly for watching how applications perform.
- [[Dynatrace]]: An enterprise monitoring tool that installs one agent and maps how everything connects.
- [[Azure Monitor]]: Azure's built-in monitoring: graphs, logs and alerts for Azure resources and connected servers.
- [[Amazon CloudWatch]]: AWS's built-in monitoring: graphs, logs and alarms for AWS resources.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "02 Monitoring/Infrastructure & APM"
WHERE type = "tool"
SORT file.name ASC
```
