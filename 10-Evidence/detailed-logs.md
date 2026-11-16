> **Illustrative log examples:** The following source log blocks are examples from the original write-up, not collected or validated telemetry. Usernames/emails are replaced with placeholders. Do not treat output as observed evidence.

> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Detailed Logs

**Last Updated:** May 2026
**Version:** 1.0
**Classification:** Internal
**Owner:** GRC Lead

---

## 1. Overview

This document contains detailed log excerpts from all four virtual machines, demonstrating security event capture, audit trail integrity, and compliance evidence. Logs are retained for 90 days minimum.

**Log Retention Policy:** 90 days for security logs, 365 days for archived logs

**Time Synchronization:** All VMs synchronized via NTP (pool.ntp.org)

---

## 2. Windows Event Logs (VM 1)

### 2.1 Security Log - Failed Logon (Event ID 4625)

Event ID 4625 indicates a failed logon attempt. Multiple failures trigger account lockout and Wazuh alerts.

**Log Details:**
- Log Name: Security
- Source: Microsoft-Windows-Security-Auditing
- Date: 2026-05-29 14:23:15
- Event ID: 4625
- Task Category: Logon
- Level: Information
- Keywords: Audit Failure
- Computer: Windows-Enterprise-01

**Description:**
Account failed to log on.

**Subject:**
- Security ID: S-1-0-0
- Account Name: -
- Account Domain: -
- Logon ID: 0x0

**Logon Type:** 3 (Network)

**Account For Which Logon Failed:**
- Account Name: lab-user
- Account Domain: APEX

**Failure Information:**
- Failure Reason: Unknown user name or bad password
- Status: 0xC000006D
- Sub Status: 0xC000006A

**Network Information:**
- Workstation Name: UBUNTU-WEB-01
- Source Network Address: 10.0.1.10
- Source Port: 54321

### 2.2 Security Log - Successful Logon (Event ID 4624)

Event ID 4624 indicates a successful logon from authorized sources.

**Log Details:**
- Log Name: Security
- Source: Microsoft-Windows-Security-Auditing
- Date: 2026-05-29 09:15:22
- Event ID: 4624
- Task Category: Logon
- Level: Information
- Keywords: Audit Success
- Computer: Windows-Enterprise-01

**Description:**
Account successfully logged on.

**Subject:**
- Security ID: APEX\lab-admin
- Account Name: lab-admin
- Account Domain: APEX
- Logon ID: 0x1A2B3C

**Logon Type:** 10 (RemoteInteractive)

**Account For Which Logon Was Successful:**
- Account Name: lab-admin
- Account Domain: APEX

**Network Information:**
- Workstation Name: MGMT-WORKSTATION
- Source Network Address: 10.0.3.50
- Source Port: 49876

### 2.3 Security Log - Account Lockout (Event ID 4740)

Event ID 4740 indicates a user account was locked out after multiple failed attempts.

**Log Details:**
- Log Name: Security
- Source: Microsoft-Windows-Security-Auditing
- Date: 2026-05-29 14:28:30
- Event ID: 4740
- Task Category: User Account Management
- Level: Information
- Keywords: Audit Success
- Computer: Windows-Enterprise-01

**Description:**
A user account was locked out.

**Subject:**
- Security ID: APEX\lab-admin
- Account Name: lab-admin
- Account Domain: APEX

**Target Account:**
- Account Name: lab-user
- Account Domain: APEX

**Additional Information:**
- Caller Computer: 10.0.3.10

### 2.4 Account Lockout Timeline

Multiple Event ID 4625 leading to 4740:

| Time | Event ID | Description |
|------|----------|-------------|
| 14:23:15 | 4625 | Failed logon for lab-user from 10.0.1.10 |
| 14:23:45 | 4625 | Failed logon for lab-user from 10.0.1.10 |
| 14:24:10 | 4625 | Failed logon for lab-user from 10.0.1.10 |
| 14:24:35 | 4625 | Failed logon for lab-user from 10.0.1.10 |
| 14:25:00 | 4625 | Failed logon for lab-user from 10.0.1.10 |
| 14:25:05 | 4740 | Account lab-user locked out |

### 2.5 Defender Malware Detection (Event ID 1116)

