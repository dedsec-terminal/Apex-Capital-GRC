# Cyber Incident Response Plan

## Document status

| Field | Value |
|---|---|
| Environment | Fictional Apex Capital security lab |
| Document owner | Proposed role: Security Lead |
| Approval | Draft for review; no approval has been recorded |
| Version | 0.1 |
| Review cycle | At least annually, and after a material incident, exercise, or environment change |
| Classification | Public learning artifact; contains no real contact details or operational credentials |

> **Scenario boundary.** Apex Capital and its operating details are fictional. This plan describes a proposed response capability for a four-VM lab: pfSense with WAN, DMZ, internal and management interfaces; an Ubuntu web server in the DMZ; a Windows workstation in the internal zone; and Wazuh in the management zone. It is a design and learning artifact. No incident response exercise, VM validation, or recovery test is represented as completed.

## 1. Purpose and objectives

This plan gives the Apex Capital scenario a repeatable way to report, assess, contain, investigate, recover from, and learn from suspected cyber incidents. It connects technical actions to business decisions: protect people and information, limit service disruption, preserve reliable evidence, meet applicable obligations, and restore services only when a responsible owner accepts the recovery evidence.

The plan sets out decision authority, response roles, severity and escalation, internal and external communications, evidence handling, remediation tracking, recovery acceptance, and post-incident improvement. Supporting procedures should supply environment-specific commands and contact details after the lab or any real organization has been configured and approved.

## 2. Scope and operating assumptions

The plan covers suspected compromise or disruption of the lab's network, systems, accounts, telemetry, and information. It also covers incidents reported by a service provider or other trusted party when they could affect Apex services or data.

The proposed zones and systems are:

| Component | Purpose in the scenario | Incident-response relevance |
|---|---|---|
| pfSense WAN interface | External connectivity | Ingress/egress policy, firewall events, suspected command-and-control or denial of service |
| pfSense DMZ interface and subnet `10.0.1.0/24` | Web-facing services | Public exposure, web attacks, outbound connections, containment of the DMZ |
| Ubuntu web server `10.0.1.10` | Fictional public application | Web, operating-system, authentication, and application logs; preserve content and configuration state |
| pfSense internal interface and subnet `10.0.2.0/24` | User workstation zone | User activity, access to business data, malware, credential theft, and lateral movement |
| Windows workstation `10.0.2.10` | Fictional employee endpoint | Authentication, process, security, and endpoint telemetry; potential user and credential impact |
| pfSense management interface and subnet `10.0.3.0/24` | Restricted administration and monitoring | Protect the control plane and Wazuh; investigate privileged access and logging integrity |
| Wazuh `10.0.3.10` | Central security monitoring | Alert triage, endpoint telemetry, log retention, and detection of monitoring interruption |

The design assumes default-deny traffic between zones with explicitly approved paths. Proposed monitoring paths include agent or event forwarding to Wazuh on TCP 1514 and controlled agent enrollment on TCP 1515; any syslog or dashboard exposure must be explicitly scoped and restricted. These are design details, not evidence that the network or agents have been configured or tested. If Wazuh or the management zone may be compromised, responders must treat its alerts and stored logs as potentially incomplete or altered and seek independent firewall and endpoint records.

This is not an approved business continuity plan, legal opinion, forensic procedure, or service-provider contract. In a real deployment, validate system owners, data classes, retention, backup availability, escalation contacts, authorities, and jurisdictional requirements before relying on it.

## 3. Response principles and framework alignment

Responders should:

1. Protect life, safety, essential services, and sensitive information before restoring convenience.
2. Use the least disruptive containment that adequately limits harm; record the risk and approver for actions that may interrupt service or destroy volatile evidence.
3. Separate observed facts, hypotheses, decisions, and unknowns in every incident record.
4. Preserve original evidence, restrict access, hash collected files where practical, and record each transfer or transformation.
5. Use an out-of-band channel if corporate identity, email, chat, or the monitoring platform may be compromised.
6. Make external notifications and public statements through an authorized owner after legal, privacy, and business review; do not wait for perfect certainty when a reporting deadline may apply.
7. Recover from a known-good state, verify control operation, and obtain explicit business acceptance before declaring normal operations.

