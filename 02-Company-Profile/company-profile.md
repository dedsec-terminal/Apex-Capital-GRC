> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Company Profile

## 1. Corporate Overview

### 1.1 Basic Information

| Attribute                         | Detail                                                  |
| --------------------------------- | ------------------------------------------------------- |
| **Legal Entity Name**             | Apex Capital (fictional lab scenario)          |
| **Entity Type**                   | Registered Investment Adviser (RIA) / Portfolio Manager |
| **AUM (Assets Under Management)** | INR 35,000 Crores (Approx. 4.2 Billion USD)             |
| **Client Count**                  | ~12,000                                                 |
| **Employee Count**                | 350 total (200 HQ-based, 150 remote)                    |
| **Headquarters**                  | Mumbai, Maharashtra                                     |
| **Year Founded**                  | 2008                                                    |
| **Regulatory Bodies**             | SEBI, RBI (as applicable)                               |

### 1.2 Business Description

Apex Capital (fictional lab scenario) provides comprehensive financial advisory services to high-net-worth individuals, family offices, and institutional clients across India.

**Core Services:**
- Mutual fund administration
- Discretionary portfolio management
- Retirement planning (NPS, pension)
- Tax-loss harvesting
- Estate and legacy planning
- Alternative investment advisory

---

## 2. Data Classification & Sensitivity

### 2.1 Data Types Held

| Data Category | Examples | Regulatory Impact |
|---------------|----------|-------------------|
| **Personal Information** | PAN, Aadhaar (masked), passport, date of birth, address, phone number, email | IT Act 2000, SEBI KYC requirements |
| **Financial Data** | Account numbers, demat details, investment holdings, trade confirmations, tax returns | SEBI regulations, RBI guidelines |
| **Beneficiary Information** | Names, relationships, inheritance details | Indian Succession Act |
| **Employee Data** | HR records, payroll, performance reviews | Labour laws, internal confidentiality |
| **Payment Data** | NEFT/RTGS/IMPS details, UPI, card information (limited) | RBI Payment and Settlement Systems Act, PCI DSS |

### 2.2 Data Volume Estimates

| Data Type | Estimated Records | Growth Rate |
|-----------|-------------------|-------------|
| Client Personal Data | 12,000 client records | 5-8% annually |
| Financial transactions | ~50,000 per month | 10% annually |
| Employee records | 350 active + terminated | 3-5% annually |

---

## 3. Technology Footprint

### 3.1 Infrastructure Overview

| System Type | Count | Operating System | Security Relevance |
|-------------|-------|------------------|---------------------|
| HQ Workstations | 200 | Windows 10/11 Pro | Endpoint protection, logging |
| Remote Employee Laptops | 150 | Windows 10/11 Pro | VPN required, remote access controls |
| Web Servers (Customer Portal) | 2 | Ubuntu 22.04 LTS | Public-facing, DMZ placement |
| Internal File Servers | 3 | Windows Server 2019 | Client data storage, access logging |
| Database Servers | 2 | Windows Server + SQL | Portfolio data, transaction history |
| Network Firewall | 1 | pfSense | Segmentation, traffic filtering |
| SIEM / Monitoring | 1 | Ubuntu + Wazuh | Log aggregation, alerting |

### 3.2 Applications in Use

| Application | Purpose | Security Controls |
|-------------|---------|-------------------|
| Microsoft 365 | Email, collaboration | Conditional access, logging |
| Salesforce Financial Cloud | CRM, client management | Role-based access, audit trails |
| Morningstar Direct | Investment research | SSO integration |
| Portfolio Management System | Order execution, client reporting | Dedicated admin accounts, audit logs |

---

## 4. Organizational Structure

### 4.1 Leadership & Security Roles

**Security Leadership Structure:**

| Role | Reporting Line | Security Responsibilities |
|------|----------------|--------------------------|
| **Board of Directors** | Oversight | Final approval of security strategy, risk appetite |
| **CEO / Managing Partner** | Board | Overall accountability for security program |
| **CISO (Virtual/Contract)** | CEO | Strategic direction, policy approval, incident response escalation |
| **CTO** | CEO | Technical implementation, infrastructure security, patch management |
| **Compliance Officer** | CEO | Regulatory reporting (SEBI/RBI), audit coordination, policy enforcement |
| **Proposed GRC Owner Role** | CISO | Risk assessments, policy development, compliance mapping, evidence management |
| **All Employees** | Respective managers | Security awareness, incident reporting, policy adherence |

