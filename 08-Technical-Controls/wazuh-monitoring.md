> **Publication status:** Fictional public lab design. Commands and settings below are proposed examples, not deployed configuration or verified output. No VM tests have been run.

# Wazuh Monitoring

**Last Updated:** May 2026
**Version:** 1.0
**VM Role:** SIEM / Monitoring / Alerting
**Classification:** Internal
**IP Address:** 10.0.3.10
**Subnet:** 10.0.3.0/24 (Management)

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | DE.AE-1 | Security events are analyzed |
| NIST CSF 2.0 | DE.CM-1 | Network is monitored |
| NIST CSF 2.0 | DE.CM-3 | Malicious code is detected |
| ISO 27001:2022 | A.8.15 | Logging and monitoring |
| ISO 27001:2022 | A.8.16 | Monitoring activities |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 10 | Track and monitor all access |

**External References:**
- Wazuh Documentation: https://documentation.wazuh.com/current/
- Wazuh Compliance Mapping: https://documentation.wazuh.com/current/compliance/index.html

---

## 2. Purpose

The proposed design places Wazuh as the central SIEM for the fictional lab. If deployed, configured agents and syslog forwarding could collect selected host and firewall events for alerting and investigation. A SIEM deployment does not itself establish audit readiness or compliance; configuration, coverage, retention, access, and operation require evidence.

**Risk Addressed:** R-002 (Credential Theft), R-004 (Audit Failure), R-003 (Ransomware)

---

## 3. System Information

| Attribute | Value |
|-----------|-------|
| Operating System | Ubuntu 22.04.5 LTS |
| Wazuh Version | 4.9.0 |
| Components | Wazuh Indexer, Wazuh Server, Wazuh Dashboard |
| Web Interface Port | 443 (HTTPS) |
| Agent event channel | TCP 1514 (agent to manager) |
| Agent enrollment | TCP 1515 only when enabled; restrict to controlled enrollment sources |
| Initial credentials | Configure securely during deployment; do not publish defaults or credentials |

---

## 4. Wazuh Architecture

**Wazuh SIEM (VM 4) - 10.0.3.10**

Components:
- Wazuh Agent (on VMs) -> Wazuh Server (Indexer + Manager) -> Wazuh Dashboard (Web UI)

Communication (proposed; not configured or tested):

- TCP 1514: endpoint agent to manager event channel.
- TCP 1515: enrollment only when enabled; restrict source and exposure.
- TCP 443: dashboard access from named management sources only.
- UDP 514: optional pfSense syslog; disabled unless deliberately configured and not transport-encrypted.

**Monitored VMs:**
- VM 1 (Windows Enterprise): Event Logs, Defender Logs
- VM 2 (Ubuntu Web Server): Syslog, Auditd, Nginx Logs
- VM 3 (pfSense): Firewall Logs, System Logs

---

## 5. Installation and Configuration

### 5.1 Wazuh Server Installation (VM 4)

| Step | Command | Purpose |
|------|---------|---------|
| 1 | curl -sO https://packages.wazuh.com/4.9/wazuh-install.sh | Download installer |
| 2 | bash wazuh-install.sh --generate-config-files | Generate configuration |
| 3 | bash wazuh-install.sh --wazuh-server wazuh-server | Install Wazuh server |
| 4 | bash wazuh-install.sh --wazuh-dashboard wazuh-dashboard | Install dashboard |
| 5 | bash wazuh-install.sh --start-cluster | Start all services |

**Verify installation:**

sudo systemctl status wazuh-manager
sudo systemctl status wazuh-indexer
sudo systemctl status wazuh-dashboard

### 5.2 Windows Agent Installation (VM 1)

| Step | Command / Action | Purpose |
|------|------------------|---------|
| 1 | Download Wazuh agent for Windows | Get installer from wazuh.com |
| 2 | Run installer as administrator | Install agent |
| 3 | Configure server address: 10.0.3.10 | Point to Wazuh server |
| 4 | Set agent name: windows-enterprise-01 | Unique identifier |
| 5 | Start Wazuh agent service | Begin log forwarding |

**PowerShell installation (silent):**

wazuh-agent-4.9.0-1.msi /q WAZUH_MANAGER=10.0.3.10 WAZUH_AGENT_NAME=windows-enterprise-01

**Verify agent:**

Get-Service -Name "Wazuh"

