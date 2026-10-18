---
type: "guide"
level: "Mid"
area: "[[Internet & Wi-Fi problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Remote Desktop won't connect

> [!abstract] What's going on
> Remote Desktop to a work PC or server fails.

> [!tip] Think of it like
> Phoning an office where the line is busy, the receptionist doesn't know you, or the building is closed.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **NLA**: Network Level Authentication: RDP checks your login before opening a session.
> **UPN**: User principal name: the sign-in name that looks like an email address.
> **RDS**: Remote Desktop Services: many users working on one shared Windows server.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check you're connected to the VPN or using the company's gateway.
2. Check you typed the full computer name.
3. Make sure the remote PC is switched on and not asleep.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Test-NetConnection HOST -Port 3389.
- Check the user is in Remote Desktop Users or the right group.
- Check NLA and credentials (domain\user or UPN).
- RD Gateway: check its certificate and the user's policy (CAP/RAP).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Not on VPN | Connect the VPN. |
| PC asleep or off | Wake-on-LAN or power settings. |
| No permission | Add to the allowed group. |

## Escalate when

- RD Gateway or RDS farm problems affecting many users

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

> [!question]- Which port must be reachable for a direct RDP connection?
> TCP 3389 (unless changed).

## See also

[[RDP]] · [[RD Gateway]] · [[VPN won't connect]]

## Field notes

Add your own tips and client quirks here.
