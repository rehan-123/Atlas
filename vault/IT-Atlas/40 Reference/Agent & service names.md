---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Agent & service names

The Windows service or process to check for each tool when its agent goes quiet. See also [[Agent offline]].

| Tool | Category | Agent / service |
|---|---|---|
| [[Acronis Cyber Protect]] | [[Backup & DR]] | Acronis Managed Machine Service |
| [[AnyDesk]] | [[Remote Access]] | AnyDesk |
| [[Apache HTTP Server]] | [[DevOps & Containers]] | apache2 / httpd |
| [[AppLocker]] | [[Security]] | AppIDSvc |
| [[Atera]] | [[RMM]] | AteraAgent |
| [[Azure Arc]] | [[Cloud & SaaS]] | himds (Azure Connected Machine Agent) |
| [[ConnectWise Automate]] | [[RMM]] | LTService, LTSvcMon |
| [[ConnectWise RMM]] | [[RMM]] | ITSPlatform (legacy Continuum agents use SAAZ* services) |
| [[Cove Data Protection]] | [[Backup & DR]] | Backup Service Controller |
| [[CrowdStrike Falcon]] | [[Security]] | CSFalconService |
| [[Datto RMM]] | [[RMM]] | CagService |
| [[Docker]] | [[DevOps & Containers]] | docker (Linux daemon) / com.docker.service |
| [[Failover Clustering]] | [[Servers & Operating Systems]] | ClusSvc |
| [[FSLogix]] | [[Servers & Operating Systems]] | frxsvc, frxccds |
| [[Huntress]] | [[Security]] | HuntressAgent, HuntressUpdater |
| [[Hyper-V]] | [[Virtualization & Storage]] | vmms |
| [[IIS]] | [[Servers & Operating Systems]] | W3SVC, WAS |
| [[Kaseya VSA]] | [[RMM]] | Kaseya Agent (AgentMon.exe) |
| [[MeshCentral]] | [[Remote Access]] | Mesh Agent |
| [[Microsoft Entra Connect]] | [[Identity & Access]] | ADSync (miiserver.exe) |
| [[Microsoft SQL Server]] | [[Databases & Applications]] | MSSQLSERVER or MSSQL$INSTANCE, SQLAgent, SQLBrowser |
| [[MongoDB]] | [[Databases & Applications]] | mongod |
| [[N-able N-central]] | [[RMM]] | Windows Agent, Windows Agent Maintenance Service |
| [[N-able N-sight RMM]] | [[RMM]] | Advanced Monitoring Agent |
| [[Nginx]] | [[DevOps & Containers]] | nginx |
| [[NinjaOne]] | [[RMM]] | NinjaRMMAgent |
| [[OpenSSH]] | [[Servers & Operating Systems]] | sshd |
| [[Print Server]] | [[Servers & Operating Systems]] | Spooler |
| [[PRTG Network Monitor]] | [[Monitoring & Observability]] | PRTG Core Server Service, PRTG Probe Service |
| [[QuickBooks Desktop]] | [[Databases & Applications]] | QuickBooksDBXX (XX = version) |
| [[Redis]] | [[Databases & Applications]] | redis-server |
| [[RRAS]] | [[Servers & Operating Systems]] | RemoteAccess |
| [[Samba]] | [[Servers & Operating Systems]] | smbd, nmbd, winbind |
| [[ScreenConnect]] | [[Remote Access]] | ScreenConnect Client (instance ID) |
| [[SentinelOne]] | [[Security]] | SentinelAgent |
| [[Splashtop]] | [[Remote Access]] | Splashtop Remote Service |
| [[Tactical RMM]] | [[RMM]] | tacticalrmm, Mesh Agent |
| [[TeamViewer]] | [[Remote Access]] | TeamViewer |
| [[Veeam Backup & Replication]] | [[Backup & DR]] | Veeam Backup Service |
| [[Windows Defender Firewall]] | [[Servers & Operating Systems]] | mpssvc |
| [[Windows Deployment Services]] | [[Servers & Operating Systems]] | WDSServer |
| [[Windows DHCP Server]] | [[Servers & Operating Systems]] | DHCPServer |
| [[Windows DNS Server]] | [[Servers & Operating Systems]] | DNS |
| [[Windows Event Forwarding]] | [[Servers & Operating Systems]] | Wecsvc (collector), WinRM |
| [[Windows Update]] | [[Endpoint & Patch Management]] | wuauserv, BITS, TrustedInstaller |
