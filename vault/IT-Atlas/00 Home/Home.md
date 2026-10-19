---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# IT Atlas

> [!tip] Junior, mid-level or senior?
> New to IT? Start the [[Learning path]]. Growing into a sysadmin or senior role? Follow the [[Career tracks]]. Every note is tagged Junior, Mid or Senior ([[Notes by level]]). Stuck on a word? See the [[Glossary]]. First time here? Read [[How to use the IT Atlas]].

One linked atlas of IT, written in plain English for everyone from a first-week help desk tech to a senior systems administrator: everyday fixes, every tool an MSP meets, the ideas and architecture behind them, step-by-step playbooks, deep troubleshooting, compliance and lookup tables.

> [!abstract] The Atlas workflow
> Start by understanding the system, use evidence to diagnose the issue, then follow the right fix or escalation path. Guides link to related tools, concepts, and playbooks.

![[atlas-workflow.svg]]

**76 help desk guides** · **348 tools** · **133 concepts** · **48 playbooks** · **13 reference sheets** · **170 vendors**

## Fix everyday problems

- [[Help Desk]]: [[Windows PC problems]], [[Internet & Wi-Fi problems]], [[Email & Outlook problems]], [[Sign-in & password problems]], [[Printer & scanner problems]], [[Microsoft 365 & Teams problems]], [[Mac problems]], [[Phone & tablet problems]], [[Security & scam problems]], [[Software & app problems]], [[New starters & leavers]]

## Grow your career

- [[Career tracks]]: [[Track 1 - Junior]], [[Track 2 - Sysadmin]], [[Track 3 - Senior]]
- [[Learning path]]: ten weeks for new starters
- [[Notes by level]]

## Tools by category

- [[RMM]] (15)
- [[Monitoring & Observability]] (27): [[Network monitoring]], [[Infrastructure & APM]], [[Uptime monitoring]], [[Alerting & on-call]], [[Log management]]
- [[PSA & Documentation]] (12): [[PSA]], [[ITSM]], [[IT documentation]]
- [[Remote Access]] (10)
- [[Backup & DR]] (38): [[BCDR appliances]], [[Image & server backup]], [[VM backup]], [[SaaS backup]], [[Endpoint backup]], [[Enterprise backup]], [[Cloud backup & DR]], [[Backup storage targets]]
- [[Endpoint & Patch Management]] (22): [[UEM & MDM]], [[Patch management]], [[Software deployment]], [[Hardware vendor tools]]
- [[Security]] (45): [[EDR & MDR]], [[SIEM]], [[Email security]], [[DNS & web filtering]], [[Vulnerability management]], [[Privileged access & passwords]], [[SASE & ZTNA]], [[Application control]], [[Encryption]]
- [[Identity & Access]] (15)
- [[Networking]] (34): [[Firewalls]], [[Switching & routing]], [[Wireless]], [[SD-WAN]], [[VPN]], [[Load balancers]], [[DNS & IPAM]]
- [[Servers & Operating Systems]] (23): [[Windows Server roles]], [[Operating systems]]
- [[Virtualization & Storage]] (27): [[Hypervisors]], [[VDI & app delivery]], [[Storage arrays & NAS]], [[Server hardware management]]
- [[Cloud & SaaS]] (20): [[Microsoft 365 workloads]], [[Public cloud]], [[Productivity suites]], [[AI assistants]]
- [[Databases & Applications]] (8)
- [[Power & Facilities]] (6)
- [[Voice & UC]] (7)
- [[Automation & Scripting]] (15)
- [[DevOps & Containers]] (18): [[Containers & orchestration]], [[Source control & pipelines]], [[Infrastructure as code & config]], [[Web servers & proxies]], [[Secrets management]]
- [[Compliance & Governance]] (6): [[Compliance platforms]], [[Data governance & DLP]], [[Posture & assessment]]

## Learn

- [[Learning path]]: [[Week 1 - Computer basics]], [[Week 2 - Fixing everyday problems]], [[Week 3 - How networks work]] and more

## Know

- [[Concepts]]: [[IT basics]], [[Help desk skills]], [[Networking concepts]], [[Monitoring concepts]], [[Backup concepts]], [[Windows & identity concepts]], [[Security concepts]], [[Operations & process]], [[Cloud & DevOps concepts]], [[Architecture & design]], [[Advanced troubleshooting]], [[Compliance & governance]]

## Respond

- [[Playbooks]]: [[Agent offline]], [[Backup job failed]], [[Low disk space]], [[Firewall WAN down]], [[Suspected ransomware]] and more

## Look up

- [[Reference]]: [[Glossary]], [[Port reference]], [[Windows Event ID reference]], [[Agent & service names]], [[Log locations]], [[Windows command cheat sheet]]
- [[Vendors]]
- [[Tool database]]: every tool in one sortable table

## Recently updated

```dataview
TABLE type, updated FROM "" WHERE type AND type != "moc" SORT file.mtime DESC LIMIT 15
```

## Tools not yet verified

```dataview
LIST FROM "" WHERE type = "tool" AND !verified LIMIT 20
```
