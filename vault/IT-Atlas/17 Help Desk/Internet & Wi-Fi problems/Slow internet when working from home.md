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

# Slow internet when working from home

> [!abstract] What's going on
> Calls drop and files load slowly at home.

> [!tip] Think of it like
> A narrow lane shared by the whole household: everyone streaming at once makes the work traffic queue.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **Wi-Fi**: Wireless network connection using radio signals.
> **router**: Device that connects one network to another, such as the office to the internet.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Run a speed test with and without the VPN.
2. Move closer to the router or use a cable.
3. Pause big downloads and streaming during calls.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check whether full-tunnel VPN sends Teams/Zoom through the office; split tunnelling for meeting traffic helps.
- Check the home router's band (5 GHz) and firmware.
- Compare with a mobile hotspot to isolate the home broadband.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Weak Wi-Fi | Cable or move closer. |
| VPN hairpinning | Split tunnel meeting traffic. |
| Slow home plan | User contacts their provider. |

## Escalate when

- Many remote users slow at once (VPN gateway capacity)

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

> [!question]- Why can a full-tunnel VPN make Teams calls worse at home?
> All traffic travels to the office first and back out, adding delay and using the office link.

## See also

[[Wi-Fi slow or drops]] · [[VPN won't connect]] · [[Voice quality problems]]

## Field notes

Add your own tips and client quirks here.
