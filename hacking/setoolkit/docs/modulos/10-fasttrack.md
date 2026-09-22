# Fast-Track Penetration Testing — menu 2

Vetores de pentest rápido herdados do Fast-Track, 100% Python. Base:
`src/fasttrack/`. Parte de [INDICE.md](INDICE.md).

| Vetor | Arquivo | Como funciona |
|---|---|---|
| **Microsoft SQL Bruter** | `mssql.py` → `Scan and Attack` varre a rede atrás de MSSQL e testa senhas fracas; ao entrar, converte um binário em hexadecimal, implanta por estágios via SQL e reconverte no alvo para executar |
| **Connect directly** | Abre sessão SQL direta com credencial conhecida |
| **Custom Exploits** | `exploits/`: MS08-067, Firefox 3.6.16 mChannel, SolarWinds Storage Manager SQLi, RDP DoS, MySQL auth bypass, F5 root bypass |
| **SCCM Attack Vector** | `sccm/`: abuso de servidor SCCM para distribuir payload na rede gerenciada (lab) |
| **Dell DRAC Checker** | `delldrac.py`: testa credenciais padrão em iDRAC/chassis Dell |
| **RID_ENUM** | `ridenum.py`: enumera usuários Windows via RID cycling contra o alvo |
| **PSEXEC Injection** | `psexec.py`: execução/injeção PowerShell via PSEXEC no alvo autenticado |

Exemplo: `2 → 1 → 1` escaneia, brute-força e implanta o stager — tudo guiado
por perguntas no terminal.
