---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor:
deployment: "Self-hosted (open source)"
status: "current"
agent_service: "Mesh Agent"
aliases: []
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# MeshCentral

> [!abstract] In plain words
> A free, self-hosted tool for remote desktop and command line access.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Runs:** Self-hosted (open source) · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

Open-source, web-based remote management: remote desktop, terminal and file transfer through a self-hosted server. Used by Tactical RMM.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Mesh Agent`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP agent and web

## See also

[[Tactical RMM]] · [[RustDesk]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
