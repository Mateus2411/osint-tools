# GAMKERS-DDOS

Ferramenta de teste de stress UDP multithread otimizada para Python 3.

> ⚠️ **APENAS PARA FINS EDUCACIONAIS / TESTES AUTORIZADOS**
> Use apenas em localhost, laboratório próprio ou infraestrutura com permissão explícita.
> Ataque sem autorização é **ILEGAL**.

---

## 📋 Índice

- [Sobre](#-sobre)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Parâmetros](#parâmetros)
- [Erros Comuns & Soluções](#-erros-comuns--soluções)
- [Dicas de Performance](#-dicas-de-performance)
- [Considerações Legais](#-considerações-legais)

---

## 📋 Sobre

O GAMKERS-DDOS é uma ferramenta de teste de stress UDP com as seguintes características:

- **Multithread**: socket próprio por thread para máximo throughput
- **Sem print por pacote**: ~35x mais rápido que versões legadas
- **CLI via argparse**: configuração fácil de portas, threads, payload e duração
- **Tratamento de Windows**: desabilita WSAECONNRESET para manter throughput alto
- **Reporter de taxa**: mostra pps (pacotes por segundo) em tempo real

---

## 🔧 Pré-requisitos

- **Python 3.6+** (recomendado: 3.10+)
- **pip** (gerenciador de pacotes do Python)
- Não precisa de bibliotecas externas — usa apenas a stdlib

---

## 🚀 Instalação

### Método 1: Dentro do repositório OSINT

```bash
cd GAMKERS-DDOS
```

Pronto — o script é dependência zero, só precisa do Python.

### Método 2: Clonar separadamente

```bash
git clone https://github.com/Mateus2411/osint-tools.git
cd osint-tools/GAMKERS-DDOS
```

### Verificar que funciona

```bash
python GAMKERS-DDOS.py --help
```

---

## 🎯 Como Usar

### Teste básico (localhost)

```bash
python GAMKERS-DDOS.py 127.0.0.1
```

### Com portas e duração específicas

```bash
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10
```

Isso envia pacotes UDP para as portas 80-65535, usando 4 threads, por 10 segundos.

### Múltiplas threads com payload pequeno (mais pps)

```bash
python GAMKERS-DDOS.py 127.0.0.1 -p 9 -t 32 -s 64
```

### Modo silencioso (sem reporter de taxa)

```bash
python GAMKERS-DDOS.py 127.0.0.1 -q -d 5
```

---

## ⚙️ Parâmetros

| Parâmetro | Descrição | Padrão |
|-----------|-----------|--------|
| `host` | IP ou hostname do alvo (**obrigatório**) | — |
| `-p, --port` | Porta inicial do ciclo | 80 |
| `-e, --end-port` | Porta final do ciclo | 65535 |
| `-t, --threads` | Número de threads | 4 |
| `-d, --duration` | Duração em segundos (0 = infinito) | 0 |
| `-s, --size` | Tamanho do payload em bytes | 1490 |
| `-q, --quiet` | Esconde o reporter de taxa | false |

### Exemplos de combinação

```bash
# Teste rápido: 5 segundos, 8 threads
python GAMKERS-DDOS.py 127.0.0.1 -t 8 -d 5

# Porta específica com payload mínimo
python GAMKERS-DDOS.py 127.0.0.1 -p 443 -e 443 -s 64 -d 3

# Range de portas específico
python GAMKERS-DDOS.py 127.0.0.1 -p 8000 -e 9000 -t 16 -d 20
```

---

## 🔧 Erros Comuns & Soluções

### `python: command not found`

**Causa:** Python não está instalado ou não está no PATH.

**Solução:**
```bash
# Verificar se existe
python --version
py --version

# Se não existir, baixar em: https://www.python.org/downloads/
# ⚠️ Marcar "Add Python to PATH" durante instalação (Windows)
```

### `Permission denied` / `Access denied`

**Causa:** No Windows, o firewall ou antivírus bloqueia o script.

**Solução:**
```
1. Execute o terminal como Administrador
2. Adicione exceção no firewall/antivírus para:
   - python.exe
   - A pasta do projeto
```

### `OSError: [Errno 10054]` (Windows)

**Causa:** O alvo responde com ICMP Unreachable, envenenando o socket UDP.

**Solução:** Esse erro é **tratado automaticamente** pelo script (recria o socket). Se persistir, reduza o número de threads:
```bash
python GAMKERS-DDOS.py 127.0.0.1 -t 2
```

### `socket.gaierror: [Errno 8] nodename nor servname provided`

**Causa:** Hostname não resolveu.

**Solução:**
```bash
# Usar IP direto em vez de hostname
# Descobrir o IP primeiro:
nslookup exemplo.com
ping exemplo.com
```

### `Portas inválidas (1-65535, inicio <= fim)`

**Causa:** Porta fora do range ou porta inicial maior que final.

**Solução:**
```bash
# Porta inicial deve ser <= porta final, ambas entre 1 e 65535
python GAMKERS-DDOS.py 127.0.0.1 -p 1 -e 65535
```

### `Payload inválido (1-65507 bytes)`

**Causa:** Tamanho do payload fora do limite UDP.

**Solução:**
```bash
# Limite: 1 a 65507 bytes
python GAMKERS-DDOS.py 127.0.0.1 -s 64   # mínimo eficiente
python GAMKERS-DDOS.py 127.0.0.1 -s 65507 # máximo teórico
```

### Alta CPU / PC trava

**Causa:** Muitas threads com payload grande consomem muita CPU.

**Solução:**
```bash
# Reduza threads e/ou duração
python GAMKERS-DDOS.py 127.0.0.1 -t 2 -d 5

# Ou use payload menor (menos bytes por pacote = menos CPU)
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 4 -d 10
```

### Resultado mostra 0 pacotes

**Causa:** Alvo inacessível, firewall bloqueando, ou duração muito curta.

**Solução:**
```bash
# Teste primeiro no localhost
python GAMKERS-DDOS.py 127.0.0.1 -p 9 -t 4 -d 5

# Se funcionar no localhost mas não no alvo:
# - Verifique se o alvo está acessível: ping <ip>
# - Verifique se a porta está aberta: telnet <ip> <porta>
# - Verifique o firewall local
```

---

## 💡 Dicas de Performance

### PPS vs Payload

| Payload | Bytes no fio | PPS (~12 Mbps upload) |
|---------|-------------|----------------------|
| 1490 | ~1514 | ~1.000 |
| 512 | ~536 | ~2.900 |
| 128 | ~152 | ~10.000 |
| 64 | ~88 | ~16.000 |

> Cada pacote de 1490 bytes custa ~11.9 kbit na rede.
> Reduzir o payload pra 64 bytes resulta em **~16x mais pacotes/segundo**.

### Threads

- **2 threads**: ideal para loopback (localhost)
- **4 threads**: sweet spot para rede real
- **8-16 threads**: use com cuidado — pode saturar a CPU

### Otimizações aplicadas nesta versão

1. **Socket por thread** — evita contenção de lock no socket
2. **Sem print por pacote** — ~35x mais rápido que versões legadas
3. **Sync a cada 500 pacotes** — minimiza overhead de lock
4. **Reporter em thread separada** — não bloqueia o loop de envio
5. **Tratamento de WSAECONNRESET** — mantém throughput no Windows

---

## ⚖️ Considerações Legais

### ✅ Uso Permitido
- Testes no **próprio computador** (localhost)
- Laboratórios de segurança com infraestrutura dedicada
- Pentest **autorizado** por escrito
- Pesquisa acadêmica e educacional

### ❌ Uso Proibido
- Ataques a sistemas de terceiros sem autorização
- Qualquer uso que viole leis locais ou internacionais
- DDoS contra sites, serviços ou infraestrutura

> **Responsabilidade:** O uso desta ferramenta é de inteira responsabilidade do usuário.
> Os desenvolvedores não se responsabilizam por danos causados por uso indevido.

---

## 📚 Links

- **Repositório**: https://github.com/Mateus2411/osint-tools
- **Autor original**: GAMKERS (template base)
- **Otimizado por**: Mateus2411
