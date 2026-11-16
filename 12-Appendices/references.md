> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# REFERENCES

**Last Updated:** May 2026
**Version:** 1.0
**Classification:** Internal
**Owner:** GRC Lead

---

## 1. Framework References

### 1.1 NIST Cybersecurity Framework (CSF) 2.0

| Reference | URL | Description |
|-----------|-----|-------------|
| NIST CSF 2.0 Official Website | https://www.nist.gov/cyberframework | Main framework page |
| NIST CSF 2.0 Core Document | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | Functions, categories, subcategories |
| NIST CSF 2.0 Implementation Tiers | https://www.nist.gov/cyberframework/tiers | Maturity levels |
| NIST SP 800-30 Rev 1 | https://csrc.nist.gov/pubs/sp/800/30/r1/final | Risk assessment guide |

### 1.2 ISO/IEC 27001:2022

| Reference | URL | Description |
|-----------|-----|-------------|
| ISO 27001 Official Website | https://www.iso.org/standard/27001 | ISMS requirements |
| ISO 27001 Annex A Controls | https://www.iso27001security.com/html/27001.html | Control mapping |
| ISO 27002:2022 | https://www.iso.org/standard/75652.html | Implementation guidance |

### 1.3 Historical PCI DSS 3.2.1-inspired reference (not current compliance)

| Reference | URL | Description |
|-----------|-----|-------------|
| PCI DSS Official Website | https://www.pcisecuritystandards.org/document_library | Main framework |
| PCI DSS Requirements | https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf | 12 requirements |
| SAQ Instructions | https://www.pcisecuritystandards.org/saq | Self-assessment questionnaire |

---

## 2. Policy Framework References

### 2.1 SANS Policy Templates

| Reference | URL | Description |
|-----------|-----|-------------|
| SANS Security Policy Templates | https://www.sans.org/information-security-policy-templates/ | Industry standard templates |
| SANS Acceptable Use Policy | https://www.sans.org/information-security-policy-templates/acceptable-use-policy/ | AU policy template |
| SANS Access Control Policy | https://www.sans.org/information-security-policy-templates/access-control-policy/ | Access control template |
| SANS Incident Response Policy | https://www.sans.org/information-security-policy-templates/incident-response-policy/ | IR policy template |

### 2.2 CIS Benchmarks

| Reference | URL | Description |
|-----------|-----|-------------|
| CIS Benchmarks | https://www.cisecurity.org/benchmarks/ | Security configuration benchmarks |
| CIS Windows Benchmark | https://www.cisecurity.org/benchmark/microsoft_windows/ | Windows hardening |
| CIS Ubuntu Benchmark | https://www.cisecurity.org/benchmark/ubuntu_linux/ | Ubuntu hardening |

---

## 3. Technical References

### 3.1 pfSense

| Reference | URL | Description |
|-----------|-----|-------------|
| pfSense Documentation | https://docs.netgate.com/pfsense/en/latest/ | Official documentation |
| pfSense Firewall Rules | https://docs.netgate.com/pfsense/en/latest/firewall/index.html | Rule configuration |
| pfSense Segmentation Guide | https://docs.netgate.com/pfsense/en/latest/book/firewall/firewall-quick-start.html | Network segmentation |

### 3.2 Microsoft Windows Security

| Reference | URL | Description |
|-----------|-----|-------------|
| Microsoft Security Baselines | https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines | Security baselines |
| Windows Defender Documentation | https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint | Defender configuration |
| Windows Event Logs | https://learn.microsoft.com/en-us/windows/win32/eventlog/event-logging | Event ID reference |
| Microsoft Security Compliance Toolkit | https://www.microsoft.com/en-us/download/details.aspx?id=55319 | Compliance tools |

### 3.3 Ubuntu Linux Security

