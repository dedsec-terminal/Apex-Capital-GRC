> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Acceptable Use Policy

**Policy Number:** APX-POL-004
**Version:** 1.0
**Effective Date:** May 2026
**Classification:** Internal
**Owner:** Information Security
**Approval status (not approved):** CISO

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.AA-05 | Identities and credentials are managed |
| NIST CSF 2.0 | PR.AA-05 | Access permissions and authorizations are managed |
| ISO 27001:2022 | A.8.1 | Acceptable use of information assets |
| ISO 27001:2022 | A.8.7 | Protection against malware |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Req 8.7 | Restrict access to critical systems |

**External References:**
- SANS Acceptable Use Policy Template: https://www.sans.org/information-security-policy-templates/
- NIST SP 800-53 (AC-8): System Use Notification

---

## 2. Purpose

This policy defines acceptable behavior for employees, contractors, and third parties using Apex Capital's information systems, networks, and data. The purpose is to protect client financial data, prevent unauthorized access, and ensure compliance with regulatory requirements (SEC, FINRA, GLBA).

**Risk Addressed:** R-002 (Credential Theft), R-006 (Insider Threat)

---

## 3. Scope

This policy applies to:

| Category | Description |
|----------|-------------|
| **Employees** | All full-time and part-time employees of Apex Capital |
| **Contractors** | Temporary staff, consultants, and outsourced vendors |
| **Third Parties** | Business partners with access to Apex systems |
| **Devices** | Company-issued and personal (BYOD) devices accessing company resources |
| **VMs** | All 4 virtual machines in the environment (Windows, Ubuntu, pfSense, Wazuh) |

---

## 4. Policy Statements

### 4.1 Authorized Use

Company systems and network access are provided for **business purposes only**. Limited personal use is permitted if it:

- Does not consume significant bandwidth or storage
- Does not violate any other policy
- Does not expose the company to legal or security risk
- Does not interfere with job performance

### 4.2 Prohibited Activities

The following activities are **strictly prohibited** on any Apex Capital system:

| Category | Prohibited Activities |
|----------|----------------------|
| **Illegal Activities** | Downloading copyrighted material, hacking tools, pirated software, gambling, accessing illegal content |
| **Security Violations** | Password sharing, credential sharing, bypassing security controls, disabling antivirus |
| **Unauthorized Software** | Installing unapproved applications, unapproved browser extensions, peer-to-peer file sharing |
| **Inappropriate Content** | Accessing adult content, hate speech, discriminatory material, harassment |
| **Data Exfiltration** | Copying client data to personal devices, USB drives, unauthorized cloud storage |
| **Network Abuse** | Port scanning, vulnerability scanning, denial of service attacks, cryptomining |
| **Personal Business** | Running personal business, unauthorized side work, competing with Apex Capital |

### 4.3 Credential Management

| Rule | Requirement | Enforcement |
|------|-------------|-------------|
| No credential sharing | Passwords must not be shared with anyone | Logged violation = disciplinary action |
| No writing down passwords | Passwords must not be stored on sticky notes or unencrypted files | Physical security audits |
| No reusing work passwords | Work passwords must not be used for personal accounts | Breach monitoring |
| No storing in browsers | Browser password save feature is disabled | Group Policy enforcement on VM 1 |

### 4.4 Software Installation

| Rule | Requirement | Technical Control |
|------|-------------|-------------------|
| No unauthorized software | Only approved software may be installed | Windows AppLocker (recommended), user lacks admin rights (VM 1) |
| No unapproved browser extensions | Only business-approved extensions allowed | Group Policy restriction |
| No self-installed VPNs | Only company-approved VPN for remote access | pfSense VPN rules (VM 3) |

### 4.5 Monitoring and Logging

All user activity on company systems is subject to monitoring:

| Monitored Activity | How It Is Logged | Retention |
|--------------------|------------------|------------|
| Login attempts | Windows Event Log (Event ID 4624, 4625) | 90 days (VM 1, VM 4) |
| Software installation | Windows Event Log, Defender logs | 90 days (VM 1, VM 4) |
| Network traffic | pfSense firewall logs | 90 days (VM 3, VM 4) |
| File access | Windows access logs, Wazuh FIM (optional) | 90 days (VM 1, VM 4) |

**User Notice:** By logging into Apex Capital systems, you consent to monitoring as described in this policy.

### 4.6 Remote Access and BYOD

For employees working remotely or using personal devices:

| Requirement | Description | Technical Control |
|-------------|-------------|-------------------|
| VPN required | All remote access must go through company VPN | pfSense VPN configuration (VM 3) |
| MFA required | Multi-factor authentication for remote access | Recommended for Phase 2 |
| No local admin | Personal devices should not have local admin rights | User responsibility |
| Antivirus required | Personal devices must have active antivirus | Self-certification |
| No data storage | Client data must not be stored on personal devices | Policy enforcement |

### 4.7 Email and Communication

| Allowed | Prohibited |
|---------|-------------|
| Business correspondence | Sending client data to personal email |
| Internal collaboration | Phishing or misleading emails |
| Regulatory communications | Harassment or threatening language |
| Professional networking | Spam or bulk unsolicited emails |

### 4.8 Internet Usage

| Allowed | Prohibited |
|---------|-------------|
| Business research | Streaming video/audio (non-business) |
| Industry news | Social media (excessive personal use) |
| Cloud collaboration tools | Downloading unapproved files |
| Software updates | Accessing gambling/adult sites |

