# Create a Payload and Listener — menu 1 → 4

Gera o binário e **já abre o listener** que recebe a conexão reversa
(`AUTOMATIC_LISTENER=ON`). Base: `src/payloads/` + `src/core/payloadgen/`.
Parte de [INDICE.md](INDICE.md).

## Payloads nativos (sem Metasploit)

| Payload | Arquivo-base | Ideia |
|---|---|---|
| SE Toolkit Interactive Shell | `set_payloads/` | shell reverso próprio, via stager que baixa o estágio 2 (`SET_SHELL_STAGER`) |
| SE Toolkit HTTP Reverse Shell | `set_payloads/http_shell.py`, `set_http_server.py` | shell puro em HTTP com AES |
| RATTE HTTP Tunneling Payload | `payloads/ratte/` | tunela toda a comunicação por HTTP para furar filtragem de saída |

Com Metasploit configurado somem Meterpreter via PowerShell, multi-injeção e
shellcodeexec.

## Como usar

Informe LHOST (seu IP no lab) e LPORT (ex.: 443) e **deixe o terminal aberto**:
ele fica aguardando a conexão reversa e registra as sessões na tela.
`STAGE_ENCODING`, `UPX_ENCODE` e `ENCOUNT=4` tentam ofuscar o binário contra
antivírus básico.
