---
type: "playbook"
level: "Mid"
severity: "P3 (P2 for security baselines)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Group Policy not applying

> [!abstract] What this alert means
> A Group Policy setting isn't reaching the computers or users it should.
>
> **Why it matters:** Security settings, drive maps and software rely on policies; a silent failure leaves devices unprotected or misconfigured.

**How urgent:** P3 (P2 for security baselines). See [[Severity levels]].

> [!info]+ Words on this page
> **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **DC**: Domain controller: a server running Active Directory.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **SMB**: The Windows file-sharing protocol (port 445).
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- A setting that should be enforced is missing on clients
- Event 1058/1030 or 7016 in the GroupPolicy logs
- gpresult shows the GPO as denied or not listed

## First 5 minutes

1. Run gpresult /h report.html on an affected machine and read the Denied GPOs section
2. Check the object is in the OU where the GPO is linked and the link is enabled
3. Check security filtering and WMI filters

## Find the cause

- Security filtering removed Authenticated Users read rights
- Setting is in the Computer half but linked to a users OU (or the reverse)
- SYSVOL not replicating: different GPO versions on different DCs (check DFS-R)
- Client can't reach SYSVOL (DNS, network, SMB signing)
- A higher-precedence GPO or loopback processing overrides it

## Fix it

- Correct the link, filtering or permissions
- Fix SYSVOL replication first if DCs disagree
- gpupdate /force and recheck gpresult

## Ask for help (escalate) when

- SYSVOL/DFS-R replication is broken
- A security baseline isn't applying across many devices

## Write it up

Copy this into the ticket and fill it in:

```
GPO: 
Affected scope: 
gpresult finding: 
Cause: 
Fix: 
Verified:
```

## See also

[[Group Policy]] · [[Group Policy troubleshooting]] · [[AD replication failure]] · [[DNS resolution failure]]
