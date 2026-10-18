---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
aliases:
  - "Network Policy Server"
  - "RADIUS"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# NPS

> [!abstract] In plain words
> Windows' RADIUS server: it checks usernames and passwords when people join Wi-Fi or VPN.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Microsoft's RADIUS server for 802.1X Wi-Fi, VPN and switch authentication against Active Directory, often with certificates from AD CS.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 1812/UDP authentication
- 1813/UDP accounting

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Wi-Fi or VPN auth failing | Read Security log events 6272 (granted) and 6273 (denied); the reason code says why |

## See also

[[AD CS]] · [[Active Directory]] · [[802.1X]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
