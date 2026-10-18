---
type: "guide"
level: "Junior"
area: "[[Email & Outlook problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Outlook won't open

> [!abstract] What's going on
> Outlook gets stuck on 'Loading profile', crashes, or keeps asking for a password.

> [!tip] Think of it like
> A notebook (profile) with a torn page: making a fresh notebook usually fixes it, and your mail is safe on the server.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **token**: A temporary digital key used to prove you're allowed in.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Restart the PC.
2. Try Outlook on the web (outlook.office.com). If mail works there, your mailbox is fine.
3. Start Outlook in safe mode: press Windows+R and type `outlook.exe /safe`.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- If safe mode works, disable add-ins (File > Options > Add-ins > COM Add-ins).
- Create a new profile: Control Panel > Mail (Microsoft Outlook) > Show Profiles > Add.
- Repair Office: Settings > Apps > Microsoft 365 Apps > Modify > Quick Repair, then Online Repair.
- Password loops: clear Office entries in Credential Manager and check `dsregcmd /status` for sign-in problems.
- Note whether the user has new Outlook or classic Outlook; the fixes differ.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Faulty add-in | Disable it. |
| Damaged profile or cache | Create a new profile. |
| Damaged Office install | Quick or Online Repair. |
| Sign-in token problem | Clear credentials; sign out and in of Office. |

## Escalate when

- Outlook on the web also fails (mailbox or tenant issue)
- Many users have the same problem
- The mailbox is on-premises Exchange and the server is down

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

> [!question]- Outlook won't open but Outlook on the web works. Is the user's email lost?
> No. The mailbox lives on the server; the problem is the PC's Outlook profile, cache or add-ins.

## See also

[[Exchange Online]] · [[Microsoft 365]] · [[Outlook not receiving email]] · [[Office activation error]]

## Field notes

Add your own tips and client quirks here.
