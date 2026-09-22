# Global-Tools - Complete Guide (OSINT + Hacking)

<p align="center">
  <a href="./README.md">🇧🇷 Português</a> | <b>🇬🇧 English</b>
</p>

<sub style="color:gray;">
All tools provided must be used ethically and responsibly.
Misuse to compromise the security or privacy of third parties is not recommended.
</sub>

---

## 📁 Project Structure

```
Global-Tools/
├── 📂 osint/            # OSINT tools
│   ├── holohe/          # Account discovery by email
│   ├── spiderfoot/      # Automated OSINT
│   ├── theHarvester/    # Email/subdomain gathering
│   └── Mr.Holmes/       # GUI investigation
├── 📂 hacking/          # Pentest/hacking tools
│   ├── GAMKERS-DDOS/    # UDP stress testing
│   └── RedTiger-Tools/  # Pentest + OSINT all-in-one
├── OSINT-REPOS.md       # OSINT/pentest repository list
├── README.md            # This guide (PT)
└── README.en.md         # This guide (EN)
```

---

## 🛠️ Available Tools

### 1️⃣ [Holehe](./osint/holohe/) 📧
**Tool to discover accounts associated with an email**
- **Repository**: https://github.com/megadose/holehe
- **Function**: Check accounts on 100+ sites (Instagram, Twitter, etc)
- **Prerequisite**: Python 3.6+
- **Install**: `pip install holehe`
- **Usage**: `holehe email@email.com`

### 2️⃣ [SpiderFoot](./osint/spiderfoot/) 🕷️
**Extremely powerful automated OSINT tool**
- **Repository**: https://github.com/smicallef/spiderfoot
- **Function**: Complete and automated investigation
- **Targets**: Domains, emails, IPs, phones, companies, breaches
- **Interface**: Web + CLI
- **Usage**: `py -3.14 sf.py -l 127.0.0.1:5001`

### 3️⃣ [theHarvester](./osint/theHarvester/) 🌾
**Classic OSINT information gathering tool**
- **Repository**: https://github.com/laramies/theHarvester
- **Function**: Collect emails, subdomains, hosts, IPs from multiple sources
- **Sources**: Google, Bing, SHODAN, VirusTotal, DNSDumpster, +40 others
- **Install**: `pip install theHarvester`
- **Usage**: `theHarvester -d domain.com -b google,bing`

