# Guia de Uso do SET em Português — Social-Engineer Toolkit 8.1.3

> **Aviso:** use somente em testes **autorizados** (lab, localhost, red team com
> consentimento e escopo por escrito). Sem autorização é crime (ex.: art. 154-A
> do Código Penal, LGPD). O SET é ferramenta de auditoria, não de ataque real.

## 1. Iniciando

```powershell
# PowerShell (pede a senha do WSL). O cd é obrigatório:
wsl -d Ubuntu -- bash -lc "cd /home/keila/setoolkit && sudo /home/keila/.venvs/setoolkit/bin/python /home/keila/setoolkit/setoolkit"
```

```bash
# Dentro do WSL:
cd ~/setoolkit && sudo ~/.venvs/setoolkit/bin/python ~/setoolkit/setoolkit
```

Na primeira vez digite `y` para aceitar os termos. O prompt do SET é `set>`.

## 2. Menu principal

```
1) Social-Engineering Attacks      → vetores de engenharia social (o coração do SET)
2) Penetration Testing (Fast-Track)→ pentest rápido (MSSQL, exploits, enumeração)
3) Third Party Modules             → módulos de terceiros (pasta modules/)
4) Update the Social-Engineer Toolkit → atualiza via git
5) Update SET configuration        → reconfigura IP, Metasploit, etc.
6) Help, Credits, and About
99) Exit
```

## 3. Opção 1 — Social-Engineering Attacks

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
1) Perform a Mass Email Attack   → envia e-mails com anexo malicioso (usa templates)
2) Create a FileFormat Payload   → só gera o arquivo (PDF, DOC etc.) com payload
3) Create a Social-Engineering Template → cria seu template de e-mail/arquivo
```

Fluxo típico: escolha o exploit de fileformat (ex.: `Adobe PDF Embedded EXE`),
o payload (ex.: reverse TCP), o IP de retorno (LHOST) e gere o arquivo. Depois
use a opção 1 para disparar no lab ou a 2 para pegar só o arquivo.

### 3.2 Website Attack Vectors (2) — o mais usado

```
1) Java Applet Attack Method        → exige Metasploit; applet falso com payload
2) Metasploit Browser Exploit Method→ iframe com exploit de navegador (lista de ~40)
3) Credential Harvester Attack Method → clona site e rouba login digitado (SEM payload)
4) Tabnabbing Attack Method         → troca a aba quando a vítima muda de tab
5) Web Jacking Attack Method        → iframe que falsifica o link legítimo
6) Multi-Attack Web Method          → combina vários métodos de uma vez
7) HTA Attack Method                → site clonado + PowerShell via arquivo .hta
```

Depois de escolher o método, o SET pergunta **como montar o site**:

```
1) Web Templates  → modelos prontos (Google, Twitter etc.)
2) Site Cloner    → clona qualquer URL que você informar
3) Custom Import  → importa seu próprio index.html
```

**Exemplo guiado — Credential Harvester no lab:**

```
set> 1          (Social-Engineering Attacks)
set> 2          (Website Attack Vectors)
set> 3          (Credential Harvester)
set> 2          (Site Cloner)
IP de retorno:  127.0.0.1            (seu IP no lab)
URL a clonar:   http://localhost:8000/login   (seu alvo de TESTE)
```

O SET sobe um servidor na porta 80. Acesse `http://127.0.0.1`, digite um
login falso e veja o relatório no terminal + em `~/.set/reports/`. Para parar,
`Ctrl+C`. O harvester só captura o que é digitado — ideal para provar risco
sem entregar payload.

### 3.3 Infectious Media Generator (3)

```
1) File-Format Exploits            → USB/CD com autorun.inf + exploit
2) Standard Metasploit Executable  → USB/CD com executável direto
```

Gera a estrutura para mídia física de teste (autorun desabilitado em Windows
modernos — valor mais didático que prático).

### 3.4 Create a Payload and Listener (4)

Gera payload + já abre o listener (quem recebe a conexão reversa). Sem
Metasploit instalado, as opções são as nativas do SET:

```
1) SE Toolkit Interactive Shell   → shell reverso próprio do SET
2) SE Toolkit HTTP Reverse Shell  → shell HTTP com AES
3) RATTE HTTP Tunneling Payload   → tunela tudo por HTTP
```

Com Metasploit configurado aparecem ainda Meterpreter via PowerShell,
shellcodeexec etc. Informe LHOST (seu IP) e LPORT (ex.: 443) e deixe o
terminal aberto aguardando a conexão do lab.

### 3.5 Mass Mailer Attack (5)

Disparo de e-mail em massa para a base do teste (usa sendmail do Linux;
configure `SENDMAIL=ON` na opção 5 do menu principal). Defina remetente,
destinatários, assunto e corpo/template, e revise antes de enviar — no lab,
aponte para contas de teste.

