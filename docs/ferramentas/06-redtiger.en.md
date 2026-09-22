# RedTiger-Tools — all-in-one pentest + OSINT

**Folder:** `hacking/RedTiger-Tools/` · **Site:** https://github.com/loxy0devlp/RedTiger-Tools ·
**Install:** `python setup.py` · **Run:** `python redtiger.py`

> Use only on your own/authorized targets.

## What it is and how it works

CLI + interactive suite with a **plugin** system (`Plugins/Example.py` as a
template). The `redtiger.py` entry dispatches to `Program/` in 3 families:

| Prefix | Family | Modules |
|---|---|---|
| `NS*` | Network Scanner (pentest) | `NSAdvancedScanner`, `NSPortScanner`, `NSVulnerabilityScanner`, `NSUrlDiscoveryCrawler`, `NSHostDiscovery`, `NSIpPinger` (continuous ping) |
| `O*` | OSINT | `ODorkingQueryEngine` (Google dorks), `OUsernameTracker`, `OEmailLookup`/`OEmailTracker`, `OIpLookup`, `OPhoneNumerLookup`, `OInstagramProfileLookup`, `OWalletTracker` (crypto) |
| `U*` | Utilities | `UFileMetadataScanner`/`UFileMetadataDeleter`, `UWebsiteCloner` |
| `T*` | System | `THelp`, `TSettingsUpdate`, `TVersion` |

Config in `Config/`, data in `Data/`, results in `Ouput/`.

## Usage

```bash
cd hacking/RedTiger-Tools
python setup.py       # first time
python redtiger.py    # interactive menu
python redtiger.py -pnl -p "+5511999999999"   # direct phone lookup
```

Chain it: find emails with theHarvester → validate with Holehe → investigate
phones/IPs here → port-scan your lab with `NSPortScanner`.
