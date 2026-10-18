---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[Patch management]]"
vendor: "[[Microsoft]]"
deployment: "On-prem Windows Server role"
status: "deprecated"
aliases:
  - "Windows Server Update Services"
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# WSUS

> [!abstract] In plain words
> A Windows Server role that lets you approve and hand out Microsoft updates from your own server. Microsoft has stopped developing it.
>
> **What kind of tool is this?** Patching means installing updates, mostly security fixes. These tools decide what gets installed, when, and report what's missing.

**Made by:** [[Microsoft]] · **Runs:** On-prem Windows Server role · **Status:** deprecated · **Category:** [[Endpoint & Patch Management]] › [[Patch management]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **HTTPS**: Encrypted HTTP (port 443).
> **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Windows Server Update Services: on-prem approval and distribution of Microsoft updates. Microsoft announced its deprecation in 2024 (no new features, still supported); plan a move to cloud patching.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8530/TCP HTTP
- 8531/TCP HTTPS

## Alerts you'll see

- Clients not reporting
- WSUS database or content growing out of control
- Sync failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Console times out | Run the WSUS Server Cleanup Wizard and re-index the SUSDB database |
| Clients not reporting | Check the GPO WSUS URL and port, and the client's Windows Update log |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-WsusServer
Invoke-WsusServerCleanup -CleanupObsoleteUpdates -CleanupUnneededContentFiles -DeclineSupersededUpdates
```

## See also

[[Windows Update]] · [[Microsoft Configuration Manager]] · [[Windows Update for Business]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
