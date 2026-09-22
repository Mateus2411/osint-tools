# Infectious Media Generator — menu 1 → 3

Gera estrutura de mídia física de teste (USB/CD/DVD). Parte de
[INDICE.md](INDICE.md).

## Opções

```
1) File-Format Exploits            → autorun.inf + exploit de documento
2) Standard Metasploit Executable  → executável direto
```

## Como funciona

Monta a árvore de arquivos pronta para gravar na mídia: o `autorun.inf`
aponta para o payload, executado ao inserir o dispositivo — **se** o autorun
estiver habilitado. Como Windows modernos bloqueiam autorun, o valor hoje é
didático: demonstra o vetor "pendrive perdido no estacionamento" em exercícios
de conscientização.
