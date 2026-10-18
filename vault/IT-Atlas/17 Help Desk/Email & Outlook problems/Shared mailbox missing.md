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

# Shared mailbox missing

> [!abstract] What's going on
> A shared mailbox (like info@ or accounts@) doesn't show in Outlook, or you can't send as it.

> [!tip] Think of it like
> A key to a shared office: you need to be given the key (permission) and then hang it on your keyring (Outlook).

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Restart Outlook; new access can take up to an hour to appear.
2. Check whether it shows in Outlook on the web (click your picture > Open another mailbox).

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Grant access: `Add-MailboxPermission -Identity SHARED -User USER -AccessRights FullAccess -AutoMapping $true`.
- Grant send: `Add-RecipientPermission -Identity SHARED -Trustee USER -AccessRights SendAs`.
- Check existing permissions: `Get-MailboxPermission SHARED`.
- If auto-mapping doesn't appear, add it manually in Account Settings > More Settings > Advanced.

## Common causes and fixes

| Cause | Fix |
|---|---|
| No permission yet | Grant Full Access and Send As (with manager approval). |
| Permission just added | Wait and restart Outlook. |
| Auto-mapping off | Add the mailbox manually. |
| Sending 'on behalf' instead of 'as' | Grant Send As rather than Send on Behalf. |

## Escalate when

- The mailbox contains sensitive data and the owner hasn't approved access

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

> [!question]- What's the difference between Send As and Send on Behalf?
> Send As looks like it came from the shared mailbox itself. Send on Behalf shows 'USER on behalf of SHARED'.

## See also

[[Exchange Online]] · [[Microsoft 365 PowerShell cheat sheet]] · [[User accounts and permissions]]

## Field notes

Add your own tips and client quirks here.
