---
type: "guide"
level: "Junior"
area: "[[Software & app problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Install software request

> [!abstract] What's going on
> A user needs a new app installed.

> [!tip] Think of it like
> A building with an approved suppliers list: anything else needs a check before it comes in.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Software & app problems]]

> [!info]+ Words on this page
> **Company Portal**: Intune's app store where users install approved work apps.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check the company app store first: Company Portal (Intune), Self Service (Jamf) or Software Center.
2. Raise a ticket with the app name and why you need it.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check the app is approved and licensed.
- Deploy through the RMM, Intune or `winget install --id APP.ID` rather than by hand.
- Never give users admin rights to install things; use the deployment tool or an admin elevation tool.

## Common causes and fixes

| Cause | Fix |
|---|---|
| App not approved | Send for approval. |
| Needs admin rights | Deploy via management tool. |
| License needed | Purchase via the right channel. |

## Escalate when

- Security review needed for unknown software

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

> [!question]- Why not just give the user local admin rights to install it?
> Admin rights let malware install too. Use the deployment tool so installs stay controlled and repeatable.

## See also

[[winget]] · [[Microsoft Intune]] · [[Least privilege]] · [[Software deployment]]

## Field notes

Add your own tips and client quirks here.
