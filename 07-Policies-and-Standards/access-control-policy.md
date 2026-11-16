> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Access Control Policy

**Policy Number:** APX-POL-001
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
| NIST CSF 2.0 | PR.AA-03 | User, device, and other asset authentication |
| ISO 27001:2022 | A.8.2 | Privileged access rights |
| ISO 27001:2022 | A.8.3 | User access reviews |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Req 7 | Restrict access to cardholder data |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Req 8 | Identify and authenticate access |

**External References:**
- NIST SP 800-53 (AC-1 to AC-25): Access Control Family
- SANS Access Control Policy Template

---

## 2. Purpose

This policy ensures that only authorized individuals have access to Apex Capital's systems, applications, and client data, following the principle of least privilege.

**Risk Addressed:** R-002 (Credential Theft), R-006 (Insider Threat)

---

## 3. Scope

This policy applies to:

| Category | Description |
|----------|-------------|
| **Employees** | All full-time and part-time employees of Apex Capital |
| **Contractors** | Temporary staff, consultants, and outsourced vendors |
| **Third Parties** | Business partners with access to Apex systems |
| **Systems** | All 4 VMs (Windows, Ubuntu, pfSense, Wazuh) and all applications |
| **Data** | All client data, financial information, and internal documents |

---

## 4. Core Principles

| Principle | Definition | Implementation |
|-----------|------------|----------------|
| **Least Privilege** | Users receive only the minimum access required to perform their job | Role-Based Access Control (RBAC) via Windows local users |
| **Need-to-Know** | Access granted only when necessary for business role | User group membership based on job function |
| **Separation of Duties** | Critical functions divided between different individuals | Admin accounts separate from standard user accounts |
| **Default Deny** | All access not explicitly approved is denied | pfSense default deny rule, Windows UAC |

---

## 5. Role-Based Access Control (RBAC)

### 5.1 User Roles (Windows - VM 1)

| Role | Access Level | Responsibilities | Example Users |
|------|-------------|-----------------|---------------|
| **Standard User** | Basic workstation access | Daily job functions, email, client portal | Advisors, Client Service Reps |
| **Power User** | Limited administrative privileges | Application installation (approved list only) | Senior Advisors, Team Leads |
| **Local Administrator** | Full workstation control | Software installation, configuration changes | IT Support Staff |
| **Domain Administrator** | Full system control | All systems, all data, all configurations | CISO, IT Manager, GRC Lead |

### 5.2 User Roles (Ubuntu - VM 2)

| Role | Access Level | Responsibilities | sudo Access |
|------|-------------|-----------------|--------------|
| **Standard User** | Read-only web server access | Monitor web server status | None |
| **Web Administrator** | Web server configuration | Update web content, manage services | systemctl, nginx, ufw |
| **System Administrator** | Full Ubuntu control | OS updates, security configuration, SSH | Full sudo access |

### 5.3 User Roles (pfSense - VM 3)

| Role | Access Level | Responsibilities | WebGUI Access |
|------|-------------|-----------------|----------------|
| **Read-Only User** | View firewall status | Monitor traffic, review logs | Read-only |
| **Firewall Administrator** | Manage firewall rules | Create rules, modify segmentation | Read-Write |
| **System Administrator** | Full pfSense control | All configurations, updates, backups | Full admin |

### 5.4 User Roles (Wazuh - VM 4)

| Role | Access Level | Responsibilities | API Access |
|------|-------------|-----------------|------------|
| **Read-Only User** | View alerts and dashboards | Security monitoring, incident review | Read-only |
| **Analyst** | Manage alerts, create reports | Investigate incidents, document findings | Limited write |
| **Administrator** | Full Wazuh control | Configure agents, rules, integrations | Full admin |

---

## 6. Authentication Requirements

### 6.1 Password Requirements

| Requirement | Setting | Enforcement |
|-------------|---------|-------------|
| Minimum length | 14 characters | VM 1 (Windows policy) |
| Password complexity | Upper, lower, number, special (3 of 4) | VM 1 (Windows policy) |
| Password history | 24 passwords remembered | VM 1 (Windows policy) |
| Maximum password age | 90 days | VM 1 (Windows policy) |
| Minimum password age | 1 day | VM 1 (Windows policy) |

### 6.2 Account Lockout Requirements

| Requirement | Setting | Enforcement |
|-------------|---------|-------------|
| Lockout threshold | 5 failed attempts | VM 1 (Windows policy) |
| Lockout duration | 30 minutes | VM 1 (Windows policy) |
| Reset lockout counter | 30 minutes | VM 1 (Windows policy) |

### 6.3 Multi-Factor Authentication (MFA)

MFA is **mandatory** for the following access types:

