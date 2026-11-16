> **Publication status:** Fictional public lab scenario. This chapter preserves source material for completeness. Configurations and test procedures are proposed; results are expected outcomes, not executed evidence. No real client, engagement, approval, compliance opinion or control effectiveness is asserted. Organization, workforce, data and regulatory details are hypothetical planning assumptions.

# Ubuntu Web Server Hardening

**Last Updated:** May 2026
**Version:** 1.0
**VM Role:** Public-facing customer investment portal (DMZ Asset)
**Classification:** Internal
**IP Address:** 10.0.1.10
**Subnet:** 10.0.1.0/24 (DMZ)

---

## 1. Framework References

| Framework | Control Reference | Control Description |
|-----------|-------------------|---------------------|
| NIST CSF 2.0 | PR.AA-03 | User, device, and other asset authentication |
| NIST CSF 2.0 | DE.CM-09 | Malware protection is Proposed |
| NIST CSF 2.0 | PR.DS-2 | Data-in-transit is protected |
| ISO 27001:2022 | A.8.8 | Management of technical vulnerabilities |
| ISO 27001:2022 | A.8.20 | Networks security |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 2 | Do not use vendor-supplied defaults |
| Historical PCI DSS 3.2.1-inspired reference (not current compliance) | Requirement 4 | Encrypt transmission of cardholder data |

**External References:**
- CIS Ubuntu Linux 22.04 LTS Benchmark
- Ubuntu Security Documentation: https://ubuntu.com/security
- OWASP Web Security Guidelines

---

## 2. Purpose

The Ubuntu web server hosts Apex Capital's customer investment portal, a public-facing asset accessible from the internet. Maximum hardening is applied to reduce attack surface, prevent unauthorized access, and protect client data.

**Risk Addressed:** R-005 (Web Server Breach), R-001 (Lateral Movement)

**Threat Model:** Public internet exposure — maximum hardening applied.

---

## 3. System Information

| Attribute | Value |
|-----------|-------|
| Operating System | Ubuntu 22.04.5 LTS (Jammy Jellyfish) |
| Kernel Version | 5.15.0-91-generic |
| Web Server | Nginx 1.18.0 |
| SSH Version | OpenSSH 8.9p1 |
| Firewall | UFW (Uncomplicated Firewall) |
| Monitoring | Wazuh Agent 4.9.0 |

---

## 4. OS Hardening

### 4.1 Minimal Installation

| Check | Command | Expected Result |
|-------|---------|-----------------|
| Unnecessary packages removed | `dpkg -l telnet ftp sendmail rsh-server` | Each package shows `un` (not installed) |
| Minimal package set | `apt list --installed` | Review inventory and record the installed-package count |
| Remove compilers | `dpkg -l gcc g++` | Both packages show `un` (not installed) |

**Commands executed:**

sudo apt remove --purge telnet ftp rsh-server sendmail
sudo apt autoremove
sudo apt remove --purge gcc g++

### 4.2 Automatic Security Updates

| Setting | Value | Configuration File |
|---------|-------|-------------------|
| Automatic updates | Enabled | /etc/apt/apt.conf.d/20auto-upgrades |
| Security updates only | Yes | /etc/apt/apt.conf.d/50unattended-upgrades |
| Update frequency | Daily | Same file |
| Reboot after updates | Never (manual) | Same file |

**Configuration (/etc/apt/apt.conf.d/20auto-upgrades):**

APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
APT::Periodic::Unattended-Upgrade "1";

**Verification:**

sudo systemctl status unattended-upgrades
sudo cat /etc/apt/apt.conf.d/20auto-upgrades

### 4.3 Kernel Hardening (sysctl)

| Setting | Value | Purpose | File |
|---------|-------|---------|------|
| net.ipv4.tcp_syncookies | 1 | Prevent SYN flood attacks | /etc/sysctl.conf |
| net.ipv4.conf.all.rp_filter | 1 | Source address validation | /etc/sysctl.conf |
| net.ipv4.conf.default.rp_filter | 1 | Source address validation | /etc/sysctl.conf |
| net.ipv4.tcp_timestamps | 0 | Reduce information disclosure | /etc/sysctl.conf |
| net.ipv6.conf.all.disable_ipv6 | 1 | Disable IPv6 if not used | /etc/sysctl.conf |

**Apply settings:**

sudo sysctl -p

---

## 5. SSH Security Hardening

### 5.1 SSH Configuration (/etc/ssh/sshd_config)

