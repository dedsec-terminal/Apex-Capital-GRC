> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Windows Enterprise Hardening

**Last Updated:** May 2026
**Version:** 1.0
**VM Role:** Internal workstation / server
**Classification:** Internal
**IP Address:** 10.0.2.10
**Subnet:** 10.0.2.0/24 (Internal)

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.AA-05 | Identities and credentials are managed |
| NIST CSF 2.0 | DE.CM-09 | Malware protection is Proposed |
| NIST CSF 2.0 | PR.IR-01 | Network segregation is enforced |
| ISO 27001:2022 | A.8.2 | Privileged access rights |
| ISO 27001:2022 | A.8.7 | Protection against malware |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 5 | Protect all systems against malware |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 8 | Identify and authenticate access |

**External References:**
- CIS Microsoft Windows 10/11 Benchmark
- Microsoft Security Baselines
- NIST SP 800-53: AC, AU, SC families

---

## 2. Purpose

Windows Enterprise VM is hardened according to CIS Benchmarks and organizational policy to protect client financial data, prevent unauthorized access, and ensure compliance with regulatory requirements.

**Risk Addressed:** R-002 (Credential Theft), R-003 (Ransomware), R-006 (Insider Threat)

---

## 3. System Information

| Attribute | Value |
|-----------|-------|
| Operating System | Windows 11 Enterprise |
| Build Version | 23H2 (22631.XXXX) |
| Defender Version | 4.18.24030.9 |
| Local Users | Administrator (renamed), Standard User |
| Wazuh Agent | Version 4.9.0 |

---

## 4. Account and Authentication Controls

### 4.1 Password Policy

**Configure via Local Security Policy (secpol.msc):**

| Setting | Value | Location |
|---------|-------|----------|
| Enforce password history | 24 passwords remembered | secpol.msc > Account Policies > Password Policy |
| Maximum password age | 90 days | secpol.msc > Account Policies > Password Policy |
| Minimum password age | 1 day | secpol.msc > Account Policies > Password Policy |
| Minimum password length | 14 characters | secpol.msc > Account Policies > Password Policy |
| Password must meet complexity requirements | Enabled | secpol.msc > Account Policies > Password Policy |
| Store passwords using reversible encryption | Disabled | secpol.msc > Account Policies > Password Policy |

**Verification via Command Prompt (Admin):**

net accounts

**Expected Output:**

Minimum password age (days): 1
Maximum password age (days): 90
Minimum password length: 14
Length of password history maintained: 24
Lockout threshold: 5
Lockout duration (minutes): 30
Lockout observation window (minutes): 30

### 4.2 Account Lockout Policy

| Setting | Value | Location |
|---------|-------|----------|
| Account lockout duration | 30 minutes | secpol.msc > Account Policies > Account Lockout Policy |
| Account lockout threshold | 5 invalid attempts | secpol.msc > Account Policies > Account Lockout Policy |
| Reset account lockout counter after | 30 minutes | secpol.msc > Account Policies > Account Lockout Policy |

### 4.3 Local Administrator Account

| Action | Command (Admin PowerShell) | Purpose |
|--------|---------------------------|---------|
| Rename Administrator account | `wmic useraccount where name="Administrator" rename "APEX-CISO"` | Prevent targeted attacks |
| Disable built-in Administrator | `net user "Administrator" /active:no` | Reduce attack surface |
| Create separate admin account | `net user lab-admin [SYNTHETIC-TEST-CREDENTIAL] /add` | Administrative tasks |
| Add admin to Administrators group | `net localgroup Administrators lab-admin /add` | Grant admin privileges |
| Create standard user account | `net user lab-user [SYNTHETIC-TEST-CREDENTIAL] /add` | Daily use account |
| Remove standard user from Administrators | `net localgroup Administrators lab-user /delete` | Enforce least privilege |

---

## 5. Endpoint Protection (Microsoft Defender)

### 5.1 Defender Configuration

**Configure via Windows Security or PowerShell:**

