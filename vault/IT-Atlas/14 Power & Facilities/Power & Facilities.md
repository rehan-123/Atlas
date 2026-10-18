---
type: "moc"
level: "All"
tags:
  - "moc"
  - "power"
created: "2026-10-18"
updated: "2026-10-18"
---

# Power & Facilities

> [!abstract] In plain words
> A UPS is a big battery that keeps equipment running during a power cut and shuts it down safely if the battery runs out.

UPS, power and environmental monitoring. Often the root cause nobody checks first.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Test UPS runtime and graceful shutdown scripts; a UPS that drops the load at the first outage is worse than none.
> - Monitor temperature and humidity; overheating kills hardware slowly and then all at once.
> - Label power feeds and keep a rack diagram; it saves hours during an incident.

## Tools

- [[APC Smart-UPS]]: APC's UPS units: a battery that keeps servers running in a power cut and can shut them down safely.
- [[Eaton UPS]]: Eaton's UPS units and their shutdown software.
- [[Vertiv Liebert]]: Large UPS and cooling systems for server rooms.
- [[CyberPower]]: Budget UPS units.
- [[APC NetBotz]]: Sensors and cameras for server rooms that watch temperature, humidity, water leaks and door opening.
- [[Raritan PDU]]: Smart power strips for racks that measure power use and can switch individual outlets off and on remotely.

## Playbooks for this area

[[Temperature alarm]] · [[UPS on battery]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "14 Power & Facilities"
WHERE type = "tool"
SORT file.name ASC
```
