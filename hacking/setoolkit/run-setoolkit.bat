@echo off
REM Launcher SET (Social-Engineer Toolkit) via WSL2 Ubuntu - Global-Tools
REM O codigo executavel mora em ~/setoolkit dentro do WSL (ext4), imune ao Defender.
REM Uso: duplo clique ou .\run-setoolkit.bat
REM Vai pedir a senha do WSL (sudo) — digite e tecle Enter.
wsl -d Ubuntu -- bash -lc "cd /home/keila/setoolkit && sudo /home/keila/.venvs/setoolkit/bin/python /home/keila/setoolkit/setoolkit"
pause