Event ID 1116 indicates malware detection (including EICAR test file).

**Log Details:**
- Log Name: Microsoft-Windows-Windows Defender/Operational
- Source: Windows Defender
- Date: 2026-05-29 15:30:45
- Event ID: 1116
- Level: Warning
- Keywords: Malware Detection
- User: SYSTEM
- Computer: Windows-Enterprise-01

**Description:**
Windows Defender Antivirus has detected malware.

- Name: EICAR Test File
- ID: 2147519003
- Severity: Severe
- Category: Test
- Path: C:\Users\lab-user\Downloads\eicar.com
- Detection Time: 2026-05-29T15:30:45.123Z
- Status: Removed (Quarantined)
- Action: Block
- User: APEX\lab-user
- Process: C:\Windows\explorer.exe

### 2.6 Controlled Folder Access Block (Event ID 1123)

Event ID 1123 indicates Controlled Folder Access blocked an unauthorized application.

**Log Details:**
- Log Name: Microsoft-Windows-Windows Defender/Operational
- Source: Windows Defender
- Date: 2026-05-29 16:45:20
- Event ID: 1123
- Level: Warning
- Keywords: Controlled Folder Access
- User: SYSTEM
- Computer: Windows-Enterprise-01

**Description:**
Controlled Folder Access blocked an application from making changes.

- Application: C:\temp\test.exe
- Protected Folder: C:\Users\lab-user\Documents
- Process Name: test.exe
- Block Time: 2026-05-29T16:45:20.456Z
- User: APEX\lab-user

### 2.7 Audit Policy Change (Event ID 4719)

Event ID 4719 logs changes to audit policy.

**Log Details:**
- Log Name: Security
- Source: Microsoft-Windows-Security-Auditing
- Date: 2026-05-28 10:00:00
- Event ID: 4719
- Task Category: Policy Change
- Level: Information
- Keywords: Audit Success
- Computer: Windows-Enterprise-01

**Description:**
System audit policy was changed.

**Subject:**
- Security ID: APEX\lab-admin
- Account Name: lab-admin
- Account Domain: APEX

**Audit Policy Changes:**
- Subcategory: Logon/Logoff
- Changes: Enabled Success and Failure

---

## 3. Ubuntu System Logs (VM 2)

### 3.1 SSH Failed Login Attempt - auth.log

Failed SSH login attempts from unauthorized source.

**Log Entry 1:** May 29 14:30:22 ubuntu-web-01 sshd[2456]: Failed password for invalid user admin from 203.0.113.50 port 12345 ssh2

**Log Entry 2:** May 29 14:30:25 ubuntu-web-01 sshd[2456]: Failed password for invalid user admin from 203.0.113.50 port 12345 ssh2

**Log Entry 3:** May 29 14:30:28 ubuntu-web-01 sshd[2456]: Failed password for invalid user admin from 203.0.113.50 port 12345 ssh2

**Log Entry 4:** May 29 14:30:31 ubuntu-web-01 sshd[2458]: Connection closed by authenticating user admin 203.0.113.50 port 12345 preauth

### 3.2 SSH Successful Login - auth.log

Successful SSH login using key authentication from management subnet.

**Log Entry 1:** May 29 09:15:30 ubuntu-web-01 sshd[1892]: Accepted publickey for lab-user from 10.0.3.50 port 49876 ssh2: RSA SHA256:abc123def456

**Log Entry 2:** May 29 09:15:30 ubuntu-web-01 sshd[1892]: pam_unix(sshd:session): session opened for user lab-user by (uid=0)

**Log Entry 3:** May 29 09:15:30 ubuntu-web-01 systemd-logind[1234]: New session 42 of user lab-user.

### 3.3 UFW Firewall Blocks - ufw.log

UFW firewall blocking unauthorized access attempts.

**Log Entry 1:** May 29 14:35:10 ubuntu-web-01 kernel: [UFW BLOCK] IN=eth0 OUT= SRC=203.0.113.50 DST=10.0.1.10 PROTO=TCP SPT=12345 DPT=22

**Log Entry 2:** May 29 14:35:11 ubuntu-web-01 kernel: [UFW BLOCK] IN=eth0 OUT= SRC=203.0.113.51 DST=10.0.1.10 PROTO=TCP SPT=12346 DPT=80

