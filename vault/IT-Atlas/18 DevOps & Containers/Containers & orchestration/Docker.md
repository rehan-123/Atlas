---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[Docker]]"
deployment: "Linux, Windows, macOS (Docker Desktop)"
status: "current"
agent_service: "docker (Linux daemon) / com.docker.service"
aliases: []
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Docker

> [!abstract] In plain words
> The tool that made containers popular. You describe an app in a Dockerfile, build an image, and run it as a container on any machine with Docker.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[Docker]] · **Runs:** Linux, Windows, macOS (Docker Desktop) · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **YAML**: A plain-text format used for configuration files and pipeline definitions; indentation matters.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **registry**: Windows' central settings database.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Container engine and tooling: images built from Dockerfiles, containers run from images, registries (Docker Hub, ACR, ECR) store images, and Docker Compose runs multi-container apps.

## Main parts

- Image: a read-only template built from a Dockerfile
- Container: a running instance of an image
- Registry: where images are stored and pulled from
- Volume: storage that survives the container
- Compose: YAML that runs several containers together

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`docker (Linux daemon) / com.docker.service`

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Container exits immediately | docker logs CONTAINER shows the app's error; check the entrypoint and environment variables |
| Port not reachable | Check the -p host:container mapping and the host firewall |
| Disk filling | Old images and stopped containers pile up: docker system df, then docker system prune (carefully) |

## Where to find its logs

- docker logs CONTAINER
- `/var/lib/docker (Linux data root)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
docker ps -a
docker logs -f CONTAINER
docker exec -it CONTAINER sh
docker images
docker system df
docker compose up -d
docker compose logs -f
```

## Good to know

- Docker Desktop needs a paid subscription for larger companies; check licensing before rolling it out.
- Containers share the host kernel: Linux containers need a Linux kernel (WSL 2 on Windows).

## See also

[[Containers vs virtual machines]] · [[Kubernetes]] · [[Linux servers]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
