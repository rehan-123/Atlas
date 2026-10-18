---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Switching & routing]]"
vendor: "[[Cisco]]"
deployment: "Hardware"
status: "current"
aliases:
  - "Cisco IOS"
  - "IOS-XE"
  - "Cisco switch"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Cisco Catalyst

> [!abstract] In plain words
> Cisco's main switch range. Its commands are the ones most network tutorials teach.
>
> **What kind of tool is this?** Switches connect devices inside a building; routers connect different networks together.

**Made by:** [[Cisco]] · **Runs:** Hardware · **Category:** [[Networking]] › [[Switching & routing]]

> [!info]+ Words on this page
> **CLI**: Command-line interface: typing commands instead of clicking.
> **CPU**: The processor, the part of a computer that does the calculations.
> **router**: Device that connects one network to another, such as the office to the internet.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Cisco's enterprise switching line running IOS-XE (and IOS on older models). The CLI most network commands are modelled on.

## Alerts you'll see

- Interface down or flapping
- Input errors and CRC errors
- Spanning tree topology changes
- High CPU
- Power supply or fan failure

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Port errors | show interfaces counters errors; CRC errors usually mean cabling, optics or a duplex mismatch |
| Loop or broadcast storm | show spanning-tree and check for many topology changes; look for a rogue unmanaged switch |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
show version
show ip interface brief
show interfaces status
show interfaces counters errors
show logging
show spanning-tree
show mac address-table address MAC
show cdp neighbors detail
show power inline
show processes cpu sorted
```

## See also

[[VLAN]] · [[Spanning Tree]] · [[Interface errors and packet loss]] · [[Meraki MS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