The workflow is intended to support risk-based incident handling and can be mapped to NIST CSF 2.0 Govern, Identify, Protect, Detect, Respond, and Recover outcomes, and to the organization's chosen ISO/IEC 27001 information-security controls. Incident-management procedures may also be mapped to the ISO/IEC 27035 series. A mapping describes intended alignment; it does not establish conformity, certification, or control effectiveness.

## 4. Incident types and initial response

| Incident type | Examples | First response focus |
|---|---|---|
| Phishing or credential compromise | Malicious link, token theft, unusual sign-in, unexpected MFA prompt | Preserve the message and authentication records; revoke sessions or credentials through a trusted admin path; identify affected accounts and subsequent access |
| Malware or ransomware | Malicious process, encryption, endpoint detection alert | Isolate affected endpoint or segment; protect backups and shared services; preserve volatile and disk evidence when feasible; do not reconnect until cleared |
| Web application compromise | Defacement, injection, unexpected files, anomalous web requests | Preserve web, reverse-proxy/firewall, application, and host logs; restrict affected route or server; assess data access and outbound activity |
| Denial of service or abuse | Service saturation, brute-force traffic, resource exhaustion | Confirm availability impact and traffic pattern; apply proportionate filtering or rate controls; preserve relevant flow and firewall telemetry |
| Data exposure or exfiltration | Publicly accessible data, unusual downloads, suspected transfer | Restrict exposure, preserve access/configuration logs, identify data types and likely subjects, engage privacy/legal review promptly |
| Privileged access or configuration misuse | Unapproved account, firewall rule, security-tool change | Protect administrative access, preserve change and identity logs, verify whether logging or recovery paths were altered |
| Lost device or removable media | Missing endpoint or storage | Revoke credentials/tokens, identify encryption and data stored, preserve access records, assess privacy and contractual impact |
| Supplier or cloud-service incident | Provider advisory, lost telemetry, compromised integration | Confirm affected service, tenant, data, and time window; invoke contractual contacts and evidence-retention requests; assess dependent services |

Threat vectors include web and email delivery, credential abuse, exploitation of exposed services, removable media, misconfiguration, insider misuse, lost equipment, and supplier compromise. A threat vector is a starting hypothesis, not a conclusion about cause.

## 5. Roles, authority, and contacts

The fictional lab has no named on-call staff. Before using this plan operationally, fill the contact register and ensure a backup for every decision role. Keep a controlled copy accessible if the primary identity or collaboration service is unavailable.

| Role | Core responsibilities | Decision authority |
|---|---|---|
| Reporter / service desk | Record initial report, preserve original message or alert, avoid unnecessary system changes, and reach the incident lead | May raise an incident at any time; does not close or downgrade it |
| Incident Manager | Coordinate response, establish the incident record and timeline, assign owners, maintain situation reports, and convene decision-makers | Proposes severity and coordinates approved actions; may initiate pre-authorized low-impact containment |
| Technical Lead / responders | Scope systems, collect logs and artifacts, recommend containment, eradication, and recovery steps | Executes approved technical actions and records commands, outcomes, and exceptions |
| System or service owner | Explain business purpose, dependencies, data, recovery priority, and acceptable service impact | Accepts business risk and signs off service restoration for their system |
| Security / privacy / legal adviser | Assess information sensitivity, evidence handling, applicable reporting, contracts, privilege, and notification content | Advises on legal/privacy duties; authorized organizational officer approves external notifications |
| Communications lead | Prepare internal and external messages from confirmed facts; track recipients and updates | Releases only messages approved by the designated executive and legal/privacy adviser |
| Executive decision group | Set business priorities, resources, risk appetite, customer posture, and crisis direction | Approves high-impact service decisions, material risk acceptance, and public positions |
| Supplier coordinator | Contact provider, preserve contractual and technical evidence, track provider actions and dependencies | Escalates under the service agreement; cannot accept risk for the service owner |

One person may fill multiple roles in a small exercise, but the incident record must show which role they were acting in. Avoid having a responder independently approve their own material risk acceptance or declare their own recovery evidence sufficient.

### Contact register to complete before operational use

