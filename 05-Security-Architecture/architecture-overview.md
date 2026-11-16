> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Security Architecture Overview

## Design Principles

- Defense-in-Depth
- Network Segmentation (Zero Trust inspired)
- Least Privilege
- Centralized Logging & Monitoring
- Auditability and Compliance Evidence

---

## 4-VM Architecture

| VM | Hostname | IP Address | Subnet | Role |
|----|----------|------------|--------|------|
| VM 1 | Windows-Enterprise | 10.0.2.10 | Internal (10.0.2.0/24) | Workstation / Server |
| VM 2 | Ubuntu-Web | 10.0.1.10 | DMZ (10.0.1.0/24) | Public Web Server |
| VM 3 | pfSense | 10.0.1.1, 10.0.2.1, 10.0.3.1 | All | Firewall / Router |
| VM 4 | Wazuh-SIEM | 10.0.3.10 | Management (10.0.3.0/24) | SIEM / Monitoring |

---

## pfSense Interface Configuration

| Interface | Name | IP Address | Subnet | Connected system |
|-----------|------|------------|--------|-------------------|
| WAN | Upstream isolated lab uplink | Assigned by lab network; unspecified | Outside lab zones | Virtual uplink, not a guest VM |
| OPT1 | DMZ | 10.0.1.1 | 10.0.1.0/24 | VM 2 (Ubuntu) |
| LAN | Internal | 10.0.2.1 | 10.0.2.0/24 | VM 1 (Windows) |
| OPT2 | Management | 10.0.3.1 | 10.0.3.0/24 | VM 4 (Wazuh) |

This is the proposed four-interface design. The upstream WAN address, virtual-switch attachment and NAT method remain unspecified. No running pfSense configuration has been inspected.
## Network Zones

The proposed design uses four pfSense interfaces: one upstream WAN uplink and three isolated zones. The WAN address/NAT is unspecified; this is not a captured pfSense configuration. The DMZ is not the WAN interface.

### 1. DMZ Zone (10.0.1.0/24)
- **VM 2 - Ubuntu Web Server** (Customer Investment Portal)
- Simulated public-facing service; external exposure requires explicit isolated-lab NAT/port-forward
- Only ports 80 (HTTP) and 443 (HTTPS) are open
- SSH access restricted to Management Zone only

### 2. Internal Trusted Zone (10.0.2.0/24)
- **VM 1 - Windows Enterprise** (Workstation / Server)
- No direct internet access
- RDP (3389) blocked from DMZ and internet
- RDP only allowed from Management Zone

### 3. Management Zone (10.0.3.0/24)
- **VM 4 - Wazuh SIEM** (Monitoring and Alerting)
- Centralized log collection
- Administrative access point
- Can initiate RDP to Windows and SSH to Ubuntu

---

## Traffic Flow

The network-architecture.mermaid file in this section provides the proposed logical topology. The permitted flows below are design intent only.

| Source | Destination | Protocol / port | Policy intent |
|---|---|---|---|
| WAN uplink | Ubuntu DMZ | TCP 80/443 through explicit port-forward only | Optional simulated web exposure; never expose management ports |
| Approved admin source in management zone | Ubuntu DMZ | TCP 22 | Restrict SSH to approved administrators |
| Approved admin source in management zone | Windows internal | TCP 3389 | Restrict RDP to approved administrators |
| Windows and Ubuntu endpoints | Wazuh management | TCP 1514 | Endpoint-initiated Wazuh agent telemetry |
| Endpoints during controlled enrollment | Wazuh management | TCP 1515 | Temporary/restricted agent enrollment only |
| pfSense | Wazuh management | UDP 514, if syslog collection is enabled | Optional firewall log forwarding; collector is disabled by default |
| Approved admin sources | Wazuh management | TCP 443 | Restricted dashboard access |
| DMZ | Internal | Any | Deny by default; verify with paired tests |
| Internal/management | WAN | Explicitly defined outbound services only | Egress must be deliberately scoped |

