# Website Attack Vectors — menu 1 → 2

The web module (`src/webattack/`) clones or builds an attacker site and starts
its own HTTP server (port `WEB_PORT=80` by default) to receive test victims.
Part of [INDICE.en.md](INDICE.en.md).

## Methods

| Method | How it works |
|---|---|
| **Credential Harvester** (`harvester/harvester.py`) | Serves the cloned site and intercepts every `POST` (typed login/password). Writes to `src/logs/harvester.log` and prints to the terminal with IP and timestamp. Delivers no payload — it only proves the credential would be stolen. `HARVESTER_REDIRECT`/`HARVESTER_URL` redirect the victim after capture; `HARVESTER_LOG_PASSWORDS` controls password logging |
| **Site Cloner** (`web_clone/cloner.py`) | Downloads the target's HTML (with a Chrome `USER_AGENT_STRING`) and rewrites forms to post to the SET server |
| **Web Templates** | Ready-made templates (Google, Twitter, etc.) in `src/html/templates/` — no cloning needed |
| **Tabnabbing** (`tabnabbing/`) | Page that detects tab switching and reloads fake content to steal the next login |
| **Web Jacking** | Iframe showing the real site but swapping the clicked link for the malicious one (`WEBJACKING_TIME=2000` ms) |
| **Multi-Attack** (`multi_attack/`) | Combines applet + harvester + tabnabbing on one page (`AUTO_REDIRECT=ON` redirects after the first success) |
| **HTA Attack** (`hta/`) | Cloned site delivering a `.hta` file with PowerShell injection (Windows targets) |
| **Java Applet** | Falsely signed applet (`JAVA_ID_PARAM`) executing a Metasploit payload; `JAVA_REPEATER=ON` keeps nagging if the victim clicks "cancel" |
| **Browser Exploit** (`browser_exploits/gen_payload.py`) | Iframe trying ~40 browser exploits (Flash, IE, Java…) via `METASPLOIT_IFRAME_PORT=8080` |
| **Web Profiler** (`profiler/`) | Fingerprints the visitor's machine versions (gated by `WEB_PROFILER`, currently OFF by default) |
| **DLL Hijacking** (`dll_hijacking/`) | Zips/RARs a document + malicious DLL: opening the file calls the DLL, then the payload |

## Building the site

After picking the method:

```
1) Web Templates  → ready-made templates, no target needed
2) Site Cloner    → give a URL and SET copies and rewrites the forms
3) Custom Import  → import your own index.html
```

## Example (harvester in the lab)

```
set> 1  (Social-Engineering Attacks) → 2 (Website) → 3 (Credential Harvester)
→ 2 (Site Cloner) → LHOST 127.0.0.1 → URL http://localhost:8000/login
```

Visit `http://127.0.0.1`, type a fake login and check the terminal and
`~/.set/reports/`. Stops with `Ctrl+C`.

## Extras

- `UNC_EMBED=ON` injects a UNC `img src` to capture LM hashes over SMB
- `WEBATTACK_SSL` + `SELF_SIGNED_CERT` serve everything over HTTPS
- `APACHE_SERVER=ON` swaps the Python server for Apache (`APACHE_DIRECTORY`)
