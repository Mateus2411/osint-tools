# setoolkit — Social-Engineer Toolkit (via WSL2)

**Pasta:** `hacking/setoolkit/` · **Site:** https://github.com/trustedsec/social-engineer-toolkit

> Somente testes autorizados. O Defender pode sinalizar como hacktool.

## O que é

Framework de vetores guiados de engenharia social para red team autorizado:
phishing, credential harvester, payloads, PowerShell, Fast-Track e mais.
Roda via **WSL2 Ubuntu** (Python 3.12): `run-setoolkit.bat` ou

```powershell
wsl -d Ubuntu -- bash -lc "cd /home/keila/setoolkit && sudo /home/keila/.venvs/setoolkit/bin/python /home/keila/setoolkit/setoolkit"
```

## Documentação completa (já pronta na pasta)

| Doc | Conteúdo |
|---|---|
| `hacking/setoolkit/MODULOS.md` | visão geral + estrutura + mapa dos módulos |
| `hacking/setoolkit/docs/modulos/INDICE.md` | índice: 1 arquivo por módulo (12) |
| `hacking/setoolkit/GUIA-DE-USO.md` | passo a passo tecla por tecla |
| `hacking/setoolkit/README-WINDOWS-WSL.md` | setup Windows/WSL |

(Todas com versão `.en.md` correspondente.)
