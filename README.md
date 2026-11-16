# Apex Capital Security and GRC Report

A security design and incident response case study by **Swaraj Singh**, demonstrating how business requirements become risk decisions, technical controls, validation procedures and evidence-based recommendations.

**[Explore the website](https://dedsec-terminal.github.io/Apex-Capital-GRC/) · [Read the complete report](https://dedsec-terminal.github.io/Apex-Capital-GRC/site/report/) · [Browse the Markdown report](COMPLETE-REPORT.md)**

Editable documents: [Security and GRC report](downloads/Apex_Capital_Security_and_GRC_Report.docx) · [Incident response plan](downloads/Apex_Capital_Incident_Response_Plan.docx).

## What the project demonstrates

- **Risk assessment:** eight scenario risks, explicit likelihood and impact scoring, accountable roles and proposed treatments.
- **Security architecture:** a four-VM design with a pfSense boundary, Ubuntu web service, Windows endpoint and Wazuh monitoring across separate DMZ, internal and management zones.
- **GRC reasoning:** selected NIST CSF 2.0 and ISO/IEC 27001:2022 associations, policy decisions and requirements-to-evidence traceability.
- **Incident response:** activation and severity decisions, response roles, evidence handling, communications, containment, recovery gates and improvement tracking.
- **Validation:** technical test procedures, a proposed facilitated tabletop exercise, evaluation criteria and an evidence register.
- **Supplier assurance:** a supplier-risk thread and its relationship to the separate [Vendor Assurance Desk](https://github.com/dedsec-terminal/Vendor-Assurance-Desk) implementation.

Apex Capital is a fictional organization. This report demonstrates analysis and design. The VM controls and tabletop exercise are **not executed**; expected results and target risk ratings are not measured outcomes. No client engagement, regulatory compliance or certification is claimed.

## Start with one complete decision

Read the [capability evaluation](09-Testing-and-Validation/capability-evaluation.md) for the business problem, control tradeoffs, proposed incident walkthrough and measurement method. Continue to the [incident response plan](07-Policies-and-Standards/incident-response-plan.md) and [tabletop exercise](09-Testing-and-Validation/tabletop-exercise.md) to see how the response would be governed and evaluated.

The full reader preserves all **29 original Markdown chapters** in an ordered structure, with three additional chapters for capability evaluation, incident response and the tabletop exercise. The website includes architecture, permitted network flows, telemetry, risk-to-evidence traceability, response and supplier-workflow diagrams. It is a reading interface for the complete report, not a replacement for its detail.

## Report structure

| Folder | Contents |
|---|---|
| [00 Front Matter](00-Front-Matter/) | Cover, contents and report index |
| [01 Executive Summary](01-Executive-Summary/) | Purpose, principal risks and proposed direction |
| [02 Company Profile](02-Company-Profile/) | Fictional operating context and assumptions |
| [03 Business Requirements](03-Business-Requirements/) | Business needs and technical security requirements |
| [04 Risk Assessment](04-Risk-Assessment/) | Method, risk register and illustrative heatmap |
| [05 Security Architecture](05-Security-Architecture/) | Network zones, systems and design decisions |
| [06 Framework Mapping](06-Framework-Mapping/) | Selected framework associations and historical learning material |
| [07 Policies and Standards](07-Policies-and-Standards/) | Access, data, acceptable use, authentication and incident response |
| [08 Technical Controls](08-Technical-Controls/) | Proposed pfSense, Ubuntu, Windows and Wazuh configurations |
| [09 Testing and Validation](09-Testing-and-Validation/) | Test procedures, expected outcomes, capability evaluation and tabletop |
| [10 Evidence](10-Evidence/) | Required artifacts and illustrative log formats |
| [11 Residual Risk](11-Residual-Risk/) | Proposed treatment targets and recommendations |
| [12 Appendices](12-Appendices/) | Technical references |

The [manifest](report-manifest.json) records chapter order and publication status. The `docs/` folder provides short reference summaries of the [architecture](docs/architecture.md), [canonical risk register](docs/risk-register.md), [control crosswalk](docs/control-mapping.md) and [validation plan](docs/validation-plan.md).

## Build and check

```powershell
python -m pip install -r requirements.txt
python scripts/build_report.py
python scripts/validate_publication.py
python -m http.server 8766 --bind 127.0.0.1
```

Open `http://127.0.0.1:8766/site/`. The build produces a searchable chapter reader, a printable full-report view and the combined Markdown report. The validator checks publication links, chapter coverage and register consistency. Browser checks cover navigation, diagrams and responsive layout. These checks validate the publication, not the proposed security controls.

## Next evidence to collect

Provision the isolated lab, execute paired allowed and denied network tests, trace a controlled event through the logging pipeline and verify an isolated restore. Run the tabletop with real participants and capture their decisions, feedback and resulting changes. Update findings and residual risk only after reviewing those artifacts.

See [scope and assumptions](docs/scope-and-assumptions.md), [evidence status](docs/validation-plan.md) and [limitations](docs/limitations-and-next-steps.md) for the current boundaries.