---

## 5. Technical Controls by VM

| VM | Technical Control | Policy Enforcement |
|----|-------------------|---------------------|
| VM 1 (Windows) | User lacks admin rights | Prevents unauthorized software installation |
| VM 1 (Windows) | Windows Defender enabled | Prevents malware downloads |
| VM 1 (Windows) | Event logging enabled | Logs user activity for monitoring |
| VM 2 (Ubuntu) | UFW firewall | Restricts unauthorized outbound traffic |
| VM 2 (Ubuntu) | SSH key auth only | Prevents password brute force |
| VM 3 (pfSense) | Firewall rules | Blocks unauthorized protocols (P2P, gaming) |
| VM 3 (pfSense) | VPN required for remote access | Encrypts remote connections |
| VM 4 (Wazuh) | Failed login alerts | Detects unauthorized access attempts |
| VM 4 (Wazuh) | Log aggregation | Centralized monitoring of user activity |

---

## 6. BYOD (Bring Your Own Device) Requirements

Employees using personal devices to access corporate resources must comply with:

| Requirement | Description | Verification |
|-------------|-------------|--------------|
| VPN connection | All access must go through corporate VPN | Technical control on VM 3 |
| Antivirus software | Active, updated antivirus required | Self-certification form |
| Screen lock | Device must lock after 5 minutes of inactivity | User responsibility |
| Encryption | Device storage must be encrypted | Self-certification form |
| Reporting | Lost or stolen devices must be reported within 4 hours | Policy requirement |

---

## 7. Compliance and Enforcement

| Violation | First Offense | Second Offense | Third Offense |
|-----------|---------------|----------------|---------------|
| Minor violation (personal internet use) | Verbal warning | Written warning | HR referral |
| Moderate violation (unauthorized software) | Written warning | Suspension (1 week) | Termination |
| Severe violation (data exfiltration, credential sharing) | Immediate suspension pending investigation | Termination | Legal action |
| Illegal activity (hacking, copyright infringement) | Immediate termination | Legal action | Criminal prosecution |

---

## 8. User Acknowledgment

All employees must sign this acknowledgment form:

**Apex Capital (fictional lab scenario) - Acceptable Use Policy Acknowledgment**

Employee Name: __________________________

Employee ID: __________________________

Department: __________________________

Date: __________________________

By signing below, I acknowledge that:

1. I have read and understood the Acceptable Use Policy of Apex Capital (fictional lab scenario).

2. I understand that my activities on company systems may be monitored and logged.

3. I understand that violations may result in disciplinary action up to and including termination and legal action.

4. I agree to comply with all provisions of this policy.

5. I will report any security incidents or policy violations immediately to my supervisor or the CISO.

6. I understand that this policy applies to both company-issued and personal devices used to access company resources.

**Employee Signature:** __________________________

**Date:** __________________________

**Manager Signature:** __________________________

**Date:** __________________________

**For IT Use Only:**
- Policy Acknowledgment Recorded in HR System: Yes / No
- Date Recorded: __________________________
- IT Administrator Signature: __________________________

---

## 9. Exceptions

Any exception to this policy requires:

1. **Business justification** (e.g., developer needs temporary admin access)
2. **Compensating controls** (e.g., elevated logging, time-limited access)
3. **Approval** from CISO
4. **Expiration date** (max 30 days for temporary exceptions)
5. **Quarterly review** for recurring exceptions

**Exception Request Form:**

| Field | Value |
|-------|-------|
| Requester Name | __________________________ |
| Policy Exception Requested | __________________________ |
| Business Justification | __________________________ |
| Compensating Controls | __________________________ |
| Requested Duration (days) | __________________________ |
| CISO Approval Signature | __________________________ |
| Approval Date | __________________________ |
| Expiration Date | __________________________ |

---

## 10. Review Cycle

This policy will be reviewed:

- Annually (minimum)
- After significant security incidents
- When regulatory requirements change (SEC/FINRA/GLBA)
- When new technology is deployed

---

## 11. Evidence of Implementation

| Evidence ID | Description | Location | VM |
|-------------|-------------|----------|-----|
| EV-001 | User lacks admin rights (standard user) | `evidence/windows-standard-user.png` | VM 1 |
| EV-002 | Windows Defender enabled | `evidence/windows-defender-enabled.png` | VM 1 |
| EV-003 | Failed login alert (unauthorized access detection) | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| EV-004 | VPN required for remote access (pfSense rule) | `evidence/pfsense-vpn-rule.png` | VM 3 |
| EV-005 | Policy acknowledgment form | `evidence/acceptable-use-acknowledgment.png` | N/A |

---

## 12. Related Documents

| Document | Location |
|----------|----------|
| Access Control Policy | `07-Policies-and-Standards/access-control-policy.md` |
| Password Policy | `07-Policies-and-Standards/password-policy.md` |
| Incident Response Policy | `07-Policies-and-Standards/incident-response-policy.md` |
| Data Classification Policy | `07-Policies-and-Standards/data-classification-policy.md` |

---

## 13. Policy Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | March 2026 | S. Singh | Initial draft |
| 0.5 | April 2026 | S. Singh | Added BYOD section, monitoring details |
| 1.0 | May 2026 | S. Singh | Draft learning edition with 4-VM integration |

---

**Policy Approval status (not approved):** \underline{\hspace{5cm}} **Date:** \underline{\hspace{5cm}}

**CISO Signature**

---

**End of Acceptable Use Policy**
