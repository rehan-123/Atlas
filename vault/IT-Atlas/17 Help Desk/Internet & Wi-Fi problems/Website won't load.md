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

# Website won't load

> [!abstract] What's going on
> One website won't open, but others work.

> [!tip] Think of it like
> One shop on the high street is closed while the others are open: the road is fine, that shop has the problem.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **cookie**: Small note a website stores in your browser, for example to remember that you're signed in.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Try another browser or a private (InPrivate or Incognito) window.
2. Try on your phone using mobile data to see if the site is down for everyone.
3. Clear the browser cache and cookies for that site.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- `Resolve-DnsName SITE` and `Test-NetConnection SITE -Port 443` to test name lookup and connection.
- Check the web filter or firewall logs (DNSFilter, Umbrella, FortiGate) for a block.
- Check the certificate error message, and the PC's date and time.
- Check proxy settings (Settings > Network & internet > Proxy).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Site is down for everyone | Nothing to fix locally; wait or contact the site owner. |
| Blocked by web filter | Request an allow-list change if the business needs it. |
| Old cached data | Clear cache and cookies. |
| Wrong PC clock causing certificate errors | Fix the time. |

## Escalate when

- A business-critical site is blocked by the filter
- A client's own website is down (NOC playbook: Website down)

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

> [!question]- A site shows a certificate error only on one PC. What simple thing do you check?
> The PC's date and time. A wrong clock makes valid certificates look invalid.

## See also

[[Cache and cookies]] · [[Browser acting up]] · [[SSL & TLS]] · [[Website down]] · [[DNSFilter]] · [[Cisco Umbrella]]

## Field notes

Add your own tips and client quirks here.
