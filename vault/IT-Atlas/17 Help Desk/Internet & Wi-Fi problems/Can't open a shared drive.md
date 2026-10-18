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

# Can't open a shared drive

> [!abstract] What's going on
> A mapped drive (like S: or H:) has a red X, or a network folder says access denied.

> [!tip] Think of it like
> A locked filing cabinet in another room: you need a path to the room (network) and a key (permission).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **DFS**: Distributed File System: gives shared folders one path and keeps copies in sync between servers.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check you're on the office network or connected to the VPN.
2. Restart the PC so mapped drives reconnect.
3. Ask whether colleagues can open the same drive.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- `Test-NetConnection SERVER -Port 445` to test file sharing access.
- `net use` lists mapped drives and their status.
- Check the user's group membership against the folder permissions.
- Clear saved credentials in Credential Manager if the password was recently changed.
- Check Group Policy drive maps with `gpresult /r`.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Not on the network or VPN | Connect the VPN first. |
| Missing permission | Add the user to the right group (needs a sign-off from the folder owner). |
| Old saved password | Clear Credential Manager entries. |
| File server down | Escalate to the NOC. |

## Escalate when

- Nobody can open the share (server or DFS problem)
- The user needs access to sensitive data (needs the owner's approval)

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

> [!question]- After a password change, a user's mapped drive keeps asking for credentials. Where do you look?
> Windows Credential Manager: remove the old saved credentials for that server.

## See also

[[User accounts and permissions]] · [[File Server & DFS]] · [[Group Policy]] · [[VPN won't connect]]

## Field notes

Add your own tips and client quirks here.