### 3.6 Arduino-Based Attack Vector (6)

Gera sketches `.pde` para Teensy/Arduino (dispositivo USB que se passa por
teclado). Opções: downloaders PowerShell, reverse shell, Beef hook, Binário
via Teensy, ataques X10 etc. Exige o hardware (~US$ 22) e o Arduino IDE.

### 3.7 Wireless Access Point Attack Vector (7)

```
1) Start → cria AP falso + DHCP + DNS spoof (exige AirBase-NG, AirMon-NG, DNSSpoof, dhcpd3)
2) Stop  → derruba o AP
```

Com o AP no ar, rode qualquer vetor web (ex.: harvester) e o tráfego da rede
de teste cai no seu servidor.

### 3.8 QRCode Generator Attack Vector (8)

Gera um QR Code apontando para sua URL de teste (ex.: o harvester). Útil para
campanhas de conscientização: quantos escaneiam? O relatório mostra os acessos.

### 3.9 Powershell Attack Vectors (9)

```
1) Powershell Alphanumeric Shellcode Injector → injeta shellcode via PowerShell
2) Powershell Reverse Shell                   → shell reverso em PS puro
3) Powershell Bind Shell                      → abre porta no alvo de teste
4) Powershell Dump SAM Database               → extrai hashes SAM (pós-exploração, lab)
```

Gera comandos `.ps1`/one-liners prontos para colar no ambiente de teste.

### 3.10 Third Party Modules (10)

Carrega módulos da pasta `modules/` (ex.: `ratte_module.py`,
`google_analytics_attack.py`). Para criar o seu, copie
`modules/test_module.example` e registre no menu.

## 4. Opção 2 — Penetration Testing (Fast-Track)

```
1) Microsoft SQL Bruter  → 1) Scan and Attack MSSQL | 2) Connect directly
2) Custom Exploits       → MS08-067, Firefox 3.6.16, SolarWinds SQLi, RDP DoS,
                           MySQL auth bypass, F5 auth bypass...
3) SCCM Attack Vector    → abuso de System Center Configuration Manager (lab)
4) Dell DRAC/Chassis Default Checker → testa credenciais padrão de iDRAC
5) RID_ENUM              → enumera usuários via RID cycling (alvo Windows/lab)
6) PSEXEC Powershell Injection → injeção PowerShell via PSEXEC
```

Exemplo: `2 → 1 → 1` escaneia a rede de teste em busca de MSSQL, tenta
credenciais fracas e, se conseguir, implanta o stager hexadecimal do SET.

## 5. Opções 3, 4, 5, 6

- **3 Third Party Modules:** mesmo da seção 3.10, atalho pelo menu principal.
- **4 Update:** `git pull` do repositório oficial. (A cópia de referência em
  `hacking/setoolkit/` não atualiza sozinha — rode `git pull` nela à parte.)
- **5 Update SET configuration:** edita `/etc/setoolkit/set.config` — IP
  externo/LHOST, caminho do Metasploit (`METASPLOIT_PATH`), SENDMAIL, etc.
  Rode após mudar de rede/lab.
- **6 Help/Credits:** ajuda, créditos e `readme/User_Manual.pdf` (manual
  completo, em inglês, na pasta `readme/`).

## 6. Utilitários de linha de comando

Estão na raiz do SET (rode do WSL, dentro de `~/setoolkit`):

| Comando | Para que serve |
|---|---|
| `sudo ./setoolkit` | menu interativo (o guia acima) |
| `./seautomate arquivo.txt` | executa o SET por script (respostas prontas, sem digitar) |
| `./seproxy` | proxy/relé auxiliar do SET |
| `./seupdate` | atualiza o SET sem abrir o menu |

Exemplo de `seautomate` (harvester automático no lab):

```
1
2
3
2
127.0.0.1
http://localhost:8000/login
```

## 7. Onde ficam os resultados

- Relatórios: `~/.set/reports/` (dentro do WSL)
- Logs: `~/setoolkit/src/logs/set_logfile.log`
- Config: `/etc/setoolkit/set.config` (+ `set.config.py` gerado)

## 8. Dicas de lab

1. **Ordem de aprendizado:** harvester (3.2) → payload+listener (3.4) →
   PowerShell (3.9) → Fast-Track (4). Sem Metasploit dá para aprender tudo
   o essencial.
2. **Rede:** prefira `127.0.0.1` ou uma VM/rede host-only; nunca a rede da
   empresa sem autorização escrita.
3. **Antivírus:** o Defender sinaliza o SET/impacket como hacktool. A cópia
   que roda mora no ext4 do WSL (`~/setoolkit`), fora do alcance dele.
4. **Limpeza:** `99` sai dos menus; `Ctrl+C` para servidores/listeners e
   responda `yes` para finalizar listeners presos.
