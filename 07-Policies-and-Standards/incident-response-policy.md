> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Incident Response Policy

**Policy Number:** APX-POL-005
**Version:** 1.0
**Effective Date:** May 2026
**Classification:** Confidential
**Owner:** Information Security
**Approval status (not approved):** CISO

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | RS.MA-1 | Incident response plan is prepared |
| NIST CSF 2.0 | RS.AN-1 | Incident investigations are performed |
| NIST CSF 2.0 | RS.IM-1 | Incidents are contained |
| ISO 27001:2022 | A.5.24 | Incident management planning |
| ISO 27001:2022 | A.8.33 | Incident response information |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Req 12.9 | Incident response plan |

**External References:**
- NIST SP 800-61 Rev 2: Computer Security Incident Handling Guide
- SANS Incident Response Policy Template: https://www.sans.org/information-security-policy-templates/

---

## 2. Purpose

This policy establishes the framework for detecting, responding to, and recovering from security incidents that could impact Apex Capital's systems, client data, or business operations.

**Risk Addressed:** R-002 (Credential Theft), R-003 (Ransomware), R-004 (Audit Failure)

---

## 3. Scope

This policy applies to:

| Category | Description |
|----------|-------------|
| **Personnel** | All employees, contractors, and third parties |
| **Systems** | All 4 VMs (Windows, Ubuntu, pfSense, Wazuh) and all company assets |
| **Data** | All client data, financial information, and internal documents |
| **Incident Types** | Security breaches, malware infections, unauthorized access, data exfiltration, DDoS, ransomware |

---

## 4. Incident Severity Levels

| Level | Name | Description | Response Timeline | Escalation |
|-------|------|-------------|-------------------|------------|
| Level 1 | Critical | Client data breach, ransomware, unauthorized access to Restricted data, system compromise | Immediate (15 min) | CISO, CEO, Legal, Compliance |
| Level 2 | High | Malware infection (non-ransomware), unauthorized access attempt (successful), DoS attack | 1 hour | CISO, IT Manager |
| Level 3 | Medium | Suspicious activity, multiple failed logins, policy violation | 4 hours | IT Manager, Department Head |
| Level 4 | Low | Single failed login, minor policy violation, false positive | 24 hours | IT Support |

---

## 5. Incident Response Team (IRT) Roles

| Role | Name/Position | Responsibility | Contact |
|------|---------------|----------------|---------|
| IRT Lead | CISO | Overall incident coordination, final decisions | [Phone/Email] |
| Technical Lead | IT Manager | Technical analysis, containment, eradication | [Phone/Email] |
| Communications Lead | Compliance Officer | Internal/external communications, regulatory reporting | [Phone/Email] |
| Legal Lead | Legal Counsel | Legal guidance, breach notification requirements | [Phone/Email] |
| GRC Lead | Project Author | Documentation, evidence preservation, lessons learned | [Phone/Email] |
| Backup IRT Lead | CEO | Acts as IRT Lead when CISO unavailable | [Phone/Email] |

---

## 6. Incident Response Phases (NIST SP 800-61)

The incident response process follows six phases as defined by NIST SP 800-61:

| Phase | Name | Description | Key Activities |
|-------|------|-------------|----------------|
| 1 | Preparation | Establish IR capabilities before an incident | IRT training, tool setup, contact list, backups |
| 2 | Detection and Analysis | Identify and validate security events | Wazuh alerts, log analysis, user reports |
| 3 | Containment | Limit incident impact | Isolate systems, block IPs, disable accounts |
| 4 | Eradication | Remove threat from environment | Malware removal, patch vulnerabilities, reset passwords |
| 5 | Recovery | Restore normal operations | Restore from backup, verify integrity, monitor |
| 6 | Post-Mortem | Learn and improve | Root cause analysis, lessons learned, policy update |

### 6.1 Preparation

| Activity | Description | Owner | Status |
|----------|-------------|-------|--------|
| IRT training | Annual tabletop exercises | CISO | Planned for Phase 2 |
| Tool availability | Wazuh, pfSense logs, Windows Event Viewer | IT Manager | Planned / not executed |
| Contact list | Updated emergency contacts | Compliance | Planned / not executed |
| Backup verification | Tested recovery procedures | IT Manager | Planned / not executed |