### 3.4 Nginx Access Log - access.log

Web server access logs showing HTTP/HTTPS requests.

**Log Entry 1:** 10.0.2.10 - - [29/May/2026:10:15:30 +0000] GET /index.html HTTP/1.1 200 2456

**Log Entry 2:** 203.0.113.50 - - [29/May/2026:14:30:22 +0000] GET /admin HTTP/1.1 404 153

**Log Entry 3:** 10.0.3.50 - - [29/May/2026:15:00:00 +0000] GET /api/health HTTP/1.1 200 45

### 3.5 Nginx Error Log - error.log

Web server errors.

**Log Entry:** 2026/05/29 14:30:22 [error] 1893#1893: *12345 /var/www/html/admin/index.html is not found (2: No such file or directory), client: 203.0.113.50

### 3.6 fail2ban Log - fail2ban.log

fail2ban banning IP addresses after multiple SSH failures.

**Log Entry 1:** 2026-05-29 14:30:35,123 fail2ban.filter [2459]: INFO [sshd] Found 203.0.113.50

**Log Entry 2:** 2026-05-29 14:30:35,124 fail2ban.filter [2459]: INFO [sshd] Found 203.0.113.50

**Log Entry 3:** 2026-05-29 14:30:35,124 fail2ban.filter [2459]: INFO [sshd] Found 203.0.113.50

**Log Entry 4:** 2026-05-29 14:30:36,456 fail2ban.actions [2459]: NOTICE [sshd] Ban 203.0.113.50

### 3.7 Auditd Log - audit.log

Auditd monitoring SSH configuration changes.

**Log Entry:** type=SYSCALL msg=audit(1748548800.123:456): arch=c000003e syscall=257 success=yes exit=3 a0=ffffff9c items=1 ppid=1892 pid=2458 auid=1000 uid=0 gid=0 comm=nano exe=/usr/bin/nano key=ssh_changes

---

## 4. pfSense Firewall Logs (VM 3)

### 4.1 Firewall Block Log - filter.log

pfSense blocking traffic from DMZ (Ubuntu) to Internal (Windows).

**Log Entry 1:** May 29 14:35:22 pfsense filterlog: 5,,,16777216,em1,match,block,in,4,0x0,,64,0,0,DF,6,tcp,60,10.0.1.10,10.0.2.10,54321,445,0,S

**Log Entry 2:** May 29 14:35:23 pfsense filterlog: 5,,,16777216,em1,match,block,in,4,0x0,,64,0,0,DF,6,tcp,60,10.0.1.10,10.0.2.10,54322,3389,0,S

### 4.2 Default Deny Log - filter.log

pfSense default deny rule blocking unexpected traffic.

**Log Entry:** May 29 14:40:15 pfsense filterlog: 5,,,16777216,em0,match,block,in,4,0x0,,64,0,0,DF,6,tcp,60,203.0.113.50,10.0.1.10,54345,443,0,S

### 4.3 Syslog Forwarding Status

pfSense syslog forwarding configuration to Wazuh.

- Remote syslog server: 10.0.3.10
- Port: 514
- Protocol: UDP
- Facilities: All except VPN

---

## 5. Wazuh Logs (VM 4)

### 5.1 Wazuh Agent Connection Log - ossec.log

Wazuh agent connection events.

**Log Entry 1:** 2026-05-29 09:00:00 wazuh-agent[1234]: INFO: Connected to server (10.0.3.10:1514)

**Log Entry 2:** 2026-05-29 09:00:01 wazuh-agent[1234]: INFO: Agent started successfully

### 5.2 Wazuh Alert - Failed Login

Wazuh alert generated for Windows failed login (Event ID 4625).

**Alert JSON:**
{
  "rule": {
    "id": 100001,
    "level": 10,
    "description": "Windows Failed Login Attempt"
  },
  "agent": {
    "name": "windows-enterprise-01",
    "ip": "10.0.2.10"
  },
  "data": {
    "win": {
      "eventID": 4625,
      "account": "lab-user",
      "sourceIp": "10.0.1.10"
    }
  },
  "timestamp": "2026-05-29T14:23:15.123Z"
}

### 5.3 Wazuh Alert - EICAR Malware

