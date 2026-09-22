# Infectious Media Generator — menu 1 → 3

Builds physical-media test layouts (USB/CD/DVD). Part of
[INDICE.en.md](INDICE.en.md).

## Options

```
1) File-Format Exploits            → autorun.inf + document exploit
2) Standard Metasploit Executable  → straight executable
```

## How it works

Assembles the file tree ready to burn onto the media: `autorun.inf` points at
the payload, executed when the device is inserted — **if** autorun is enabled.
Since modern Windows blocks autorun, the value today is educational: it
demonstrates the "lost USB stick in the parking lot" vector in awareness
exercises.
