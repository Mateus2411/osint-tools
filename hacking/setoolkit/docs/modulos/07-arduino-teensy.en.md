# Arduino-Based Attack Vector — menu 1 → 6

Generates sketches for Teensy/Arduino, which the PC sees as a **USB
keyboard** — bypassing disabled autorun and some endpoint protection. Base:
`src/teensy/` (`teensy_gen.py`, `ino_gen.py`, `ino_header.txt`/`ino_tail.txt`).
Part of [INDICE.en.md](INDICE.en.md).

## Options

PowerShell and WSCRIPT downloaders, reverse shell, Beef hook, "go to the
malicious site and accept the applet", `Binary 2 Teensy` (converts an EXE with
`binary2teensy.py`), `SDCard 2 Teensy` (Windows and OSX), X10 sniffer/jammer,
direct shellcode and dip-switch + SDCard multi-attack.

## How to use it

Pick the payload in the menu, import the generated `.pde` into the Arduino IDE
and flash the device. Requires the hardware (~US$ 22). Typical authorized
physical test: the plugged device types the downloader by itself and calls the
SET listener (see `05-payload-listener.en.md`).