| Contact | Primary | Backup | Secure channel / out-of-band method | Last verified |
|---|---|---|---|---|
| Incident Manager | To be assigned | To be assigned | To be confirmed | Not verified |
| Technical Lead / SOC | To be assigned | To be assigned | To be confirmed | Not verified |
| Executive decision-maker | To be assigned | To be assigned | To be confirmed | Not verified |
| Privacy / legal adviser | To be assigned | To be assigned | To be confirmed | Not verified |
| Communications lead | To be assigned | To be assigned | To be confirmed | Not verified |
| Internet, cloud, and security providers | To be assigned | To be assigned | Contract-specific | Not verified |
| Applicable regulator / national CSIRT | Maintain in controlled jurisdiction register | Backup contact path | Verify at incident time | Not verified |

## 6. Severity and activation

Assign initial severity using business impact, not alert criticality alone. Consider confidentiality, integrity, availability, safety, legal exposure, customer impact, financial loss, duration, spread, and confidence in the facts. If dimensions differ, use the highest credible impact and revisit as evidence changes. Record the rationale and the next review time.

| Severity | Working definition | Response posture |
|---|---|---|
| Critical | Essential service unavailable; management plane or multiple zones plausibly controlled; confirmed or credible sensitive-data exposure at material scale; serious safety or legal consequences | Activate full response and executive decision group immediately; use out-of-band communications; consider crisis and provider support |
| High | Confirmed compromise of a production-facing system or privileged account; likely data exposure; malware with plausible lateral movement; serious service degradation | Activate core response team promptly; notify executive and advisers; increase situation-report frequency |
| Medium | Limited system or account compromise, suspicious activity with bounded scope, or contained event with uncertain data impact | Partial response; assign investigation owner and decision checkpoints; escalate if scope or impact grows |
| Low | Isolated policy or technical event with no current evidence of compromise or material impact | Handle through standard operations with a recorded rationale; escalate on new evidence |

The Incident Manager may activate the response team for any credible suspected incident. A responder must not wait for a complete root-cause analysis before raising a high-impact concern. The executive decision group is convened for Critical incidents and for High incidents involving sensitive data, customer impact, major business interruption, or significant external obligations. The service owner and privacy/legal adviser may be brought in at any severity when relevant. De-escalation requires a recorded explanation and approval by the Incident Manager plus the affected service owner; Critical cases also require executive agreement.

## 7. Intake, triage, and investigation

### Initial report

Capture what the reporter observed, when and how they noticed it, affected account/system/service, current operational impact, actions already taken, and a safe callback method. Preserve the original alert, message, URL, screenshot, or provider advisory where appropriate. Do not ask the reporter to investigate or forward suspected malware through ordinary channels.

### First-hour decision record

The Incident Manager opens a unique incident ID and records:

- detection time, report time, time zone, source, and confidence;
- observed facts versus hypotheses, initial incident type, and severity rationale;
- affected and potentially affected zones, accounts, data, users, suppliers, and service dependencies;
- whether the incident is active, spreading, or disrupting service;
- immediate safety, privacy, legal, contractual, and financial questions;
- actions taken, who authorized them, and known side effects;
- next owner, next decision point, and next update time.

### Investigation questions

Use questions to guide evidence collection; unanswered items remain explicitly unknown:

1. What was the first reliable indicator and the earliest known time of suspicious activity?
2. What initial access path is supported by evidence: web, email, exposed service, account, supplier, device, or configuration?
3. Which hosts, accounts, subnets, applications, identities, and data are affected or potentially affected?
4. Is there evidence of privilege escalation, persistence, lateral movement, command-and-control, or additional access?
5. Were security controls, clocks, agents, logs, backups, or administrative accounts changed or disabled?
6. Was information viewed, altered, encrypted, copied, or transferred? What data class and approximate volume are in scope?
7. What is the current service and customer impact, and which dependencies could extend it?
8. What evidence would confirm containment, eradication, and safe recovery?
9. Which external parties must be consulted, and what reporting or contractual time limits may apply?

### Lab telemetry sources to consider

The proposed design offers pfSense firewall and DHCP records, Ubuntu authentication/system/web/application logs, Windows security and process events, and Wazuh alerts/agent status. Investigators should verify time synchronization, retention, collection coverage, and source integrity before drawing conclusions. The existence of a proposed source in this document does not mean its logging has been configured or its events have been collected.

## 8. Containment, evidence, and remediation

### Containment decisions