### 6.2 Detection and Analysis

| Detection Source | Method | VM | Alert Trigger |
|------------------|--------|-----|---------------|
| Wazuh SIEM | Failed login alert (Event ID 4625) | VM 4 | 5+ failures in 5 minutes |
| Wazuh SIEM | Malware detection alert | VM 4 | EICAR or real malware detected |
| Windows Defender | Real-time protection block | VM 1 | Malware download blocked |
| pfSense | Firewall log analysis | VM 3 | Unusual traffic patterns |
| Employee report | Manual notification | All | Suspicious activity observed |

### 6.3 Containment

| Incident Type | Immediate Containment Action | Responsible | VM Action |
|---------------|------------------------------|-------------|-----------|
| Credential compromise | Disable compromised account | IT Manager | VM 1 (User disable) |
| Malware infection | Isolate system from network | IT Manager | VM 3 (pfSense block rule) |
| Web server compromise | Block IP, take server offline | IT Manager | VM 2 (shutdown), VM 3 (block) |
| Data exfiltration | Block outbound traffic to destination | IT Manager | VM 3 (pfSense block rule) |
| Ransomware | Disconnect network, power off affected systems | IT Manager | VM 1, VM 2, VM 3 |

### 6.4 Eradication

| Incident Type | Eradication Action | Verification |
|---------------|---------------------|--------------|
| Credential compromise | Reset password, review account activity | Wazuh logs (VM 4) |
| Malware infection | Run full antivirus scan, remove malware | Defender scan results (VM 1) |
| Web server compromise | Restore from clean backup, patch vulnerability | Vulnerability scan (VM 2) |
| Data exfiltration | Review and patch data leak source | Data audit (VM 1, VM 4) |

### 6.5 Recovery

| Incident Type | Recovery Action | Success Criteria |
|---------------|-----------------|------------------|
| Credential compromise | Re-enable account after password reset | User can log in normally |
| Malware infection | Restore from backup, reconnect to network | System clean, monitoring resumed |
| Web server compromise | Deploy restored server, monitor traffic | Web server online, no anomalies |
| Data exfiltration | Restore data from backup, close exposure | Data restored, access logs reviewed |

### 6.6 Post-Mortem and Lessons Learned

| Activity | Description | Timeline |
|----------|-------------|----------|
| Root cause analysis | Determine how incident occurred | Within 7 days |
| Lessons learned | Identify improvements | Within 14 days |
| Policy update | Update IR policy based on findings | Within 30 days |
| Evidence preservation | Retain logs and evidence for legal/regulatory | 1 year |

---

## 7. Incident Reporting Procedures

### 7.1 Internal Reporting

| Step | Action | Responsible | Timeline |
|------|--------|-------------|----------|
| 1 | Detect or suspect incident | Any employee | Immediately |
| 2 | Report to IT Manager or CISO | Employee | Within 1 hour |
| 3 | Open incident ticket | IT Manager | Within 2 hours |
| 4 | Assign IRT members | CISO | Within 4 hours |
| 5 | Begin investigation | IRT Lead | Immediately |

### 7.2 External Reporting

| Reporting Requirement | Authority | Timeline | Responsible |
|----------------------|-----------|----------|-------------|
| Data breach (client PII) | SEC / FINRA | Within 48 hours | Compliance Officer |
| Data breach (GLBA covered) | FTC | Within 72 hours | Compliance Officer |
| State privacy breach | State Attorneys General | Varies (24-72 hours) | Legal Counsel |
| Affected clients | Direct notification | Without unreasonable delay | Compliance Officer |

---

## 8. Incident Documentation

### 8.1 Required Documentation

| Document | Content | Retention |
|----------|---------|-----------|
| Incident ticket | Date, time, detection method, initial impact | 3 years |
| Investigation log | Actions taken, findings, evidence collected | 3 years |
| Evidence chain of custody | Who handled evidence, when, where | 3 years |
| Communications log | Internal/external communications, timestamps | 3 years |
| Post-mortem report | Root cause, lessons learned, action items | 5 years |

