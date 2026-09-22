# theHarvester — email and subdomain harvesting

**Folder:** `osint/theHarvester/` · **Site:** https://github.com/laramies/theHarvester ·
**Install:** `pip install theHarvester`

> Use only on your own/authorized domains.

## What it is and how it works

Passive collection: queries search engines and APIs, extracting **emails,
subdomains, hosts, IPs and URLs** tied to a domain. Each source is a plugin in
`theHarvester/discovery/` (google, bing, crtsh, github, shodan, virustotal,
dnssearch, haveibeenpwned… — dozens); `parsers/` cleans results and `lib/`
centralizes requests/keys (`~/.theHarvester/api-keys.yaml` for key-based sources).

## Usage

```bash
theHarvester -d target.com -b google
theHarvester -d target.com -b google,bing,crtsh,github -l 200
theHarvester -d target.com -b all -f result   # saves HTML/XML
theHarvester -d target.com -b dnssearch       # DNS brute-force
```

| Flag | Effect |
|---|---|
| `-d` | target domain (required) |
| `-b` | comma-separated sources, or `all` |
| `-l` | result limit per source |
| `-f` | report filename prefix (HTML + XML) |
| `-c` | dictionary DNS brute-force |
| `-e` | extra DNS (AXFR/shuffle) |

## Output

Terminal: emails, hosts and IPs grouped by source; with `-f`, reports to chain
into Holehe (emails) and SpiderFoot (domain).
