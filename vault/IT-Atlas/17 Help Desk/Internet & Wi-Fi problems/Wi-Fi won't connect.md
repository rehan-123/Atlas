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

# Wi-Fi won't connect

> [!abstract] What's going on
> The laptop can't join the Wi-Fi, or joins but says 'No internet, secured'.

> [!tip] Think of it like
> A guest list at a door: the right name (network), the right password and the door must be open (access point working).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Make sure Wi-Fi and Airplane mode are set correctly (Windows+A).
2. Click the network, choose Forget, then reconnect and re-enter the password.
3. Move closer to the access point and restart the laptop.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- `netsh wlan show interfaces` shows the network, signal strength and channel.
- `netsh wlan show wlanreport` builds a report of recent connection failures.
- Corporate Wi-Fi (802.1X): check the device certificate and that the user or device is in the allowed group.
- Check the Wi-Fi driver version and power-saving settings on the adapter.
- Check the access point or controller (UniFi, Meraki) for the client's failure reason.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong or changed password | Forget and reconnect with the current password. |
| Expired certificate on corporate Wi-Fi | Renew via Intune or Group Policy. |
| Weak signal | Move closer; check AP coverage. |
| Old Wi-Fi driver | Update the driver. |

## Escalate when

- Many users can't join the same Wi-Fi
- An access point is offline
- 802.1X or RADIUS (NPS) is failing

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

> [!question]- Which command produces an HTML report of recent Wi-Fi connection problems?
> `netsh wlan show wlanreport`.

## See also

[[Wi-Fi basics]] · [[Wireless]] · [[802.1X]] · [[NPS]] · [[Wi-Fi slow or drops]]

## Field notes

Add your own tips and client quirks here.
