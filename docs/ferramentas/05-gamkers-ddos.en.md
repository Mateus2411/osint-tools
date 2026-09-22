# GAMKERS-DDOS — UDP stress test

**Folder:** `hacking/GAMKERS-DDOS/` · **Zero dependencies** (stdlib only) ·
**Run:** `python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10`

> **Localhost/own lab with authorization only.** Traffic against third parties
> without consent is a crime, even "just testing".

## What it is and how it works

Multithreaded UDP packet generator for resilience measurement (`GAMKERS-DDOS.py`):

- **Worker per thread** (`flood`): each thread owns a UDP socket and cycles the
  port range (`port += 1`, wraps around)
- **No per-packet printing** (~35x faster): local counter synced every
  `SYNC_EVERY=500` packets under lock; reporter shows live **pps**
- **Windows anti-stall**: disables `SIO_UDP_CONNRESET` via direct `WSAIoctl`
  and recreates the socket on error 10054 (ICMP unreachable)
- Random payload of `DEFAULT_PAYLOAD_SIZE=1490` bytes (limits 1–65507)

## Usage

```bash
cd hacking/GAMKERS-DDOS
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10   # 4 threads, 10s, port 80
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 8 -d 5    # smaller payload = more pps
```

Flags: `-p` port/range, `-t` threads (2–4 loopback, 4–8 LAN), `-d` duration in
seconds, `-s` payload size. Always start small and scale up.
