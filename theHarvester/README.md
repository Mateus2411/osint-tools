# theHarvester - Coleta de Informações OSINT

<sub style="color:gray;">
Ferramenta poderosa para coleta de e-mails, subdomínios, hosts, nomes de funcionários, portas abertas e banners de diferentes fontes públicas como motores de busca, servidores PGP e base de dados SHODAN.
</sub>

---

## 📋 Sobre o theHarvester

O theHarvester é uma das ferramentas OSINT mais populares e eficazes para coleta de informações. Desenvolvida por Christian Martorella, ela automatiza o processo de coleta de dados de múltiplas fontes públicas, sendo essencial para reconhecimento passivo.

### 🎯 O que o theHarvester pode coletar:
- **E-mails**: Endereços de e-mail associados ao domínio
- **Subdomínios**: Descoberta de subdomínios e hosts
- **Nomes de pessoas**: Funcionários e contatos
- **Endereços IP**: IPs associados aos hosts
- **Portas abertas**: Via integração com SHODAN
- **Banners**: Informações de serviços
- **URLs**: Links e páginas relacionadas

---

## 🔧 Instalação

### Método 1: Via pip (Recomendado)
```bash
# Instalar theHarvester
pip install theHarvester

# Ou instalar a versão mais recente
pip install git+https://github.com/laramies/theHarvester.git
```

### Método 2: Clonando o Repositório
```bash
# Clonar repositório
git clone https://github.com/laramies/theHarvester.git
cd theHarvester

# Instalar dependências
pip install -r requirements.txt

# Executar
python theHarvester.py -d exemplo.com -b google
```

### Verificar Instalação
```bash
theHarvester --help
```

---

## 🚀 Como Usar

### Comando Básico
```bash
theHarvester -d dominio.com -b fonte
```

### Exemplos Práticos

#### 1. Busca Simples com Google
```bash
theHarvester -d microsoft.com -b google -l 100
```

#### 2. Múltiplas Fontes
```bash
theHarvester -d github.com -b dnsdumpster,hackertarget,crtsh
```

#### 3. Salvar Resultados
```bash
theHarvester -d empresa.com -b all -f resultados
```

#### 4. Usar SHODAN para Portas
```bash
theHarvester -d alvo.com -b shodan -s
```

#### 5. Busca com Limite Específico
```bash
theHarvester -d dominio.com -b bing -l 200
```

---

## 📊 Fontes de Dados Disponíveis

### Motores de Busca
- **google**: Google Search
- **bing**: Bing Search  
- **yahoo**: Yahoo Search
- **duckduckgo**: DuckDuckGo
- **brave**: Brave Search
- **mojeek**: Mojeek Search

### DNS e Certificados
- **dnsdumpster**: DNSDumpster
- **crtsh**: Certificate Transparency
- **certspotter**: CertSpotter
- **chaos**: ProjectDiscovery Chaos

### Threat Intelligence
- **shodan**: SHODAN
- **virustotal**: VirusTotal
- **otx**: AlienVault OTX
- **threatcrowd**: ThreatCrowd
- **securitytrails**: SecurityTrails

### Redes Sociais e Código
- **github-code**: GitHub Code Search
- **gitlab**: GitLab
- **bitbucket**: Bitbucket

### Vazamentos e Breaches
- **haveibeenpwned**: HaveIBeenPwned
- **dehashed**: Dehashed
- **leakix**: LeakIX
- **hudsonrock**: Hudson Rock

### Outras Fontes
- **hunter**: Hunter.io
- **rocketreach**: RocketReach
- **fullhunt**: FullHunt
- **netlas**: Netlas
- **fofa**: FOFA
- **zoomeye**: ZoomEye

---

## ⚙️ Opções Avançadas

### Parâmetros Principais
```bash
-d, --domain DOMAIN     # Domínio alvo (obrigatório)
-b, --source SOURCE     # Fonte de dados (obrigatório)
-l, --limit LIMIT       # Limite de resultados (padrão: 500)
-S, --start START       # Começar do resultado X (padrão: 0)
-f, --filename FILE     # Salvar em XML e JSON
-s, --shodan           # Usar SHODAN para hosts descobertos
-c, --dns-brute        # Força bruta DNS
-t, --take-over        # Verificar subdomain takeover
-r, --dns-resolve      # Resolver DNS dos hosts
-n, --dns-lookup       # Lookup DNS reverso
-p, --proxies          # Usar proxies
-e, --dns-server DNS   # Servidor DNS customizado
```

