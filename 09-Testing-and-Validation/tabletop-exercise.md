# Tabletop Exercise Scenario

## Exercise status

This is a proposed discussion-based exercise for the fictional Apex Capital lab. It has not been conducted. The scenario and injects are fictional; the prompts do not represent observed telemetry, an actual compromise, a test result, or participant feedback. Complete the attendance, decision, observation, and action records during a future facilitated session.

## Exercise at a glance

| Item | Design |
|---|---|
| Objective | Practice incident intake, severity assignment, evidence-aware containment, executive communication, privacy/legal escalation, supplier coordination, and recovery acceptance |
| Format | Facilitated tabletop; no system changes or live attack activity |
| Suggested duration | 60–75 minutes, plus a short debrief |
| Participants | Incident Manager, technical responder, Ubuntu service owner, Windows endpoint owner, privacy/legal adviser, communications lead, executive decision-maker, supplier coordinator, facilitator, and observer |
| Environment model | pfSense separating WAN, DMZ (`10.0.1.0/24`), internal (`10.0.2.0/24`), and management (`10.0.3.0/24`); Ubuntu web server, Windows workstation, Wazuh |
| Materials | Current incident response plan, blank situation report, incident log, evidence register, action register, and fictional service/contact map |
| Safety boundary | Use discussion only. Do not send real notifications, contact actual providers, block live addresses, isolate systems, or share personal data. |

## Exercise objectives and observations

The facilitator records whether the team can:

1. Open an incident record with times, facts, hypotheses, impact, and an assigned lead.
2. Select and explain a severity, escalation path, and next decision time as information changes.
3. Choose containment that limits spread while considering service impact and evidence preservation.
4. Identify which independent sources could establish scope if the monitoring plane is incomplete.
5. Assign legal/privacy and supplier decisions without inventing a reporting conclusion or deadline.
6. Give executives and staff a clear update that separates known facts from unknowns.
7. Define recovery acceptance checks and name the owner who must approve return to service.
8. Convert observations into owned, dated, verifiable improvement actions.

The observer uses **Demonstrated**, **Partly demonstrated**, **Not demonstrated**, or **Not observed**. Capture the supporting decision, record, or statement; a score without evidence is not useful.

## Scenario background

The fictional Apex web service is hosted on Ubuntu in the DMZ. A Windows workstation is used by an employee who administers content through a restricted workflow. Wazuh is intended to receive endpoint events in the management zone. Firewall policy is intended to deny unsolicited traffic between zones. No actual service-level objective, customer count, data inventory, backup recovery point, or named supplier contact is supplied; exercise participants should identify these as information gaps rather than assume values.

### Inject 1 — unusual web activity

**Facilitator release:** The service owner reports an unexpected change to a public web page. A Wazuh alert shows repeated web-server errors and a new process on the Ubuntu host. The alert time and the host's local timestamp differ. The service remains reachable. No reliable evidence yet identifies who made the change or whether data was accessed.

**Prompts:**

- Who opens the incident, sets the initial severity, and owns the timeline?
- Which facts and unknowns are recorded? What time source and time zone will be used?
- What evidence should be preserved from Wazuh, Ubuntu, web/application logs, and pfSense before remediation?
- Would you isolate the host, restrict only the web route, or observe briefly? Who approves the service impact and why?
- What initial message can be sent to the service owner and executive without overstating the event?

**Expected decisions to observe:** An incident ID and owner; explicit severity rationale; preservation plan; containment choice with approver, effect, and review time; clear separation of confirmed defacement from unconfirmed data access.

### Inject 2 — possible credential misuse and monitoring gap

**Facilitator release:** The content administrator reports an unexpected sign-in prompt and a successful login they do not recognize. The Windows endpoint has a new scheduled-task alert. Wazuh has not received events from that endpoint for 40 minutes. The firewall record shows a connection from the internal zone toward the DMZ, but the destination is not yet confirmed as authorized.

**Prompts:**

