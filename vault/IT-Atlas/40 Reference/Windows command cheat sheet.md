---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows command cheat sheet

Windows commands for first-response troubleshooting.

```powershell
# System
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, OsLastBootUpTime
systeminfo | findstr /B /C:"OS Name" /C:"System Boot Time"
Get-CimInstance Win32_OperatingSystem | Select-Object LastBootUpTime

# Disk
Get-Volume | Sort-Object DriveLetter
Get-PSDrive -PSProvider FileSystem
Get-ChildItem C:\ -Directory | ForEach-Object { $s = (Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum; [pscustomobject]@{Folder=$_.FullName; GB=[math]::Round($s/1GB,2)} } | Sort-Object GB -Descending
DISM /Online /Cleanup-Image /StartComponentCleanup
vssadmin list shadowstorage

# Processes and services
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 10 Name, @{n='MB';e={[int]($_.WorkingSet64/1MB)}}
Get-Service | Where-Object { $_.StartType -eq 'Automatic' -and $_.Status -ne 'Running' }
tasklist /svc /fi "imagename eq svchost.exe"

# Network
ipconfig /all
Test-NetConnection HOST -Port 443
Resolve-DnsName NAME
pathping HOST
Get-NetTCPConnection -State Listen | Sort-Object LocalPort
netstat -ano | findstr :3389
route print

# Events
Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddHours(-24)}
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4740} -MaxEvents 20

# Updates and health
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending'

# Active Directory
dcdiag /e /q
repadmin /replsummary
nltest /dsgetdc:DOMAIN
w32tm /query /status
Search-ADAccount -LockedOut
gpresult /r

# VSS
vssadmin list writers
vssadmin list providers
```
