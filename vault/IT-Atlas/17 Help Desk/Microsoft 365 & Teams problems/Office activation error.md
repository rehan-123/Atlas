---
type: "guide"
level: "Junior"
area: "[[Microsoft 365 & Teams problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Office activation error

> [!abstract] What's going on
> Word or Excel says 'Unlicensed product', 'Account error' or keeps asking you to activate.

> [!tip] Think of it like
> A gym membership card: the app checks with the gym (Microsoft) that your membership (license) is still valid.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Microsoft 365 & Teams problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Sign out of Office (File > Account > Sign out) and sign back in with your work account.
2. Restart the PC.
3. Check you're online.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check the user has a license that includes the desktop apps (Microsoft 365 admin center).
- Check the number of installs on their account (each user can activate on a limited number of devices).
- Clear old Office identities in Credential Manager and `dsregcmd /status` for device sign-in health.
- Repair Office (Quick, then Online Repair).

## Common causes and fixes

| Cause | Fix |
|---|---|
| License removed or wrong plan | Assign the right license. |
| Signed in with a personal account | Sign in with the work account. |
| Too many activated devices | Sign out an old device. |
| Damaged install | Repair. |

## Escalate when

- The license needs buying
- Shared computers need Shared Computer Activation set up

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

> [!question]- A user's license was changed to a web-only plan. What happens to their desktop Office?
> It goes into reduced functionality (unlicensed) after a grace period; they need a plan that includes desktop apps.

## See also

[[Microsoft 365]] · [[Microsoft Entra ID]] · [[Outlook won't open]]

## Field notes

Add your own tips and client quirks here.