- Which accounts and sessions should be protected, and through what trusted administrative path?
- What independent records can help determine whether the endpoint, web server, or management plane is affected?
- What conditions would cause escalation to High or Critical? Could lateral movement be confirmed from current facts?
- How will responders preserve endpoint, identity, firewall, and agent-health evidence?
- What business decision is needed before isolating the endpoint or disrupting content publishing?

**Expected decisions to observe:** Containment protects credentials without relying on a possibly compromised session; monitoring loss is treated as a coverage gap; the team seeks independent logs; severity is updated only with a recorded rationale; endpoint isolation authority and business impact are explicit.

### Inject 3 — provider notification and potential data exposure

**Facilitator release:** A fictional hosting provider sends an advisory that a shared management component may have exposed customer metadata. The notice does not confirm that Apex data was accessed. The provider can preserve tenant-specific logs only if requested promptly. The service owner cannot determine which metadata fields are stored without checking the data inventory.

**Prompts:**

- Who contacts the provider, preserves the notice, and requests tenant-specific logs and retention?
- What data inventory, access logs, contracts, and service dependencies must be checked?
- Who determines whether privacy, regulatory, contractual, or customer notification thresholds are met, and what facts are needed?
- If India-based reporting obligations may apply, who checks the current rule and incident category, calculates the trigger from verified facts, and records the decision?
- What can be communicated internally while data exposure remains unconfirmed?

**Expected decisions to observe:** The provider's statement is not treated as proof or exoneration; evidence and retention requests are assigned; a named privacy/legal decision owner is engaged; the team checks current applicable requirements and records the basis for notifying or not notifying; communications distinguish exposure from potential exposure.

### Inject 4 — restoration pressure

**Facilitator release:** The business asks to restore the public page immediately. The technical team has a backup from an unknown point in time, has not verified its integrity, and has not identified how the administrator account was misused. Wazuh forwarding is still unavailable for the Windows endpoint.

**Prompts:**

- What minimum conditions must be met before rebuilding or reconnecting the web server?
- How will the team select and validate a clean image or backup?
- Which credentials, tokens, or keys may require rotation? How can this be done without trusting a suspected endpoint?
- What tests demonstrate that segmentation, authentication, logging, data integrity, and monitoring work after restoration?
- Who accepts the residual risk and authorizes return to service? What rollback trigger and heightened monitoring period are appropriate?

**Expected decisions to observe:** The team does not equate availability with recovery; it identifies root-cause and clean-state questions, assigns verification evidence, identifies an independent reviewer and service-owner acceptance, records residual risk and rollback criteria, and communicates a realistic next update.

## Facilitator notes

- Release one inject at a time and allow the group to state decisions before revealing the next fact.
- Do not supply missing architecture, contacts, log contents, or legal conclusions. Ask participants how they would obtain and verify them.
- If participants propose an action that changes a real system, stop the discussion and remind them this is a no-action tabletop.
- Capture the exact decision, responsible role, evidence requested, approval needed, unresolved question, and time at which the team expects to revisit it.
- Where the group lacks an owner or procedure, record a gap rather than resolving it by facilitator assumption.

## Exercise record

| Field | Entry |
|---|---|
| Facilitator / observer |  |
| Date and duration |  |
| Participants and roles |  |
| Plan version used |  |
| Scenario changes |  |
| Overall objective results |  |

### Observation log

| Objective | Demonstrated / partly / not / not observed | Supporting decision or artifact | Gap / contributing factor |
|---|---|---|---|
| Incident intake and timeline |  |  |  |
| Severity and escalation |  |  |  |
| Containment and evidence |  |  |  |
| Scope and independent telemetry |  |  |  |
| Legal, privacy, supplier coordination |  |  |  |
| Communications |  |  |  |
| Recovery acceptance |  |  |  |
| Improvement actions |  |  |  |

### Improvement action register

| ID | Observed gap | Corrective action | Owner | Due date | Verification evidence | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | Open |

## Debrief

Discuss which decisions were clear, which depended on missing information, and where authority or evidence paths were uncertain. Review preparation, role coverage, process, organization, support arrangements, technology, training, and exercise design. Record successful practices as well as gaps. Assign each action to an owner and verify it through an artifact, retest, or follow-up exercise; do not mark improvement complete because a meeting agreed with it.
