---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# ESXi and Hyper-V command cheat sheet

Hypervisor commands for first response.

## ESXi (SSH or console)
```bash
esxcli system version get
esxcli system maintenanceMode get
vim-cmd vmsvc/getallvms
vim-cmd vmsvc/power.getstate VMID
vim-cmd vmsvc/snapshot.get VMID
esxcli storage core device list
esxcli storage vmfs extent list
df -h
esxcli network nic list
esxcli network ip interface ipv4 get
esxtop                      # c=CPU, m=memory, d=disk adapter, u=disk device, n=network
/etc/init.d/hostd restart && /etc/init.d/vpxa restart
tail -n 100 /var/log/vmkernel.log
```

## Hyper-V (PowerShell)
```powershell
Get-VM | Select-Object Name, State, CPUUsage, MemoryAssigned, Uptime, Status
Get-VMSnapshot -VMName *
Get-VMHardDiskDrive -VMName VM | Get-VHD | Select-Object Path, VhdType, FileSize, Size
Get-VMReplication
Get-VMSwitch
Get-ClusterNode; Get-ClusterSharedVolume
Get-WinEvent -LogName Microsoft-Windows-Hyper-V-VMMS-Admin -MaxEvents 20
```