| Setting | Value | PowerShell Command |
|---------|-------|-------------------|
| Real-time protection | Enabled | `Set-MpPreference -DisableRealtimeMonitoring $false` |
| Cloud-delivered protection | Enabled | `Set-MpPreference -CloudBlockLevel High` |
| Cloud timeout | 50 seconds | `Set-MpPreference -CloudTimeout 50` |
| Network protection | Block mode | `Set-MpPreference -EnableNetworkProtection Enabled` |
| Tamper protection | Enabled | Configure via Windows Security UI |
| Sample submission | Send safe samples | `Set-MpPreference -SubmitSamplesConsent 1` |

**Verification (PowerShell Admin):**

Get-MpComputerStatus

**Look for:**

AntivirusEnabled         : True
RealTimeProtectionEnabled : True
BehaviorMonitorEnabled    : True
IoavProtectionEnabled     : True
OnAccessProtectionEnabled : True

### 5.2 Controlled Folder Access (CFA)

| Setting | Value | PowerShell Command |
|---------|-------|-------------------|
| Controlled Folder Access | Enabled | `Set-MpPreference -EnableControlledFolderAccess Enabled` |
| Protected folders | Desktop, Documents, Pictures, Videos | Default + custom |
| Blocked apps | Logged and blocked | Default configuration |

**Protected folders list:**

- C:\Users\%USERNAME%\Desktop
- C:\Users\%USERNAME%\Documents
- C:\Users\%USERNAME%\Pictures
- C:\Users\%USERNAME%\Videos
- C:\Users\%USERNAME%\Downloads

**Verification:**

Get-MpPreference | Select-Object EnableControlledFolderAccess, ControlledFolderAccessProtectedFolders

### 5.3 Attack Surface Reduction (ASR) Rules

| ASR Rule ID | Description | Action |
|-------------|-------------|--------|
| D4F940AB-401B-4EFC-AADC-AD5F3C50688A | Block executable content from email client | Enabled (Block) |
| 3B576869-A4EC-4529-8536-B80A7769E899 | Block Office apps from creating child processes | Enabled (Block) |
| 75668C1F-73B5-4CF0-BB93-3ECF5CB7CC84 | Block Office apps from injecting into processes | Enabled (Block) |

**Enable ASR rules via PowerShell:**

Set-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC-AADC-AD5F3C50688A -AttackSurfaceReductionRules_Actions Enabled
Set-MpPreference -AttackSurfaceReductionRules_Ids 3B576869-A4EC-4529-8536-B80A7769E899 -AttackSurfaceReductionRules_Actions Enabled

### 5.4 EICAR Malware Test Validation

**EICAR Test String:**

X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Notepad | Notepad opens |
| 2 | Copy EICAR test string | String copied |
| 3 | Save as eicar.com | File deleted/quarantined immediately |
| 4 | Check Defender history | Threat detected - EICAR Test File |

**Note:** EICAR is a safe test file recognized by antivirus as a test signature.

---

## 6. System Hardening

### 6.1 Windows Firewall

**Configure via PowerShell (Admin):**

| Rule | Command | Purpose |
|------|---------|---------|
| Enable firewall all profiles | `Set-NetFirewallProfile -All -Enabled True` | Firewall active |
| Block inbound by default | `Set-NetFirewallProfile -All -DefaultInboundAction Block` | Default deny inbound |
| Allow outbound by default | `Set-NetFirewallProfile -All -DefaultOutboundAction Allow` | Outbound internet |
| Block RDP from public subnets | `New-NetFirewallRule -DisplayName "Block RDP from Public" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Block -RemoteAddress 10.0.1.0/24` | Lateral movement prevention |
| Allow RDP from management | `New-NetFirewallRule -DisplayName "Allow RDP from Management" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow -RemoteAddress 10.0.3.0/24` | Admin access only |

**Verification:**

Get-NetFirewallProfile | Select-Object Name, Enabled
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*RDP*"} | Select-Object DisplayName, Action, Enabled

### 6.2 Disable Unnecessary Services

