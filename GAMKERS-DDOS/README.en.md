# GAMKERS-DDOS

[Português](./README.md) | **English**

Optimized multithreaded UDP stress testing tool for Python 3.

> ⚠️ **FOR EDUCATIONAL PURPOSES / AUTHORIZED TESTING ONLY**
> Use only on localhost, your own lab, or infrastructure with explicit permission.
> Unauthorized attacks are **ILLEGAL**.

---

## 📋 Index

- [About](#-about)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Parameters](#-parameters)
- [Common Errors & Fixes](#-common-errors--fixes)
- [Performance Tips](#-performance-tips)
- [Legal Notice](#-legal-notice)

---

## 📋 About

GAMKERS-DDOS is a UDP stress testing tool with the following features:

- **Multithreaded**: own socket per thread for maximum throughput
- **No per-packet printing**: ~35x faster than legacy versions
- **CLI via argparse**: easy configuration of ports, threads, payload, and duration
- **Windows handling**: disables WSAECONNRESET to maintain high throughput
- **Rate reporter**: shows pps (packets per second) in real time

---

## 🔧 Prerequisites

- **Python 3.6+** (recommended: 3.10+)
- **pip** (Python package manager)
- No external libraries needed — uses only the standard library

---

## 🚀 Installation

### Method 1: Within the OSINT repository

```bash
cd GAMKERS-DDOS
```

Done — the script has zero dependencies, just needs Python.

### Method 2: Clone separately

```bash
git clone https://github.com/Mateus2411/osint-tools.git
cd osint-tools/GAMKERS-DDOS
```

### Verify it works

```bash
python GAMKERS-DDOS.py --help
```

---

## 🎯 How to Use

### Basic test (localhost)

```bash
python GAMKERS-DDOS.py 127.0.0.1
```

### With specific ports and duration

```bash
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10
```

This sends UDP packets to ports 80-65535, using 4 threads, for 10 seconds.

### Multiple threads with small payload (more pps)

```bash
python GAMKERS-DDOS.py 127.0.0.1 -p 9 -t 32 -s 64
```

### Silent mode (no rate reporter)

```bash
python GAMKERS-DDOS.py 127.0.0.1 -q -d 5
```

---

## ⚙️ Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `host` | Target IP or hostname (**required**) | — |
| `-p, --port` | Start port of the cycle | 80 |
| `-e, --end-port` | End port of the cycle | 65535 |
| `-t, --threads` | Number of threads | 4 |
| `-d, --duration` | Duration in seconds (0 = infinite) | 0 |
| `-s, --size` | Payload size in bytes | 1490 |
| `-q, --quiet` | Hide rate reporter | false |

### Example combinations

```bash
# Quick test: 5 seconds, 8 threads
python GAMKERS-DDOS.py 127.0.0.1 -t 8 -d 5

# Specific port with minimal payload
python GAMKERS-DDOS.py 127.0.0.1 -p 443 -e 443 -s 64 -d 3

# Specific port range
python GAMKERS-DDOS.py 127.0.0.1 -p 8000 -e 9000 -t 16 -d 20
```

---

## 🔧 Common Errors & Fixes

### `python: command not found`

**Cause:** Python is not installed or not in PATH.

**Fix:**
```bash
# Check if it exists
python --version
py --version

# If not, download from: https://www.python.org/downloads/
# ⚠️ Check "Add Python to PATH" during installation (Windows)
```

### `Permission denied` / `Access denied`

**Cause:** On Windows, firewall or antivirus blocks the script.

**Fix:**
```
1. Run the terminal as Administrator
2. Add exceptions in firewall/antivirus for:
   - python.exe
   - The project folder
```

### `OSError: [Errno 10054]` (Windows)

**Cause:** Target responds with ICMP Unreachable, poisoning the UDP socket.

**Fix:** This error is **handled automatically** by the script (recreates the socket). If it persists, reduce threads:
```bash
python GAMKERS-DDOS.py 127.0.0.1 -t 2
```

### `socket.gaierror: [Errno 8] nodename nor servname provided`

**Cause:** Hostname did not resolve.

**Fix:**
```bash
# Use a direct IP instead of hostname
# Discover the IP first:
nslookup example.com
ping example.com
```

### `Portas inválidas (1-65535, inicio <= fim)` / `Invalid ports`

**Cause:** Port out of range or start port greater than end port.

**Fix:**
```bash
# Start port must be <= end port, both between 1 and 65535
python GAMKERS-DDOS.py 127.0.0.1 -p 1 -e 65535
```

### `Payload inválido (1-65507 bytes)` / `Invalid payload`

**Cause:** Payload size outside UDP limits.

**Fix:**
```bash
# Range: 1 to 65507 bytes
python GAMKERS-DDOS.py 127.0.0.1 -s 64   # minimum efficient
python GAMKERS-DDOS.py 127.0.0.1 -s 65507 # theoretical max
```

### High CPU / PC freezes

**Cause:** Too many threads with large payload consume too much CPU.

**Fix:**
```bash
# Reduce threads and/or duration
python GAMKERS-DDOS.py 127.0.0.1 -t 2 -d 5

# Or use smaller payload (fewer bytes per packet = less CPU)
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 4 -d 10
```

### Result shows 0 packets

**Cause:** Target unreachable, firewall blocking, or duration too short.

**Fix:**
```bash
# Test on localhost first
python GAMKERS-DDOS.py 127.0.0.1 -p 9 -t 4 -d 5

# If it works on localhost but not on target:
# - Check if target is reachable: ping <ip>
# - Check if port is open: telnet <ip> <port>
# - Check local firewall
```

---

## 💡 Performance Tips

### PPS vs Payload

| Payload | Bytes on wire | PPS (~12 Mbps upload) |
|---------|-------------|----------------------|
| 1490 | ~1514 | ~1,000 |
| 512 | ~536 | ~2,900 |
| 128 | ~152 | ~10,000 |
| 64 | ~88 | ~16,000 |

> Each 1490-byte packet costs ~11.9 kbit on the network.
> Reducing payload to 64 bytes results in **~16x more packets/second**.

### Threads

- **2 threads**: ideal for loopback (localhost)
- **4 threads**: sweet spot for real networks
- **8-16 threads**: use with caution — may saturate CPU

### Optimizations in this version

1. **Socket per thread** — avoids lock contention on the socket
2. **No per-packet printing** — ~35x faster than legacy versions
3. **Sync every 500 packets** — minimizes lock overhead
4. **Reporter in separate thread** — doesn't block the send loop
5. **WSAECONNRESET handling** — maintains throughput on Windows

---

## ⚖️ Legal Notice

### ✅ Allowed Use
- Testing on your **own computer** (localhost)
- Security labs with dedicated infrastructure
- **Authorized** penetration testing (written consent)
- Academic and educational research

### ❌ Prohibited Use
- Attacks on third-party systems without authorization
- Any use that violates local or international laws
- DDoS against websites, services, or infrastructure

> **Responsibility:** Use of this tool is entirely the user's responsibility.
> Developers are not responsible for damages caused by misuse.

---

## 📚 Links

- **Repository**: https://github.com/Mateus2411/osint-tools
- **Original author**: GAMKERS (base template)
- **Optimized by**: Mateus2411
