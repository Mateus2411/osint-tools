# Holehe — email account discovery

**Folder:** `osint/holohe/` · **Site:** https://github.com/megadose/holehe ·
**Install:** `pip install holehe` (already installed here: v1.61)

> Use only with your own emails or with consent.

## What it is and how it works

Holehe checks an email against **100+ sites** (Instagram, Twitter, Adobe,
Gravatar, etc.) via each site's "forgot password"/signup flow: if the site
says the email exists, the account exists. It cracks nothing — it only reveals
**where an account is registered**. Runs locally, no API key.

## Usage

```bash
holehe email@target.com
holehe a@mail.com b@mail.com --only-used   # only sites with accounts
holehe email@mail.com -C                    # export CSV
holehe email@mail.com -T 20                 # 20s timeout per site
```

| Flag | Effect |
|---|---|
| `--only-used` | show only sites with an account found |
| `--no-color` / `--no-clear` | plain output, no screen clearing |
| `-NP` | skip password-recovery attempts |
| `-C` | write results to CSV |
| `-T` | per-site timeout (default 10s) |

## Output

Terminal table (`[+]` = account found) or CSV with `-C`. Chain it with
SpiderFoot (domain emails) and theHarvester for full investigations.
