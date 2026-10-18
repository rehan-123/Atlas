---
type: "guide"
level: "Junior"
area: "[[Internet & Wi-Fi problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Wi-Fi slow or drops

> [!abstract] What's going on
> Wi-Fi is connected but slow, or keeps disconnecting, especially on calls.

> [!tip] Think of it like
> Trying to talk in a crowded, noisy room: the further away and the more people talking, the more you have to repeat yourself.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **bandwidth**: How much data a link can carry per second.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Move closer to the access point, away from thick walls and microwaves.
2. Plug in a network cable for important calls.
3. Close large downloads or cloud sync during calls.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check signal and speed: `netsh wlan show interfaces` (look at Signal and Receive rate).
- Check whether the laptop is on 2.4 GHz (slower, crowded) or 5/6 GHz.
- Turn off power saving on the Wi-Fi adapter (Device Manager > adapter > Power Management).
- Check the access point for channel congestion and how many clients it has.
- Run a speed test on Wi-Fi and on a cable to compare.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Weak signal or too far from the access point | Move closer or add an access point. |
| Crowded 2.4 GHz band | Prefer 5 or 6 GHz. |
| Adapter power saving | Disable it. |
| Internet line itself is saturated | Check firewall bandwidth use: escalate to the NOC. |

## Escalate when

- Whole office has slow Wi-Fi
- The internet link is maxed out
- An access point keeps rebooting

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why does a cable often fix call quality when Wi-Fi seems 'connected'?
> Wi-Fi shares airtime with everyone nearby and loses packets with distance and interference; a cable doesn't.

## See also

[[Wi-Fi basics]] · [[Wireless]] · [[High latency]] · [[Voice quality problems]]

## Field notes

Add your own tips and client quirks here.
