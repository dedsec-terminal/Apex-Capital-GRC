# Security capability evaluation

## Purpose and decision

This report demonstrates how I would translate a financial-services security problem into requirements, control choices, an incident response workflow and evidence-based improvement decisions. Apex Capital is a fictional organization. The four-VM design provides a bounded environment for testing the reasoning before extending it to a business network.

The design is ready for structured review. Operational acceptance remains pending: the virtual machines have not been provisioned, the security tests have not been run and no stakeholder has approved the proposed risk decisions. The appropriate next step is to review the response plan through a tabletop exercise, then implement the isolated lab and collect the specified evidence. A written procedure is a deliverable; control effectiveness is a separate conclusion that requires execution evidence.

## Business context and service priorities

The scenario separates a public web service in the DMZ, an internal Windows system holding synthetic business records, and a management network containing Wazuh. pfSense mediates the WAN and the three internal zones. These are representative services, not a complete replica of a financial institution.

| Service or information | Why it matters | Response priority | Decision needed before deployment |
|---|---|---|---|
| Internal records and privileged identities | Unauthorized access could undermine confidentiality and the integrity of business decisions | Stop suspected misuse, establish the scope of affected identities and preserve records | Data owner confirms classification, access roles and acceptable recovery point |
| Public web service | An exposed service can be an entry point and an availability dependency | Contain the affected service without unnecessarily removing management visibility | Service owner defines minimum acceptable service and restoration order |
| Monitoring and administration | Responders need trustworthy telemetry and a clean path for recovery | Protect log collection and administrative access while isolating compromised assets | Security owner confirms retention, time synchronization and responder access |
| Supplier connections and evidence | A service provider may affect access, data handling or recovery | Establish dependency, request evidence and restrict risky integration where justified | Supplier owner records criticality, contractual duties and escalation contacts |

Recovery time and recovery point objectives are deliberately unset until a business impact review establishes them. Targets chosen only because the lab can achieve them would not demonstrate that business requirements were met.

## Requirements and traceability

The following matrix connects intended outcomes to the proposed control crosswalk, a validation activity and the evidence needed for a conclusion. Framework references are selected associations, not a claim of certification or complete coverage. The short `T-01` identifiers refer to the grouped [validation plan](../docs/validation-plan.md); the longer `T-001` identifiers in the original test chapter are detailed technical procedures.

| Outcome | Risks | Proposed references | Validation activity | Evidence required |
|---|---|---|---|---|
| Prevent a DMZ compromise from reaching internal records | R-001, R-008 | NIST PR.IR-01; ISO A.8.22, A.8.32 | T-01, T-08 | Approved flow matrix; allowed and denied connection results; firewall rule and log correlation |
| Restrict administration and sensitive-data access | R-002, R-006 | NIST PR.AA-05; ISO A.5.18, A.8.2 | T-02, T-03 | Effective access policy; separate privileged accounts; positive and negative access tests |
| Identify and investigate suspicious activity | R-004, R-005 | NIST DE.CM-01, DE.CM-09; ISO A.8.15, A.8.16 | T-05 | Original source event; corresponding Wazuh record; host, timestamp and rule identifiers |
| Contain an incident with accountable decisions | R-001, R-002, R-003 | NIST RS.MA-01; ISO A.5.24, A.5.26 | Proposed tabletop exercise | Activation decision; authority; evidence references; containment tradeoff and decision log |
| Recover trusted data and service | R-003 | NIST PR.DS-11, RC.RP-01; ISO A.8.13, A.5.30 | T-06 and recovery tabletop | Backup provenance; isolated restore; integrity and service checks; owner acceptance |
| Review suppliers before relying on their security claims | R-007 | NIST GV.SC-04, GV.SC-06, GV.SC-07; ISO A.5.19, A.5.20 | T-07 | Scoped evidence packet; reviewer rationale; unresolved gaps; treatment decision and reassessment trigger |

All execution results in this matrix are pending. Evidence filenames identify what should be collected; a filename alone does not establish that the artifact exists.

## Control decisions and their tradeoffs

**Segmentation.** The DMZ does not need general access to the internal Windows network. The proposed policy therefore denies this path by default and permits only documented service dependencies. An allowed management connection must also be tested: a failed connection could reflect a broken route or an unavailable service rather than an effective deny rule.

**Administrative access.** Restrict SSH and RDP to approved management sources and separate routine user activity from privileged administration. Network location alone does not establish identity or authorization. If a VPN or MFA service is added, its configuration and failure behavior become separate evidence requirements.

**Monitoring.** A Wazuh alert is an investigation lead. The analyst should establish which source produced it, whether the clocks agree and whether a second source corroborates the activity before asserting compromise. Retention and retrieval matter alongside alert creation because a missing investigation window can prevent an otherwise well-designed response.

**Containment.** Isolating an affected host can limit propagation but may interrupt business activity or remove access to volatile evidence. The incident manager records the observed risk, the isolation scope and the approving role. Where active harm requires immediate action, responders document the emergency decision and obtain retrospective review rather than inventing prior approval.

**Recovery.** Restoring a file does not establish that the host, credentials or exploited entry point are trustworthy. Recovery includes a clean baseline, remediation of the entry point, credential rotation from a clean administrative system, validation of restored data and functioning monitoring before reconnection.

**Supplier assurance.** An assurance report must match the supplier entity, service, period and relevant control scope. A marketing badge or a corrected document is not independent evidence that a control operated effectively. Open gaps remain visible until a reviewer evaluates the evidence and the accountable business role records a decision.