### 5.3 Ubuntu Agent Installation (VM 2)

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `curl -sSfo /tmp/WAZUH-GPG-KEY https://packages.wazuh.com/key/GPG-KEY-WAZUH && sudo apt-key add /tmp/WAZUH-GPG-KEY` | Download and add GPG key |
| 2 | `sudo sh -c 'printf "%s\n" "deb https://packages.wazuh.com/4.x/apt/ stable main" > /etc/apt/sources.list.d/wazuh.list'` | Add repository |
| 3 | sudo apt update | Update package list |
| 4 | sudo apt install wazuh-agent -y | Install agent |
| 5 | sudo systemctl enable wazuh-agent | Enable on boot |
| 6 | sudo systemctl start wazuh-agent | Start agent |

**Configure agent - edit /var/ossec/etc/ossec.conf:**

Find the client section and update the server address:

<client>
    <server>
        <address>10.0.3.10</address>
        <port>1514</port>
        <protocol>tcp</protocol>
    </server>
</client>

**Restart agent after configuration:**

sudo systemctl restart wazuh-agent

### 5.4 pfSense Syslog Forwarding (VM 3)

| Step | Action | Location |
|------|--------|----------|
| 1 | Enable remote syslog | Status > System Logs > Settings |
| 2 | Add remote syslog server: 10.0.3.10:514 | Remote Syslog Servers |
| 3 | Select log facilities to send | Only selected facilities justified by the test plan |
| 4 | Apply changes | Save button |

**Configuration summary:**

- Remote syslog server: 10.0.3.10
- Port: 514
- Protocol: UDP
- Logs sent: Firewall, System, DHCP, Authentication

---

## 6. Alert Rules Configuration

### 6.1 Failed Login Detection (Windows - Event ID 4625)

**Edit /var/ossec/etc/rules/local_rules.xml - Add the following:**

<group name="windows,failed_login,">
  <rule id="100001" level="10">
    <if_sid>6000</if_sid>
    <field name="win.eventID">4625</field>
    <description>Windows Failed Login Attempt</description>
    <group>authentication_failed,</group>
  </rule>

  <rule id="100002" level="12">
    <if_sid>100001</if_sid>
    <match>5 times in 5 minutes</match>
    <description>Multiple Windows Failed Logins - Brute Force</description>
    <group>brute_force,</group>
  </rule>
</group>

### 6.2 Malware Detection (EICAR)

**Edit /var/ossec/etc/rules/local_rules.xml - Add the following:**

<group name="malware,">
  <rule id="100010" level="15">
    <if_sid>6000</if_sid>
    <field name="win.eventID">1006</field>
    <field name="win.system.providerName">Microsoft-Windows-Windows Defender</field>
    <regex>EICAR Test File</regex>
    <description>EICAR Test File Detected - Malware Test</description>
    <group>malware,eicar,</group>
  </rule>
</group>

### 6.3 SSH Failed Login Detection (Ubuntu)

**Edit /var/ossec/etc/rules/local_rules.xml - Add the following:**

<group name="ssh,failed_login,">
  <rule id="100020" level="10">
    <if_sid>5715</if_sid>
    <regex>Failed password</regex>
    <description>SSH Failed Login Attempt</description>
    <group>authentication_failed,ssh,</group>
  </rule>

  <rule id="100021" level="12">
    <if_sid>100020</if_sid>
    <match>5 times in 5 minutes</match>
    <description>Multiple SSH Failed Logins - Brute Force</description>
    <group>brute_force,ssh,</group>
  </rule>
</group>

### 6.4 pfSense Firewall Block Alert

**Edit /var/ossec/etc/rules/local_rules.xml - Add the following:**

<group name="firewall,block,">
  <rule id="100030" level="8">
    <if_sid>6000</if_sid>
    <field name="program_name">pfSense</field>
    <regex>block</regex>
    <description>pfSense Firewall Block Rule Matched</description>
    <group>firewall,block,</group>
  </rule>
</group>

---

## 7. Alert Levels and Severity

| Level | Name | Description | Examples | Action |
|-------|------|-------------|----------|--------|
| 1-3 | Low | Informational | User login, service start | Log only |
| 4-6 | Medium | Suspicious | Failed single login | Monitor |
| 7-9 | High | Potential threat | Multiple failed logins, policy change | Email alert |
| 10-12 | Critical | Confirmed threat | Brute force detected | Email + SMS alert |
| 13-15 | Emergency | Active compromise | Malware detected, data exfiltration | Immediate response |

### 7.1 Alert Examples

| Alert | Level | Rule ID | Description |
|-------|-------|---------|-------------|
| Single failed login | 5 | 100001 | Windows single failed login |
| Multiple failed logins (5 in 5 min) | 12 | 100002 | Brute force detected |
| EICAR test file detected | 15 | 100010 | Malware test - EICAR |
| SSH failed login | 10 | 100020 | SSH authentication failure |
| SSH brute force | 12 | 100021 | 5+ SSH failures in 5 minutes |
| pfSense block | 8 | 100030 | Firewall blocked connection |

