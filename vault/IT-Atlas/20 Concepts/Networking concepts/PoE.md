---
type: "concept"
level: "Mid"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# PoE

> [!abstract] In one line
> Power over Ethernet powers APs, phones and cameras from the switch.

> [!tip] Think of it like
> PoE sends power down the same network cable, so access points and phones don't need a plug.

## How it works

- Standards: 802.3af (15.4 W), 802.3at PoE+ (30 W), 802.3bt (60 W and 90 W).
- Switches have a total PoE budget; exceeding it means devices randomly lose power.
- `show power inline` on Cisco shows budget and per-port draw.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- New cameras randomly reboot after being added to a switch. What should you check?
> The switch's total PoE budget: it may be giving out more power than it can supply.

## See also

[[Cisco Catalyst]] · [[Meraki MS]]
