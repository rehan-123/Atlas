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

# MFA not working or new phone

> [!abstract] What's going on
> The sign-in approval doesn't arrive, or the user got a new phone and can't approve sign-ins.

> [!tip] Think of it like
> A second lock on the door whose key lives on your phone. A new phone means a new key has to be cut.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **authenticator app**: Phone app (such as Microsoft Authenticator) that approves sign-ins or shows one-time codes for MFA.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Open the Microsoft Authenticator app and pull down to refresh; check notifications are allowed.
2. Check the phone's time is set automatically.
3. Use another method if you have one (code from the app, text message).
4. New phone: you need IT to reset your MFA unless you set up the old phone's backup.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Verify identity first; MFA resets are a favourite attacker trick.
- Entra admin center > Users > USER > Authentication methods: remove the old method or choose 'Require re-register multifactor authentication'.
- Issue a Temporary Access Pass if the organization uses them.
- Check sign-in logs for the reason MFA failed.

## Common causes and fixes

| Cause | Fix |
|---|---|
| New or reset phone | Re-register MFA after verifying identity. |
| Notifications off or battery saver | Allow notifications. |
| Wrong phone time | Set time automatically. |
| MFA fatigue attack (many unexpected prompts) | Tell the user to deny; reset password; investigate. |

## Escalate when

- The user gets prompts they didn't start (someone has their password)
- An admin account needs an MFA reset

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

> [!question]- A user gets MFA prompts at 2 a.m. that they didn't trigger. What does it mean?
> Someone else has their password and is trying to sign in. Deny the prompts, reset the password and investigate.

## See also

[[Multi-factor authentication]] · [[Microsoft Entra ID]] · [[Account hacked or sending spam]] · [[Can't sign in to Microsoft 365]]

## Field notes

Add your own tips and client quirks here.
