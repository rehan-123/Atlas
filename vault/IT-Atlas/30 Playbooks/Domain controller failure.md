---
type: "playbook"
level: "Senior"
severity: "P1 if the last DC at a site or holding FSMO roles, otherwise P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Domain controller failure

> [!abstract] What this alert means
> A domain controller has crashed, been corrupted or is gone for good.
>
> **Why it matters:** If it held FSMO roles or was the only DC at a site, sign-ins, DNS and password changes can fail.

**How urgent:** P1 if the last DC at a site or holding FSMO roles, otherwise P2. See [[Severity levels]].

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **FSMO**: Five special Active Directory roles that only one domain controller holds at a time.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## You'll see this when

- DC unreachable or failing dcdiag
- Users at a site can't log on or resolve names
- Replication errors pointing at one DC

## First 5 minutes

1. Confirm other DCs are healthy (dcdiag /e /q, repadmin /replsummary)
2. Check which DC holds the FSMO roles: netdom query fsmo
3. Make sure clients have another DNS server that's a working DC

## Find the cause

- Hardware or VM failure (console, hypervisor)
- AD database corruption (NTDS events)
- USN rollback after a snapshot restore (event 2095)

## Fix it

- Restore the DC from a proper system-state backup only if it's the only one; otherwise build a new DC
- If the old DC is gone for good: seize FSMO roles to a healthy DC (Move-ADDirectoryServerOperationMasterRole -Force) and clean up metadata
- Never bring a seized-from DC back online
- Update DHCP DNS options and static DNS settings

## Ask for help (escalate) when

- Any FSMO seizure
- Suspected USN rollback
- All DCs affected or signs of compromise

## Write it up

Copy this into the ticket and fill it in:

```
DC: 
Failure: 
FSMO holder before/after: 
Other DCs healthy: 
Recovery path chosen: 
Metadata cleanup done:
```

## See also

[[Active Directory]] · [[FSMO roles]] · [[AD replication failure]] · [[DNS resolution failure]]
