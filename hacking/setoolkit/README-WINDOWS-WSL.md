# SET no Windows (via WSL2) — Global-Tools

O SET **não roda nativo no Windows**. O README oficial pede Linux, macOS
experimental ou Windows via WSL/WSL2. O Python do Windows aqui é 3.14 e o
SET 8.1.3 exige Python 3.11–3.13, por isso usamos o Ubuntu 24.04 do WSL
(Python 3.12). Testado: `compileall` OK, **34 testes passed**, menu abre e
pede root como esperado.

## Duas cópias: entenda

| Cópia | Caminho | Papel |
|---|---|---|
| Referência | `Global-Tools/hacking/setoolkit/` (esta pasta) | Leitura, launchers, docs. Trazida de `C:\Users\keila\Mateus\setoolkit` (sem `.venv/`, `.git/`, `__pycache__/`). |
| Executável | `~/setoolkit` **dentro** do WSL (ext4) | É a que realmente roda. Clonada do GitHub pelo script abaixo. |

Por quê? O Windows Defender detecta o SET/impacket como hacktool por
assinatura e colocou `src/core/setcore.py` em quarentena durante os testes
(arquivo depois restaurado). No `/mnt/c` qualquer scan trava a execução;
no ext4 do WSL isso não acontece. Venv no `/mnt/c` também quebra
(`Errno 22`); o venv funcional mora em `~/.venvs/setoolkit`.

## Como rodar (recomendado)

Duplo clique em `hacking/setoolkit/run-setoolkit.bat`, ou no PowerShell:

```powershell
wsl -d Ubuntu -- bash -lc "cd /home/keila/setoolkit && sudo /home/keila/.venvs/setoolkit/bin/python /home/keila/setoolkit/setoolkit"
```

Vai pedir a **senha do WSL (sudo)** — digite e tecle Enter. Na primeira vez,
aceite os termos (`y`) e o SET cria `/etc/setoolkit/set.config`.

## Setup do zero (dentro do WSL)

```bash
bash /mnt/c/Users/keila/Mateus/Global-Tools/hacking/setoolkit/run-setoolkit-wsl.sh
```

O script clona `https://github.com/trustedsec/social-engineer-toolkit/`
em `~/setoolkit`, cria `~/.venvs/setoolkit`, instala `requirements.txt` e
inicia com `sudo`. Equivalente manual:

```bash
git clone --depth 1 https://github.com/trustedsec/social-engineer-toolkit/ ~/setoolkit
python3 -m venv ~/.venvs/setoolkit
~/.venvs/setoolkit/bin/pip install --upgrade pip
~/.venvs/setoolkit/bin/pip install -r ~/setoolkit/requirements.txt
cd ~/setoolkit && sudo ~/.venvs/setoolkit/bin/python ~/setoolkit/setoolkit
```

## Observações

- Nunca crie venv dentro de `/mnt/c` — use sempre `~/.venvs/setoolkit`.
- Não commitar venvs: `.venv/`, `.venv-wsl/` (ver `.gitignore`).
- Se o Defender voltar a quarentenar a cópia de referência, restaure pela
  central do Defender; a cópia executável no WSL não é afetada.
- Uso somente autorizado (pentest consentido, lab). Veja `readme/LICENSE` e `SECURITY.md`.