### Exemplos de Uso Avançado

#### 1. Busca Completa com Todas as Fontes
```bash
theHarvester -d empresa.com -b all -l 1000 -f empresa_completo
```

#### 2. DNS Brute Force
```bash
theHarvester -d alvo.com -b dnsdumpster -c
```

#### 3. Verificar Subdomain Takeover
```bash
theHarvester -d dominio.com -b crtsh -t
```

#### 4. Usar Proxies
```bash
theHarvester -d alvo.com -b google -p
```

#### 5. Resolver IPs dos Hosts
```bash
theHarvester -d empresa.com -b hackertarget -r
```

---

## 🔍 Interpretando Resultados

### Saída no Terminal
```
[*] Target: exemplo.com
[*] Searching Google...
[*] Searching Bing...

[*] IPs found: 5
---------------------
192.168.1.1
10.0.0.1

[*] Emails found: 12
---------------------
admin@exemplo.com
contato@exemplo.com

[*] Hosts found: 25
---------------------
www.exemplo.com
mail.exemplo.com
ftp.exemplo.com
```

### Arquivos Gerados
- **arquivo.json**: Dados estruturados em JSON
- **arquivo.xml**: Dados em formato XML
- Ambos contêm: hosts, emails, IPs, pessoas

### Exemplo de JSON
```json
{
  "cmd": "-d exemplo.com -b google",
  "hosts": [
    "www.exemplo.com:192.168.1.1",
    "mail.exemplo.com:192.168.1.2"
  ],
  "emails": [
    "admin@exemplo.com",
    "contato@exemplo.com"
  ],
  "ips": [
    "192.168.1.1",
    "192.168.1.2"
  ]
}
```

---

## 🔑 Configuração de API Keys

### Arquivo de Configuração
O theHarvester cria automaticamente: `~/.theHarvester/api-keys.yaml`

### APIs que Requerem Chaves
```yaml
# Editar ~/.theHarvester/api-keys.yaml
shodan: "SUA_API_KEY_AQUI"
virustotal: "SUA_API_KEY_AQUI"
hunter: "SUA_API_KEY_AQUI"
securitytrails: "SUA_API_KEY_AQUI"
fullhunt: "SUA_API_KEY_AQUI"
```

### Como Obter API Keys
- **SHODAN**: https://account.shodan.io/
- **VirusTotal**: https://www.virustotal.com/gui/join-us
- **Hunter.io**: https://hunter.io/api
- **SecurityTrails**: https://securitytrails.com/corp/api
- **FullHunt**: https://fullhunt.io/

---

## 🔍 Casos de Uso

### 1. Reconhecimento Passivo
```bash
# Descobrir subdomínios
theHarvester -d alvo.com -b crtsh,dnsdumpster -l 500

# Encontrar emails
theHarvester -d empresa.com -b google,bing,hunter
```

### 2. Bug Bounty
```bash
# Mapear superfície de ataque
theHarvester -d programa.com -b all -f recon_completo

# Verificar subdomain takeover
theHarvester -d alvo.com -b crtsh -t
```

### 3. Pentest
```bash
# Coleta inicial de informações
theHarvester -d cliente.com -b google,shodan -s

# Força bruta DNS
theHarvester -d alvo.com -b dnsdumpster -c
```

### 4. Threat Intelligence
```bash
# Monitorar vazamentos
theHarvester -d empresa.com -b haveibeenpwned,dehashed

# Verificar threat feeds
theHarvester -d dominio.com -b otx,threatcrowd
```

---

## 🛡️ Considerações Legais e Éticas

### ✅ Uso Permitido
- **Domínios próprios**: Seus próprios assets
- **Bug bounty autorizado**: Programas oficiais
- **Pentest contratado**: Com autorização por escrito
- **Pesquisa acadêmica**: Para fins educacionais
- **Threat intelligence**: Monitoramento defensivo

### ❌ Uso Proibido
- **Reconhecimento não autorizado**: Sem permissão
- **Stalking corporativo**: Espionagem industrial
- **Atividades maliciosas**: Preparação para ataques
- **Violação de privacidade**: Coleta não consensual

### 📋 Boas Práticas
1. **Obtenha autorização** por escrito quando necessário
2. **Respeite rate limits** das APIs
3. **Use proxies** para evitar bloqueios
4. **Documente o propósito** da coleta
5. **Mantenha dados seguros** e criptografados
6. **Delete dados** quando não precisar mais