| Service Name | Display Name | Command |
|--------------|--------------|---------|
| RemoteRegistry | Remote Registry | `Stop-Service RemoteRegistry; Set-Service RemoteRegistry -StartupType Disabled` |
| Telnet | Telnet | `Disable-WindowsOptionalFeature -Online -FeatureName TelnetClient` |

### 6.3 Windows Update Configuration

| Setting | Value |
|---------|-------|
| Automatic updates | Enabled |
| Quality updates | Monthly (Patch Tuesday) |
| Feature updates | Defer 90 days |

**Check update status via PowerShell:**

Get-WindowsUpdate
Get-HotFix | Select-Object InstalledOn, Description

### 6.4 User Account Control (UAC)

| Setting | Value |
|---------|-------|
| UAC level | Always notify |
| Admin approval mode | Enabled |
| Secure desktop | Enabled |

---

## 7. Logging and Auditing

### 7.1 Advanced Audit Policy Configuration

**Enable via PowerShell (Admin):**

| Audit Category | Subcategory | Setting |
|----------------|-------------|---------|
| Account Logon | Credential Validation | Success and Failure |
| Logon/Logoff | Logon | Success and Failure |
| Logon/Logoff | Account Lockout | Success and Failure |
| Object Access | File System | Success |
| Policy Change | Audit Policy Change | Success and Failure |

**Commands:**

auditpol /set /subcategory:"Credential Validation" /success:enable /failure:enable
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Account Lockout" /success:enable /failure:enable

**Verify audit policy:**

auditpol /get /category:*

### 7.2 Critical Event IDs to Monitor

| Event ID | Event Type | Description |
|----------|-----------|-------------|
| 4624 | Success | Successful logon |
| 4625 | Failure | Failed logon |
| 4740 | Success | Account locked out |
| 4688 | Success | Process creation |
| 7045 | Success | Service installed |

### 7.3 Wazuh Agent Configuration

**Wazuh configuration file location:**

C:\Program Files (x86)\ossec-agent\ossec.conf

**Configuration content to add/modify:**

The client section must point to the Wazuh server (VM 4) at 10.0.3.10. The localfile sections define which Windows event logs to forward.

**Client configuration - set server address:**

Set the server address to 10.0.3.10 and port to 1514 using TCP protocol.

**Localfile configuration for Security events:**

Configure localfile to forward Windows Security event channel.

**Localfile configuration for System events:**

Configure localfile to forward Windows System event channel.

**Localfile configuration for Defender events:**

Configure localfile to forward Microsoft-Windows-Windows Defender/Operational event channel.

**Example of properly configured ossec.conf sections:**

For the client section, configure:
- Server address: 10.0.3.10
- Port: 1514
- Protocol: tcp

For event collection, add localfile entries for:
- Security event channel
- System event channel
- Microsoft-Windows-Windows Defender/Operational event channel

**Restart Wazuh agent after configuration:**

Restart-Service -Name "Wazuh"

**Verify agent connection:**

Get-Service -Name "Wazuh"
Check service status should be "Running"

---

## 8. Hardening Checklist

| Check | Command / Action | Status | Evidence |
|-------|------------------|--------|----------|
| Password policy applied | net accounts | Pending | Screenshot |
| Account lockout configured | net accounts | Pending | Screenshot |
| Weak password rejected | Attempt "[SYNTHETIC-TEST-CREDENTIAL]" | Pending | Screenshot |
| Administrator renamed | wmic useraccount get name | Pending | Screenshot |
| Built-in admin disabled | net user Administrator /active | Pending | Screenshot |
| Standard user created | net user lab-user | Pending | Screenshot |
| Defender real-time protection | Get-MpComputerStatus | Pending | Screenshot |
| Controlled Folder Access enabled | Get-MpPreference | Pending | Screenshot |
| EICAR test blocked | Download eicar.com | Pending | Screenshot |
| Windows Firewall enabled | Get-NetFirewallProfile | Pending | Screenshot |
| RDP restricted | Get-NetFirewallRule | Pending | Screenshot |
| Audit policy configured | auditpol /get /category:* | Pending | Screenshot |
| Wazuh agent connected | Get-Service -Name "Wazuh" | Pending | Screenshot |

