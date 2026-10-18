---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# DevOps & Containers

> [!abstract] In plain words
> DevOps tools help teams build, test and ship software and infrastructure automatically, so changes are repeatable instead of done by hand.

How modern software and infrastructure are built and shipped: containers, orchestration, source control, CI/CD pipelines, infrastructure as code, web servers and secrets.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Version everything (code, infrastructure, configuration) and deploy through pipelines, not by hand.
> - Keep images small, patched and scanned; pin versions instead of using 'latest'.
> - Plan for persistent data, backups and monitoring of clusters; containers are disposable, data isn't.

## [[Containers & orchestration]]

A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

- [[Docker]]
- [[Kubernetes]]
- [[Azure Kubernetes Service]]
- [[Amazon EKS]]
- [[Helm]]
- [[Podman]]

## [[Source control & pipelines]]

Source control keeps every version of code and scripts. CI/CD pipelines test and deploy changes automatically when someone pushes.

- [[GitHub]]
- [[GitHub Actions]]
- [[Azure DevOps]]
- [[GitLab]]
- [[Jenkins]]

## [[Infrastructure as code & config]]

Infrastructure as code means writing servers, networks and settings down in files, so building them is a repeatable command instead of a checklist.

- [[Bicep]]
- [[Puppet]]
- [[PowerShell DSC]]

## [[Web servers & proxies]]

Web servers answer browser requests; reverse proxies sit in front of apps to add HTTPS, routing and caching.

- [[Nginx]]
- [[Apache HTTP Server]]

## [[Secrets management]]

Secrets managers store passwords, API keys and certificates centrally, so they're never pasted into scripts.

- [[HashiCorp Vault]]
- [[Azure Key Vault]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
