# Ferramentas de OSINT - Guia Completo

<p align="center">
  <a href="./README.en.md">🇬🇧 English</a> | <b>🇧🇷 Português</b>
</p>

<sub style="color:gray;">
Todas as ferramentas disponibilizadas devem ser utilizadas de forma ética e responsável.
O uso indevido para comprometer a segurança ou privacidade de terceiros não é recomendado.
</sub>

---

## 🛠️ Ferramentas Disponíveis

### 1️⃣ [Holehe](./holohe/) 📧
**Ferramenta para descobrir contas associadas a e-mail**
- **Repositório**: https://github.com/megadose/holehe
- **Função**: Verificar contas em mais de 100 sites (Instagram, Twitter, etc)
- **Pré-requisito**: Python 3.6+
- **Instalação**: `pip install holehe`
- **Uso**: `holehe email@email.com`

### 2️⃣ [SpiderFoot](./spiderfoot/) 🕷️
**Ferramenta extremamente poderosa de OSINT automático**
- **Repositório**: https://github.com/smicallef/spiderfoot
- **Função**: Investigação completa e automática
- **Alvos**: Domínios, emails, IPs, telefones, empresas, vazamentos
- **Interface**: Web + CLI
- **Uso**: `py -3.14 sf.py -l 127.0.0.1:5001`

### 3️⃣ [theHarvester](./theHarvester/) 🌾
**Ferramenta clássica para coleta de informações OSINT**
- **Repositório**: https://github.com/laramies/theHarvester
- **Função**: Coleta de emails, subdomínios, hosts, IPs de múltiplas fontes
- **Fontes**: Google, Bing, SHODAN, VirusTotal, DNSDumpster, +40 outras
- **Instalação**: `pip install theHarvester`
- **Uso**: `theHarvester -d dominio.com -b google,bing`