---

## 8. Alert Notifications

### 8.1 Email Alert Configuration

**Edit /var/ossec/etc/ossec.conf - Add/modify the following:**

<global>
  <email_notification>yes</email_notification>
  <smtp_server>smtp.gmail.com</smtp_server>
  <smtp_port>587</smtp_port>
  <email_from>[REDACTED-EMAIL]</email_from>
  <email_to>[REDACTED-EMAIL]</email_to>
  <email_to>[REDACTED-EMAIL]</email_to>
  <email_idsname>Wazuh SIEM</email_idsname>
</global>

<alerts>
  <log_alert_level>7</log_alert_level>
  <email_alert_level>10</email_alert_level>
</alerts>

### 8.2 Alert Summary by Level

| Level Range | Notification Method | Response SLA |
|-------------|---------------------|--------------|
| 1-6 | Log only | None |
| 7-9 | Dashboard highlight | End of day |
| 10-12 | Email to security team | Within 1 hour |
| 13-15 | Email + SMS to CISO | Immediate |

---

## 9. Log Collection Summary

### 9.1 Log Sources by VM

| VM | Log Source | Log Types | Collection Method |
|----|-----------|-----------|-------------------|
| VM 1 (Windows) | Windows Event Log | Security (4624,4625), System, Application | Wazuh Agent |
| VM 1 (Windows) | Windows Defender | Malware detection, protection history | Wazuh Agent |
| VM 2 (Ubuntu) | Syslog | Auth.log, syslog, kern.log | Wazuh Agent |
| VM 2 (Ubuntu) | Nginx | Access.log, error.log | Wazuh Agent |
| VM 2 (Ubuntu) | Auditd | System calls, file access | Wazuh Agent |
| VM 3 (pfSense) | Firewall logs | Filter.log, block events | Syslog forward |
| VM 3 (pfSense) | System logs | DHCP, DNS, authentication | Syslog forward |

### 9.2 Critical Events Monitored

| Event | Log Source | Event ID / Pattern | Alert Level |
|-------|------------|-------------------|-------------|
| Failed login | Windows Event Log | 4625 | 10 |
| Successful login (admin) | Windows Event Log | 4624 | 3 |
| Account lockout | Windows Event Log | 4740 | 8 |
| Malware detection | Windows Defender | 1006, 1116 | 15 |
| EICAR test | Windows Defender | "EICAR Test File" | 15 |
| SSH failed login | Ubuntu auth.log | "Failed password" | 10 |
| SSH root login attempt | Ubuntu auth.log | "Invalid user root" | 12 |
| Firewall block | pfSense filter.log | "block" | 8 |
| Configuration change | pfSense | "config change" | 7 |
| Service stop | Windows Event Log | 7036 | 6 |

---

## 10. Compliance Reporting

### 10.1 Pre-built Compliance Dashboards

| Compliance Framework | Dashboard | Controls Addressed |
|---------------------|-----------|-------------------|
| NIST CSF 2.0 | NIST CSF Dashboard | DE.AE, DE.CM, RS.AN |
| ISO 27001 | ISO 27001 Dashboard | A.8.15, A.8.16 |
| PCI DSS | PCI DSS Dashboard | Req 10 |

### 10.2 Custom Report Templates

| Report Name | Frequency | Recipients | Content |
|-------------|-----------|------------|---------|
| Daily Security Summary | Daily | Security Team | Alerts by level, failed logins |
| Weekly Failed Login Report | Weekly | IT Manager | Top failed login attempts |
| Monthly Compliance Report | Monthly | CISO, Compliance | Alert trends, agent health |
| Audit Evidence Package | On demand | Auditors | All logs for specified period |

---

## 11. Evidence Collection

| Evidence ID | Description | Command / Location | Status |
|-------------|-------------|--------------------|--------|
| EV-001 | Wazuh Dashboard overview | https://10.0.3.10 | Pending |
| EV-002 | Agents list showing all 3 agents | Dashboard > Agents | Pending |
| EV-003 | Failed login alert (Event ID 4625) | Dashboard > Alerts > Search | Pending |
| EV-004 | EICAR malware alert | Dashboard > Alerts > Search "EICAR" | Pending |
| EV-005 | pfSense firewall block alert | Dashboard > Alerts > Search "block" | Pending |
| EV-006 | Compliance dashboard (NIST) | Dashboard > Compliance > NIST | Pending |
| EV-007 | Custom alert rule configuration | /var/ossec/etc/rules/local_rules.xml | Pending |
| EV-008 | Syslog forwarding from pfSense | Status > System Logs > Settings | Pending |

