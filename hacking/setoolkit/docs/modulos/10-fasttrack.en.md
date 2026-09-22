# Fast-Track Penetration Testing — menu 2

Quick pentest vectors inherited from Fast-Track, 100% Python. Base:
`src/fasttrack/`. Part of [INDICE.en.md](INDICE.en.md).

| Vector | File | How it works |
|---|---|---|
| **Microsoft SQL Bruter** | `mssql.py` → `Scan and Attack` sweeps the network for MSSQL and tries weak passwords; once in, it converts a binary to hexadecimal, deploys it in stages over SQL and converts it back on target for execution | |
| **Connect directly** | Opens a direct SQL session with a known credential | |
| **Custom Exploits** | `exploits/`: MS08-067, Firefox 3.6.16 mChannel, SolarWinds Storage Manager SQLi, RDP DoS, MySQL auth bypass, F5 root bypass | |
| **SCCM Attack Vector** | `sccm/`: abuses an SCCM server to push the payload across the managed network (lab) | |
| **Dell DRAC Checker** | `delldrac.py`: tries default credentials on Dell iDRAC/chassis | |
| **RID_ENUM** | `ridenum.py`: enumerates Windows users via RID cycling against the target | |
| **PSEXEC Injection** | `psexec.py`: PowerShell execution/injection via PSEXEC on the authenticated target | |

Example: `2 → 1 → 1` scans, brute-forces and deploys the stager — all guided
by terminal questions.
