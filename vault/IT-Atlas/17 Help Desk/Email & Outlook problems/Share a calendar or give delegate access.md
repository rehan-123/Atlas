---
type: "guide"
level: "Mid"
area: "[[Email & Outlook problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Share a calendar or give delegate access

> [!abstract] What's going on
> A user wants a colleague or assistant to see or manage their calendar.

> [!tip] Think of it like
> Giving a colleague a spare key to your diary: decide whether they can just read it or also write in it.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. In Outlook, right-click the calendar > Sharing permissions, add the person and choose a level (can view, can edit, delegate).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Admins: Add-MailboxFolderPermission -Identity USER:\Calendar -User DELEGATE -AccessRights Editor.
- Check existing rights: Get-MailboxFolderPermission USER:\Calendar.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Delegate sees nothing | Wait for sync or re-add the calendar. |
| Wrong level | Change the permission. |

## Escalate when

- Executive calendars with sensitive meetings (confirm with the owner)

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

> [!question]- Which permission level lets someone change calendar items but not get meeting requests?
> Editor (Delegate also receives meeting requests).

## See also

[[Exchange Online]] · [[Shared mailbox missing]]

## Field notes

Add your own tips and client quirks here.