---

## 12. Security Validation Tests

### 12.1 Failed Login Detection Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt RDP login to Windows with wrong password 3 times | Failed login events generated |
| 2 | Check Wazuh dashboard for alerts | Alert with Event ID 4625 appears |
| 3 | Verify alert details show source IP and username | Correct metadata displayed |

### 12.2 EICAR Malware Detection Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Download EICAR test file from eicar.org | Windows Defender blocks |
| 2 | Check Wazuh dashboard for alert | Alert level 15 appears |
| 3 | Verify alert shows "EICAR Test File" | Correct description |

### 12.3 pfSense Block Alert Test

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | From Ubuntu VM, attempt to connect to Windows on port 445 | Connection refused |
| 2 | Check pfSense firewall logs | Block rule logged |
| 3 | Check Wazuh dashboard for alert | Alert from pfSense appears |

### 12.4 SSH Failed Login Test (Ubuntu)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt SSH login to Ubuntu with wrong password 3 times | Failed login events |
| 2 | Check Wazuh dashboard for alert | Alert level 10 appears |
| 3 | Attempt 5 more failures (total 8) | Alert level 12 (brute force) appears |

---

## 13. Maintenance Procedures

### 13.1 Daily Tasks

| Task | Command / Action |
|------|------------------|
| Check agent status | Dashboard > Agents > All agents green |
| Review critical alerts (Level 10+) | Dashboard > Alerts > Level > 10 |
| Verify log collection | Dashboard > Events > Last 24 hours |

### 13.2 Weekly Tasks

| Task | Command / Action |
|------|------------------|
| Review alert trends | Dashboard > Statistics > Alerts |
| Update rule signatures | sudo /var/ossec/bin/wazuh-update |
| Check disk space | df -h /var/ossec |
| Backup configuration | sudo tar -czf wazuh-backup.tar.gz /var/ossec/etc |

### 13.3 Monthly Tasks

| Task | Command / Action |
|------|------------------|
| Generate compliance report | Dashboard > Compliance > Export PDF |
| Review agent health | Dashboard > Agents > Health check |
| Test alert rules | Run EICAR test, failed login test |
| Apply Wazuh updates | sudo apt update && sudo apt upgrade wazuh-* |

### 13.4 Log Retention Management

| Setting | Value | Configuration |
|---------|-------|---------------|
| Index retention | 90 days | /etc/wazuh-indexer/opensearch.yml |
| Archive old logs | 365 days | /var/ossec/etc/ossec.conf |
| Disk space threshold | 80% alert, 90% auto-delete | /etc/wazuh-indexer/jvm.options |

---

## 14. Troubleshooting Commands

| Problem | Command | Solution |
|---------|---------|----------|
| Agent not connecting | sudo tail -f /var/ossec/logs/ossec.log | Check server IP, firewall |
| Dashboard not loading | sudo systemctl status wazuh-dashboard | Check service, restart |
| No alerts for events | sudo /var/ossec/bin/ossec-logtest | Test rule matching |
| High CPU usage | top | Check rule complexity |
| Indexer not responding | sudo systemctl status wazuh-indexer | Check memory, restart |
| Syslog not received | sudo tcpdump -i eth0 port 514 | Check pfSense forwarding |

---

## 15. Hardening Checklist

| Check | Command / Action | Status | Evidence |
|-------|------------------|--------|----------|
| Dashboard HTTPS only | https://10.0.3.10 | Pending | Screenshot EV-001 |
| Default admin password changed | wazuh-passwd tool | Pending | Config file |
| Firewall rules restrict access | sudo ufw status | Pending | Screenshot |
| API access restricted | /var/ossec/etc/ossec.conf | Pending | Config file |
| Log rotation configured | /etc/logrotate.d/wazuh | Pending | Config file |
| Backups scheduled | crontab -l | Pending | Cron entry |

---

## 16. Related Documents

| Document | Location |
|----------|----------|
| pfSense Network Security | 08-Technical-Controls/pfsense-network.md |
| Windows Hardening Guide | 08-Technical-Controls/windows-hardening.md |
| Ubuntu Web Server Hardening | 08-Technical-Controls/ubuntu-web-server.md |
| Network Architecture Diagram | 05-Security-Architecture/diagrams/network-architecture.md |

---

## 17. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added alert rules and validation tests |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Wazuh Monitoring**