### 8.2 Incident Report Template

**Apex Capital Incident Report Form**

| Field | Value |
|-------|-------|
| Incident ID | IR-[YYYY]-[XXX] |
| Date Reported | __________________________ |
| Time Reported | __________________________ |
| Reported By | __________________________ |
| Detection Method | (Wazuh / Employee / Other) |
| Incident Severity | (Critical / High / Medium / Low) |
| Affected Systems | __________________________ |
| Affected Data Classification | (Restricted / Confidential / Internal) |
| Description of Incident | __________________________ |
| Immediate Actions Taken | __________________________ |
| Current Status | (Active / Contained / Resolved / Closed) |
| IRT Lead Signature | __________________________ |

---

## 9. Evidence Preservation

| Evidence Type | Preservation Method | VM Source |
|---------------|---------------------|-----------|
| System logs | Export to secure share, hash verification | VM 1, VM 2, VM 3, VM 4 |
| Network traffic | pfSense logs, packet capture (if enabled) | VM 3 |
| Malware samples | Quarantine, do not delete | VM 1 |
| User activity | Windows Event Logs, Wazuh logs | VM 1, VM 4 |
| Configuration changes | pfSense backup, Windows registry export | VM 1, VM 3 |

**Chain of Custody Form:**

| Field | Value |
|-------|-------|
| Evidence ID | __________________________ |
| Description | __________________________ |
| Collected By | __________________________ |
| Date/Time Collected | __________________________ |
| Hash Value (SHA-256) | __________________________ |
| Transfer History | __________________________ |
| Destroyed On | __________________________ |

---

## 10. Specific Incident Response Procedures

### 10.1 Ransomware Response (Critical - Level 1)

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Isolate infected system from network (disconnect cable / disable switch port) | Immediate |
| 2 | Do not pay ransom (policy prohibits payment) | N/A |
| 3 | Preserve evidence (logs, screenshots, ransom note) | Within 1 hour |
| 4 | Identify patient zero and spread method | Within 4 hours |
| 5 | Restore affected systems from clean backups | Within 24 hours |
| 6 | Report to law enforcement (FBI/CISA) | Within 48 hours |

### 10.2 Credential Compromise Response (Critical - Level 1)

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Disable compromised account immediately | Immediate |
| 2 | Review account activity for unauthorized actions | Within 2 hours |
| 3 | Reset password with strong complexity | Within 4 hours |
| 4 | Enable MFA for affected account (if available) | Within 24 hours |
| 5 | Notify affected data owners (if client data accessed) | Within 48 hours |

### 10.3 Web Server Compromise Response (High - Level 2)

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Take web server offline (VM 2 shutdown) | Immediate |
| 2 | Block source IP at pfSense (VM 3) | Within 15 min |
| 3 | Preserve server image for forensic analysis | Within 1 hour |
| 4 | Restore from clean backup to new VM | Within 4 hours |
| 5 | Review and patch vulnerability | Within 24 hours |
| 6 | Notify clients if their data was exposed | Within 48 hours |

### 10.4 Failed Login Alert Response (Medium - Level 3)

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Review Wazuh alert for source IP and target account | Within 15 min |
| 2 | Verify if legitimate user (forgotten password) | Within 1 hour |
| 3 | If malicious, block source IP at pfSense (VM 3) | Within 2 hours |
| 4 | Notify user to reset password if account at risk | Within 4 hours |

---

## 11. Communication Plan

### 11.1 Internal Communication

| Audience | Method | Message Content | Responsible |
|----------|--------|-----------------|-------------|
| IRT members | Phone call + Email | Incident details, response actions | IRT Lead |
| Executive leadership | Phone call + Email | Incident summary, business impact | CISO |
| All employees | Email (if widespread) | Awareness, reporting instructions | Communications Lead |
| Legal counsel | Phone call + Email | Legal implications, regulatory reporting | CISO |

### 11.2 External Communication