pfSense state handling, rule order, NAT, logging and source limits must be checked against the eventual configuration. A subnet label does not grant every host administrative access.
## Firewall Rules Summary

Rules are design intent and require implementation and validation. Apply them to the correct pfSense interface, account for stateful return traffic, and keep management access limited to approved source hosts.

### WAN uplink

| Source | Destination | Service | Intended action |
|---|---|---|---|
| External test source | Ubuntu DMZ | TCP 80/443 via explicit NAT/port-forward | Optional allow only for an isolated lab; no WAN-to-admin access |
| Any | Firewall management interfaces | Any | Deny |

### DMZ / OPT1

| Source | Destination | Service | Intended action |
|---|---|---|---|
| Approved management source | Ubuntu DMZ | TCP 22 | Allow |
| DMZ subnet | Internal subnet | Any | Deny |
| Ubuntu endpoint | Wazuh management | TCP 1514 | Allow agent telemetry |
| Ubuntu endpoint | Wazuh management | TCP 1515 | Allow only during controlled enrollment |
| DMZ | Other zones | Any | Deny unless explicitly listed |

### Internal / LAN

| Source | Destination | Service | Intended action |
|---|---|---|---|
| Approved management source | Windows host | TCP 3389 | Allow |
| Windows endpoint | Wazuh management | TCP 1514 | Allow agent telemetry |
| Windows endpoint | Wazuh management | TCP 1515 | Allow only during controlled enrollment |
| Windows host | WAN | Required update destinations/services only | Proposed egress; define before use |
| Internal | DMZ/management | Any | Deny unless explicitly listed |

### Management / OPT2

| Source | Destination | Service | Intended action |
|---|---|---|---|
| Approved management source | Windows host | TCP 3389 | Allow |
| Approved management source | Ubuntu DMZ | TCP 22 | Allow |
| Approved management source | Wazuh dashboard | TCP 443 | Allow |
| pfSense | Wazuh management | UDP 514 | Optional syslog only when configured |
| Any other source | Management zone | Any | Deny by default |

Wazuh default ports: TCP 1514 for agent communication; TCP 1515 for enrollment. UDP 514 syslog collection is optional and disabled by default. Confirm the installed version and service configuration before creating rules.
## Key Protection Goals

| Goal | Implementation | Validation |
|------|----------------|------------|
| **Prevent lateral movement** | pfSense block rule: DMZ to Internal | `nc -zv` from Ubuntu to Windows fails |
| **Protect client data at rest** | NTFS permissions, Windows policy | Access control verification |
| **Protect data in transit (design intent)** | TLS/SSH configured to approved protocol/cipher baselines | Review negotiated protocol/cipher and certificate chain; verify by test |
| **Enable secure remote access** | RDP only from Management subnet | RDP from Management works, from internet fails |
| **Support rapid detection** | Wazuh SIEM alerting intent | Validate receipt, parsing, rule match, timestamp, and measured latency |
| **Support rapid response** | Incident response policy | Documented IR plan |

---

## Logging and Monitoring Flow

| Source | Destination | Flow |
|---|---|---|
| Windows endpoint | Wazuh server (10.0.3.10) | Agent connection to TCP 1514 |
| Ubuntu endpoint | Wazuh server (10.0.3.10) | Agent connection to TCP 1514 |
| Endpoint during enrollment | Wazuh server (10.0.3.10) | TCP 1515 only during controlled enrollment |
| pfSense | Wazuh server (10.0.3.10) | Optional syslog to UDP 514 after explicitly enabling collection |
| Approved management sources | Wazuh dashboard | HTTPS TCP 443, restricted by source policy |

These flows describe a proposed design, not observed telemetry or an operational alerting pipeline. Validate event receipt, parsing, timestamps, retention, alert rules and measured latency before claiming monitoring coverage.
## Key Protection Goals

- Prevent lateral movement between DMZ and Internal zones

- Protect client data at rest and in transit

- Enable secure remote access (RDP restricted to Management subnet)

- Support rapid detection and response via Wazuh SIEM

---

**End of Security Architecture Overview**