### 4️⃣ [Mr.Holmes](./osint/Mr.Holmes/) 🔍
**OSINT information gathering tool with GUI**
- **Repository**: https://github.com/Lucksi/Mr.Holmes
- **Function**: Gather information on domains, usernames and phone numbers via public sources
- **Extras**: Google Dorks, anonymous proxies, WhoIS API, silent email lookup, interactive maps and graphs, target hypotheses, PDF export, QR Code transfer
- **Interface**: GUI (dark/light/high-contrast) + CLI
- **Install (Windows)**: `git clone` + `Install.cmd`
- **Usage**: `python MrHolmes.py` (or `Launchers/Win_Launcher.exe`)
- **Config**: `Configuration/Configuration.ini` (WhoIS API: https://whois.whoisxmlapi.com)

### 5️⃣ [GAMKERS-DDOS](./hacking/GAMKERS-DDOS/) ⚡
**Optimized multithreaded UDP stress testing tool**
- **Repository**: https://github.com/Mateus2411/osint-tools
- **Function**: UDP stress/denial testing with multithreaded packets
- **Language**: Python 3 (zero dependencies — stdlib only)
- **Optimizations**: socket per thread, no per-packet printing (~35x faster), real-time pps reporter
- **Usage**: `python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10`
- **⚠️ Authorized testing / localhost only**

### 6️⃣ [RedTiger-Tools](./hacking/RedTiger-Tools/) 🐯
**Multifunction pentest + OSINT platform with plugin system**
- **Repository**: https://github.com/loxy0devlp/RedTiger-Tools
- **Function**: Centralize pentest and OSINT in one tool (CLI + interactive interface)
- **Pentest**: advanced scanner, vulnerability scanner, port scanner, URL crawler, continuous ping, host discovery
- **OSINT**: Google dorks, crypto wallet tracker, username/email/IP/phone lookup, Instagram lookup
- **Extras**: metadata scanner/deleter, website cloner, Python plugins
- **Install**: `python setup.py`
- **Usage**: `python redtiger.py` (e.g. `python redtiger.py -pnl -p "+551****9999"`)

---

## 📋 Quick Installation Guide

### Mr.Holmes
```bash
# 1. Clone the repository:
git clone https://github.com/Lucksi/Mr.Holmes
# 2. Enter folder and install:
cd osint/Mr.Holmes
Install.cmd
# 3. Run:
python MrHolmes.py
```

### RedTiger-Tools
```bash
# 1. Clone the repository:
git clone https://github.com/loxy0devlp/RedTiger-Tools
# 2. Enter folder:
cd hacking/RedTiger-Tools
# 3. Install dependencies:
python setup.py
# 4. Run:
python redtiger.py
```

### Holehe
```bash
# 1. Install Python: https://www.python.org/downloads/
# ⚠️ Check "Add Python to PATH"
# 2. Install Holehe:
pip install holehe
# 3. Test:
holehe email@email.com
```

### SpiderFoot
```bash
# 1. Enter folder: C:\Global-Tools
# 2. Clone:
git clone https://github.com/smicallef/spiderfoot
# 3. Enter folder:
cd osint/spiderfoot
# 4. Install dependencies:
pip install -r requirements.txt
# 5. Run:
python spiderfoot.py -l 127.0.0.1:5001
# 6. Open in browser: http://127.0.0.1:5001
```

### theHarvester
```bash
# 1. Install: pip install theHarvester
# 2. Basic usage:
theHarvester -d domain.com -b google
# 3. Multiple sources:
theHarvester -d target.com -b google,bing,dnsdumpster
# 4. Save results:
theHarvester -d company.com -b all -f results
```

### GAMKERS-DDOS
```bash
# 1. Enter folder:
cd hacking/GAMKERS-DDOS
# 2. Run (zero dependencies, just needs Python 3):
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10
```

---

## 🧠 What Each Tool Does Best

| Tool | Best Use | Data Type |
|------|----------|-----------|
| **Holehe** | Discover accounts by email | Social media, online platforms |
| **SpiderFoot** | Automated OSINT | Everything: domains, IPs, emails, vulnerabilities |
| **theHarvester** | Information gathering | Emails, subdomains, hosts from multiple sources |
| **Mr.Holmes** | Complete GUI investigation | Domains, usernames, phones, dorks, graphs/maps |
| **GAMKERS-DDOS** | UDP stress testing | Multithreaded UDP packets, pps, configurable payload |
| **RedTiger-Tools** | Pentest + OSINT all-in-one | Scanners, dorks, crypto wallets, phone/IP/email/Instagram |

---

## 🚀 Recommended Workflow

### 1. Person Investigation
```bash
# 1. Start with email (if available)
holehe person@email.com

# 2. Investigate phone (if found)
python redtiger.py -pnl -p "+551****9999"

# 3. Complete OSINT on the email domain
# SpiderFoot: Target = email.com, Type = Domain
```

### 2. Company Investigation
```bash
# 1. Automated OSINT on domain
# SpiderFoot: Target = company.com, Type = Domain

# 2. Verify found emails
holehe email@company.com

# 3. Investigate found phones
python redtiger.py -pnl -p "+551****9999"
```

### 3. Domain/Site Investigation
```bash
# 1. SpiderFoot first (massive collection)
# Target = site.com, Scan Type = All

# 2. Verify found emails
holehe admin@site.com

# 3. Investigate found IPs and phones
python redtiger.py -il -i <found_ip> && python redtiger.py -pnl -p <found_number>
```

### 4. Stress Testing (authorized only)
```bash
# 1. Resolve target IP
nslookup target.com

# 2. Test on localhost first
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10

# 3. Smaller payload = more pps
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 8 -d 5
```

---

## ⚠️ Legal and Ethical Considerations

### ✅ Allowed Use
- **Own investigation**: Your own data
- **Consent**: With authorization from the person/company
- **Academic research**: For educational purposes
- **Journalism**: Legitimate investigative journalism
- **Security**: Authorized pentest, bug bounty

### ❌ Prohibited Use
- **Stalking**: Harassment or persecution
- **Privacy invasion**: Without consent
- **Malicious activities**: Fraud, blackmail
- **Unauthorized commercial use**: Data selling
- **ToS violation**: Breaking terms of service

### 📋 Best Practices
1. **Always obtain consent** when applicable
2. **Respect local laws** (LGPD, GDPR, etc.)
3. **Use only public sources**
4. **Don't store sensitive data** unnecessarily
5. **Keep logs secure** and encrypted
6. **Document the purpose** of the investigation
7. **Limit scope** to what's necessary

---

## 🔧 Common Troubleshooting

### Python not found
```bash
# Download Python: https://www.python.org/downloads/
# ⚠️ Check "Add Python to PATH" during installation
# Verify: python --version
```

### Dependency errors
```bash
# Update pip:
python -m pip install --upgrade pip

# Install dependencies:
pip install -r requirements.txt
```

### SpiderFoot - lxml error
```bash
# Already fixed in this version
# If it persists, install manually:
pip install lxml
```

### Firewall/Antivirus blocking
```bash
# Add exceptions for:
# - Python.exe
# - Project folder
```

---

## 📚 Additional Resources

### Official Documentation
- **Holehe**: https://github.com/megadose/holehe/wiki
- **Mr.Holmes**: https://github.com/Lucksi/Mr.Holmes
- **RedTiger-Tools**: https://github.com/loxy0devlp/RedTiger-Tools
- **SpiderFoot**: https://www.spiderfoot.net/documentation
- **theHarvester**: https://github.com/laramies/theHarvester/wiki

### Communities
- **SpiderFoot Discord**: https://discord.gg/vyvztrG
- **Reddit OSINT**: r/OSINT
- **Twitter**: @spiderfoot

### Courses and Training
- **OSINT Framework**: https://osintframework.com/
- **Bellingcat**: https://www.bellingcat.com/resources/
- **SANS OSINT**: https://www.sans.org/cyber-security-courses/

---

## 💡 Advanced Tips

### Automation
```bash
# Script for complete investigation
#!/bin/bash
TARGET_EMAIL="target@email.com"
TARGET_PHONE="+5511999999999"
TARGET_DOMAIN="email.com"

echo "=== Investigating Email ==="
holehe $TARGET_EMAIL > holehe_results.txt

echo "=== Investigating Phone ==="
python redtiger.py -pnl -p "$TARGET_PHONE" > phone_results.txt

echo "=== Automated OSINT ==="
# Use SpiderFoot via CLI or web interface
```

### Data Integration
```bash
# Combine results in JSON format
jq -s '.[0] + .[1]' holehe.json redtiger_output.json > combined.json
```

### Backup and Security
```bash
# Encrypt sensitive results
gpg -c investigation_results.json

# Secure backup
tar -czf backup_$(date +%Y%m%d).tar.gz *.json *.txt
```

---

## 🎯 Executive Summary

This OSINT toolset provides comprehensive capabilities for digital investigation:

- **Holehe**: Expert in email-based account discovery
- **SpiderFoot**: Complete automated OSINT platform
- **theHarvester**: Multi-source information gathering
- **Mr.Holmes**: GUI investigation with dorks, maps, and graphs
- **GAMKERS-DDOS**: Multithreaded UDP stress testing
- **RedTiger-Tools**: Pentest + OSINT suite with plugins

**Always use ethically, legally, and responsibly!** 🕵️‍♂️🔍