The Technical Lead recommends containment options and explains expected risk, service impact, evidence effect, and rollback path. The Incident Manager approves actions within delegated authority; the service owner approves material service interruption, and executive approval is required where the action could affect critical business operations. For an immediate threat, a responder may take a pre-authorized emergency action and notify the Incident Manager as soon as safe, recording the reason and time.

Possible actions include disabling a compromised account and revoking sessions, isolating a host, restricting a firewall rule or web route, blocking a verified indicator, disabling a vulnerable integration, or pausing a supplier connection. Avoid broad blocks based on unverified indicators. Do not power off or wipe a suspected system until the evidence value and safety impact have been considered, unless continued operation creates unacceptable harm.

### Evidence handling

1. Assign an evidence ID and record the incident ID, collector, source, acquisition method, date/time and time zone, system identity, and reason for collection.
2. Record the original filename, size, relevant device identifiers, source and destination, and any tool/version used. Capture volatile data only when trained responders can do so safely and the expected value justifies the impact.
3. Preserve the original read-only where practical. Calculate a cryptographic hash, such as SHA-256, for collected files and verify it after transfer. A hash supports integrity checking; it does not prove source authenticity or completeness.
4. Store evidence in an access-controlled location with encryption, backup, and an access log. Do not place sensitive incident evidence in public repositories or general chat.
5. For every transfer, copy, conversion, redaction, or analysis, record who handled it, when, why, and the resulting evidence ID/hash. Keep working copies separate from originals.
6. Follow approved retention, privacy, legal hold, and deletion rules. Escalate uncertain evidentiary requirements to the legal adviser before altering or disposing of material.

If the monitoring plane is suspect, obtain independent copies from firewall and endpoint sources, the platform provider, or a trusted acquisition path. Record collection limitations and gaps.

### Remediation action register

Every action has a unique ID, linked finding/evidence, priority, owner, approver, target date, current status, validation method, result, and closure authority. Status values are **Open**, **In progress**, **Blocked**, **Implemented—verification pending**, and **Closed—verified**. The action owner may provide implementation evidence; a separate reviewer should verify high-risk remediation. A plan or intended control is not closure evidence.

## 9. Communications and notifications

The Incident Manager maintains a single approved situation report. Internal updates state what is known, what remains uncertain, business impact, actions, decisions needed, and the next update time. Use a trusted out-of-band channel if identity or messaging systems may be affected. Staff should preserve relevant evidence, follow approved workarounds, and direct enquiries to the named communications lead.

External messages are coordinated by the communications lead with the executive decision-maker and legal/privacy adviser. Share only verified, necessary information. Record what was sent, to whom, by whom, when, through which channel, and the basis for the decision. Do not promise a resolution time or describe a breach as confirmed or ruled out without supporting evidence.

### Notification and jurisdiction review

At triage, the privacy/legal adviser records the potentially applicable jurisdictions, entity type, affected data, incident category, contractual commitments, regulator/sector contacts, reporting threshold, decision owner, and the source/date checked. Recheck current requirements for the specific facts; do not rely on the illustrative plan as a legal determination.

