---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Event ID reference

Event IDs worth knowing by heart, grouped by log. Always read the event text; IDs can be reused by different sources.

## System
| ID | Source | Meaning |
|---|---|---|
| 41 | Kernel-Power | Rebooted without a clean shutdown (crash or power loss) |
| 6008 | EventLog | Previous shutdown was unexpected |
| 6005 / 6006 | EventLog | Event log started / stopped (boot / clean shutdown) |
| 1074 | User32 | Shutdown or restart initiated, and by what |
| 1001 | BugCheck | System recovered from a bugcheck (BSOD) |
| 7000 / 7009 | Service Control Manager | Service failed to start / timed out |
| 7031 / 7034 | Service Control Manager | Service terminated unexpectedly |
| 7036 | Service Control Manager | Service changed state |
| 7045 | Service Control Manager | New service installed (watch for attackers) |
| 129 / 153 | storport / disk | Device reset / IO retried: storage latency or failing paths |
| 7 / 11 / 51 | disk | Bad block / controller error / paging error |
| 55 / 98 | Ntfs | File system corruption / volume needs repair |
| 1014 | DNS Client | Name resolution timed out |
| 5719 | NETLOGON | Could not reach a domain controller |
| 1129 / 1030 / 1058 | GroupPolicy | Group Policy processing failures |
| 19 / 20 / 43 | WindowsUpdateClient | Update installed / failed / started |
| 1135 / 1069 / 1177 | FailoverClustering | Node removed / resource failed / quorum lost |

## Security
| ID | Meaning |
|---|---|
| 4624 / 4625 | Logon success / failure |
| 4634 | Logoff |
| 4648 | Logon with explicit credentials |
| 4672 | Special privileges assigned (admin logon) |
| 4688 | Process created (if auditing enabled) |
| 4697 | Service installed |
| 4698 | Scheduled task created |
| 4720 / 4722 / 4725 / 4726 | User created / enabled / disabled / deleted |
| 4728 / 4732 / 4756 | Member added to global / local / universal security group |
| 4738 | User account changed |
| 4740 | Account locked out (on the PDC emulator: shows caller computer) |
| 4767 | Account unlocked |
| 4768 / 4769 / 4771 | Kerberos TGT / service ticket / pre-authentication failed |
| 4776 | NTLM credential validation |
| 1102 | Security log cleared |
| 6272 / 6273 | NPS granted / denied access |

## Application and services logs
| ID | Source | Meaning |
|---|---|---|
| 1000 / 1002 | Application Error / Hang | Application crashed / hung |
| 8193 / 8194 / 12289 | VSS | Shadow copy errors |
| 2213 | DFSR | Replication paused after dirty shutdown |
| 4012 | DFSR | Replication stopped: offline longer than MaxOfflineTimeInDays |
| 5002 | DFSR | Error communicating with partner |
| 2042 | NTDS Replication | Too long since last replication (tombstone) |
| 1311 | NTDS KCC | Replication topology problem |
| 1988 | NTDS Replication | Lingering object detected |
| 4013 | DNS Server | Waiting for AD initial sync |
| 1020 / 1063 | DHCP-Server | Scope nearly full / no free addresses (verify for your version) |
| 21 / 23 / 24 / 25 | TerminalServices-LocalSessionManager | RDP logon / logoff / disconnect / reconnect |
| 1149 | TerminalServices-RemoteConnectionManager | RDP network authentication succeeded |
| 36874 / 36887 | Schannel | TLS handshake failures |

Query example: `Get-WinEvent -FilterHashtable @{LogName='System'; Id=41,6008,1001; StartTime=(Get-Date).AddDays(-7)}`
