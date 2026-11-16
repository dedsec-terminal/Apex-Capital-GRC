> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Data Classification Policy

**Policy Number:** APX-POL-003
**Version:** 1.0
**Effective Date:** May 2026
**Classification:** Internal
**Owner:** Information Security
**Approval status (not approved):** CISO

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.DS-1 | Data-at-rest is protected |
| NIST CSF 2.0 | PR.DS-2 | Data-in-transit is protected |
| NIST CSF 2.0 | ID.AM-3 | Data assets are classified |
| ISO 27001:2022 | A.8.2 | Information classification |
| ISO 27001:2022 | A.8.3 | Handling of information assets |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Req 3 | Protect stored cardholder data |

**External References:**
- NIST SP 800-60: Guide for Mapping Types of Information and Systems
- SANS Data Classification Policy Template

---

## 2. Purpose

This policy establishes a data classification framework to ensure proper handling, protection, and disposal of information based on its sensitivity, business value, and regulatory requirements (SEBI, IT Act 2000, GLBA).

**Risk Addressed:** R-001 (Data Breach), R-005 (Web Server Breach), R-006 (Insider Threat)

---

## 3. Scope

This policy applies to:

| Category | Description |
|----------|-------------|
| **Data Types** | All information created, received, stored, or transmitted by Apex Capital |
| **Formats** | Electronic, paper, verbal, and any other format |
| **Assets** | All 4 VMs (Windows, Ubuntu, pfSense, Wazuh), databases, file shares, email, cloud services |
| **Personnel** | All employees, contractors, and third parties handling Apex Capital data |

---

## 4. Data Classification Levels

### Level 1: Restricted

| Attribute | Detail |
|-----------|--------|
| **Description** | Highly sensitive data. Unauthorized disclosure would cause severe damage to clients or the firm. |
| **Impact** | Severe - Financial loss, regulatory fines, reputational damage, legal liability |
| **Examples** | Client financial portfolios, PAN, Aadhaar (masked), banking details, demat information, investment holdings, encryption keys, trade secrets |
| **Protection Requirements** | Encrypted at rest and in transit, strict access control, MFA, full audit logging |

### Level 2: Confidential

| Attribute | Detail |
|-----------|--------|
| **Description** | Sensitive business data. Unauthorized disclosure would cause significant harm. |
| **Impact** | Moderate - Competitive disadvantage, employee relations issues |
| **Examples** | Employee PII, internal financial reports, contracts, attorney-client communications, security configurations |
| **Protection Requirements** | Encrypted, role-based access, logging |

### Level 3: Internal Use

| Attribute | Detail |
|-----------|--------|
| **Description** | Data for internal business use only. Not intended for public release. |
| **Impact** | Low - Operational inconvenience |
| **Examples** | Internal memos, operational procedures, org charts, internal meeting notes |
| **Protection Requirements** | Standard access controls, no external sharing |

### Level 4: Public

| Attribute | Detail |
|-----------|--------|
| **Description** | Information intended for public release. |
| **Impact** | None - No impact |
| **Examples** | Marketing materials, website content, press releases, annual reports, job postings |
| **Protection Requirements** | No special controls |

---

## 5. Protection Requirements by Level

### 5.1 Restricted (Level 1)

| Requirement | Implementation | VM / Control |
|-------------|----------------|--------------|
| Encryption at rest | BitLocker, NTFS encryption, database encryption | VM 1 (Windows) |
| Encryption in transit | HTTPS, TLS, SSH for all transmissions | VM 2 (Ubuntu), VM 1 (Windows) |
| Access control | Strict role-based access, least privilege | VM 1 (Windows RBAC) |
| MFA requirement | Multi-factor authentication required | Recommended for Phase 2 |
| Audit logging | Full audit trail, 90-day retention | VM 4 (Wazuh) |
| Data retention | Per regulatory requirements (SEBI = 8 years) | Policy enforcement |
| Data disposal | Secure deletion (overwrite or physical destruction) | IT procedure |
| Storage location | Authorized systems only, no cloud unless approved | VM 1, approved cloud services |
| Personal devices | Strictly prohibited | Acceptable Use Policy |

### 5.2 Confidential (Level 2)

