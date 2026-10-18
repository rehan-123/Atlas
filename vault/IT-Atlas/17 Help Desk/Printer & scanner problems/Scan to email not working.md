---
type: "guide"
level: "Mid"
area: "[[Printer & scanner problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Scan to email not working

> [!abstract] What's going on
> The copier scans but the email never arrives, or it shows an SMTP or login error.

> [!tip] Think of it like
> A post room that needs a valid stamp (sign-in) before it will send letters. Old stamps stop working when the post office (Microsoft) changes the rules.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Printer & scanner problems]]

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **SPF**: A DNS record listing which servers may send email for a domain.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check the email address typed on the copier.
2. Check your Junk folder.
3. Try scanning to a different address.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Read the copier's error code in its web admin page.
- Check how it sends: SMTP AUTH to smtp.office365.com (port 587), direct send to the domain's MX, or an SMTP relay connector.
- SMTP AUTH: Microsoft is retiring basic authentication for it, so move the copier to a relay connector, direct send or a scanning service if it uses a username and password.
- Check the sending account's password hasn't changed or expired, and that it isn't blocked by MFA.
- Run a message trace for the copier's sender address.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Saved password changed | Update it on the copier. |
| Basic authentication blocked | Move to a connector, direct send or OAuth-capable firmware. |
| Mail flagged as spam | Fix SPF to include the sending IP; release from quarantine. |

## Escalate when

- The copier firmware can't do any supported method (vendor needed)

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

> [!question]- Why do many copiers suddenly stop scanning to email after Microsoft changes?
> They use SMTP basic authentication (username and password), which Microsoft is retiring. They need a relay connector, direct send or newer firmware.

## See also

[[Exchange Online]] · [[SPF, DKIM & DMARC]] · [[Email delivery problems]]

## Field notes

Add your own tips and client quirks here.