---

## 🛠️ Solução de Problemas

### Erro: "No module named 'theHarvester'"
```bash
# Reinstalar
pip uninstall theHarvester
pip install theHarvester

# Ou usar Python diretamente
python -m theHarvester -d exemplo.com -b google
```

### Erro: "API key missing"
```bash
# Verificar arquivo de configuração
cat ~/.theHarvester/api-keys.yaml

# Adicionar chave manualmente
echo "shodan: SUA_CHAVE" >> ~/.theHarvester/api-keys.yaml
```

### Rate Limiting / Bloqueios
```bash
# Usar proxies
theHarvester -d alvo.com -b google -p

# Reduzir limite
theHarvester -d alvo.com -b bing -l 50

# Usar delay entre requests (editar código)
```

### Timeout Errors
```bash
# Usar DNS server específico
theHarvester -d alvo.com -b dnsdumpster -e 8.8.8.8

# Tentar fonte diferente
theHarvester -d alvo.com -b hackertarget
```

---

## 📈 Integração com Outras Ferramentas

### 1. Combinar com Amass
```bash
# theHarvester para coleta inicial
theHarvester -d alvo.com -b all -f harvester_results

# Amass para enumeração profunda
amass enum -d alvo.com -o amass_results.txt
```

### 2. Usar com Subfinder
```bash
# theHarvester
theHarvester -d empresa.com -b crtsh -f th_results

# Subfinder
subfinder -d empresa.com -o sf_results.txt

# Combinar resultados
cat th_results.json sf_results.txt | sort -u > combined.txt
```

### 3. Pipeline com SpiderFoot
```bash
# 1. theHarvester para coleta rápida
theHarvester -d alvo.com -b google,bing -f quick_recon

# 2. SpiderFoot para análise profunda
# Usar domínios encontrados como targets no SpiderFoot
```

### 4. Integrar com Maltego
```bash
# Exportar para formato compatível
theHarvester -d empresa.com -b all -f maltego_import

# Importar JSON no Maltego para visualização
```

---

## 🔄 Automação e Scripts

### Script Bash para Múltiplos Domínios
```bash
#!/bin/bash
# harvester_multi.sh

DOMAINS_FILE="dominios.txt"
OUTPUT_DIR="resultados"

mkdir -p $OUTPUT_DIR

while read domain; do
    echo "Processando: $domain"
    theHarvester -d $domain -b all -f "$OUTPUT_DIR/${domain}_results"
    sleep 10  # Delay para evitar rate limiting
done < $DOMAINS_FILE
```

### Script Python para Análise
```python
#!/usr/bin/env python3
import json
import sys

def analyze_harvester_results(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    print(f"Domínio: {data.get('cmd', '').split('-d ')[1].split(' ')[0]}")
    print(f"Hosts encontrados: {len(data.get('hosts', []))}")
    print(f"Emails encontrados: {len(data.get('emails', []))}")
    print(f"IPs encontrados: {len(data.get('ips', []))}")

if __name__ == "__main__":
    analyze_harvester_results(sys.argv[1])
```

---

## 📚 Recursos Adicionais

### Links Úteis
- **Repositório GitHub**: https://github.com/laramies/theHarvester
- **Documentação**: https://github.com/laramies/theHarvester/wiki
- **Issues**: https://github.com/laramies/theHarvester/issues

### Ferramentas Complementares
- **Amass**: Enumeração de subdomínios
- **Subfinder**: Descoberta de subdomínios
- **SpiderFoot**: OSINT automático completo
- **Maltego**: Visualização de dados
- **Recon-ng**: Framework de reconhecimento

### Cursos e Treinamentos
- **OSINT Framework**: https://osintframework.com/
- **Bellingcat**: https://www.bellingcat.com/resources/
- **SANS OSINT**: Cursos especializados

---

## 💡 Resumo Rápido

```bash
# Instalação
pip install theHarvester

# Uso básico
theHarvester -d dominio.com -b google

# Múltiplas fontes
theHarvester -d alvo.com -b google,bing,dnsdumpster

# Salvar resultados
theHarvester -d empresa.com -b all -f resultados

# Com SHODAN
theHarvester -d alvo.com -b shodan -s

# Todas as fontes
theHarvester -d dominio.com -b all -l 1000
```

**O theHarvester é uma ferramenta fundamental para qualquer profissional de OSINT. Use sempre de forma ética e legal!** 🕵️‍♂️🔍