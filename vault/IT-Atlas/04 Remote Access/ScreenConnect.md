---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[ConnectWise]]"
deployment: "Cloud or self-hosted"
status: "current"
agent_service: "ScreenConnect Client (instance ID)"
aliases:
  - "ConnectWise Control"
  - "ConnectWise ScreenConnect"
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# ScreenConnect

> [!abstract] In plain words
> ConnectWise's remote control tool. You can join a user's session while they watch, or connect to unattended machines.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[ConnectWise]] · **Runs:** Cloud or self-hosted · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **TCP**: A connection-based network protocol that confirms delivery.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

ConnectWise's remote support and access tool, formerly ConnectWise Control: attended support sessions, unattended access agents and a backstage mode.

## Main parts

- Web server and relay
- Access (unattended) agents
- Support (attended) sessions
- Backstage mode
- Extensions

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`ScreenConnect Client (instance ID)`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8040/TCP web (self-hosted default)
- 8041/TCP relay (self-hosted default)

## Alerts you'll see

- Unexpected new sessions or admin logins
- Agents offline
- Version behind current

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent not connecting | Check the ScreenConnect Client service and that the relay port is reachable |
| Self-hosted server exposed | Confirm it is on a patched version and protected by MFA |

## Good to know

- February 2024: CVE-2024-1709, an authentication bypass rated CVSS 10, was mass-exploited on self-hosted servers. Self-hosted instances must be patched the day a fix ships.

## See also

[[ConnectWise PSA]] · [[ConnectWise Automate]] · [[Splashtop]] · [[TeamViewer]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