| Audience | Method | Message Content | Responsible |
|----------|--------|-----------------|-------------|
| Regulatory bodies (SEC/FINRA) | Formal written notice | Incident details, impact, remediation | Compliance Officer |
| Affected clients | Written letter + Email | What happened, what data, what to do | Compliance Officer |
| Law enforcement (FBI/CISA) | Phone + Formal report | Evidence, attacker indicators | Legal Counsel |
| Media (if public) | Press release | General statement, no specific details | CEO |

### 11.3 Communication Hold

No external communications except to regulators and law enforcement without CEO approval.

---

## 12. Training and Testing

| Activity | Frequency | Participants | Success Criteria |
|----------|-----------|--------------|------------------|
| IR policy review | Annually | All employees | Acknowledgment signed |
| Tabletop exercise | Bi-annually | IRT members | Scenario completed within timeline |
| Technical drill | Quarterly | IT staff | Detection to containment under 1 hour |
| Full simulation | Annually | IRT + IT staff | End-to-end response under 4 hours |

---

## 13. Compliance and Enforcement

| Violation | Consequence |
|-----------|-------------|
| Failure to report incident | Written warning (first), Suspension (second) |
| Destruction of evidence | Immediate termination, legal action |
| Unauthorized communication with media | Immediate termination |
| Failure to follow containment procedures | Written warning |
| False incident report | Written warning (first), Termination (second) |

---

## 14. User Acknowledgment

All employees must sign this acknowledgment form:

**Apex Capital (fictional lab scenario) - Incident Response Policy Acknowledgment**

Employee Name: __________________________

Employee ID: __________________________

Department: __________________________

Date: __________________________

By signing below, I acknowledge that:

1. I have read and understood the Incident Response Policy of Apex Capital (fictional lab scenario).

2. I understand my obligation to report security incidents immediately.

3. I know how to report an incident (IT Manager or CISO).

4. I understand that failure to report incidents may result in disciplinary action.

5. I will cooperate with incident investigations.

**Employee Signature:** __________________________

**Date:** __________________________

**Manager Signature:** __________________________

**Date:** __________________________

---

## 15. Exceptions

Any exception to this policy requires:

1. Business justification
2. Compensating controls
3. Approval from CISO
4. Expiration date (max 90 days)

**Exception Request Form:**

| Field | Value |
|-------|-------|
| Requester Name | __________________________ |
| Policy Exception Requested | __________________________ |
| Business Justification | __________________________ |
| Compensating Controls | __________________________ |
| Requested Duration (days) | __________________________ |
| CISO Approval Signature | __________________________ |
| Expiration Date | __________________________ |

---

## 16. Review Cycle

This policy will be reviewed:

- Annually (minimum)
- After significant security incidents
- When regulatory requirements change
- After major system changes

---

## 17. Evidence of Implementation

| Evidence ID | Description | Location | VM |
|-------------|-------------|----------|-----|
| EV-001 | Wazuh failed login alert | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| EV-002 | Incident report template | `evidence/incident-report-template.png` | N/A |
| EV-003 | IRT contact list | `evidence/irt-contact-list.png` | N/A |
| EV-004 | pfSense block rule (containment) | `evidence/pfsense-contain-block.png` | VM 3 |
| EV-005 | Backup verification log | `evidence/backup-verification.png` | VM 1 |

---

## 18. Related Documents

| Document | Location |
|----------|----------|
| Access Control Policy | `07-Policies-and-Standards/access-control-policy.md` |
| Password Policy | `07-Policies-and-Standards/password-policy.md` |
| Acceptable Use Policy | `07-Policies-and-Standards/acceptable-use-policy.md` |
| Data Classification Policy | `07-Policies-and-Standards/data-classification-policy.md` |

---

## 19. Policy Version History

| Version | Date       | Author   | Changes                        |
| ------- | ---------- | -------- | ------------------------------ |
| 0.1     | March 2026 | S. Singh | Initial draft                  |
| 0.5     | April 2026 | S. Singh | Added 4-VM response procedures |
| 1.0     | May 2026   | S. Singh | Draft learning edition                  |

---

| Role                   | Signature         | Date              |
| ---------------------- | ----------------- | ----------------- |
| **Policy Approval status (not approved)** | _________________ | _________________ |
| **CISO Signature**     | _________________ | _________________ |


---

**End of Incident Response Policy**
