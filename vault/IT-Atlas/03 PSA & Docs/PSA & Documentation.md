---
type: "moc"
level: "All"
tags:
  - "moc"
  - "psa"
created: "2026-10-18"
updated: "2026-10-18"
---

# PSA & Documentation

Where the work is tracked and the knowledge is kept: tickets, contracts and SLAs, and the documentation platforms techs live in.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Ticket categories and time entries drive reporting; design them with the service desk manager, not ad hoc.
> - Documentation needs owners and review dates; stale docs are worse than none.
> - Automate the flow: RMM alerts to tickets, tickets to documentation links, offboarding checklists from templates.

## [[PSA]]

A PSA is the MSP's ticketing and billing system: every request, alert and hour worked ends up here.

- [[ConnectWise PSA]]
- [[Autotask PSA]]
- [[HaloPSA]]
- [[Kaseya BMS]]

## [[ITSM]]

ITSM tools are the ticketing systems big internal IT departments use, built around formal processes for incidents and changes.

- [[ServiceNow ITSM]]
- [[Jira Service Management]]
- [[Freshservice]]
- [[Zendesk]]

## [[IT documentation]]

Documentation tools hold everything you need to know about each client: devices, passwords, network details and how-to guides.

- [[IT Glue]]
- [[Hudu]]
- [[Liongard]]
- [[Confluence]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "03 PSA & Docs"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