## Proposed incident walkthrough

This is an illustrative reasoning exercise. The signals and decisions below have not been observed in a running Apex environment and do not represent a completed tabletop session.

| Stage and synthetic prompt | Expected decision and rationale | Record to retain |
|---|---|---|
| Wazuh reports unusual authentication activity for Windows at `10.0.2.10`; an endpoint signal suggests file modification | Open a case; validate source and time; collect authentication and endpoint context. Treat compromise as suspected until corroborated | Incident record, original alert reference and initial confidence assessment |
| A second source confirms unexpected encryption of synthetic records | Activate the response team, grade severity against business impact and authorize targeted isolation. Keep the monitoring network available | Severity rationale, activation time, containment decision and affected asset list |
| Firewall records suggest attempted connections from the affected host | Compare the observed path with the approved flow matrix. Determine whether it was permitted, denied or not logged; do not infer successful lateral movement from an attempt | Source and destination, action, rule, timestamp and follow-up query |
| A supplier support account appears in the investigation | Review session and access records, restrict exposed access where justified and request scoped supplier evidence through the supplier owner | Access decision, supplier request, contractual dependency and outstanding questions |
| The business owner requests an immediate return to service | Explain the remaining uncertainty and require clean-baseline, credential, data-integrity and monitoring checks before reconnection | Recovery checklist, validation evidence and recorded acceptance or rejection |
| A review identifies that a critical log source was absent | Open an improvement action and update the risk assessment. Preserve the limitation in the investigation conclusion | Gap, owner, proposed due date, closure evidence and retest requirement |

If corroboration is absent, the analyst records uncertainty and continues proportionate investigation. The walkthrough must include that branch so that a participant is not rewarded merely for declaring every alert a confirmed incident.

## Evaluation method

The exercise facilitator should record actual prompts, decisions and timestamps separately from the expected answers. A self-review is useful practice but is not stakeholder feedback. For a facilitated session, record who participated, the role they played, the recommendations discussed and any resulting changes to the plan.

| Measure | Definition | How to collect it | Current result |
|---|---|---|---|
| Classification decision time | Time from delivery of the first incident prompt to a recorded severity and activation decision | Facilitator prompt timestamp and decision-log timestamp | Not measured |
| Containment decision time | Time from delivery of corroborating compromise evidence to an authorized containment decision | Inject and authorization records | Not measured |
| Evidence completeness | Completed applicable required fields divided by total applicable required fields | Check the evidence register against its defined schema | Not measured |
| Decision traceability | Decisions with an evidence reference and rationale divided by all material decisions | Review the incident decision log | Not measured |
| Communication accuracy | Supported factual statements divided by all factual statements in the situation report | Compare each statement with the scenario evidence available at that stage | Not measured |
| Recovery readiness | Required recovery gates addressed with evidence or a documented blocker divided by all required gates | Review recovery checklist and acceptance decision | Not measured |
| Improvement closure | Actions with accepted closure evidence divided by actions due for review | Review action register, evidence and reviewer disposition | Not measured |

Where the denominator is zero, report the metric as not applicable rather than 100%. Timing in a tabletop measures decision handling under the exercise conditions; it is not production detection, containment or recovery performance. No percentage improvement should be claimed without a comparable baseline, a repeated exercise and a clear description of the measurement conditions.

## Review and improvement register

The actions below are proposed work, not findings from a completed exercise. Due dates should be agreed when ownership and resources are confirmed.

| Action | Reason | Accountable role | Evidence required to close | Status |
|---|---|---|---|---|
| Confirm business service and recovery priorities | Technical recovery must follow business needs | Business service owner | Reviewed impact assessment and approved recovery objectives | Proposed |
| Establish the isolated four-VM environment | Technical controls cannot be evaluated from documentation alone | Lab administrator | VM inventory, versions, network isolation and baseline snapshots | Pending |
| Execute paired allowed and denied network tests | A blocked path alone does not identify the cause | Network security owner | Rule export, positive/negative results and correlated logs | Pending |
| Exercise the incident communication and recovery gates | Demonstrate decisions under incomplete information | Incident manager | Facilitator notes, situation report, decision log and reviewed actions | Pending |
| Review the supplier evidence packet and decision | Demonstrate third-party risk reasoning and accountability | Supplier risk owner | Scoped assessment, evidence limitations, recommendation and reviewer decision | Pending |
| Validate monitoring and backup retrieval | Alerts and backups need retrievable, usable evidence | Security operations and resilience owners | Source-to-alert trace and isolated restore evidence | Pending |

## How to demonstrate the work

A review can follow one complete thread: choose a business requirement, explain the associated risk, justify the control, show its proposed implementation, walk through a failure scenario and identify the evidence needed to accept or reject the control. Close with the business recommendation and its limitations. This demonstrates technical reasoning and risk communication without presenting a planned lab as deployed infrastructure.

The full report contains the detailed policies, architecture and technical procedures. The [incident response plan](../07-Policies-and-Standards/incident-response-plan.md) provides the operational decision process. The [tabletop exercise](tabletop-exercise.md) defines how to test that process. The separate [Vendor Assurance Desk](https://github.com/dedsec-terminal/Vendor-Assurance-Desk) implements a synthetic supplier evidence workflow; its automated fixture results do not validate the Apex VM controls.
