# Ferramentas de OSINT - Guia Completo

<sub style="color:gray;">
Todas as ferramentas disponibilizadas devem ser utilizadas de forma ética e responsável.
O uso indevido para comprometer a segurança ou privacidade de terceiros não é recomendado.
</sub>

---

## 🛠️ Ferramentas Disponíveis

### 1️⃣ [PhoneInfoga](./phoneinfoga_Windows_x86_64/) 📞
**Ferramenta para investigar números de telefone**
- **Site oficial**: https://github.com/sundowndev/phoneinfoga
- **Função**: Obter informações detalhadas sobre números de telefone
- **Dados coletados**: Operadora, localização, tipo de linha, validação
- **Uso**: `./phoneinfoga.exe scan -n +5511999999999`

### 2️⃣ [Holehe](./holohe/) 📧
**Ferramenta para descobrir contas associadas a e-mail**
- **Repositório**: https://github.com/megadose/holehe
- **Função**: Verificar contas em mais de 100 sites (Instagram, Twitter, etc)
- **Pré-requisito**: Python 3.6+
- **Instalação**: `pip install holehe`
- **Uso**: `holehe email@email.com`

### 3️⃣ [SpiderFoot](./spiderfoot/) 🕷️
**Ferramenta extremamente poderosa de OSINT automático**
- **Repositório**: https://github.com/smicallef/spiderfoot
- **Função**: Investigação completa e automática
- **Alvos**: Domínios, emails, IPs, telefones, empresas, vazamentos
- **Interface**: Web + CLI
- **Uso**: `py -3.14 sf.py -l 127.0.0.1:5001`

### 4️⃣ [theHarvester](./theHarvester/) 🌾
**Ferramenta clássica para coleta de informações OSINT**
- **Repositório**: https://github.com/laramies/theHarvester
- **Função**: Coleta de emails, subdomínios, hosts, IPs de múltiplas fontes
- **Fontes**: Google, Bing, SHODAN, VirusTotal, DNSDumpster, +40 outras
- **Instalação**: `pip install theHarvester`
- **Uso**: `theHarvester -d dominio.com -b google,bing`

---

## 📋 Guia de Instalação Rápida

### PhoneInfoga
```bash
# 1. Baixar phoneinfoga_Windows_x86_64.tar.gz
# 2. Extrair na pasta: C:\osint\phoneinfoga
# 3. Executar:
./phoneinfoga.exe scan -n +5511999999999
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

---

## 🧠 O que cada ferramenta faz melhor

| Ferramenta | Melhor uso | Tipo de dados |
|------------|------------|---------------|
| **PhoneInfoga** | Investigar telefones | Operadora, localização, validação |
| **Holehe** | Descobrir contas com email | Redes sociais, plataformas online |
| **SpiderFoot** | OSINT automático | Tudo: domínios, IPs, emails, vulnerabilidades |
| **theHarvester** | Coleta de informações | Emails, subdomínios, hosts de múltiplas fontes |

---

## 🚀 Fluxo de Trabalho Recomendado

### 1. Investigação de Pessoa
```bash
# 1. Começar com email (se disponível)
holehe pessoa@email.com

# 2. Investigar telefone (se encontrado)
./phoneinfoga.exe scan -n +5511999999999

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
./phoneinfoga.exe scan -n +5511999999999
```

### 3. Investigação de Domínio/Site
```bash
# 1. SpiderFoot primeiro (coleta massiva)
# Target = site.com, Scan Type = All

# 2. Verificar emails encontrados
holehe admin@site.com

# 3. Investigar IPs e telefones descobertos
./phoneinfoga.exe scan -n +numero_encontrado
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
# - phoneinfoga.exe
# - Python.exe
# - Pasta do projeto
```

---

## 📚 Recursos Adicionais

### Documentação Oficial
- **PhoneInfoga**: https://sundowndev.github.io/phoneinfoga/
- **Holehe**: https://github.com/megadose/holehe/wiki
- **SpiderFoot**: https://www.spiderfoot.net/documentation
- **theHarvester**: https://github.com/laramies/theHarvester/wiki

### Comunidades
- **Discord SpiderFoot**: https://discord.gg/vyvztrG
- **Reddit OSINT**: r/OSINT
- **Twitter**: @spiderfoot, @phoneinfoga

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
./phoneinfoga.exe scan -n $TARGET_PHONE > phone_results.txt

echo "=== OSINT Automático ==="
# Usar SpiderFoot via CLI ou interface web
```

### Integração de Dados
```bash
# Combinar resultados em formato JSON
jq -s '.[0] + .[1]' holehe.json phoneinfoga.json > combined.json
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

- **PhoneInfoga**: Especialista em números de telefone
- **Holehe**: Expert em descoberta de contas por email  
- **SpiderFoot**: Plataforma completa de OSINT automático
- **theHarvester**: Coleta de informações de múltiplas fontes

**Use sempre de forma ética, legal e responsável!** 🕵️‍♂️🔍