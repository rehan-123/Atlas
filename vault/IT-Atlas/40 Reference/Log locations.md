---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Log locations

Where each tool keeps its logs.

| Tool | Logs |
|---|---|
| [[Acronis Cyber Protect]] | C:\ProgramData\Acronis\BackupAndRecovery\MMS (Managed Machine Service logs) |
| [[Active Directory]] | Event Viewer: Directory Service, DFS Replication, DNS Server and System logs; Security log on DCs (4740 lockouts, 4625 failed logons) |
| [[Always On VPN]] | Event Viewer: Application log, source RasClient |
| [[Apache HTTP Server]] | /var/log/apache2/error.log (Debian/Ubuntu); /var/log/httpd/error_log (RHEL) |
| [[AppLocker]] | Event Viewer: Applications and Services Logs > Microsoft > Windows > AppLocker |
| [[Atera]] | C:\Program Files\ATERA Networks\AteraAgent (agent folder) |
| [[ConnectWise Automate]] | C:\Windows\LTSvc\LTErrors.txt |
| [[Datto BCDR]] | Device and agent logs in the Datto partner portal and appliance web UI |
| [[Datto RMM]] | C:\ProgramData\CentraStage (agent data and logs); Job results and audit trail in the web portal |
| [[Docker]] | docker logs CONTAINER; /var/lib/docker (Linux data root) |
| [[File Server & DFS]] | Event Viewer: DFS Replication log; C:\Windows\debug (DFSR debug logs) |
| [[FortiGate]] | Log & Report in the GUI, or FortiAnalyzer; Event logs: system, VPN, SD-WAN and HA |
| [[FSLogix]] | C:\ProgramData\FSLogix\Logs; Event Viewer: Microsoft > FSLogix > Apps > Operational and Admin |
| [[Hyper-V]] | Event Viewer: Microsoft > Windows > Hyper-V-VMMS > Admin; Event Viewer: Microsoft > Windows > Hyper-V-Worker > Admin |
| [[IIS]] | C:\inetpub\logs\LogFiles; C:\Windows\System32\LogFiles\HTTPERR |
| [[Jamf Pro]] | /var/log/jamf.log; /var/log/install.log |
| [[Kaseya VSA]] | Agent Logs and Procedure History in the VSA console |
| [[Linux servers]] | journalctl; /var/log/syslog (Debian, Ubuntu) or /var/log/messages (RHEL); /var/log/auth.log or /var/log/secure |
| [[macOS]] | /var/log/install.log; log show --predicate 'process == "softwareupdated"' --last 1h |
| [[Microsoft Configuration Manager]] | C:\Windows\CCM\Logs (client); Site server logs in the installation folder's Logs directory |
| [[Microsoft Defender for Endpoint]] | Event Viewer: Microsoft > Windows > Windows Defender > Operational |
| [[Microsoft Entra Connect]] | Synchronization Service Manager operations tab; Application log, sources ADSync and Directory Synchronization |
| [[Microsoft Intune]] | C:\ProgramData\Microsoft\IntuneManagementExtension\Logs; Event Viewer: Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider |
| [[Microsoft SQL Server]] | C:\Program Files\Microsoft SQL Server\MSSQLnn.INSTANCE\MSSQL\Log\ERRORLOG |
| [[N-able N-central]] | C:\Program Files (x86)\N-able Technologies\Windows Agent\log |
| [[N-able N-sight RMM]] | C:\Program Files (x86)\Advanced Monitoring Agent (agent folder and logs) |
| [[Nginx]] | /var/log/nginx/error.log; /var/log/nginx/access.log |
| [[NinjaOne]] | C:\ProgramData\NinjaRMMAgent\logs |
| [[OpenSSH]] | /var/log/auth.log (Ubuntu); /var/log/secure (RHEL) |
| [[PRTG Network Monitor]] | C:\ProgramData\Paessler\PRTG Network Monitor\Logs |
| [[RDS]] | Event Viewer: TerminalServices-LocalSessionManager and RemoteConnectionManager operational logs |
| [[Samba]] | /var/log/samba/ |
| [[Unitrends]] | Jobs and system reports in the appliance UI |
| [[Veeam Backup & Replication]] | C:\ProgramData\Veeam\Backup (server and job logs) |
| [[VMware vSphere]] | /var/log/vmkernel.log; /var/log/hostd.log; /var/log/vpxa.log; /var/log/vobd.log; vCenter: /var/log/vmware/vpxd/vpxd.log |
| [[Windows Defender Firewall]] | %windir%\System32\LogFiles\Firewall\pfirewall.log (if logging enabled) |
| [[Windows DHCP Server]] | Event Viewer: Microsoft > Windows > DHCP-Server; C:\Windows\System32\dhcp (DhcpSrvLog-*.log audit logs) |
| [[Windows DNS Server]] | Event Viewer: Applications and Services Logs > DNS Server; DNS debug logging (enable temporarily) |
| [[Windows Server]] | Event Viewer: System, Application, Security; C:\Windows\Logs\CBS\CBS.log |
| [[Windows Server Backup]] | Event Viewer: Applications and Services Logs > Microsoft > Windows > Backup |
| [[Windows Update]] | Get-WindowsUpdateLog (builds WindowsUpdate.log from ETW traces); C:\Windows\Logs\CBS\CBS.log; System log, source WindowsUpdateClient (event 19 installed, 20 failed) |
| [[Zabbix]] | /var/log/zabbix/zabbix_server.log; /var/log/zabbix/zabbix_agentd.log |