Wazuh alert generated for EICAR test file detection.

**Alert JSON:**
{
  "rule": {
    "id": 100010,
    "level": 15,
    "description": "EICAR Test File Detected - Malware Test"
  },
  "agent": {
    "name": "windows-enterprise-01",
    "ip": "10.0.2.10"
  },
  "data": {
    "threat": "EICAR Test File",
    "action": "blocked"
  },
  "timestamp": "2026-05-29T15:30:45.123Z"
}

### 5.4 Wazuh Alert - pfSense Block

Wazuh alert generated for pfSense firewall block.

**Alert JSON:**
{
  "rule": {
    "id": 100030,
    "level": 8,
    "description": "pfSense Firewall Block Rule Matched"
  },
  "agent": {
    "name": "pfsense-01",
    "ip": "10.0.3.1"
  },
  "data": {
    "source": "10.0.1.10",
    "destination": "10.0.2.10",
    "port": 445
  },
  "timestamp": "2026-05-29T14:35:22.456Z"
}

### 5.5 Wazuh Alert - SSH Failed Login

Wazuh alert generated for Ubuntu SSH failed login.

**Alert JSON:**
{
  "rule": {
    "id": 100020,
    "level": 10,
    "description": "SSH Failed Login Attempt"
  },
  "agent": {
    "name": "ubuntu-web-01",
    "ip": "10.0.1.10"
  },
  "data": {
    "user": "admin",
    "sourceIp": "203.0.113.50"
  },
  "timestamp": "2026-05-29T14:30:22.789Z"
}

### 5.6 Wazuh Alert - Brute Force Detection

Wazuh alert generated for multiple SSH failures (brute force).

**Alert JSON:**
{
  "rule": {
    "id": 100021,
    "level": 12,
    "description": "Multiple SSH Failed Logins - Brute Force"
  },
  "agent": {
    "name": "ubuntu-web-01",
    "ip": "10.0.1.10"
  },
  "data": {
    "sourceIp": "203.0.113.50",
    "failures": 5,
    "timeframe": 300
  },
  "timestamp": "2026-05-29T14:30:35.456Z"
}

---

## 6. Log Retention Summary

| VM | Log Type | Retention Period | Storage Location |
|----|----------|------------------|-------------------|
| VM 1 (Windows) | Security Event Log | 90 days | C:\Windows\System32\winevt\Logs |
| VM 1 (Windows) | Defender Logs | 90 days | C:\ProgramData\Microsoft\Windows Defender\Scans |
| VM 2 (Ubuntu) | Syslog / Auth.log | 90 days | /var/log/ |
| VM 2 (Ubuntu) | Nginx Logs | 90 days | /var/log/nginx/ |
| VM 2 (Ubuntu) | Auditd Logs | 90 days | /var/log/audit/ |
| VM 3 (pfSense) | Firewall Logs | 90 days | /var/log/filter.log |
| VM 4 (Wazuh) | Alerts Index | 90 days | /var/ossec/logs/alerts |
| VM 4 (Wazuh) | Archives Index | 365 days | /var/ossec/logs/archives |

---

## 7. Log Analysis Findings

| Finding | Description | Frequency | Action Taken |
|---------|-------------|-----------|--------------|
| Failed RDP logins from DMZ | Multiple 4625 events from 10.0.1.10 | 5 attempts | Blocked by firewall; Wazuh alert generated |
| EICAR detection | Test malware blocked | 1 test | Defender quarantined; Wazuh alert level 15 |
| SSH brute force attempt | 5+ failures from 203.0.113.50 | 1 incident | fail2ban banned IP; Wazuh alert generated |
| Unauthorized web scan | /admin path probe | 1 attempt | Returned 404; no further action |
| Unauthorized port scan | 22, 80, 443 probes | 1 attempt | UFW blocked; pfSense logged |

---

## 8. Related Documents

| Document | Location |
|----------|----------|
| Testing Results | 09-Testing-and-Validation/results.md |
| Test Scenarios | 09-Testing-and-Validation/test-scenarios.md |
| Evidence Summary | 10-Evidence/evidence-summary.md |
| Wazuh Monitoring | 08-Technical-Controls/wazuh-monitoring.md |

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added pfSense and Wazuh logs |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Detailed Logs**
