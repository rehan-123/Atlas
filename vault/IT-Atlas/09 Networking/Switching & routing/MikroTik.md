---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Switching & routing]]"
vendor: "[[MikroTik]]"
deployment: "Hardware or CHR VM"
status: "current"
aliases:
  - "RouterOS"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# MikroTik

> [!abstract] In plain words
> Cheap, powerful routers common at ISPs and small offices.
>
> **What kind of tool is this?** Switches connect devices inside a building; routers connect different networks together.

**Made by:** [[MikroTik]] · **Runs:** Hardware or CHR VM · **Category:** [[Networking]] › [[Switching & routing]]

> [!info]+ Words on this page
> **ISP**: Internet service provider.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **CLI**: Command-line interface: typing commands instead of clicking.
> **TCP**: A connection-based network protocol that confirms delivery.
> **router**: Device that connects one network to another, such as the office to the internet.
> **branch**: A separate line of changes in Git, merged back into main after review.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Low-cost routers and switches running RouterOS, managed with Winbox, WebFig or CLI. Common in ISPs and branch offices.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8291/TCP Winbox

## Good to know

- Keep RouterOS updated and Winbox off the internet; old versions were widely exploited for botnets.

## See also

[[BGP]] · [[OSPF]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