| Requirement | Implementation | VM / Control |
|-------------|----------------|--------------|
| Encryption at rest | Recommended for high value data | VM 1 (Windows) |
| Encryption in transit | HTTPS, TLS, SSH for transmissions | VM 2 (Ubuntu), VM 1 (Windows) |
| Access control | Role-based access, need-to-know | VM 1 (Windows RBAC) |
| MFA requirement | Recommended for sensitive Confidential data | Recommended for Phase 2 |
| Audit logging | Standard audit logging, 90-day retention | VM 4 (Wazuh) |
| Data retention | Per policy (minimum 5 years) | Policy enforcement |
| Data disposal | Secure deletion | IT procedure |
| Storage location | Authorized systems only | VM 1, approved services |
| Personal devices | Allowed with encryption and IT approval | Acceptable Use Policy |

### 5.3 Internal Use (Level 3)

| Requirement | Implementation | VM / Control |
|-------------|----------------|--------------|
| Encryption at rest | Not required | N/A |
| Encryption in transit | Not required internally; required for external | N/A |
| Access control | Standard network access controls | VM 1, VM 3 |
| Audit logging | Basic logging (90 days) | VM 4 (Wazuh) |
| Data retention | Per policy (minimum 3 years) | Policy enforcement |
| Data disposal | Standard deletion | IT procedure |
| Personal devices | Allowed | Acceptable Use Policy |

### 5.4 Public (Level 4)

| Requirement | Implementation | VM / Control |
|-------------|----------------|--------------|
| Encryption at rest | Not required | N/A |
| Encryption in transit | Not required | N/A |
| Access control | No access controls | N/A |
| Audit logging | Not required | N/A |
| Data retention | As needed | N/A |
| Personal devices | Allowed | N/A |

---

## 6. Data Classification by Type

| Data Type | Classification | Justification | Primary VM |
|-----------|---------------|---------------|------------|
| Client PII (PAN, Aadhaar masked) | Restricted | Severe harm if disclosed | VM 1 |
| Client financial portfolio holdings | Restricted | Client confidentiality, competitive risk | VM 1 |
| Client bank account details | Restricted | Direct financial risk | VM 1 |
| Client investment strategy | Confidential | Competitive disadvantage if disclosed | VM 1 |
| Employee PII (salary, reviews, HR) | Confidential | Privacy laws, employee trust | VM 1 |
| Internal financial reports | Confidential | Business sensitive | VM 1 |
| Security policies and configurations | Confidential | Avoid aiding attackers | VM 1, VM 2, VM 3, VM 4 |
| Client portal content (public) | Public | Intended for public access | VM 2 |
| Marketing materials | Public | Intended for public release | VM 2 |
| Internal memos | Internal Use | Not for external release | VM 1 |
| Operational procedures | Internal Use | Internal knowledge only | VM 1 |

---

## 7. Data Handling Requirements by VM

| VM | Data Classification Stored | Protection Controls |
|----|---------------------------|---------------------|
| VM 1 (Windows) | Restricted, Confidential, Internal Use | BitLocker (optional), NTFS permissions, EDR, logging |
| VM 2 (Ubuntu) | Public only | HTTPS, firewall, SSH hardening |
| VM 3 (pfSense) | Configuration (Confidential) | WebGUI access restricted, backup encryption |
| VM 4 (Wazuh) | Logs (Confidential, Internal Use) | Access controls, retention policy |

---

## 8. Data Labeling Requirements

### 8.1 Electronic Data

| Data Type | Labeling Requirement | Example |
|-----------|---------------------|---------|
| Restricted | Marked in document header/footer and filename | `[RESTRICTED] Client Financial Report` |
| Confidential | Marked in document header/footer | `[CONFIDENTIAL] Employee Salary Report` |
| Internal Use | Marked in document footer | `[INTERNAL USE ONLY]` |
| Public | No marking required | N/A |

### 8.2 Email Subject Line Markings

| Classification | Email Subject Prefix |
|----------------|----------------------|
| Restricted | `[RESTRICTED]` |
| Confidential | `[CONFIDENTIAL]` |
| Internal Use | No prefix required |
| Public | No prefix required |

---

## 9. Data Retention and Disposal

### 9.1 Retention Periods

