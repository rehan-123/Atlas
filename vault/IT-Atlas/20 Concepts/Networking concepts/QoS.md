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

# QoS

> [!abstract] In one line
> Quality of Service prioritizes latency-sensitive traffic such as voice and video.

> [!tip] Think of it like
> QoS is a priority lane: voice calls skip the queue ahead of big downloads.

## How it works

- Marks traffic (DSCP EF for voice) and queues it first.
- Only helps where there is congestion and only on links you control; the internet ignores your markings.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Does QoS fix call quality when the problem is at the ISP?
> No. It only works on links you control.

## See also

[[SIP]] · [[Voice quality problems]]
