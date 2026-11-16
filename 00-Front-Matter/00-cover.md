> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Apex Capital (fictional lab scenario)

## Enterprise Cyber Risk & GRC Security Implementation

### Proposed Lab Design and Validation Plan

---

**Prepared for (fictional scenario): **<br>
Apex Capital (fictional lab scenario) Leadership Team & Board of Directors

**Prepared by:**<br>
lab-user SINGH — Cybersecurity & Project Author

**Date:** May 2026<br>
**Version:** 1.0<br>
**Classification:** PUBLIC LEARNING EDITION — FICTIONAL LAB SCENARIO

---

## Document Control

| Version | Status | Date | Author | Changes |
|:-------:|:------:|:----:|:------:|---------|
| 0.1 | Draft | March 2026 | S. Singh | Initial structure |
| 0.5 | Draft | April 2026 | S. Singh | Added technical controls |
| 1.0 | Final | May 2026 | S. Singh | Complete report for delivery |

---

## Engagement Summary

| Field | Detail |
|:------|:-------|
| **Client** | Apex Capital (fictional lab scenario) |
| **AUM** | INR 35,000 Crores (Approx. $4.2 Billion USD) |
| **Client Count** | ~12,000 high-net-worth individuals |
| **Employees** | 350 (200 HQ, 150 remote) |
| **Headquarters** | Mumbai, Maharashtra |
| **Engagement Scope** | Enterprise Cyber Risk Assessment & GRC Implementation |
| **Frameworks Applied** | NIST CSF 2.0, ISO 27001:2022, Historical PCI DSS 3.2.1-inspired learning reference (not current compliance) |
| **Regulatory Context** | SEBI, RBI, IT Act 2000 |
| **Engagement Period** | March 2026 – May 2026 |
| **Engagement ID** | APX-CYBER-2024-001 |

---

## 4-VM Architecture

| VM | Hostname | IP Address | Subnet | Role |
|:--:|----------|------------|--------|------|
| VM 1 | Windows-Enterprise | 10.0.2.10 | Internal (10.0.2.0/24) | Workstation / Server |
| VM 2 | Ubuntu-Web | 10.0.1.10 | DMZ (10.0.1.0/24) | Public Web Server |
| VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All | Firewall / Router |
| VM 4 | Wazuh-SIEM | 10.0.3.10 | Management (10.0.3.0/24) | SIEM / Monitoring |

---

## Distribution Restrictions

This document contains **FICTIONAL SCENARIO; PUBLIC LEARNING EDITION** information pertaining to Apex Capital (fictional lab scenario)'s security posture, risk assessments, and internal controls.

**Authorized Recipients:**
- Apex Capital Board of Directors
- Chief Information Security Officer (CISO)
- Internal Audit Team
- Legal Counsel (as needed)
- SEBI / RBI (only if formally requested)

This is a public fictional lab case study; no client or engagement exists.

---

## Approvals

| Role | Name | Signature | Date |
|:-----|:-----|:----------|:-----|
| **Prepared By** | lab-user SINGH, Project Author | \_\_\_\_\_\_\_\_\_\_\_ | May 2026 |
| **Reviewed By** | Internal Quality Assurance | \_\_\_\_\_\_\_\_\_\_\_ | May 2026 |
| **Approval status (not approved)** | Engagement Lead | \_\_\_\_\_\_\_\_\_\_\_ | May 2026 |
| **Acceptance status (not accepted)** | Apex Capital CISO | \_\_\_\_\_\_\_\_\_\_\_ | May 2026 |

---

*This report is the property of Apex Capital (fictional lab scenario). Unauthorized reproduction or distribution is prohibited.*

---

**End of Cover Page**
