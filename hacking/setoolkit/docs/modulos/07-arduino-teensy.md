# Arduino-Based Attack Vector — menu 1 → 6

Gera sketches para Teensy/Arduino, que o PC reconhece como **teclado USB** —
bypassa autorun desabilitado e parte da proteção de endpoint. Base:
`src/teensy/` (`teensy_gen.py`, `ino_gen.py`, `ino_header.txt`/`ino_tail.txt`).
Parte de [INDICE.md](INDICE.md).

## Opções

Downloaders PowerShell e WSCRIPT, reverse shell, hook do Beef, "vá ao site
malicioso e aceite o applet", `Binary 2 Teensy` (converte EXE com
`binary2teensy.py`), `SDCard 2 Teensy` (Windows e OSX), sniffer/jammer X10,
shellcode direto e multi-ataque com dip switch + SDCard.

## Como usar

Escolha o payload no menu, importe o `.pde` gerado no Arduino IDE e grave no
dispositivo. Exige o hardware (~US$ 22). Uso típico em teste físico autorizado:
dispositivo plugado digita sozinho o downloader e chama o listener do SET
(ver `05-payload-listener.md`).
