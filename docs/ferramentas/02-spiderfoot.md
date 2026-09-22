# SpiderFoot — OSINT automático

**Pasta:** `osint/spiderfoot/` · **Site:** https://github.com/smicallef/spiderfoot ·
**Docs:** https://www.spiderfoot.net/documentation

> Use apenas em alvos próprios/autorizados.

## O que é e como funciona

Plataforma de OSINT 100% automática: você dá um alvo (domínio, IP, e-mail,
username, telefone, nome…) e ele roda **235 módulos** (`modules/sfp_*.py`) que
consultam fontes públicas — DNS, WHOIS, Shodan, VirusTotal, redes sociais,
vazamentos, blockchain etc. Cada achado vira um **evento** correlacionado
(`correlations/`, `SpiderFootCorrelator`) e gravado no SQLite. Núcleo:
`sflib.py` (motor), `sfscan.py` (scanner), `sfwebui.py` + `sf.py` (web),
`sfcli.py` (CLI).

## Uso

```bash
cd osint/spiderfoot
pip install -r requirements.txt
python sf.py -l 127.0.0.1:5001     # abre http://127.0.0.1:5001
```

Na web: **New Scan** → nome, tipo do alvo (Domain, Email, IP, Username,
Phone…), tipo de scan (All = completo, demora) → **Run**. Acompanhe eventos em
tempo real, filtre por tipo (ex.: `EMAILADDR`, `INTERNET_NAME`) e exporte
CSV/JSON/GEXF.

## Módulos (categorias)

| Categoria | Exemplos |
|---|---|
| DNS/rede | `sfp_dnsresolve`, `sfp_dnscommonsrv`, `sfp_portscan_tcp`, `sfp_sslcert` |
| Domínio/empresa | `sfp_whois`, `sfp_crt`, `sfp_sublist3r`, `sfp_builtwith`, `sfp_shodan` |
| E-mail/vazamento | `sfp_email`, `sfp_haveibeenpwned`, `sfp_pwned`, `sfp_adblock` |
| Social/username | `sfp_twitter`, `sfp_github`, `sfp_instagram`, `sfp_accounts` |
| Reputação/malware | `sfp_virustotal`, `sfp_abuseipdb`, `sfp_malcheck`, `sfp_phishstats` |

Cada módulo tem opções próprias (API keys, limites) na aba **Settings** do scan.
