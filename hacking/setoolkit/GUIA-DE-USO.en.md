# SET Usage Guide in English — Social-Engineer Toolkit 8.1.3

> **Warning:** use only for **authorized** testing (lab, localhost, red team
> with written consent and defined scope). Unauthorized use is a crime. SET is
> an auditing tool, not a real-attack weapon.

## 1. Starting it

```powershell
# PowerShell (asks for the WSL password). The cd is mandatory:
wsl -d Ubuntu -- bash -lc "cd /home/keila/setoolkit && sudo /home/keila/.venvs/setoolkit/bin/python /home/keila/setoolkit/setoolkit"
```

```bash
# Inside WSL:
cd ~/setoolkit && sudo ~/.venvs/setoolkit/bin/python ~/setoolkit/setoolkit
```

On first run type `y` to accept the terms. The SET prompt is `set>`.

## 2. Main menu

```
1) Social-Engineering Attacks      → social-engineering vectors (the heart of SET)
2) Penetration Testing (Fast-Track)→ quick pentest (MSSQL, exploits, enumeration)
3) Third Party Modules             → third-party modules (modules/ folder)
4) Update the Social-Engineer Toolkit → updates via git
5) Update SET configuration        → reconfigures IP, Metasploit, etc.
6) Help, Credits, and About
99) Exit
```

## 3. Option 1 — Social-Engineering Attacks

Submenu (`set:>`):

```
1) Spear-Phishing Attack Vectors
2) Website Attack Vectors
3) Infectious Media Generator
4) Create a Payload and Listener
5) Mass Mailer Attack
6) Arduino-Based Attack Vector
7) Wireless Access Point Attack Vector
8) QRCode Generator Attack Vector
9) Powershell Attack Vectors
10) Third Party Modules
99) Return to Main Menu
```

### 3.1 Spear-Phishing (1)

```
1) Perform a Mass Email Attack   → sends emails with a malicious attachment (uses templates)
2) Create a FileFormat Payload   → only generates the file (PDF, DOC, etc.) with a payload
3) Create a Social-Engineering Template → creates your own email/file template
```

Typical flow: pick the fileformat exploit (e.g. `Adobe PDF Embedded EXE`),
the payload (e.g. reverse TCP), the return IP (LHOST) and generate the file.
Then use option 1 to send it in the lab, or option 2 to just grab the file.

### 3.2 Website Attack Vectors (2) — the most used

```
1) Java Applet Attack Method        → requires Metasploit; fake applet with payload
2) Metasploit Browser Exploit Method→ iframe with browser exploit (~40 to choose from)
3) Credential Harvester Attack Method → clones a site and steals typed logins (NO payload)
4) Tabnabbing Attack Method         → swaps the tab when the victim switches tabs
5) Web Jacking Attack Method        → iframe that fakes the legitimate link
6) Multi-Attack Web Method          → combines several methods at once
7) HTA Attack Method                → cloned site + PowerShell via .hta file
```

After picking the method, SET asks **how to build the site**:

```
1) Web Templates  → ready-made templates (Google, Twitter, etc.)
2) Site Cloner    → clones any URL you provide
3) Custom Import  → imports your own index.html
```

**Guided example — Credential Harvester in the lab:**

```
set> 1          (Social-Engineering Attacks)
set> 2          (Website Attack Vectors)
set> 3          (Credential Harvester)
set> 2          (Site Cloner)
Return IP:      127.0.0.1                  (your lab IP)
URL to clone:   http://localhost:8000/login (your TEST target)
```

SET starts a server on port 80. Visit `http://127.0.0.1`, type a fake login
and watch the report in the terminal + under `~/.set/reports/`. To stop,
`Ctrl+C`. The harvester only captures what is typed — ideal for proving risk
without delivering a payload.

### 3.3 Infectious Media Generator (3)

```
1) File-Format Exploits            → USB/CD with autorun.inf + exploit
2) Standard Metasploit Executable  → USB/CD with a straight executable
```

Generates the layout for physical-media testing (autorun is disabled on modern
Windows — more educational than practical).

### 3.4 Create a Payload and Listener (4)

Generates a payload + already opens the listener (which receives the reverse
connection). Without Metasploit installed, the options are SET-native:

```
1) SE Toolkit Interactive Shell   → SET's own reverse shell
2) SE Toolkit HTTP Reverse Shell  → HTTP shell with AES
3) RATTE HTTP Tunneling Payload   → tunnels everything over HTTP
```

With Metasploit configured you also get PowerShell Meterpreter,
shellcodeexec, etc. Enter LHOST (your IP) and LPORT (e.g. 443) and leave the
terminal open waiting for the lab connection.

