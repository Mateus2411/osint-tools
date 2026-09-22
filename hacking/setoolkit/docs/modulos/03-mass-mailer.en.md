# Mass Mailer Attack — menu 1 → 5

Bulk email sending **with text/HTML only, no exploitable attachment**.
Part of [INDICE.en.md](INDICE.en.md).

## How it works

Same SMTP engine as spear-phishing (`src/phishing/smtp/`): Gmail/Hotmail/Yahoo
providers (`EMAIL_PROVIDER`) or local sendmail (`SENDMAIL=ON` for sender
spoofing). Define sender, recipient list, subject and body/template, review
and send.

## When to use it

Awareness campaign: measuring how many users click/open, without delivering a
payload. In the lab, always point it at test accounts.
