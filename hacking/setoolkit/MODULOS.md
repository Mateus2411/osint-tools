# SET — visão geral

Social-Engineer Toolkit 8.1.3: framework de testes de engenharia social
autorizados (red team com consentimento, lab, localhost). O detalhamento de
cada módulo está em [`docs/modulos/INDICE.md`](docs/modulos/INDICE.md); o
passo a passo em [`GUIA-DE-USO.md`](GUIA-DE-USO.md); como rodar no Windows em
[`README-WINDOWS-WSL.md`](README-WINDOWS-WSL.md).

> Sem autorização por escrito, usar qualquer módulo abaixo é crime.

## Como o SET funciona (resumo)

Todo vetor segue o mesmo fluxo: **menu → perguntas** (IP, porta, URL, payload)
→ **geração** (arquivo, site clonado ou listener) → **execução + relatório**
em `~/.set/reports/` e log em `src/logs/`. O núcleo (`src/core/setcore.py`)
cuida de banner, menus, checagem de root, versão e configuração.

## Estrutura

```
hacking/setoolkit/
├── MODULOS.md / MODULOS.en.md      ← este geral
├── GUIA-DE-USO.md / .en.md         ← passo a passo de uso
├── README-WINDOWS-WSL.md           ← como rodar no Windows via WSL2
├── run-setoolkit.bat / run-setoolkit-wsl.sh  ← launchers
├── docs/modulos/                   ← 1 arquivo por módulo + INDICE.md
│   ├── INDICE.md                   ← direciona a cada módulo
│   ├── 01-webattack.md             ← sites falsos, harvester, applets…
│   ├── 02-spear-phishing.md        ← e-mail com anexo
│   ├── 03-mass-mailer.md           ← e-mail em massa
│   ├── 04-infectious-media.md      ← USB/CD
│   ├── 05-payload-listener.md      ← payloads + listener
│   ├── 06-powershell.md            ← vetores PowerShell
│   ├── 07-arduino-teensy.md        ← dispositivo USB-teclado
│   ├── 08-wireless.md              ← AP falso
│   ├── 09-qrcode.md                ← QRCode
│   ├── 10-fasttrack.md             ← pentest (MSSQL, exploits…)
│   ├── 11-third-party.md           ← módulos da comunidade + como criar
│   └── 12-utilitarios.md           ← seautomate, seproxy, seupdate
├── src/                            ← código (core, webattack, phishing…)
├── modules/                        ← third-party instalados
└── setoolkit / seautomate / seproxy / seupdate  ← executáveis
```

## Mapa rápido dos módulos

| Menu | Módulo | Ideia em 1 frase | Doc |
|---|---|---|---|
| 1 → 2 | Website Attack Vectors | site clonado/falso que rouba login ou entrega payload | [01](docs/modulos/01-webattack.md) |
| 1 → 1 | Spear-Phishing | e-mail direcionado com documento malicioso | [02](docs/modulos/02-spear-phishing.md) |
| 1 → 5 | Mass Mailer | e-mail em massa, sem anexo | [03](docs/modulos/03-mass-mailer.md) |
| 1 → 3 | Infectious Media | USB/CD com autorun + payload | [04](docs/modulos/04-infectious-media.md) |
| 1 → 4 | Payload + Listener | gera binário e aguarda a conexão reversa | [05](docs/modulos/05-payload-listener.md) |
| 1 → 9 | Powershell Vectors | ataques via PowerShell nativo do Windows | [06](docs/modulos/06-powershell.md) |
| 1 → 6 | Arduino/Teensy | USB que digita sozinho o ataque | [07](docs/modulos/07-arduino-teensy.md) |
| 1 → 7 | Wireless AP | AP falso + DNS spoof para a rede de teste | [08](docs/modulos/08-wireless.md) |
| 1 → 8 | QRCode | QR apontando p/ URL de teste | [09](docs/modulos/09-qrcode.md) |
| 2 | Fast-Track | MSSQL bruter, exploits Python, enumeração | [10](docs/modulos/10-fasttrack.md) |
| 3 / 1→10 | Third Party | módulos extras + como criar o seu | [11](docs/modulos/11-third-party.md) |
| — | Utilitários | automação, proxy, update sem menu | [12](docs/modulos/12-utilitarios.md) |

## Configuração essencial (`/etc/setoolkit/set.config`, opção 5 do menu)

| Opção | Padrão | Efeito |
|---|---|---|
| `METASPLOIT_PATH` | `/opt/metasploit/...` | sem ele, payloads MSF somem do menu |
| `METASPLOIT_MODE` | ON | OFF = só vetores SET/RATTE |
| `WEB_PORT` | 80 | porta do servidor de ataque |
| `APACHE_SERVER` | OFF | ON = Apache em vez do servidor Python |
| `WEBATTACK_SSL` / `SELF_SIGNED_CERT` | OFF | HTTPS com cert próprio |
| `SENDMAIL` / `EMAIL_PROVIDER` | OFF / GMAIL | spoof de remetente / provedor SMTP |
| `ETTERCAP` / `DSNIFF` | OFF | ARP poisoning no vetor web (rede local) |
| `HARVESTER_REDIRECT` / `HARVESTER_URL` | OFF | para onde mandar a vítima após o roubo |
| `DNS_SERVER` | OFF | mini-DNS que resolve tudo para o SET |
| `TRACK_EMAIL_ADDRESSES` | OFF | rastreia quem clicou (exige e-mail web + Apache) |

## Arquivos gerados

- Relatórios: `~/.set/reports/` · log do harvester: `src/logs/harvester.log`
- Erros do núcleo: `src/logs/set_logfile.log` · estado: `~/.set/set.options`

## Ordem de estudo sugerida

harvester ([01](docs/modulos/01-webattack.md)) → payload+listener
([05](docs/modulos/05-payload-listener.md)) → PowerShell
([06](docs/modulos/06-powershell.md)) → Fast-Track
([10](docs/modulos/10-fasttrack.md)).
