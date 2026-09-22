#!/bin/bash
# Setup + launcher do SET no WSL2 Ubuntu ( Rode DENTRO do WSL: bash run-setoolkit-wsl.sh )
# O codigo executavel mora em ~/setoolkit (ext4). Esta pasta no /mnt/c e copia de referencia.
set -e
REPO_URL="https://github.com/trustedsec/social-engineer-toolkit/"
TARGET="$HOME/setoolkit"
VENV="$HOME/.venvs/setoolkit"

if [ ! -d "$TARGET" ]; then
  echo "[*] Clonando SET em $TARGET ..."
  git clone --depth 1 "$REPO_URL" "$TARGET"
fi
if [ ! -d "$VENV" ]; then
  echo "[*] Criando venv $VENV (Python 3.11-3.13)..."
  python3 -m venv "$VENV"
fi
"$VENV/bin/pip" install --upgrade pip
"$VENV/bin/pip" install -r "$TARGET/requirements.txt"
echo "[*] Iniciando SET (precisa de root — vai pedir a senha do WSL)..."
sudo "$VENV/bin/python" "$TARGET/setoolkit" "$@"
