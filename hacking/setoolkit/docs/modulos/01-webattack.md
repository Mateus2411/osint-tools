# Website Attack Vectors — menu 1 → 2

O módulo web (`src/webattack/`) clona ou monta um site atacante e sobe um
servidor HTTP próprio (porta `WEB_PORT=80` por padrão) para receber as
vítimas do teste. Parte de [INDICE.md](INDICE.md).

## Métodos

| Método | Como funciona |
|---|---|
| **Credential Harvester** (`harvester/harvester.py`) | Serve o site clonado e intercepta todo `POST` (login/senha digitados). Grava em `src/logs/harvester.log` e exibe no terminal com IP e horário. Não entrega payload — só prova que a credencial seria roubada. `HARVESTER_REDIRECT`/`HARVESTER_URL` redirecionam a vítima após a captura; `HARVESTER_LOG_PASSWORDS` controla o log de senhas |
| **Site Cloner** (`web_clone/cloner.py`) | Baixa o HTML do alvo (com `USER_AGENT_STRING` de Chrome) e reescreve os formulários para postar no servidor do SET |
| **Web Templates** | Modelos prontos (Google, Twitter etc.) em `src/html/templates/` — dispensa clonagem |
| **Tabnabbing** (`tabnabbing/`) | Página que detecta a troca de aba e recarrega conteúdo falso para roubar o próximo login |
| **Web Jacking** | Iframe que exibe o site real mas troca o link clicado pelo malicioso (`WEBJACKING_TIME=2000` ms) |
| **Multi-Attack** (`multi_attack/`) | Combina applet + harvester + tabnabbing na mesma página (`AUTO_REDIRECT=ON` redireciona após o primeiro sucesso) |
| **HTA Attack** (`hta/`) | Site clonado que entrega arquivo `.hta` com injeção PowerShell (alvos Windows) |
| **Java Applet** | Applet assinado falsamente (`JAVA_ID_PARAM`) que executa payload Metasploit; `JAVA_REPEATER=ON` reinsiste se a vítima clicar "cancelar" |
| **Browser Exploit** (`browser_exploits/gen_payload.py`) | Iframe que testa ~40 exploits de navegador (Flash, IE, Java…) via `METASPLOIT_IFRAME_PORT=8080` |
| **Web Profiler** (`profiler/`) | Identifica versões/software da máquina visitante (ligado por `WEB_PROFILER`, hoje OFF por padrão) |
| **DLL Hijacking** (`dll_hijacking/`) | Compacta em ZIP/RAR um documento + DLL maliciosa: ao abrir o arquivo, a DLL chama o payload |

## Como montar o site

Após escolher o método:

```
1) Web Templates  → modelos prontos, sem precisar de alvo
2) Site Cloner    → informa a URL e o SET copia e reescreve os formulários
3) Custom Import  → importa seu próprio index.html
```

## Exemplo (harvester no lab)

```
set> 1  (Social-Engineering Attacks) → 2 (Website) → 3 (Credential Harvester)
→ 2 (Site Cloner) → LHOST 127.0.0.1 → URL http://localhost:8000/login
```

Acesse `http://127.0.0.1`, digite um login falso e confira o terminal e
`~/.set/reports/`. Encerra com `Ctrl+C`.

## Extras

- `UNC_EMBED=ON` injeta `img src` UNC para capturar hashes LM via SMB
- `WEBATTACK_SSL` + `SELF_SIGNED_CERT` servem tudo em HTTPS
- `APACHE_SERVER=ON` troca o servidor Python pelo Apache (`APACHE_DIRECTORY`)