### 4.2 Security Responsibilities by Role

| Role | Security Responsibilities |
|------|--------------------------|
| **CISO (Virtual)** | Strategic direction, policy approval, incident response escalation |
| **Proposed GRC Owner Role** | Risk assessments, policy development, compliance mapping, evidence management |
| **CTO** | Technical implementation, infrastructure security, patch management |
| **Compliance Officer** | SEBI/RBI reporting, audit coordination, policy enforcement |
| **All Employees** | Security awareness, incident reporting, policy adherence |

---

## 5. Current Security Pain Points

### 5.1 Stated by Fictional Scenario Stakeholders

> *"We passed our last SEBI audit, but it was painful – weeks of scrambling for evidence."*

> *"We have no formal risk register. If something happens, we don't know what we prioritized."*

> *"Our remote advisors use personal laptops inconsistently. Some have antivirus. Some don't."*

> *"If a regulator asked for real-time evidence of controls today, we could not produce it."*

> *"We need cyber resilience without slowing down trading operations."*

### 5.2 Identified Gaps (Pre-Engagement)

| Gap Area | Description | Severity |
|----------|-------------|----------|
| **No Risk Register** | No formal documented risks or treatment plans | Critical |
| **Missing Policies** | No written security policies | Critical |
| **No Centralized Logging** | Logs exist only on individual systems | High |
| **No Network Segmentation** | Web servers and internal servers on same network | Critical |
| **Weak Password Policy** | Default Windows settings, no lockout | High |
| **No Malware Detection Validation** | Antivirus installed but never tested | Medium |
| **No Incident Response Plan** | No documented procedures for breaches | High |

---

## 6. Target State Vision

### 6.1 Fictional Scenario Statement

> *"Audit-ready at all times. Continuous compliance monitoring. Cyber resilience without slowing down trading operations."*

### 6.2 Target State Attributes

| Attribute | Target Description |
|-----------|---------------------|
| **Risk Management** | Documented risk register reviewed regularly |
| **Compliance** | Evidence repository exportable on demand for SEBI audits |
| **Detection** | Real-time alerting for security events |
| **Response** | Documented IR plan tested periodically |
| **Segmentation** | Isolation between public-facing and internal networks |
| **Monitoring** | Centralized SIEM with log retention |

---

## 7. Security Frameworks Applied

### 7.1 Framework Alignment

| Framework | Application | Proposed Evidence (Not Captured) |
|-----------|-------------|-------------------------------|
| **NIST CSF 2.0** | Risk assessment, controls mapping, incident response | Risk register, control implementation, IR policy |
| **ISO 27001:2022** | Information Security Management System (ISMS) | Policies, access controls, logging, asset management |
| **Historical PCI DSS 3.2.1-inspired learning reference (not current compliance)** | Payment data protection (Req 5, 8, 10) | Malware detection (EICAR), password policy, audit logs |

### 7.2 SEBI Alignment (Contextual)

While this engagement is technically aligned to global frameworks (NIST/ISO/PCI), the Proposed controls directly support SEBI's cybersecurity expectations for registered investment advisers:

| SEBI Expectation | Proposed Control | Evidence |
|------------------|---------------------|----------|
| Access control and authentication | Password policy (14 char, lockout), role-based access | Windows security policy screenshots |
| Network segmentation | pfSense firewall separating public and private subnets | Firewall rule screenshots |
| Logging and audit trails | Wazuh SIEM centralized logging, failed login alerts | Wazuh dashboard screenshots |
| Malware protection | Microsoft Defender with EICAR testing | EICAR block screenshot |
| Incident response | Documented incident response policy | IR policy document |
| Vulnerability management | OS hardening (CIS benchmarks) | Hardening configuration screenshots |

---

## 8. Engagement Scope & Boundaries

### 8.1 In Scope

- Risk assessment and risk register development
- Security policy development (6 core policies)
- Technical control implementation on 4 domains (Windows, Ubuntu, pfSense, Wazuh)
- Framework mapping (NIST CSF, ISO 27001, PCI-inspired)
- Testing and validation (EICAR, segmentation, passwords, alerting)
- Evidence repository and documentation

### 8.2 Out of Scope

- Full penetration testing (separate engagement recommended)
- Third-party vendor risk assessments (recommended for Phase 2)
- Employee security awareness training (HR to lead)
- Cyber insurance policy review (legal/finance to lead)
- Physical security assessment (facilities to lead)
- Legal interpretation of SEBI circulars (external counsel recommended)

---

**End of Company Profile**
