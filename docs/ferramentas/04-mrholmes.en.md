# Mr.Holmes — GUI-driven investigation

**Folder:** `osint/Mr.Holmes/` · **Site:** https://github.com/Lucksi/Mr.Holmes ·
**Install (Windows):** `Install.cmd` · **Run:** `python MrHolmes.py`

> Use only on your own/authorized targets.

## What it is and how it works

OSINT investigation with a **GUI** (light/dark/high-contrast) + CLI. The entry
(`MrHolmes.py` → `Core/Support/Menu`) calls the searchers in `Core/`:

| Module (`Core/`) | Purpose |
|---|---|
| `Searcher_website.py` | domains: WHOIS, DNS, tech stack, links |
| `Searcher.py` | usernames across dozens of sites |
| `Searcher_phone.py` | phones: carrier, region, messengers |
| `Searcher_person.py` | people: aggregates and drafts hypotheses about the target |
| `E_Mail.py` | silent email lookup |
| `Dork.py` | ready-made Google Dorks against the target |
| `Port_Scanner.py` | host ports |
| `PDF_Converter.py` | exports the dossier as PDF |
| `Transfer.py` + `QRCodes/` | moves results via QR Code |
| `Decoder.py` | decodes hashes/encodings |
| `Proxies/` | anonymous proxies; `Useragents/` rotates user-agent |

Config in `Configuration/Configuration.ini` (e.g. WhoIS key at
https://whois.whoisxmlapi.com); languages in `Lang/`; sessions and evidence in
`Logs/`, `Temp/`, `Transfer/`.

## Usage

```bash
cd osint/Mr.Holmes
Install.cmd        # first time only (Windows)
python MrHolmes.py # menu → Domain / Username / Phone / Person / Dork
```

Follow the menu: enter the target, review maps/charts/hypotheses and export the PDF.
