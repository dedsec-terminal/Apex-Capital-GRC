# Proposed control crosswalk

This is a working reference crosswalk between the documented control intent and selected NIST Cybersecurity Framework 2.0 subcategories and ISO/IEC 27001:2022 Annex A controls. It is not a control implementation assessment, Statement of Applicability, certification, or finding that any requirement is satisfied. IDs and titles below follow the framework catalog references; mappings are analyst-selected and should be confirmed against the final scope.

| Control theme | Scenario implementation intent | NIST CSF 2.0 | ISO/IEC 27001:2022 Annex A |
|---|---|---|---|
| Supplier governance and lifecycle | Define supplier security expectations, prioritize suppliers, conduct pre-contract due diligence and monitor risk | GV.SC-01, GV.SC-02, GV.SC-04, GV.SC-05, GV.SC-06, GV.SC-07 | A.5.19, A.5.20, A.5.21; A.5.23 when cloud service use applies |
| Identity and access | Define and review access rights, protect privileged access and apply least privilege | PR.AA-05 | A.5.15, A.5.18, A.8.2 |
| Network boundaries | Restrict and monitor zone-to-zone access; review firewall changes | PR.IR-01 | A.8.20, A.8.21, A.8.22, A.8.32 |
| Secure configuration and vulnerabilities | Maintain known baselines and address technical vulnerabilities | PR.PS-01, PR.PS-02 | A.8.8, A.8.9 |
| Logging and detection | Monitor networks, network services, endpoints and runtime environments for adverse events | DE.CM-01, DE.CM-09 | A.8.15, A.8.16 |
| Incident response | Prepare response responsibilities, coordinate and document response | RS.MA-01 | A.5.24, A.5.26 |
| Backup and continuity | Create, protect, maintain and test backups; execute recovery planning | PR.DS-11, RC.RP-01 | A.8.13, A.5.29, A.5.30 |
| Secure service development | Define application security requirements and integrate security into lifecycle | PR.PS-06 | A.8.25, A.8.26 |
| Cryptographic protection | Select and manage encryption for relevant data and connections | PR.DS-01, PR.DS-02 | A.8.24 |

### Mapping notes

- A reference relationship does not mean the mapped safeguard is implemented or effective.
- NIST CSF subcategories describe outcomes; they are not prescriptive technical configurations.
- ISO Annex A selection and applicability require organizational context and a risk-based Statement of Applicability.
- Legacy source references such as CSF 1.1 `PR.AC`/`PR.IP` and ISO 27001:2013 `A.9.4.3` have been removed from this 2.0/2022 crosswalk.
- The CSF references `PR.PS-01`, `PR.PS-02`, `PR.PS-06`, `PR.DS-01`, and `PR.DS-02` are from NIST CSF 2.0; the architecture and control catalog must be reviewed before claiming direct alignment.