| Setting | Value | Purpose |
|---------|-------|---------|
| PermitRootLogin | no | Prevent root login |
| PasswordAuthentication | no | Key-based authentication only |
| PubkeyAuthentication | yes | Enable SSH keys |
| ChallengeResponseAuthentication | no | Disable challenge-response |
| UsePAM | yes | Pluggable Authentication Modules |
| X11Forwarding | no | Disable X11 forwarding |
| MaxAuthTries | 3 | Limit authentication attempts |
| ClientAliveInterval | 300 | Disconnect idle sessions |
| ClientAliveCountMax | 2 | Maximum keepalive messages |
| AllowUsers | lab-user | Only allow specific user |
| Protocol | 2 | Use SSH protocol 2 only |

**Configuration file:**

sudo nano /etc/ssh/sshd_config

# Add or modify these lines:
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers lab-user
Protocol 2

**Restart SSH service:**

sudo systemctl restart sshd

### 5.2 SSH Key Authentication Setup

| Step | Command | Purpose |
|------|---------|---------|
| 1 | ssh-keygen -t rsa -b 4096 | Generate SSH key pair (on client) |
| 2 | ssh-copy-id lab-user@10.0.1.10 | Copy public key to server |
| 3 | ssh lab-user@10.0.1.10 | Test key-based login |

### 5.3 fail2ban Installation

| Step | Command |
|------|---------|
| 1 | sudo apt install fail2ban -y |
| 2 | sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local |
| 3 | sudo systemctl enable fail2ban |
| 4 | sudo systemctl start fail2ban |

**Verification:**

sudo fail2ban-client status sshd

---

## 6. Firewall Configuration (UFW)

### 6.1 UFW Rules

| Rule | Command | Purpose |
|------|---------|---------|
| Default deny incoming | sudo ufw default deny incoming | Block all by default |
| Default allow outgoing | sudo ufw default allow outgoing | Allow outbound traffic |
| Allow HTTP | sudo ufw allow 80/tcp | Web traffic |
| Allow HTTPS | sudo ufw allow 443/tcp | Encrypted web traffic |
| Allow SSH from management | sudo ufw allow from 10.0.3.0/24 to any port 22 | Management only |
| Deny all other | Implicit | Default deny |

**Complete UFW setup:**

sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow from 10.0.3.0/24 to any port 22
sudo ufw enable

**Verify UFW status:**

sudo ufw status verbose

**Expected output:**

Status: active
Default: deny (incoming), allow (outgoing), disabled (routed)
To                         Action      From
--                         ------      ----
80/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
22/tcp                     ALLOW IN    10.0.3.0/24

---

## 7. Web Server (Nginx) Hardening

### 7.1 Nginx Security Headers

| Header | Value | Purpose |
|--------|-------|---------|
| X-Frame-Options | DENY | Prevent clickjacking |
| X-Content-Type-Options | nosniff | Prevent MIME type sniffing |
| X-XSS-Protection | 1; mode=block | Cross-site scripting protection |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | Enforce HTTPS |
| Content-Security-Policy | default-src 'self' | Restrict content sources |

**Configuration (/etc/nginx/sites-available/default):**

add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'" always;

### 7.2 TLS/SSL Configuration

| Setting | Value | Purpose |
|---------|-------|---------|
| TLS version | TLS 1.2 and 1.3 only | Deprecate older protocols |
| Cipher suite | Modern ciphers only | Strong encryption |
| Session tickets | Disabled | Prevent replay attacks |
| OCSP stapling | Enabled | Certificate status checking |

**SSL configuration (/etc/nginx/sites-available/default):**

ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
ssl_prefer_server_ciphers off;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;

### 7.3 Nginx Hardening Settings

| Setting | Value | Purpose |
|---------|-------|---------|
| Server tokens | off | Hide Nginx version |
| Client max body size | 10M | Limit upload size |
| Disable directory listing | off | Prevent information disclosure |
| Timeout values | Reduced | Prevent slowloris attacks |

**Configuration (/etc/nginx/nginx.conf):**

server_tokens off;
client_max_body_size 10M;
sendfile on;
tcp_nopush on;
tcp_nodelay on;
keepalive_timeout 65;
types_hash_max_size 2048;

### 7.4 Verify Nginx Configuration

sudo nginx -t
sudo systemctl restart nginx

---

## 8. Web Application Security

### 8.1 Directory Structure

| Directory | Permissions | Purpose |
|-----------|-------------|---------|
| /var/www/html | 755 | Web root |
| /var/log/nginx | 640 | Log files |
| /etc/nginx | 755 | Configuration files |

**Apply permissions:**

sudo chmod 755 /var/www/html
sudo chown -R www-data:www-data /var/www/html

