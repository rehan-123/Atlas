---
type: "moc"
level: "All"
tags:
  - "moc"
  - "devops"
created: "2026-10-18"
updated: "2026-10-18"
---

# Containers & orchestration

> [!abstract] In plain words
> A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

Part of [[DevOps & Containers]].

- [[Docker]]: The tool that made containers popular. You describe an app in a Dockerfile, build an image, and run it as a container on any machine with Docker.
- [[Kubernetes]]: Software that runs lots of containers across many servers, restarts them when they crash and spreads the load. Often shortened to K8s.
- [[Azure Kubernetes Service]]: Microsoft's managed Kubernetes. Azure runs the control plane; you run and pay for the worker nodes.
- [[Amazon EKS]]: Amazon's managed Kubernetes service on AWS.
- [[Helm]]: A package manager for Kubernetes: one command installs an app with all its Kubernetes pieces.
- [[Podman]]: A Docker-compatible container tool from Red Hat that doesn't need a background service or root.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "18 DevOps & Containers/Containers & orchestration"
WHERE type = "tool"
SORT file.name ASC
```
