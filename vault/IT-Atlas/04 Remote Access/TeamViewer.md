---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[TeamViewer]]"
deployment: "SaaS"
status: "current"
agent_service: "TeamViewer"
aliases: []
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# TeamViewer

> [!abstract] In plain words
> A very common remote control tool. Scammers use it too, so be careful with unknown requests.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[TeamViewer]] · **Runs:** SaaS · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Widely used remote support and access tool with attended and unattended modes; TeamViewer Tensor is the enterprise edition.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`TeamViewer`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5938/TCP primary (falls back to 443 and 80)

## Good to know

- A frequent target of tech-support scams and account takeover. Enforce 2FA and allowlists on business accounts.

## See also

[[AnyDesk]] · [[ScreenConnect]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