### 3.5 Mass Mailer Attack (5)

Bulk-email sender for the test base (uses the Linux sendmail; set
`SENDMAIL=ON` in option 5 of the main menu). Define sender, recipients,
subject and body/template, and review before sending — in the lab, point it
at test accounts.

### 3.6 Arduino-Based Attack Vector (6)

Generates `.pde` sketches for Teensy/Arduino (a USB device that poses as a
keyboard). Options: PowerShell downloaders, reverse shell, Beef hook, binary
via Teensy, X10 attacks, etc. Requires the hardware (~US$ 22) and the Arduino
IDE.

### 3.7 Wireless Access Point Attack Vector (7)

```
1) Start → creates a rogue AP + DHCP + DNS spoof (needs AirBase-NG, AirMon-NG, DNSSpoof, dhcpd3)
2) Stop  → takes the AP down
```

With the AP up, run any web vector (e.g. the harvester) and test-network
traffic falls into your server.

### 3.8 QRCode Generator Attack Vector (8)

Generates a QR Code pointing at your test URL (e.g. the harvester). Useful
for awareness campaigns: how many people scan it? The report shows the hits.

### 3.9 Powershell Attack Vectors (9)

```
1) Powershell Alphanumeric Shellcode Injector → injects shellcode via PowerShell
2) Powershell Reverse Shell                   → pure-PS reverse shell
3) Powershell Bind Shell                      → opens a port on the test target
4) Powershell Dump SAM Database               → dumps SAM hashes (post-exploitation, lab)
```

Generates ready-to-paste `.ps1`/one-liners for the test environment.

### 3.10 Third Party Modules (10)

Loads modules from the `modules/` folder (e.g. `ratte_module.py`,
`google_analytics_attack.py`). To write your own, copy
`modules/test_module.example` and register it in the menu.

## 4. Option 2 — Penetration Testing (Fast-Track)

```
1) Microsoft SQL Bruter  → 1) Scan and Attack MSSQL | 2) Connect directly
2) Custom Exploits       → MS08-067, Firefox 3.6.16, SolarWinds SQLi, RDP DoS,
                           MySQL auth bypass, F5 auth bypass...
3) SCCM Attack Vector    → System Center Configuration Manager abuse (lab)
4) Dell DRAC/Chassis Default Checker → tests iDRAC default credentials
5) RID_ENUM              → user enumeration via RID cycling (Windows target/lab)
6) PSEXEC Powershell Injection → PowerShell injection via PSEXEC
```

Example: `2 → 1 → 1` scans the test network for MSSQL, tries weak credentials
and, on success, deploys SET's hexadecimal stager.

## 5. Options 3, 4, 5, 6

- **3 Third Party Modules:** same as section 3.10, a shortcut from the main menu.
- **4 Update:** `git pull` from the official repository. (The reference copy
  in `hacking/setoolkit/` does not update itself — `git pull` it separately.)
- **5 Update SET configuration:** edits `/etc/setoolkit/set.config` — external
  IP/LHOST, Metasploit path (`METASPLOIT_PATH`), SENDMAIL, etc. Run it after
  switching networks/labs.
- **6 Help/Credits:** help, credits and `readme/User_Manual.pdf` (full manual,
  in English, in the `readme/` folder).

## 6. Command-line utilities

They live in the SET root (run from WSL, inside `~/setoolkit`):

| Command | Purpose |
|---|---|
| `sudo ./setoolkit` | interactive menu (this guide) |
| `./seautomate file.txt` | runs SET from a script (canned answers, no typing) |
| `./seproxy` | auxiliary SET proxy/relay |
| `./seupdate` | updates SET without opening the menu |

`seautomate` example (automatic harvester in the lab):

```
1
2
3
2
127.0.0.1
http://localhost:8000/login
```

## 7. Where results go

- Reports: `~/.set/reports/` (inside WSL)
- Logs: `~/setoolkit/src/logs/set_logfile.log`
- Config: `/etc/setoolkit/set.config` (+ generated `set.config.py`)

## 8. Lab tips

1. **Learning order:** harvester (3.2) → payload+listener (3.4) →
   PowerShell (3.9) → Fast-Track (4). No Metasploit needed to learn the essentials.
2. **Network:** prefer `127.0.0.1` or a host-only VM/network; never the company
   network without written authorization.
3. **Antivirus:** Defender flags SET/impacket as hacktools. The running copy
   lives on WSL ext4 (`~/setoolkit`), out of its reach.
4. **Cleanup:** `99` exits the menus; `Ctrl+C` stops servers/listeners, answer
   `yes` to kill stuck listeners.
