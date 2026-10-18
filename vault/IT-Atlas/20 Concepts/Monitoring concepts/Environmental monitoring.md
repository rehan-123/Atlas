---
type: "concept"
level: "Mid"
category: "[[Monitoring concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Environmental monitoring

> [!abstract] In one line
> Temperature, humidity, water and power sensors in server rooms and racks.

> [!tip] Think of it like
> Smoke and temperature alarms for the server room.

> [!info]+ Words on this page
> **UPS**: Uninterruptible power supply: a big battery that keeps equipment running in a power cut.
> *More in the [[Glossary]].*

## How it works

- Sensors via UPS network cards, PDUs or dedicated devices (NetBotz and similar).
- Alert on rate of change too: a temperature rising fast means cooling has failed.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why alert on how fast temperature rises?
> A fast rise means cooling has failed, and you have minutes, not hours.

## See also

[[APC Smart-UPS]] · [[Temperature alarm]] · [[UPS on battery]]
