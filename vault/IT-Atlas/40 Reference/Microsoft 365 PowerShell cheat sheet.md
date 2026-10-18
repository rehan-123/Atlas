---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft 365 PowerShell cheat sheet

Common Microsoft 365 admin commands.

```powershell
# Connect
Connect-MgGraph -Scopes 'User.Read.All','Directory.Read.All','AuditLog.Read.All'
Connect-ExchangeOnline -UserPrincipalName ADMIN@DOMAIN

# Users and licences
Get-MgUser -All -Property DisplayName,UserPrincipalName,AccountEnabled | Select-Object DisplayName, UserPrincipalName, AccountEnabled
Get-MgSubscribedSku | Select-Object SkuPartNumber, ConsumedUnits, @{n='Enabled';e={$_.PrepaidUnits.Enabled}}

# Mailboxes
Get-EXOMailbox -ResultSize Unlimited -RecipientTypeDetails SharedMailbox
Get-EXOMailboxStatistics USER | Select-Object DisplayName, TotalItemSize, ItemCount
Get-InboxRule -Mailbox USER
Get-Mailbox -ResultSize Unlimited | Where-Object { $_.ForwardingSmtpAddress -or $_.ForwardingAddress }

# Message trace (newer modules)
Get-MessageTraceV2 -RecipientAddress USER -StartDate (Get-Date).AddDays(-2) -EndDate (Get-Date)

# Compromised account response
Update-MgUser -UserId USER -AccountEnabled:$false
Revoke-MgUserSignInSession -UserId USER
```
