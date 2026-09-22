# QRCode Generator Attack Vector — menu 1 → 8

Generates a QR Code pointing at your test URL. Base:
`src/qrcode/qrgenerator.py` (`gen_qrcode(url)`). Part of
[INDICE.en.md](INDICE.en.md).

## How it works

Uses the `qrcode` lib (error correction L), renders the PNG and saves it to
`~/.set/reports/qrcode_attack.png`. Enter the URL (e.g. your lab harvester)
and hand out the QR in the exercise: how many scan it? Hits show up on the SET
web server.