---

## 9. Security Validation Tests

### 9.1 Weak Password Rejection Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Command Prompt as standard user | cmd opens |
| 2 | Run: net user lab-test-user [SYNTHETIC-TEST-CREDENTIAL] /add | Command fails - password does not meet complexity |
| 3 | Run: net user lab-test-user [SYNTHETIC-TEST-CREDENTIAL] /add | Command succeeds |
| 4 | Clean up: net user lab-test-user /delete | Account removed |

### 9.2 Account Lockout Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt RDP login with wrong password 5 times | Account locked |
| 2 | Check login screen after 5th failure | Account locked message |
| 3 | Check Wazuh dashboard | Alert level 10 generated |
| 4 | Wait 30 minutes | Account automatically unlocked |

### 9.3 EICAR Malware Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open Notepad | Notepad opens |
| 2 | Paste EICAR test string | String pasted |
| 3 | Save as C:\eicar.com | File blocked/deleted immediately |
| 4 | Check Defender history | Threat detected - EICAR Test File |
| 5 | Check Wazuh dashboard | Alert level 15 generated |

### 9.4 Controlled Folder Access Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create test script: test.bat | File created |
| 2 | Write a command to Documents folder | Script blocked by CFA |
| 3 | Check Windows Event Log | Event ID 1123 logged |
| 4 | Check Wazuh dashboard | Alert generated |

### 9.5 Firewall Segmentation Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | From Ubuntu VM (10.0.1.10) attempt to connect to Windows (10.0.2.10) port 445 | Connection refused |
| 2 | From Ubuntu VM attempt RDP to Windows on port 3389 | Connection refused |
| 3 | From Management subnet (10.0.3.0/24) attempt RDP | Connection successful |

---

## 10. Troubleshooting Commands

| Problem | Command | Solution |
|---------|---------|----------|
| Password policy not applied | secpol.msc | Check Local Security Policy |
| Defender disabled | Get-MpComputerStatus | Re-enable via Windows Security |
| Firewall blocking legitimate traffic | Get-NetFirewallRule | Review and add allow rule |
| Wazuh agent not connecting | Get-Service Wazuh | Check server IP, restart service |
| Audit events not logging | auditpol /get /category:* | Re-enable audit policy |
| UAC not prompting | reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Check ConsentPromptBehaviorAdmin |

---

## 11. Maintenance Procedures

### 11.1 Daily Tasks

| Task | Command / Action |
|------|------------------|
| Check Windows Update status | Get-WindowsUpdate |
| Review Defender protection history | Get-MpThreatDetection |
| Verify Wazuh agent running | Get-Service Wazuh |

### 11.2 Weekly Tasks

| Task | Command / Action |
|------|------------------|
| Review security event log | Get-EventLog -LogName Security -Newest 100 |
| Check for failed logins | Get-EventLog -LogName Security -InstanceId 4625 -Newest 50 |
| Verify backup status | Check backup logs |

### 11.3 Monthly Tasks

| Task | Command / Action |
|------|------------------|
| Apply Windows updates | Install pending updates |
| Run full Defender scan | Start-MpScan -ScanType FullScan |
| Review audit policy | auditpol /get /category:* |
| Password expiration notification | Notify users of upcoming expiration |

---

## 12. Related Documents

| Document | Location |
|----------|----------|
| pfSense Network Security | 08-Technical-Controls/pfsense-network.md |
| Ubuntu Web Server Hardening | 08-Technical-Controls/ubuntu-web-server.md |
| Wazuh Monitoring | 08-Technical-Controls/wazuh-monitoring.md |
| Access Control Policy | 07-Policies-and-Standards/access-control-policy.md |
| Password Policy | 07-Policies-and-Standards/password-policy.md |

---

## 13. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added ASR rules and CFA |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Windows Enterprise Hardening**
