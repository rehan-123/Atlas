---
type: "guide"
level: "Mid"
area: "[[Sign-in & password problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Can't sign in to Microsoft 365

> [!abstract] What's going on
> Errors when signing in to Outlook, Teams or office.com, or sign-in loops.

> [!tip] Think of it like
> A building pass that works at the front door but not the lift: check which door (app, location, device) is refusing it and why.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Sign-in & password problems]]

> [!info]+ Words on this page
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **UPN**: User principal name: the sign-in name that looks like an email address.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **token**: A temporary digital key used to prove you're allowed in.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check you're using your full work email address.
2. Try a private browser window at office.com.
3. Sign out of all Office apps, restart and sign in again.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Entra admin center > Sign-in logs: find the failure and its error code.
- Check the account is enabled and licensed, and not blocked by a Conditional Access policy.
- On the PC: `dsregcmd /status` shows whether the device is Entra joined and has a valid token (AzureAdPrt: YES).
- Clear Office identities in Credential Manager.
- Check the user's password hasn't expired or been changed elsewhere (sync with Entra Connect).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong account or typo | Use the full UPN. |
| Conditional Access blocked (device not compliant, wrong country) | Fix device compliance or review the policy. |
| Account disabled or unlicensed | Enable or license it. |
| Token or cache problem | Clear credentials; sign out and in. |

## Escalate when

- Many users can't sign in (Microsoft outage or policy change)
- Sign-ins come from unknown locations

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

> [!question]- Where do you find the exact reason a Microsoft 365 sign-in failed?
> Entra ID sign-in logs: each failure shows an error code and which Conditional Access policy applied.

## See also

[[Microsoft Entra ID]] · [[Microsoft 365]] · [[Domain-joined vs cloud-joined PCs]] · [[MFA not working or new phone]]

## Field notes

Add your own tips and client quirks here.
