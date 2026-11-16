> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Authentication Policy and Configuration Exercise

## Current design decision

For a production design, select authentication requirements according to the service and assurance level, use MFA where required by the risk assessment, check new passwords against compromised/common-password lists and protect recovery paths. For centrally verified passwords within its scope, NIST SP 800-63B-4 specifies at least 15 characters for single-factor use, permits a minimum of eight when used with MFA, and rejects arbitrary composition rules and routine periodic changes. A compromise requires a password change. See the [current NIST password requirements](https://pages.nist.gov/800-63-4/sp800-63b.html#passwordver).

The numbered sections below retain a **legacy Windows configuration exercise and draft forms**. Their 14-character, composition and 90-day settings demonstrate configuration mechanics; they are not the selected production baseline, a financial-sector mandate or evidence of conformity with current NIST guidance. The same legacy settings appear in technical command examples and planned tests elsewhere in the report. Before execution, choose and document the applicable profile and supported Windows capabilities.

**Policy Number:** APX-POL-002
**Version:** 1.0
**Effective Date:** May 2026
**Classification:** Internal
**Owner:** Information Security
**Approval status (not approved):** CISO

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.AA-01 | Identities and credentials are managed |
| NIST CSF 2.0 | PR.AA-03 | User, device, and other asset authentication |
| ISO 27001:2022 | A.5.17 | Authentication information |
| Historical PCI DSS 3.2.1-inspired learning theme | Requirement 8 | Identification and authentication; no current compliance conclusion |

**External References:**
- NIST SP 800-63B (Digital Identity Guidelines – Authentication)
- SANS Password Policy Template: https://www.sans.org/information-security-policy-templates/

---

## 2. Purpose

This policy establishes password requirements to protect Apex Capital's systems, client data, and infrastructure from credential-based attacks such as brute force, dictionary attacks, and credential stuffing.

**Risk Addressed:** R-002 (Credential Theft – Score 20 Critical)

---

## 3. Scope

This policy applies to:

| Category | Description |
|----------|-------------|
| **Employees** | All full-time and part-time employees of Apex Capital |
| **Contractors** | Temporary staff, consultants, and outsourced vendors |
| **Third Parties** | Business partners with access to Apex systems |
| **Systems** | All 4 VMs (Windows, Ubuntu, pfSense, Wazuh) |
| **Applications** | All internal and external applications |
| **Service Accounts** | Application-to-application authentication |

---

## 4. Password Requirements

### 4.1 Complexity Requirements

| Requirement | Setting | Rationale |
|-------------|---------|-----------|
| Minimum length | 14 characters | Legacy exercise value; not a financial-sector requirement or the current production choice |
| Uppercase letters | At least 1 (A-Z) | Legacy composition check; does not establish resistance to guessing |
| Lowercase letters | At least 1 (a-z) | Legacy composition check; not required by current NIST password guidance |
| Numbers | At least 1 (0-9) | Legacy composition check; predictable substitutions remain guessable |
| Special characters | At least 1 (!@#$%^&*) | Legacy composition check; not a substitute for length and blocklist checks |
| Complexity enforcement | 3 of 4 categories | Demonstrates the Windows legacy-policy setting only |

### 4.2 Password History and Aging

| Requirement | Setting | Rationale |
|-------------|---------|-----------|
| Password history | 24 previous passwords remembered | Prevents password reuse |
| Minimum password age | 1 day | Prevents immediate cycling |
| Maximum password age | 90 days | Legacy exercise setting, superseded by the current design decision above |
| Password change required | Every 90 days | Legacy draft requirement; not the chosen production rotation policy |

### 4.3 Account Lockout Policy

| Requirement | Setting | Rationale |
|-------------|---------|-----------|
| Lockout threshold | 5 failed attempts | Allows for typos but blocks brute force |
| Lockout duration | 30 minutes | Deters automated attacks |
| Reset lockout counter | 30 minutes | Prevents permanent denial of service |

### 4.4 Prohibited Passwords

The following passwords are **explicitly prohibited**:

| Category | Examples | Reason |
|----------|----------|--------|
| Default passwords | [SYNTHETIC-TEST-CREDENTIAL], [SYNTHETIC-TEST-CREDENTIAL], [SYNTHETIC-TEST-CREDENTIAL], [SYNTHETIC-TEST-CREDENTIAL] | Widely known, commonly used |
| Company name variations | ApexCapital, Apex2024, Apex123 | Easily guessed |
| Season and year | [SYNTHETIC-TEST-CREDENTIAL], Winter2023, Spring2025 | Predictable patterns |
| Keyboard patterns | qwerty123, 1qaz2wsx, asdfgh | Common sequences |
| Dictionary words | Password, Admin, Letmein, Monkey | Dictionary attacks |
| Personal information | Employee names, birthdays, pet names | Social engineering |
| Repeating characters | aaaaaa, 111111, 123123 | Easily guessed |
| Sequential characters | abcdef, 123456, 987654 | Easily guessed |

---

## 5. Technical Implementation by VM

### 5.1 Windows (VM 1) - Local Security Policy

| Command | Purpose | Expected Output |
|---------|---------|-----------------|
| net accounts /minpwlen:14 | Minimum password length | 14 |
| net accounts /maxpwage:90 | Maximum password age | 90 days |
| net accounts /minpwage:1 | Minimum password age | 1 day |
| net accounts /uniquepw:24 | Password history | 24 passwords remembered |
| net accounts /lockoutthreshold:5 | Lockout threshold | 5 invalid attempts |
| net accounts /lockoutduration:30 | Lockout duration | 30 minutes |
| net accounts /lockoutwindow:30 | Reset lockout counter | 30 minutes |

**Verification Command:**
net accounts

**Expected Output:**
Minimum password age (days): 1
Maximum password age (days): 90
Minimum password length: 14
Length of password history maintained: 24
Lockout threshold: 5
Lockout duration (minutes): 30
Lockout observation window (minutes): 30

### 5.2 Windows (VM 1) - Password Complexity via secpol.msc

| Setting | Value | Path |
|---------|-------|------|
| Password must meet complexity requirements | Enabled | secpol.msc > Account Policies > Password Policy |
| Minimum password length | 14 | secpol.msc > Account Policies > Password Policy |

### 5.3 Ubuntu (VM 2) - SSH Password Authentication

| Setting | Value | File Location |
|---------|-------|---------------|
| PasswordAuthentication | no (use SSH keys only) | /etc/ssh/sshd_config |
| PermitRootLogin | no | /etc/ssh/sshd_config |
| MaxAuthTries | 3 | /etc/ssh/sshd_config |
| ClientAliveInterval | 300 | /etc/ssh/sshd_config |
| ClientAliveCountMax | 2 | /etc/ssh/sshd_config |

**Verification Command:**
sudo cat /etc/ssh/sshd_config | grep -E "PasswordAuthentication|PermitRootLogin|MaxAuthTries"

### 5.4 pfSense (VM 3) - WebGUI Password Policy

| Setting | Value | Location |
|---------|-------|----------|
| Minimum password length | 14 | System > User Manager > Settings |
| Lockout attempts | 5 | System > Advanced > Admin Access |
| Lockout time | 30 minutes | System > Advanced > Admin Access |
| WebGUI protocol | HTTPS only | System > Advanced > Admin Access |

### 5.5 Wazuh (VM 4) - API Authentication

| Setting | Value | Configuration |
|---------|-------|---------------|
| Password complexity | Enforced | Wazuh API user creation |
| Token expiration | 15 minutes | ossec.conf |
| Max login attempts | 5 | Wazuh API configuration |

---

## 6. Multi-Factor Authentication (MFA)

### 6.1 MFA Requirements

| Access Type | MFA Requirement | Status | Timeline |
|-------------|-----------------|--------|----------|
| All remote access | Required | Planned / not executed | Phase 2 |
| Administrative accounts | Required | Planned / not executed | Phase 2 |
| Client portal access | Required | Out of scope | Client responsibility |
| VPN connections | Required | Planned / not executed | Phase 2 |
| Internal network access | Recommended | Not planned | N/A |

### 6.2 MFA Methods

| Method | Supported | Recommended For |
|--------|-----------|-----------------|
| Authenticator app (TOTP) | Yes | All users (Google Authenticator, Microsoft Authenticator) |
| SMS/Text message | Yes (less secure) | Backup method only |
| Hardware token (YubiKey) | Yes | Administrative accounts |
| Biometric (fingerprint/face) | Yes (device dependent) | Mobile access |

**Note:** MFA implementation is recommended for Phase 2 of the security program.

---

## 7. Service Account Password Requirements

| Requirement | Setting | Rationale |
|-------------|---------|-----------|
| Minimum length | 20 characters | Higher entropy for privileged access |
| Complexity | All 4 categories | Maximum security |
| Change frequency | Every 180 days | Longer than user accounts |
| Storage location | Password vault | No hardcoded passwords |
| Individual accounts | No shared service accounts | Auditability |

---

## 8. Administrative Account Password Requirements

| Requirement | Setting | Rationale |
|-------------|---------|-----------|
| Minimum length | 16 characters | Higher than standard users |
| Complexity | All 4 categories | Maximum security |
| Change frequency | Every 60 days | More frequent than user accounts |
| MFA requirement | Required | Critical access protection |
| Separate from daily account | Required | Reduces exposure |

---

## 9. Password Storage and Transmission

| Requirement | Implementation | VM / System |
|-------------|----------------|--------------|
| Passwords stored with hashing | Windows NTLM hashing (modern) | VM 1 |
| Passwords never stored in plaintext | No plaintext password files | All |
| Passwords encrypted in transit | HTTPS, SSH, TLS | VM 2, VM 3, VM 4 |
| No password storage in browsers | Group Policy disabled | VM 1 |

---

## 10. Password Change Process

### 10.1 Windows (VM 1)

| Method | Steps |
|--------|-------|
| Ctrl+Alt+Del | Select "Change a password" |
| Command line | net user [username] * |
| Local Security Policy | secpol.msc > Account Policies |

### 10.2 Ubuntu (VM 2)

| Command | Purpose |
|---------|---------|
| passwd | Change current user password |
| sudo passwd [username] | Change another user's password (admin only) |

### 10.3 pfSense (VM 3)

| Steps |
|-------|
| System > User Manager > Edit User |
| Enter new password, confirm |
| Apply changes |

### 10.4 Wazuh (VM 4)

| Steps |
|-------|
| /var/ossec/bin/wazuh-passwd [username] |
| Restart Wazuh API service |

---

## 11. Password Security Best Practices

| Practice | Required | Guidance |
|----------|----------|----------|
| Do not share passwords | Yes | Never share via email, phone, or text |
| Do not write down passwords | Yes | Use password manager instead |
| Do not reuse passwords | Yes | Different password for each system |
| Do not use personal information | Yes | Avoid birthdays, names, etc. |
| Use passphrases when possible | Recommended | Use multiple random words |
| Report compromised passwords | Yes | Immediately to IT Manager |

---

## 12. Compliance and Enforcement

| Violation | First Offense | Second Offense | Third Offense |
|-----------|---------------|----------------|---------------|
| Weak password (detected at change) | Password reset required, verbal warning | Written warning, retraining | HR referral |
| Password sharing | Written warning | Suspension (3 days) | Termination |
| Writing down password | Verbal warning | Written warning | HR referral |
| Failure to change password at 90 days | Account locked (user must contact IT) | Same as first | Same as first |

---

## 13. User Acknowledgment

All employees must sign this acknowledgment form:

**Apex Capital (fictional lab scenario) - Password Policy Acknowledgment**

Employee Name: __________________________

Employee ID: __________________________

Department: __________________________

Date: __________________________

By signing below, I acknowledge that:

1. I have read and understood the Password Policy of Apex Capital (fictional lab scenario).

2. I will create strong passwords that meet the complexity requirements.

3. I will change my password every 90 days.

4. I will not share my password with anyone, including IT staff.

5. I will not write down my password or store it in unencrypted files.

6. I will use a unique password for work systems.

7. I understand that my account will lock after 5 failed attempts.

8. I understand that violations may result in disciplinary action up to termination.

**Employee Signature:** __________________________

**Date:** __________________________

**Manager Signature:** __________________________

**Date:** __________________________

**For IT Use Only:**
- Password policy applied to user account: Yes / No
- Date: __________________________
- IT Administrator Signature: __________________________

---

## 14. Exceptions

Any exception to this policy requires:

1. Business justification (e.g., legacy system limitation)
2. Compensating controls (e.g., IP whitelist + MFA)
3. Approval from CISO
4. Expiration date (max 90 days)
5. Quarterly review for continued necessity

**Exception Request Form:**

| Field | Value |
|-------|-------|
| Requester Name | __________________________ |
| System/Account | __________________________ |
| Policy exception requested | __________________________ |
| Business Justification | __________________________ |
| Compensating Controls | __________________________ |
| Requested Duration (days) | __________________________ |
| CISO Approval Signature | __________________________ |
| Expiration Date | __________________________ |

---

## 15. Review Cycle

This policy will be reviewed:

- Annually (minimum)
- After significant security incidents
- When NIST/ISO frameworks are updated
- When new authentication technologies are deployed

---

## 16. Evidence of Implementation

| Evidence ID | Description | Location | VM |
|-------------|-------------|----------|-----|
| EV-001 | net accounts output showing policy | evidence/net-accounts-output.png | VM 1 |
| EV-002 | Weak password "[SYNTHETIC-TEST-CREDENTIAL]" rejected | evidence/weak-password-rejected.png | VM 1 |
| EV-003 | Account lockout after 5 failures | evidence/account-lockout.png | VM 1 |
| EV-004 | Lockout event (Event ID 4625) | evidence/lockout-event-4625.png | VM 1 |
| EV-005 | Ubuntu SSH PasswordAuthentication no | evidence/ubuntu-ssh-config.png | VM 2 |
| EV-006 | pfSense WebGUI HTTPS enforcement | evidence/pfsense-https.png | VM 3 |
| EV-007 | Failed login alert in Wazuh | evidence/wazuh-failed-login-alert.png | VM 4 |

---

## 17. Related Documents

| Document | Location |
|----------|----------|
| Access Control Policy | 07-Policies-and-Standards/access-control-policy.md |
| Acceptable Use Policy | 07-Policies-and-Standards/acceptable-use-policy.md |
| Incident Response Policy | 07-Policies-and-Standards/incident-response-policy.md |
| Data Classification Policy | 07-Policies-and-Standards/data-classification-policy.md |

---

## 18. Policy Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | March 2026 | S. Singh | Initial draft |
| 0.5 | April 2026 | S. Singh | Added 4-VM technical implementation |
| 1.0 | May 2026 | S. Singh | Draft learning edition with MFA requirements |

---

**Policy Approval status (not approved):** \underline{\hspace{5cm}} **Date:** \underline{\hspace{5cm}}

**CISO Signature**

---

**End of Password Policy**
