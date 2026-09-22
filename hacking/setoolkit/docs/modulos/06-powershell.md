# Powershell Attack Vectors — menu 1 → 9

Aproveita que todo Windows Vista+ tem PowerShell — menos detectado que `.exe`.
Base: `src/powershell/`. Parte de [INDICE.md](INDICE.md).

## Opções

```
1) Powershell Alphanumeric Shellcode Injector → injeta shellcode alfanumérico na memória
2) Powershell Reverse Shell                   → one-liner reverso em PS puro
3) Powershell Bind Shell                      → abre porta de escuta no alvo de teste
4) Powershell Dump SAM Database               → extrai hashes SAM/SYSTEM (pós-exploração)
```

## Como funciona

Cada opção gera comandos `.ps1`/one-liners prontos para colar no ambiente de
teste. Ajustes finos no `set.config`:

- `POWERSHELL_INJECTION=ON` — acopla a injeção ao Java Applet como segundo estágio
- `POWERSHELL_MULTI_INJECTION=ON` — pulveriza as portas `21,22,25,53,443`
  (`POWERSHELL_MULTI_PORTS`) até uma sair
- `POWERSHELL_VERBOSE=ON` — mostra o código gerado (estudo/debug)