For an India-based organization, the review should determine whether the incident falls within current CERT-In reporting directions and whether other privacy, sectoral, customer, law-enforcement, or contractual notifications apply. CERT-In directions include a six-hour reporting requirement for covered entities and listed incident categories; the adviser must confirm applicability, the triggering time, and the current reporting process for the incident. Consult the current official [CERT-In directions and reporting information](https://www.cert-in.org.in/Directions70B.jsp). Record the decision and evidence even when no external notification is made. Do not let confidentiality language delay a notification that the adviser determines is legally required.

## 10. Recovery and return to service

Recovery starts only after the Incident Manager and Technical Lead agree that containment is adequate for the recovery action. The service owner identifies business priorities and acceptable interim service. Responders should:

1. Identify the likely persistence and entry path and address them before reconnecting systems.
2. Select a known-good image or backup and verify its provenance, integrity, and recovery point. Treat untested backup availability as unknown.
3. Rebuild or restore in a controlled segment; rotate exposed credentials, keys, certificates, and tokens through trusted administration paths.
4. Apply required security updates and configurations, restore monitoring, and confirm logs reach an independent or protected destination.
5. Validate authentication, network segmentation, critical application behavior, data integrity, backup status, and detection coverage against documented acceptance checks.
6. Obtain technical verification and explicit service-owner acceptance. Record residual risks, compensating controls, monitoring duration, and rollback trigger.
7. Monitor for recurrence and unusual activity for a period set by the Incident Manager and Technical Lead based on the incident, then record the review date.

Do not state that a system is recovered solely because it responds to a network check. Recovery targets and timeframes must come from an approved continuity analysis and tested recovery capability; none are asserted here.

## 11. Post-incident review and continuous improvement

After containment and immediate recovery, the Incident Manager schedules a review proportionate to severity. The review examines the timeline, people and decision roles, process and authority, organizational coordination, supporting facilities and providers, technology and controls, training, and exercise design where relevant. It asks what happened, why defenses did or did not prevent it, how it was detected, what delayed or improved response, how well communication worked, and what will reduce recurrence or impact.

The review separates established cause from unresolved hypotheses and records evidence for conclusions. Each recommendation enters the action register with an accountable owner, target date, priority, and objective validation. Update this plan, playbooks, contact register, detection logic, and training materials after material changes. Exercise revisions through a discussion-based tabletop before relying on them operationally.

## 12. Supporting procedures and readiness

This plan should be paired with maintained procedures for event intake, triage and severity, identity compromise, endpoint isolation and acquisition, firewall change control, backup restoration, business continuity, supplier incident escalation, evidence storage, privacy assessment, external communication, and recovery verification. Supporting playbooks must name decision points and rollback conditions, not just commands.

Before operational use, confirm that:

- the incident and executive contacts, alternates, and out-of-band channels are current and reachable;
- critical systems, owners, dependencies, data classes, and recovery priorities are documented;
- logging sources, time synchronization, retention, and protected evidence storage have been configured and tested;
- responder authority for account disabling, system isolation, firewall changes, and restoration is approved;
- service-provider contacts, evidence access, incident notification, and cooperation terms are available;
- legal/privacy reporting requirements and decision ownership are recorded for relevant jurisdictions;
- recovery backups can be restored and validated, and business owners know their acceptance role;
- incident records and action tracking are accessible during an outage;
- responders have practiced the plan and understand where to find current playbooks.

## Appendix A. Situation report

| Field | Entry |
|---|---|
| Incident ID / title |  |
| Report author and role |  |
| Report time and time zone |  |
| First detected / reported |  |
| Status and severity |  |
| Incident type |  |
| Confirmed facts |  |
| Unknowns / working hypotheses |  |
| Affected systems, zones, accounts, data, services |  |
| Business and customer impact |  |
| Containment and investigation actions |  |
| Decisions made, approver, rationale |  |
| Notifications sent / pending / decision owner |  |
| Assistance required |  |
| Current risks and blockers |  |
| Next actions and owners |  |
| Next update due |  |

## Appendix B. Incident log

| Timestamp and time zone | Actor / role | Fact, action, or decision | System / evidence ID | Rationale / impact | Approver | Outcome / next step |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Use one row per material observation, action, decision, or communication. Preserve original entries; correct errors with a new timestamped note.

## Appendix C. Evidence register

| Evidence ID | Source / system | Item and collection method | Collector / time zone | Original location | Hash / verification | Storage location and access | Transfers / transformations | Limitations |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Appendix D. Remediation and improvement register

| Action ID | Linked incident / finding | Action and expected risk reduction | Owner | Approver | Due date | Status | Validation evidence / reviewer | Closure date |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | Open |  |  |

## Appendix E. Post-incident review prompts

| Area | Review questions |
|---|---|
| Timeline and impact | When did activity begin, become detectable, get reported, get contained, and recover? Which services, users, and data were affected? |
| Protection | Which preventive controls were expected to help? Did they work as designed, and what evidence supports that assessment? |
| Detection | Which signals identified the event? Were logs complete and timely? What would reduce time to detect? |
| Response | Were roles, authority, escalation, containment, evidence handling, and communications effective? What caused delay or unnecessary impact? |
| Recovery | Was the source understood and removed? Were backup and control checks successful? Who accepted remaining risk? |
| People and organization | Were skills, staffing, supplier support, decision paths, and executive oversight adequate? |
| Process and technology | Which plans, tools, configurations, dependencies, and training need a specific change? |
| Actions | What measurable change will prevent recurrence, improve detection, reduce impact, or shorten recovery? Who owns and verifies it? |
