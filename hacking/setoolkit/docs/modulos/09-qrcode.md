# QRCode Generator Attack Vector — menu 1 → 8

Gera um QR Code apontando para sua URL de teste. Base:
`src/qrcode/qrgenerator.py` (`gen_qrcode(url)`). Parte de [INDICE.md](INDICE.md).

## Como funciona

Usa a lib `qrcode` (correção de erro L), renderiza o PNG e salva em
`~/.set/reports/qrcode_attack.png`. Informe a URL (ex.: seu harvester no
lab) e distribua o QR no exercício: quantos escaneiam? Os acessos aparecem no
servidor web do SET.
