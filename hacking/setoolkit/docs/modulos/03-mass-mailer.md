# Mass Mailer Attack — menu 1 → 5

Disparo de e-mail em massa **só com texto/HTML, sem anexo explorável**.
Parte de [INDICE.md](INDICE.md).

## Como funciona

Mesmo motor SMTP do spear-phishing (`src/phishing/smtp/`): provedores
Gmail/Hotmail/Yahoo (`EMAIL_PROVIDER`) ou sendmail local (`SENDMAIL=ON` para
spoofar remetente). Define remetente, lista de destinatários, assunto e
corpo/template, revisa e envia.

## Quando usar

Campanha de conscientização: medir quantos usuários clicam/abrem, sem entregar
payload. No lab, aponte sempre para contas de teste.
