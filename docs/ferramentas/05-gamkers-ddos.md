# GAMKERS-DDOS — teste de stress UDP

**Pasta:** `hacking/GAMKERS-DDOS/` · **Dependência zero** (só stdlib) ·
**Uso:** `python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10`

> **Somente localhost/lab próprio com autorização.** Tráfego contra terceiros
> sem consentimento é crime, mesmo "só testando".

## O que é e como funciona

Gerador de pacotes UDP multithread para medir resistência (`GAMKERS-DDOS.py`):

- **Worker por thread** (`flood`): cada thread tem socket UDP próprio e varre
  o intervalo de portas ciclicamente (`port += 1`, volta ao início)
- **Sem print por pacote** (~35x mais rápido): contador local sincronizado a
  cada `SYNC_EVERY=500` pacotes com lock; repórter mostra **pps em tempo real**
- **Anti-travamento no Windows**: desliga `SIO_UDP_CONNRESET` via `WSAIoctl`
  direto e recria o socket no erro 10054 (ICMP unreachable)
- Payload aleatório de `DEFAULT_PAYLOAD_SIZE=1490` bytes (limites 1–65507)

## Uso

```bash
cd hacking/GAMKERS-DDOS
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10   # 4 threads, 10s, porta 80
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 8 -d 5    # payload menor = mais pps
```

Flags: `-p` porta/faixa, `-t` threads (2–4 loopback, 4–8 rede), `-d` duração
em segundos, `-s` tamanho do payload. Comece sempre pequeno e suba aos poucos.