| Access Type | MFA Requirement | Status |
|-------------|-----------------|--------|
| All remote access | Required | Recommended for Phase 2 |
| All administrative accounts | Required | Recommended for Phase 2 |
| Client portal access | Required | Out of scope (client responsibility) |
| VPN connections | Required | Recommended for Phase 2 |

**Note:** MFA implementation is recommended for Phase 2 of the security program.

---

## 7. Access Provisioning and Deprovisioning

### 7.1 Access Request Process

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Employee/Manager submits access request form to IT | Employee |
| 2 | Manager approves request | Manager |
| 3 | Data Owner approves (if applicable) | Data Owner |
| 4 | IT implements access within 2 business days | IT |
| 5 | User notified and trained on access | IT |
| 6 | Access logged in HR system | HR |

### 7.2 Access Removal Process

| Scenario | Action Required | Timeline |
|----------|-----------------|----------|
| Voluntary termination | Disable accounts immediately | Within 4 hours |
| Involuntary termination | Disable accounts immediately, preserve evidence | Within 1 hour |
| Contract completion | Disable accounts, coordinate with vendor | Within 24 hours |
| Role change | Review and modify access based on new role | Within 5 business days |
| Extended leave (30+ days) | Suspend accounts, reactivate upon return | Before leave begins |

### 7.3 Access Request Form

| Field | Value |
|-------|-------|
| Requestor Name | __________________________ |
| Employee Name (if different) | __________________________ |
| Employee ID | __________________________ |
| Department | __________________________ |
| Job Title | __________________________ |
| Access Type (New/Change/Remove) | __________________________ |
| Systems Requiring Access | __________________________ |
| Role Requested | __________________________ |
| Business Justification | __________________________ |
| Expected Duration | __________________________ |
| Manager Approval Signature | __________________________ |
| Data Owner Approval Signature | __________________________ |
| IT Implementation Date | __________________________ |
| IT Administrator Signature | __________________________ |

---

## 8. Access Reviews and Certification

### 8.1 Review Schedule

| Review Type | Frequency | Responsible Party |
|-------------|-----------|-------------------|
| User access review | Quarterly | Department Managers |
| Privileged access review | Monthly | CISO / IT Manager |
| Service account review | Quarterly | IT Administrator |
| Application access review | Semi-annually | Application Owner |
| Third-party access review | Quarterly | Vendor Management |

### 8.2 Access Review Process

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | IT generates access report for department | IT |
| 2 | Manager reviews each user's access | Manager |
| 3 | Manager certifies access or requests changes | Manager |
| 4 | IT implements approved changes | IT |
| 5 | Review documented and stored | Compliance |

### 8.3 Access Certification Form

| Field | Value |
|-------|-------|
| Department | __________________________ |
| Manager Name | __________________________ |
| Review Period | __________________________ |
| Number of Users Reviewed | __________________________ |
| Number of Users with Changes | __________________________ |
| Certifier Signature | __________________________ |
| Date | __________________________ |
| IT Auditor Signature | __________________________ |
| Date | __________________________ |

---

## 9. Privileged Access Management

### 9.1 Privileged Account Requirements

| Requirement | Description | Enforcement |
|-------------|-------------|-------------|
| Separate admin accounts | Standard user account separate from admin account | Windows local user policy (VM 1) |
| No daily use of admin accounts | Admin accounts only for administrative tasks | Policy enforcement |
| MFA for admin accounts | Required for all privileged access | Recommended for Phase 2 |
| Just-in-Time access | Time-limited admin access where possible | Recommended for Phase 2 |
| Logging of admin actions | All admin activities logged and monitored | Wazuh (VM 4) |

### 9.2 Privileged Account Types

| Account Type | Purpose | Access Level | MFA Required |
|--------------|---------|--------------|--------------|
| Standard User | Daily job functions | Basic workstation | No |
| Admin User | System administration | Full system control | Yes (recommended) |
| Service Account | Application to application | Minimal required | No (rotated passwords) |
| Emergency Account | Break-glass scenarios | Full system control | Yes + approval |

### 9.3 Emergency Access Procedure

| Step | Action |
|------|--------|
| 1 | Security incident requiring emergency access |
| 2 | CISO or IT Manager approves verbally |
| 3 | Emergency account enabled (30-minute session) |
| 4 | All actions logged and reviewed |
| 5 | Account disabled after session |
| 6 | Written justification submitted within 24 hours |

---

## 10. No Shared Accounts

| Rule | Requirement | Exception Process |
|------|-------------|-------------------|
| No password sharing | Passwords must not be shared | No exceptions |
| No shared user accounts | Each user has unique credentials | Service accounts only |
| No group passwords | No passwords shared among teams | No exceptions |

