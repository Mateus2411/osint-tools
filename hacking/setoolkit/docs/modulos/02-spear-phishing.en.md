# Spear-Phishing — menu 1 → 1

Targeted email phishing with attachment (`src/phishing/`). Part of
[INDICE.en.md](INDICE.en.md).

## Options

```
1) Perform a Mass Email Attack   → sends emails with a malicious attachment
2) Create a FileFormat Payload   → only generates the file with a payload
3) Create a Social-Engineering Template → creates your email/file template
```

## How it works

1. **FileFormat Payload** — pick the document exploit
   (`create_payloads_menu` in `src/core/menu/text.py`: Adobe PDFs, MS Word
   RTF, Flash, etc.; default: PDF with embedded EXE) and the return payload
   (LHOST/LPORT).
2. **Mass Email Attack** — `smtp/client/` (`smtp_client.py`, `smtp_web.py`,
   `custom_template.py`) sends via Gmail/Hotmail/Yahoo (`EMAIL_PROVIDER`) or
   local sendmail (`SENDMAIL=ON`, allows sender spoofing). Pacing between
   sends: `TIME_DELAY_EMAIL=1`.
3. **Templates** — reusable email body and lure document.

## Click tracking

With `WEBATTACK_EMAIL=ON` + Apache + `TRACK_EMAIL_ADDRESSES=ON`, each email
gets a unique link and SET records who clicked — ideal for lab awareness-campaign
metrics (point it at test accounts).
