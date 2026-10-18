---
type: "guide"
level: "Mid"
area: "[[New starters & leavers]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# New starter setup

> [!abstract] What's going on
> Getting a new employee's account, email, apps and laptop ready for day one.

> [!tip] Think of it like
> Getting a hotel room ready: key card, bed made and Wi-Fi password on the desk before the guest arrives.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[New starters & leavers]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **UPN**: User principal name: the sign-in name that looks like an email address.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **Wi-Fi**: Wireless network connection using radio signals.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Managers: send the request at least a few days ahead with name, start date, job role and who to copy access from.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Create the account (AD or Entra), set the UPN and a temporary password with change at first sign-in.
- Assign the license and add the right groups (email lists, Teams, SharePoint, shared mailboxes, apps).
- Set up MFA on day one with the user (or a Temporary Access Pass).
- Prepare the device: Autopilot or MDM enrollment, apps deployed, encryption on.
- Write the setup in the ticket and send the user a short welcome guide.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Copying access from another user | Check what the role needs; don't copy everything blindly. |
| Late request | Prioritize account and email first. |
| Device not ready | Loaner device. |

## Escalate when

- Access requested to sensitive systems needs approval
- Special software or hardware needed

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

> [!question]- Why not just copy all permissions from a colleague when setting up a new user?
> The colleague may have extra access the new person shouldn't have. Give what the role needs (least privilege).

## See also

[[Windows Autopilot]] · [[Microsoft Intune]] · [[Microsoft Entra ID]] · [[Least privilege]] · [[Leaver offboarding]]

## Field notes

Add your own tips and client quirks here.
