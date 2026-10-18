---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[DNS & web filtering]]"
vendor: "[[Cisco]]"
deployment: "Cloud"
status: "current"
aliases:
  - "OpenDNS"
  - "Umbrella"
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Cisco Umbrella

> [!abstract] In plain words
> Blocks dangerous websites by filtering DNS lookups, on and off the office network.
>
> **What kind of tool is this?** DNS filtering blocks bad or unwanted websites by refusing to look up their addresses.

**Made by:** [[Cisco]] · **Runs:** Cloud · **Category:** [[Security]] › [[DNS & web filtering]]

> [!info]+ Words on this page
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

DNS-layer security and secure web gateway, from the OpenDNS acquisition; roaming protection is now part of Cisco Secure Client.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 53/UDP and TCP to 208.67.222.222 and 208.67.220.220

## See also

[[DNS]] · [[DNSFilter]] · [[Cisco Secure Client]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
