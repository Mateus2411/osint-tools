# Powershell Attack Vectors — menu 1 → 9

Leverages PowerShell present on every Windows Vista+ — less detected than `.exe`.
Base: `src/powershell/`. Part of [INDICE.en.md](INDICE.en.md).

## Options

```
1) Powershell Alphanumeric Shellcode Injector → injects alphanumeric shellcode into memory
2) Powershell Reverse Shell                   → pure-PS reverse one-liner
3) Powershell Bind Shell                      → opens a listening port on the test target
4) Powershell Dump SAM Database               → dumps SAM/SYSTEM hashes (post-exploitation)
```

## How it works

Each option generates ready-to-paste `.ps1`/one-liners for the test
environment. Fine tuning in `set.config`:

- `POWERSHELL_INJECTION=ON` — couples the injection to the Java Applet as a
  second stage
- `POWERSHELL_MULTI_INJECTION=ON` — sprays ports `21,22,25,53,443`
  (`POWERSHELL_MULTI_PORTS`) until one gets out
- `POWERSHELL_VERBOSE=ON` — prints the generated code (study/debug)