**Service Account Exception:** Service accounts are allowed but must have:
- Complex passwords (20+ characters)
- Rotated annually
- Access limited to required functions
- Logged and monitored

---

## 11. Technical Controls by VM

| VM | Control | Implementation |
|----|---------|----------------|
| VM 1 (Windows) | Local user accounts | Standard user vs Administrator separation |
| VM 1 (Windows) | Password policy | `net accounts` configured |
| VM 1 (Windows) | Account lockout | 5 attempts, 30 minute lockout |
| VM 1 (Windows) | Event logging | Event ID 4624 (success), 4625 (failure) |
| VM 2 (Ubuntu) | SSH key authentication | Password authentication disabled |
| VM 2 (Ubuntu) | sudo access | Limited sudo for specific commands |
| VM 2 (Ubuntu) | User isolation | Separate user accounts |
| VM 3 (pfSense) | WebGUI access | Restricted to management subnet |
| VM 3 (pfSense) | Firewall rules | Role-based access to interfaces |
| VM 4 (Wazuh) | User roles | Read-only, Analyst, Administrator |
| VM 4 (Wazuh) | API authentication | Token-based access |

---

## 12. Monitoring and Logging

| Activity | Logged | Retention | Monitoring |
|----------|--------|-----------|------------|
| Successful logins | Yes (Event ID 4624) | 90 days | Wazuh (VM 4) |
| Failed logins | Yes (Event ID 4625) | 90 days | Wazuh alert on 5+ failures |
| Privilege escalation | Yes (Event ID 4672) | 90 days | Wazuh (VM 4) |
| Account creation/deletion | Yes (Event IDs 4720, 4726) | 90 days | Wazuh (VM 4) |
| sudo commands (Ubuntu) | Yes (auth.log) | 90 days | Wazuh (VM 4) |
| pfSense configuration changes | Yes (config log) | 90 days | pfSense backup |

---

## 13. Compliance and Enforcement

| Violation | Consequence |
|-----------|-------------|
| Password sharing | Written warning (first), Suspension (second), Termination (third) |
| Using another user's account | Immediate suspension pending investigation |
| Unauthorized privilege escalation | Immediate termination |
| Failure to report lost credentials | Written warning |
| Bypassing access controls | Immediate termination |

---

## 14. User Acknowledgment

All employees must sign this acknowledgment form:

**Apex Capital (fictional lab scenario) - Access Control Policy Acknowledgment**

| Field | Value |
|-------|-------|
| Employee Name | __________________________ |
| Employee ID | __________________________ |
| Department | __________________________ |
| Date | __________________________ |

By signing below, I acknowledge that:

1. I have read and understood the Access Control Policy of Apex Capital (fictional lab scenario).

2. I understand that I must not share my password or credentials with anyone.

3. I understand that I must not use another user's account.

4. I understand that my access is based on my job role and the principle of least privilege.

5. I will report any unauthorized access or suspicious activity immediately.

6. I understand that violations may result in disciplinary action up to termination.

| | |
|:---|:---|
| **Employee Signature** | __________________________ |
| **Date** | __________________________ |
| **Manager Signature** | __________________________ |
| **Date** | __________________________ |

---

## 15. Exceptions

Any exception to this policy requires:

1. Business justification
2. Compensating controls
3. Approval from CISO
4. Expiration date (max 90 days)
5. Quarterly review

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
| EV-001 | Standard user vs Administrator accounts | `evidence/windows-user-accounts.png` | VM 1 |
| EV-002 | Password policy applied | `evidence/net-accounts-output.png` | VM 1 |
| EV-003 | Account lockout settings | `evidence/account-lockout.png` | VM 1 |
| EV-004 | Failed login alert | `evidence/wazuh-failed-login-alert.png` | VM 4 |
| EV-005 | Ubuntu sudoers configuration | `evidence/ubuntu-sudoers.png` | VM 2 |
| EV-006 | pfSense WebGUI access restriction | `evidence/pfsense-webgui-access.png` | VM 3 |

---

## 18. Related Documents

| Document | Location |
|----------|----------|
| Password Policy | `07-Policies-and-Standards/password-policy.md` |
| Acceptable Use Policy | `07-Policies-and-Standards/acceptable-use-policy.md` |
| Incident Response Policy | `07-Policies-and-Standards/incident-response-policy.md` |
| Data Classification Policy | `07-Policies-and-Standards/data-classification-policy.md` |

---

## 19. Policy Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | March 2026 | S. Singh | Initial draft |
| 0.5 | April 2026 | S. Singh | Added 4-VM role mapping |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

## 20. Approval

| | |
|:---|:---|
| **Policy Approval status (not approved)** | __________________________ |
| **Date** | __________________________ |
| **CISO Signature** | __________________________ |
| **Date** | __________________________ |

---

**End of Access Control Policy**
