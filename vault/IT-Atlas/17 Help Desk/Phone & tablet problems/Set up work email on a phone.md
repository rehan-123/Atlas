---
type: "guide"
level: "Mid"
area: "[[Phone & tablet problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Set up work email on a phone

> [!abstract] What's going on
> A user wants Outlook and Teams on their phone.

> [!tip] Think of it like
> A visitor badge for your phone: the company checks the phone meets the rules before handing it over.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Phone & tablet problems]]

> [!info]+ Words on this page
> **Company Portal**: Intune's app store where users install approved work apps.
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Install Microsoft Outlook and Microsoft Authenticator from the App Store or Google Play.
2. Open Outlook, add your work email and approve the sign-in.
3. If asked, install Company Portal and follow the steps (this protects work data only).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check Intune app protection or enrollment policies for what the phone must meet.
- Check Conditional Access isn't blocking the phone's OS version.
- Help with sign-in errors using Entra sign-in logs.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Phone OS too old | Update the phone. |
| App protection needs a PIN | Set the app PIN. |
| Native mail app blocked by policy | Use Outlook. |

## Escalate when

- Policy needs changing for an exception

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

> [!question]- Why do many companies require the Outlook app instead of the phone's built-in mail app?
> App protection policies can protect and wipe work data inside Outlook, but not inside the built-in mail app.

## See also

[[Microsoft Intune]] · [[Multi-factor authentication]] · [[Phone email not syncing]]

## Field notes

Add your own tips and client quirks here.
