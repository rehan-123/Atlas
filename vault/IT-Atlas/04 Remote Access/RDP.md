---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows"
status: "current"
aliases:
  - "Remote Desktop Protocol"
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# RDP

> [!abstract] In plain words
> Remote Desktop Protocol: Windows' built-in way to log in to another machine's desktop. It should never be open to the internet.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **RDS**: Remote Desktop Services: many users working on one shared Windows server.
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **NLA**: Network Level Authentication: RDP checks your login before opening a session.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **ZTNA**: Zero-trust network access: app-by-app access with checks on every connection, replacing a broad VPN.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Microsoft's Remote Desktop Protocol, used by Remote Desktop clients, RDS and most remote-access gateways.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 3389/TCP and 3389/UDP

## Alerts you'll see

- RDP exposed to the internet
- Brute-force logons (Security 4625 bursts)

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Cannot connect | Test-NetConnection HOST -Port 3389; check the service, firewall and Network Level Authentication |
| CredSSP or NLA errors | Check both ends are patched and time is in sync |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Test-NetConnection HOST -Port 3389
qwinsta /server:HOST
logoff SESSIONID /server:HOST
```

## Good to know

- Never expose 3389 to the internet. Put it behind RD Gateway, VPN or ZTNA with MFA.

## See also

[[RDS]] · [[RD Gateway]] · [[Account lockout storm]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