### 8.2 Disable Directory Listing

Ensure directory listing is disabled:

sudo sed -i 's/autoindex on/autoindex off/g' /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl reload nginx

### 8.3 Rate Limiting

**Rate limiting configuration (/etc/nginx/nginx.conf):**

limit_req_zone $binary_remote_addr zone=login:10m rate=5r/m;

**Apply to location (/etc/nginx/sites-available/default):**

location /login {
    limit_req zone=login burst=10 nodelay;
    proxy_pass http://localhost:8080;
}

---

## 9. Logging and Monitoring

### 9.1 Nginx Logging Configuration

| Log Type | Location | Retention |
|----------|----------|-----------|
| Access log | /var/log/nginx/access.log | 90 days |
| Error log | /var/log/nginx/error.log | 90 days |

**Configure log rotation (/etc/logrotate.d/nginx):**

/var/log/nginx/*.log {
    daily
    missingok
    rotate 90
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        systemctl reload nginx
    endscript
}

### 9.2 Wazuh Agent Installation

| Step | Command |
|------|---------|
| 1 | `curl -sSfo /tmp/WAZUH-GPG-KEY https://packages.wazuh.com/key/GPG-KEY-WAZUH && sudo apt-key add /tmp/WAZUH-GPG-KEY` |
| 2 | `sudo sh -c 'printf "%s\n" "deb https://packages.wazuh.com/4.x/apt/ stable main" > /etc/apt/sources.list.d/wazuh.list'` |
| 3 | sudo apt update |
| 4 | sudo apt install wazuh-agent -y |
| 5 | sudo systemctl enable wazuh-agent |
| 6 | sudo systemctl start wazuh-agent |

**Wazuh agent configuration (/var/ossec/etc/ossec.conf):**

<client>
    <server>
        <address>10.0.3.10</address>
        <port>1514</port>
        <protocol>tcp</protocol>
    </server>
</client>

### 9.3 Auditd Configuration

| Setting | Value | Purpose |
|---------|-------|---------|
| Monitor SSH config | -w /etc/ssh/sshd_config -p wa -k ssh_changes | Detect SSH config changes |
| Monitor web config | -w /etc/nginx -p wa -k nginx_changes | Detect web config changes |
| Monitor binaries | -w /usr/sbin/nginx -p x -k nginx_exec | Detect nginx execution |

**Configure auditd:**

sudo auditctl -w /etc/ssh/sshd_config -p wa -k ssh_changes
sudo auditctl -w /etc/nginx -p wa -k nginx_changes
sudo auditctl -w /usr/sbin/nginx -p x -k nginx_exec

---

## 10. System Monitoring Commands

| Command | Purpose | Frequency |
|---------|---------|-----------|
| sudo ufw status | Check firewall rules | Weekly |
| sudo fail2ban-client status sshd | Check fail2ban status | Weekly |
| sudo systemctl status nginx | Check web server status | Daily |
| sudo tail -f /var/log/nginx/access.log | Monitor access logs | Real-time |
| sudo tail -f /var/log/nginx/error.log | Monitor error logs | Real-time |
| sudo journalctl -u sshd | Check SSH logs | As needed |
| sudo wazuh-agent -f | Test Wazuh connectivity | As needed |

---

## 11. Hardening Checklist

| Check | Verification command | Execution status | Evidence |
|-------|----------------------|------------------|----------|
| No unnecessary packages | `dpkg -l telnet ftp` | Not run | Not collected |
| Automatic updates enabled | `systemctl status unattended-upgrades` | Not run | Not collected |
| SSH password auth disabled | `grep PasswordAuthentication /etc/ssh/sshd_config` | Not run | Not collected |
| SSH root login disabled | `grep PermitRootLogin /etc/ssh/sshd_config` | Not run | Not collected |
| fail2ban installed | `systemctl status fail2ban` | Not run | Not collected |
| UFW configured | `ufw status verbose` | Not run | Not collected |
| Nginx security headers | `curl -I https://10.0.1.10` | Not run | Not collected |
| TLS 1.2 or 1.3 only | `nmap --script ssl-enum-ciphers -p 443 10.0.1.10` | Not run | Not collected |
| Server tokens off | `grep -n '^server_tokens off;' /etc/nginx/nginx.conf` | Not run | Not collected |
| Directory listing disabled | `curl https://10.0.1.10/images/` | Not run | Not collected |
| Wazuh agent installed | `systemctl status wazuh-agent` | Not run | Not collected |
| Auditd configured | `auditctl -l` | Not run | Not collected |

---

## 12. Evidence Collection

| Evidence ID | Description | Command / Location | Status |
|-------------|-------------|--------------------|--------|
| EV-001 | OS version and kernel | cat /etc/os-release | Pending |
| EV-002 | UFW status | sudo ufw status verbose | Pending |
| EV-003 | SSH configuration | cat /etc/ssh/sshd_config | Pending |
| EV-004 | Nginx security headers | curl -I https://10.0.1.10 | Pending |
| EV-005 | TLS configuration | nmap --script ssl-enum-ciphers -p 443 10.0.1.10 | Pending |
| EV-006 | fail2ban status | sudo fail2ban-client status sshd | Pending |
| EV-007 | Wazuh agent status | sudo systemctl status wazuh-agent | Pending |
| EV-008 | Automatic updates status | sudo systemctl status unattended-upgrades | Pending |
| EV-009 | Auditd rules | sudo auditctl -l | Pending |
| EV-010 | Nginx error log | sudo tail -20 /var/log/nginx/error.log | Pending |

---

## 13. Security Validation Tests

### 13.1 SSH Security Test

| Test | Command | Expected Result | Execution status / evidence (not run) |
|------|---------|-----------------|---------------|
| Password auth attempt | ssh lab-user@10.0.1.10 | Permission denied (publickey) | Pending |
| Root login attempt | ssh root@10.0.1.10 | Permission denied | Pending |
| fail2ban test | Try 3 wrong passwords | IP banned after 3 attempts | Pending |

### 13.2 Firewall Test

| Test | Command | Expected Result | Execution status / evidence (not run) |
|------|---------|-----------------|---------------|
| HTTPS access | curl -I https://10.0.1.10 | HTTP 200 OK | Pending |
| HTTP access | curl -I http://10.0.1.10 | HTTP 200 OK (redirects to HTTPS) | Pending |
| SSH from non-management | ssh lab-user@10.0.1.10 from 10.0.2.0/24 | Timeout or refused | Pending |

### 13.3 Web Server Test

| Test | Command | Expected Result | Execution status / evidence (not run) |
|------|---------|-----------------|---------------|
| TLS version check | nmap --script ssl-enum-ciphers -p 443 10.0.1.10 | TLS 1.2 and 1.3 only | Pending |
| Server header | curl -I https://10.0.1.10 | No Nginx version | Pending |
| X-Frame-Options | curl -I https://10.0.1.10 | DENY | Pending |

---

## 14. Troubleshooting Commands

| Problem | Command | Solution |
|---------|---------|----------|
| UFW blocking everything | sudo ufw status verbose | Check rules, ensure SSH allowed |
| Nginx won't start | sudo nginx -t | Fix syntax errors, check logs |
| SSH key auth failing | ssh -vvv lab-user@10.0.1.10 | Check permissions, config |
| fail2ban not banning | sudo fail2ban-client status sshd | Check jail config |
| Wazuh agent not connecting | sudo tail -f /var/ossec/logs/ossec.log | Check server IP, firewall |

---

## 15. Maintenance Procedures

### 15.1 Daily Tasks

| Task | Command |
|------|---------|
| Check Nginx status | systemctl status nginx |
| Review failed SSH attempts | `sudo grep -m 20 "Failed password" /var/log/auth.log` |
| Check disk space | df -h |

### 15.2 Weekly Tasks

| Task | Command |
|------|---------|
| Check UFW status | ufw status verbose |
| Review fail2ban bans | sudo fail2ban-client status sshd |
| Check for updates | sudo apt update && sudo apt list --upgradable |
| Review Nginx error logs | sudo tail -100 /var/log/nginx/error.log |

### 15.3 Monthly Tasks

| Task | Command |
|------|---------|
| Apply security updates | sudo apt upgrade -s |
| Review auditd logs | sudo ausearch -k ssh_changes |
| Validate TLS configuration | testssl.sh https://10.0.1.10 |
| Review Wazuh alerts | Wazuh dashboard |

---

## 16. Related Documents

| Document | Location |
|----------|----------|
| pfSense Network Security | 08-Technical-Controls/pfsense-network.md |
| Windows Hardening Guide | 08-Technical-Controls/windows-hardening.md |
| Wazuh Monitoring Guide | 08-Technical-Controls/wazuh-monitoring.md |
| Network Architecture Diagram | 05-Security-Architecture/diagrams/network-architecture.md |

---

## 17. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | April 2026 | S. Singh | Initial draft |
| 0.5 | May 2026 | S. Singh | Added SSL/TLS configuration |
| 1.0 | May 2026 | S. Singh | Draft learning edition |

---

**End of Ubuntu Web Server Hardening**
