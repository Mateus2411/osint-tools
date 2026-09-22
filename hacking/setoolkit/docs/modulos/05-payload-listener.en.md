# Create a Payload and Listener — menu 1 → 4

Generates the binary **and already opens the listener** that receives the
reverse connection (`AUTOMATIC_LISTENER=ON`). Base: `src/payloads/` +
`src/core/payloadgen/`. Part of [INDICE.en.md](INDICE.en.md).

## Native payloads (no Metasploit)

| Payload | Base files | Idea |
|---|---|---|
| SE Toolkit Interactive Shell | `set_payloads/` | own reverse shell, via a stager that downloads stage 2 (`SET_SHELL_STAGER`) |
| SE Toolkit HTTP Reverse Shell | `set_payloads/http_shell.py`, `set_http_server.py` | pure-HTTP shell with AES |
| RATTE HTTP Tunneling Payload | `payloads/ratte/` | tunnels all comms over HTTP to beat egress filtering |

With Metasploit configured you additionally get PowerShell Meterpreter,
multi-injection and shellcodeexec.

## How to use it

Enter LHOST (your lab IP) and LPORT (e.g. 443) and **leave the terminal open**:
it waits for the reverse connection and logs sessions on screen.
`STAGE_ENCODING`, `UPX_ENCODE` and `ENCOUNT=4` attempt to obfuscate the binary
against basic antivirus.
