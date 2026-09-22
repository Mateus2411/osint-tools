# SpiderFoot — automated OSINT

**Folder:** `osint/spiderfoot/` · **Site:** https://github.com/smicallef/spiderfoot ·
**Docs:** https://www.spiderfoot.net/documentation

> Use only on your own/authorized targets.

## What it is and how it works

Fully automated OSINT platform: give it a target (domain, IP, email, username,
phone, name…) and it runs **235 modules** (`modules/sfp_*.py`) against public
sources — DNS, WHOIS, Shodan, VirusTotal, social networks, breaches,
blockchain, etc. Every finding becomes a correlated **event**
(`correlations/`, `SpiderFootCorrelator`) stored in SQLite. Core: `sflib.py`
(engine), `sfscan.py` (scanner), `sfwebui.py` + `sf.py` (web), `sfcli.py` (CLI).

## Usage

```bash
cd osint/spiderfoot
pip install -r requirements.txt
python sf.py -l 127.0.0.1:5001     # open http://127.0.0.1:5001
```

In the web UI: **New Scan** → name, target type (Domain, Email, IP, Username,
Phone…), scan type (All = full, slow) → **Run**. Watch events live, filter by
type (e.g. `EMAILADDR`, `INTERNET_NAME`) and export CSV/JSON/GEXF.

## Modules (categories)

| Category | Examples |
|---|---|
| DNS/network | `sfp_dnsresolve`, `sfp_dnscommonsrv`, `sfp_portscan_tcp`, `sfp_sslcert` |
| Domain/company | `sfp_whois`, `sfp_crt`, `sfp_sublist3r`, `sfp_builtwith`, `sfp_shodan` |
| Email/breach | `sfp_email`, `sfp_haveibeenpwned`, `sfp_pwned`, `sfp_adblock` |
| Social/username | `sfp_twitter`, `sfp_github`, `sfp_instagram`, `sfp_accounts` |
| Reputation/malware | `sfp_virustotal`, `sfp_abuseipdb`, `sfp_malcheck`, `sfp_phishstats` |

Each module has its own options (API keys, limits) in the scan's **Settings** tab.