| Data Type | Classification | Retention Period | Regulatory Reference |
|-----------|---------------|------------------|---------------------|
| Client records | Restricted | 8 years after account closure | SEBI regulations |
| Trade confirmations | Restricted | 8 years | SEBI regulations |
| Employee records | Confidential | 7 years after termination | Labour laws |
| Internal financials | Confidential | 5 years | Internal policy |
| Audit logs | Internal Use | 90 days (minimum) | Internal policy |
| Security policies | Internal Use | Current + previous 2 versions | Internal policy |

### 9.2 Secure Disposal Methods

| Classification | Electronic Disposal | Physical Disposal |
|----------------|---------------------|-------------------|
| Restricted | Secure overwrite (3+ passes) or cryptographic erasure | Cross-cut shredding, incineration |
| Confidential | Secure overwrite or cryptographic erasure | Cross-cut shredding |
| Internal Use | Standard deletion | Standard shredding |
| Public | Standard deletion | Recycling |

---

## 10. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Data Owner** (Department Head) | Assign classification, review annually, approve access requests |
| **Data Steward** (IT/Compliance) | Implement controls, monitor compliance, maintain inventory |
| **Data Custodian** (IT) | Store data securely, perform backups, execute disposal |
| **All Employees** | Handle data per classification, report incidents, complete training |

---

## 11. User Acknowledgment

All employees must sign this acknowledgment form:

**Apex Capital (fictional lab scenario) - Data Classification Policy Acknowledgment**

| Field | Value |
|-------|-------|
| Employee Name | __________________________ |
| Employee ID | __________________________ |
| Department | __________________________ |
| Date | __________________________ |

By signing below, I acknowledge that:

1. I have read and understood the Data Classification Policy of Apex Capital (fictional lab scenario).

2. I understand the four classification levels: Restricted, Confidential, Internal Use, and Public.

3. I will classify data appropriately when creating or receiving it.

4. I will handle and protect data according to its classification level.

5. I will report any suspected data breach immediately.

6. I understand that violations may result in disciplinary action up to termination.

| | |
|:---|:---|
| **Employee Signature** | __________________________ |
| **Date** | __________________________ |
| **Manager Signature** | __________________________ |
| **Date** | __________________________ |

---

## 12. Exceptions

Any exception to this policy requires:

1. Business justification
2. Compensating controls
3. Approval from CISO and Data Owner
4. Expiration date (max 90 days)
5. Quarterly review

**Exception Request Form:**

| Field | Value |
|-------|-------|
| Requester Name | __________________________ |
| Data Type | __________________________ |
| Current Classification | __________________________ |
| Requested Exception | __________________________ |
| Business Justification | __________________________ |
| Compensating Controls | __________________________ |
| Requested Duration (days) | __________________________ |
| Data Owner Approval | __________________________ |
| CISO Approval | __________________________ |
| Expiration Date | __________________________ |

---

## 13. Review Cycle

This policy will be reviewed:

- Annually (minimum)
- After significant security incidents
- When regulatory requirements change
- When new data types are introduced

---

## 14. Evidence of Implementation

| Evidence ID | Description | Location | VM |
|-------------|-------------|----------|-----|
| EV-001 | Data classification labels on documents | `evidence/data-classification-labels.png` | VM 1 |
| EV-002 | Restricted data access control | `evidence/restricted-access-control.png` | VM 1 |
| EV-003 | Encryption in transit (HTTPS) | `evidence/https-padlock.png` | VM 2 |
| EV-004 | Audit logging for Restricted data | `evidence/wazuh-audit-log.png` | VM 4 |
| EV-005 | Data inventory spreadsheet | `evidence/data-inventory.png` | N/A |

---

## 15. Related Documents

| Document | Location |
|----------|----------|
| Access Control Policy | `07-Policies-and-Standards/access-control-policy.md` |
| Password Policy | `07-Policies-and-Standards/password-policy.md` |
| Acceptable Use Policy | `07-Policies-and-Standards/acceptable-use-policy.md` |
| Incident Response Policy | `07-Policies-and-Standards/incident-response-policy.md` |

---

## 16. Policy Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | March 2026 | S. Singh | Initial draft |
| 0.5 | April 2026 | S. Singh | Added 4-VM classification mapping |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

## 17. Approval

| | |
|:---|:---|
| **Policy Approval status (not approved)** | __________________________ |
| **Date** | __________________________ |
| **CISO Signature** | __________________________ |
| **Date** | __________________________ |

---

**End of Data Classification Policy**