### 4️⃣ [Mr.Holmes](./Mr.Holmes/) 🔍
**Ferramenta de coleta de informações (OSINT) com interface gráfica**
- **Repositório**: https://github.com/Lucksi/Mr.Holmes
- **Função**: Coletar informações sobre domínios, usernames e telefones via fontes públicas
- **Extras**: Google Dorks, proxies anônimos, WhoIS API, email lookup silencioso, mapas e gráficos interativos, hipóteses sobre o alvo, exportação PDF, transferência via QR Code
- **Interface**: GUI (dark/light/high-contrast) + CLI
- **Instalação (Windows)**: `git clone` + `Install.cmd`
- **Uso**: `python MrHolmes.py` (ou `Launchers/Win_Launcher.exe`)
- **Config**: `Configuration/Configuration.ini` (WhoIS API: https://whois.whoisxmlapi.com)

### 5️⃣ [GAMKERS-DDOS](./GAMKERS-DDOS/) ⚡
**Ferramenta de teste de stress UDP multithread otimizada**
- **Repositório**: https://github.com/Mateus2411/osint-tools
- **Função**: Teste de stress/denial com pacotes UDP multithread
- **Linguagem**: Python 3 (dependência zero — só stdlib)
- **Otimizações**: socket por thread, sem print por pacote (~35x mais rápido), reporter de pps em tempo real
- **Uso**: `python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10`
- **⚠️ Apenas para testes autorizados / localhost**

### 6️⃣ [RedTiger-Tools](./RedTiger-Tools/) 🐯
**Plataforma multifunção de pentest + OSINT com sistema de plugins**
- **Repositório**: https://github.com/loxy0devlp/RedTiger-Tools
- **Função**: Centralizar pentest e OSINT numa ferramenta só (CLI + interface interativa)
- **Pentest**: scanner avançado, scanner de vulnerabilidades, port scanner, crawler de URLs, ping contínuo, host discovery
- **OSINT**: Google dorks, tracker de carteira crypto, username/email/IP/telefone lookup, Instagram lookup
- **Extras**: scanner/deletor de metadados, cloner de sites, plugins em Python
- **Instalação**: `python setup.py`
- **Uso**: `python redtiger.py` (ex: `python redtiger.py -pnl -p "+551****9999"`)

---

## 📋 Guia de Instalação Rápida

### Mr.Holmes
```bash
# 1. Clonar o repositório:
git clone https://github.com/Lucksi/Mr.Holmes
# 2. Entrar na pasta e instalar:
cd Mr.Holmes
Install.cmd
# 3. Rodar:
python MrHolmes.py
```

### RedTiger-Tools
```bash
# 1. Clonar o repositório:
git clone https://github.com/loxy0devlp/RedTiger-Tools
# 2. Entrar na pasta:
cd RedTiger-Tools
# 3. Instalar dependências:
python setup.py
# 4. Rodar:
python redtiger.py
```

### Holehe
```bash
# 1. Instalar Python: https://www.python.org/downloads/
# ⚠️ Marcar "Add Python to PATH"
# 2. Instalar Holehe:
pip install holehe
# 3. Testar:
holehe email@email.com
```

### SpiderFoot
```bash
# 1. Entrar na pasta: C:\osint
# 2. Clonar:
git clone https://github.com/smicallef/spiderfoot
# 3. Entrar na pasta:
cd spiderfoot
# 4. Instalar dependências:
pip install -r requirements.txt
# 5. Rodar:
python spiderfoot.py -l 127.0.0.1:5001
# 6. Abrir no navegador: http://127.0.0.1:5001
```

### theHarvester
```bash
# 1. Instalar: pip install theHarvester
# 2. Uso básico:
theHarvester -d dominio.com -b google
# 3. Múltiplas fontes:
theHarvester -d alvo.com -b google,bing,dnsdumpster
# 4. Salvar resultados:
theHarvester -d empresa.com -b all -f resultados
```

### GAMKERS-DDOS
```bash
# 1. Entrar na pasta:
cd GAMKERS-DDOS
# 2. Rodar (dependência zero, só precisa de Python 3):
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10
```

---

## 🧠 O que cada ferramenta faz melhor

| Ferramenta | Melhor uso | Tipo de dados |
|------------|------------|---------------|
| **Holehe** | Descobrir contas com email | Redes sociais, plataformas online |
| **SpiderFoot** | OSINT automático | Tudo: domínios, IPs, emails, vulnerabilidades |
| **theHarvester** | Coleta de informações | Emails, subdomínios, hosts de múltiplas fontes |
| **Mr.Holmes** | Investigação GUI completa | Domínios, usernames, telefones, dorks, gráficos/mapas |
| **GAMKERS-DDOS** | Teste de stress UDP | Pacotes UDP multithread, pps, payload configurável |
| **RedTiger-Tools** | Pentest + OSINT all-in-one | Scanners, dorks, wallets crypto, telefone/IP/email/Instagram |

---

## 🚀 Fluxo de Trabalho Recomendado

### 1. Investigação de Pessoa
```bash
# 1. Começar com email (se disponível)
holehe pessoa@email.com

# 2. Investigar telefone (se encontrado)
python redtiger.py -pnl -p "+551****9999"

# 3. OSINT completo no domínio do email
# SpiderFoot: Target = email.com, Type = Domain
```

### 2. Investigação de Empresa
```bash
# 1. OSINT automático do domínio
# SpiderFoot: Target = empresa.com, Type = Domain

# 2. Verificar emails encontrados
holehe email@empresa.com

# 3. Investigar telefones descobertos
python redtiger.py -pnl -p "+551****9999"
```

### 3. Investigação de Domínio/Site
```bash
# 1. SpiderFoot primeiro (coleta massiva)
# Target = site.com, Scan Type = All

# 2. Verificar emails encontrados
holehe admin@site.com

# 3. Investigar IPs e telefones descobertos
python redtiger.py -il -i <ip_encontrado> && python redtiger.py -pnl -p <numero_encontrado>
```

### 4. Teste de Stress (apenas autorizado)
```bash
# 1. Resolver IP do alvo
nslookup alvo.com

# 2. Teste no localhost primeiro
python GAMKERS-DDOS.py 127.0.0.1 -p 80 -t 4 -d 10

# 3. Payload menor = mais pps
python GAMKERS-DDOS.py 127.0.0.1 -s 64 -t 8 -d 5
```

---

## ⚠️ Considerações Legais e Éticas

### ✅ Uso Permitido
- **Investigação própria**: Seus próprios dados
- **Consentimento**: Com autorização da pessoa/empresa
- **Pesquisa acadêmica**: Para fins educacionais
- **Jornalismo**: Investigação jornalística legítima
- **Segurança**: Pentest autorizado, bug bounty

### ❌ Uso Proibido
- **Stalking**: Perseguição ou assédio
- **Invasão de privacidade**: Sem consentimento
- **Atividades maliciosas**: Fraude, chantagem
- **Uso comercial não autorizado**: Venda de dados
- **Violação de ToS**: Quebra de termos de serviço

### 📋 Boas Práticas
1. **Sempre obtenha consentimento** quando aplicável
2. **Respeite leis locais** (LGPD, GDPR, etc.)
3. **Use apenas fontes públicas**
4. **Não armazene dados sensíveis** desnecessariamente
5. **Mantenha logs seguros** e criptografados
6. **Documente o propósito** da investigação
7. **Limite o escopo** ao necessário

---

## 🔧 Solução de Problemas Comuns

### Python não encontrado
```bash
# Baixar Python: https://www.python.org/downloads/
# ⚠️ Marcar "Add Python to PATH" durante instalação
# Verificar: python --version
```

### Erro de dependências
```bash
# Atualizar pip:
python -m pip install --upgrade pip

# Instalar dependências:
pip install -r requirements.txt
```

### SpiderFoot - Erro lxml
```bash
# Problema já corrigido nesta versão
# Se persistir, instalar manualmente:
pip install lxml
```

### Firewall/Antivírus bloqueando
```bash
# Adicionar exceções para:
# - Python.exe
# - Pasta do projeto
```

---

## 📚 Recursos Adicionais

### Documentação Oficial
- **Holehe**: https://github.com/megadose/holehe/wiki
- **Mr.Holmes**: https://github.com/Lucksi/Mr.Holmes
- **RedTiger-Tools**: https://github.com/loxy0devlp/RedTiger-Tools
- **SpiderFoot**: https://www.spiderfoot.net/documentation
- **theHarvester**: https://github.com/laramies/theHarvester/wiki

### Comunidades
- **Discord SpiderFoot**: https://discord.gg/vyvztrG
- **Reddit OSINT**: r/OSINT
- **Twitter**: @spiderfoot

### Cursos e Treinamentos
- **OSINT Framework**: https://osintframework.com/
- **Bellingcat**: https://www.bellingcat.com/resources/
- **SANS OSINT**: https://www.sans.org/cyber-security-courses/

---

## 💡 Dicas Avançadas

### Automatização
```bash
# Script para investigação completa
#!/bin/bash
TARGET_EMAIL="alvo@email.com"
TARGET_PHONE="+5511999999999"
TARGET_DOMAIN="email.com"

echo "=== Investigando Email ==="
holehe $TARGET_EMAIL > holehe_results.txt

echo "=== Investigando Telefone ==="
python redtiger.py -pnl -p "$TARGET_PHONE" > phone_results.txt

echo "=== OSINT Automático ==="
# Usar SpiderFoot via CLI ou interface web
```

### Integração de Dados
```bash
# Combinar resultados em formato JSON
jq -s '.[0] + .[1]' holehe.json redtiger_output.json > combined.json
```

### Backup e Segurança
```bash
# Criptografar resultados sensíveis
gpg -c resultados_investigacao.json

# Backup seguro
tar -czf backup_$(date +%Y%m%d).tar.gz *.json *.txt
```

---

## 🎯 Resumo Executivo

Este conjunto de ferramentas OSINT oferece capacidades abrangentes para investigação digital:

- **Holehe**: Expert em descoberta de contas por email
- **SpiderFoot**: Plataforma completa de OSINT automático
- **theHarvester**: Coleta de informações de múltiplas fontes
- **Mr.Holmes**: Investigação GUI com dorks, mapas e gráficos
- **RedTiger-Tools**: Suite de pentest + OSINT com plugins

**Use sempre de forma ética, legal e responsável!** 🕵️‍♂️🔍