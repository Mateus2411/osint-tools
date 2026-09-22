# Spear-Phishing — menu 1 → 1

Phishing direcionado por e-mail com anexo (`src/phishing/`). Parte de
[INDICE.md](INDICE.md).

## Opções

```
1) Perform a Mass Email Attack   → dispara e-mails com anexo malicioso
2) Create a FileFormat Payload   → só gera o arquivo com payload
3) Create a Social-Engineering Template → cria seu template de e-mail/arquivo
```

## Como funciona

1. **FileFormat Payload** — escolhe o exploit de documento (lista
   `create_payloads_menu` em `src/core/menu/text.py`: PDFs Adobe, RTF/MS Word,
   Flash etc.; padrão: PDF com EXE embutido) e o payload de retorno (LHOST/LPORT).
2. **Mass Email Attack** — `smtp/client/` (`smtp_client.py`, `smtp_web.py`,
   `custom_template.py`) dispara via Gmail/Hotmail/Yahoo (`EMAIL_PROVIDER`) ou
   sendmail local (`SENDMAIL=ON`, permite spoofar o remetente). Intervalo entre
   envios: `TIME_DELAY_EMAIL=1`.
3. **Templates** — corpo de e-mail e documento isca reutilizáveis.

## Rastreio de cliques

Com `WEBATTACK_EMAIL=ON` + Apache + `TRACK_EMAIL_ADDRESSES=ON`, cada e-mail
ganha link único e o SET registra quem clicou — ideal para métrica de campanha
de conscientização no lab (aponte para contas de teste).
