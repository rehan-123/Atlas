---
type: "playbook"
level: "Mid"
severity: "P2 (P1 for production)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure VM unreachable

> [!abstract] What this alert means
> An Azure virtual machine doesn't respond to RDP, SSH or its application.
>
> **Why it matters:** Services hosted on it are down; cloud VMs can't be reached by walking to a console.

**How urgent:** P2 (P1 for production). See [[Severity levels]].

> [!info]+ Words on this page
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **BSOD**: Blue screen of death: Windows crashed.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- RDP/SSH times out
- Application health checks fail
- Azure Monitor alerts

## First 5 minutes

1. Check the VM is running and Resource Health is Available
2. Look at Boot diagnostics (screenshot and serial log)
3. Check NSG rules, route tables and whether access goes through a VPN, Bastion or firewall

## Find the cause

- Guest OS stuck (updates, BSOD) visible in boot diagnostics
- NSG or Azure Firewall rule change
- Guest firewall or RDP service disabled
- Disk full inside the VM

## Fix it

- Use Run Command or the Serial Console to repair the guest
- Fix NSG/route rules
- Redeploy the VM to new host hardware if the host is the problem
- Restore from backup if the OS is corrupted

## Ask for help (escalate) when

- Data disks not attaching
- Several VMs or a whole region affected

## Write it up

Copy this into the ticket and fill it in:

```
VM: 
Resource health: 
Boot diagnostics: 
Network path checked: 
Fix:
```

## See also

[[Microsoft Azure]] · [[Server unreachable]] · [[Azure Monitor]]
