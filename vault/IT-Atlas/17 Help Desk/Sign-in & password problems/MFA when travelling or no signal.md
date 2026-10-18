---
type: "guide"
level: "Junior"
area: "[[Sign-in & password problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# MFA when travelling or no signal

> [!abstract] What's going on
> A user abroad or without mobile signal can't approve sign-ins.

> [!tip] Think of it like
> A second key that needs a phone signal: carry a spare that works offline.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **authenticator app**: Phone app (such as Microsoft Authenticator) that approves sign-ins or shows one-time codes for MFA.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Use the Microsoft Authenticator app's one-time code (it works without signal or data).
2. Connect the phone to Wi-Fi to receive push approvals.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Register a second method before travel (another phone, a FIDO2 key).
- Check conditional access location rules that may block sign-ins from other countries.
- Issue a Temporary Access Pass after verifying identity, if allowed.

## Common causes and fixes

| Cause | Fix |
|---|---|
| No signal for SMS | Use the app code. |
| Blocked by country policy | Apply the travel exception process. |

## Escalate when

- Sign-in attempts from a country the user isn't in

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

> [!question]- Do Authenticator one-time codes need mobile data?
> No. They're generated on the phone and work offline.

## See also

[[MFA not working or new phone]] · [[Multi-factor authentication]] · [[Microsoft Authenticator]]

## Field notes

Add your own tips and client quirks here.
