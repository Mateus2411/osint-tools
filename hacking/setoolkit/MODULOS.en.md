# SET — overview

Social-Engineer Toolkit 8.1.3: an authorized social-engineering testing
framework (red team with consent, lab, localhost). Per-module details live in
[`docs/modulos/INDICE.en.md`](docs/modulos/INDICE.en.md); the step-by-step in
[`GUIA-DE-USO.en.md`](GUIA-DE-USO.en.md); running on Windows in
[`README-WINDOWS-WSL.md`](README-WINDOWS-WSL.md).

> Without written authorization, using any module below is a crime.

## How SET works (summary)

Every vector follows the same flow: **menu → questions** (IP, port, URL,
payload) → **generation** (file, cloned site or listener) → **execution +
report** in `~/.set/reports/` and log in `src/logs/`. The core
(`src/core/setcore.py`) handles banner, menus, root check, version and config.

## Layout

```
hacking/setoolkit/
├── MODULOS.md / MODULOS.en.md      ← this overview
├── GUIA-DE-USO.md / .en.md         ← step-by-step usage
├── README-WINDOWS-WSL.md           ← running on Windows via WSL2
├── run-setoolkit.bat / run-setoolkit-wsl.sh  ← launchers
├── docs/modulos/                   ← 1 file per module + index
│   ├── INDICE.md / INDICE.en.md    ← points to each module
│   ├── 01-webattack.md(.en)        ← fake sites, harvester, applets…
│   ├── 02-spear-phishing.md(.en)   ← email with attachment
│   ├── 03-mass-mailer.md(.en)      ← bulk email
│   ├── 04-infectious-media.md(.en) ← USB/CD
│   ├── 05-payload-listener.md(.en) ← payloads + listener
│   ├── 06-powershell.md(.en)       ← PowerShell vectors
│   ├── 07-arduino-teensy.md(.en)   ← USB keyboard device
│   ├── 08-wireless.md(.en)         ← rogue AP
│   ├── 09-qrcode.md(.en)           ← QRCode
│   ├── 10-fasttrack.md(.en)        ← pentest (MSSQL, exploits…)
│   ├── 11-third-party.md(.en)      ← community modules + how to write one
│   └── 12-utilitarios.md(.en)      ← seautomate, seproxy, seupdate
├── src/                            ← code (core, webattack, phishing…)
├── modules/                        ← installed third-party modules
└── setoolkit / seautomate / seproxy / seupdate  ← executables
```

## Quick module map

| Menu | Module | Idea in 1 sentence | Doc |
|---|---|---|---|
| 1 → 2 | Website Attack Vectors | cloned/fake site stealing logins or delivering payload | [01](docs/modulos/01-webattack.en.md) |
| 1 → 1 | Spear-Phishing | targeted email with malicious document | [02](docs/modulos/02-spear-phishing.en.md) |
| 1 → 5 | Mass Mailer | bulk email, no attachment | [03](docs/modulos/03-mass-mailer.en.md) |
| 1 → 3 | Infectious Media | USB/CD with autorun + payload | [04](docs/modulos/04-infectious-media.en.md) |
| 1 → 4 | Payload + Listener | builds binary and waits for the reverse connection | [05](docs/modulos/05-payload-listener.en.md) |
| 1 → 9 | Powershell Vectors | attacks via native Windows PowerShell | [06](docs/modulos/06-powershell.en.md) |
| 1 → 6 | Arduino/Teensy | USB device that types the attack by itself | [07](docs/modulos/07-arduino-teensy.en.md) |
| 1 → 7 | Wireless AP | rogue AP + DNS spoof for the test network | [08](docs/modulos/08-wireless.en.md) |
| 1 → 8 | QRCode | QR pointing at a test URL | [09](docs/modulos/09-qrcode.en.md) |
| 2 | Fast-Track | MSSQL bruter, Python exploits, enumeration | [10](docs/modulos/10-fasttrack.en.md) |
| 3 / 1→10 | Third Party | extra modules + how to write yours | [11](docs/modulos/11-third-party.en.md) |
| — | Utilities | automation, proxy, menuless update | [12](docs/modulos/12-utilitarios.en.md) |

## Essential configuration (`/etc/setoolkit/set.config`, menu option 5)

| Option | Default | Effect |
|---|---|---|
| `METASPLOIT_PATH` | `/opt/metasploit/...` | without it, MSF payloads vanish from the menu |
| `METASPLOIT_MODE` | ON | OFF = SET/RATTE vectors only |
| `WEB_PORT` | 80 | attack server port |
| `APACHE_SERVER` | OFF | ON = Apache instead of the Python server |
| `WEBATTACK_SSL` / `SELF_SIGNED_CERT` | OFF | HTTPS with a self-made cert |
| `SENDMAIL` / `EMAIL_PROVIDER` | OFF / GMAIL | sender spoofing / SMTP provider |
| `ETTERCAP` / `DSNIFF` | OFF | ARP poisoning in the web vector (local network) |
| `HARVESTER_REDIRECT` / `HARVESTER_URL` | OFF | where to send the victim after the theft |
| `DNS_SERVER` | OFF | mini-DNS resolving everything to SET |
| `TRACK_EMAIL_ADDRESSES` | OFF | tracks who clicked (needs web email + Apache) |

## Generated files

- Reports: `~/.set/reports/` · harvester log: `src/logs/harvester.log`
- Core errors: `src/logs/set_logfile.log` · state: `~/.set/set.options`

## Suggested study order

harvester ([01](docs/modulos/01-webattack.en.md)) → payload+listener
([05](docs/modulos/05-payload-listener.en.md)) → PowerShell
([06](docs/modulos/06-powershell.en.md)) → Fast-Track
([10](docs/modulos/10-fasttrack.en.md)).