| Reference | URL | Description |
|-----------|-----|-------------|
| Ubuntu Security Documentation | https://ubuntu.com/security | Official security guide |
| UFW Documentation | https://help.ubuntu.com/community/UFW | Firewall configuration |
| SSH Hardening Guide | https://ubuntu.com/server/docs/security-hardening | SSH security |
| fail2ban Documentation | https://www.fail2ban.org/wiki/index.php/Main_Page | Brute force protection |

### 3.4 Wazuh SIEM

| Reference | URL | Description |
|-----------|-----|-------------|
| Wazuh Documentation | https://documentation.wazuh.com/current/ | Official documentation |
| Wazuh Installation Guide | https://documentation.wazuh.com/current/installation-guide/index.html | Setup instructions |
| Wazuh Rules Configuration | https://documentation.wazuh.com/current/user-manual/ruleset/index.html | Alert rules |
| Wazuh Compliance Mapping | https://documentation.wazuh.com/current/compliance/index.html | Framework alignment |

---

## 4. Regulatory References (Context)

### 4.1 Financial Services Regulations

| Reference | URL | Description |
|-----------|-----|-------------|
| SEC Regulation S-P | https://www.sec.gov/rules-regulations/2000/11/privacy-consumer-financial-information-regulation-s-p | Privacy of consumer financial information |
| SEC Regulation S-ID | https://www.sec.gov/rules-regulations/2011/07/identity-theft-red-flags-rules | Identity theft red flags |
| FINRA Cybersecurity | https://www.finra.org/rules-guidance/key-topics/cybersecurity | FINRA cybersecurity best practices |
| GLBA Safeguards Rule | https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act | Security program requirements |

---

## 5. Testing and Validation References

### 5.1 EICAR Test File

| Reference | URL | Description |
|-----------|-----|-------------|
| EICAR Official Website | https://www.eicar.org/download-anti-malware-testfile/ | Safe malware test file |
| EICAR Test String | https://www.eicar.org/standard-anti-malware-test-file/ | Test string documentation |

### 5.2 Security Testing Guides

| Reference | URL | Description |
|-----------|-----|-------------|
| NIST SP 800-115 | https://csrc.nist.gov/publications/detail/sp/800-115/final | Technical testing guide |
| OWASP Testing Guide | https://owasp.org/www-project-web-security-testing-guide/ | Web application testing |

---

## 6. Threat Intelligence Frameworks

| Framework | URL | Description |
|-----------|-----|-------------|
| MITRE ATT&CK | https://attack.mitre.org/ | Adversary tactics and techniques |
| Lockheed Martin Cyber Kill Chain | https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html | Attack lifecycle model |
| NIST SP 800-61 Rev 2 | https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final | Incident response guide |

---

## 7. Tools and Software Documentation

### 7.1 Open Source Tools

| Tool | URL | Description |
|------|-----|-------------|
| Pandoc | https://pandoc.org/ | Document conversion |
| XeLaTeX | https://www.tug.org/xelatex/ | PDF generation |
| Draw.io | https://www.drawio.com/ | Network diagrams |
| Obsidian | https://obsidian.md/ | Markdown editing |

### 7.2 Virtualization

| Tool | URL | Description |
|------|-----|-------------|
| VirtualBox | https://www.virtualbox.org/ | VM host |
| VMware Workstation | https://www.vmware.com/products/workstation-pro.html | VM host |

---

## 8. How These References Are Used

| Section | Primary References |
|---------|-------------------|
| Executive Summary | NIST CSF 2.0 Functions |
| Risk Assessment | NIST SP 800-30, ISO 27001 Clause 6 |
| Risk Register | ISO 27001 Annex A |
| Policies | SANS Policy Templates |
| Windows Hardening | CIS Microsoft Windows Benchmark |
| Ubuntu Hardening | CIS Ubuntu Benchmark |
| pfSense Configuration | pfSense Documentation |
| Wazuh Monitoring | Wazuh Documentation |
| Network Segmentation | NIST SP 800-53 (AC-4, SC-7) |
| Testing | NIST SP 800-115, EICAR |
| Incident Response | NIST SP 800-61 |

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added technical references |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of References**
