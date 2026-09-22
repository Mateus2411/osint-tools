# Holehe - Descoberta de Contas por E-mail

<sub style="color:gray;">
Ferramenta para descobrir contas associadas a um endereço de e-mail em mais de 100 sites (Instagram, Twitter, Facebook, etc).
</sub>

---

## 📋 Sobre o Holehe

O Holehe é uma ferramenta OSINT que permite descobrir quais contas online estão associadas a um endereço de e-mail específico. Ele verifica automaticamente mais de 100 sites populares, incluindo redes sociais, plataformas de e-commerce, serviços de streaming e muito mais.

### 🎯 O que o Holehe pode encontrar:
- Contas em redes sociais (Instagram, Twitter, Facebook, LinkedIn)
- Perfis em plataformas de jogos (Steam, Epic Games, Xbox Live)
- Contas de streaming (Netflix, Spotify, YouTube)
- Perfis profissionais (GitHub, Stack Overflow)
- Contas de e-commerce (Amazon, eBay, PayPal)
- E muito mais...

---

## 🔧 Instalação

### Pré-requisitos
- **Python 3.6+** instalado no sistema
- **pip** (gerenciador de pacotes do Python)

### Passo 1: Instalar Python
1. Baixe o Python em: https://www.python.org/downloads/
2. **⚠️ IMPORTANTE**: Durante a instalação, marque a opção **"Add Python to PATH"**
3. Verifique a instalação:
```bash
python --version
pip --version
```

### Passo 2: Instalar Holehe
```bash
pip install holehe
```

### Passo 3: Verificar Instalação
```bash
holehe --help
```

---

## 🚀 Como Usar

### Comando Básico
```bash
holehe email@exemplo.com
```

### Exemplos Práticos

#### 1. Verificação Simples
```bash
holehe joao.silva@gmail.com
```

#### 2. Salvar Resultados em Arquivo
```bash
holehe email@exemplo.com > resultados.txt
```

#### 3. Verificar Múltiplos E-mails
```bash
holehe email1@exemplo.com
holehe email2@exemplo.com
holehe email3@exemplo.com
```

#### 4. Usar com Lista de E-mails
Crie um arquivo `emails.txt` com um e-mail por linha:
```
email1@exemplo.com
email2@exemplo.com
email3@exemplo.com
```

Depois execute:
```bash
for email in $(cat emails.txt); do holehe $email; done
```

---

## 📊 Interpretando os Resultados

### Códigos de Status
- **✅ [+]** - Conta encontrada e confirmada
- **❌ [-]** - Conta não encontrada
- **⚠️ [?]** - Status incerto (pode existir, mas não confirmado)
- **🔒 [!]** - Site bloqueou a verificação (rate limit/captcha)

### Exemplo de Saída
```
[+] Instagram: https://instagram.com/usuario
[+] Twitter: https://twitter.com/usuario
[-] Facebook: Not found
[?] LinkedIn: Uncertain
[!] GitHub: Rate limited
```

---

## 🛡️ Sites Verificados (100+)

### Redes Sociais
- Instagram, Twitter, Facebook, LinkedIn
- TikTok, Snapchat, Pinterest, Reddit
- Discord, Telegram, WhatsApp Business

### Plataformas Profissionais
- GitHub, GitLab, Stack Overflow
- Behance, Dribbble, DeviantArt
- AngelList, Crunchbase

### Streaming e Entretenimento
- YouTube, Twitch, Spotify
- Netflix, Amazon Prime, Hulu
- Steam, Epic Games, PlayStation

### E-commerce e Serviços
- Amazon, eBay, PayPal, Stripe
- Uber, Airbnb, Booking.com
- Adobe, Microsoft, Google

### E muito mais...

---

## ⚙️ Opções Avançadas

### Verificar Sites Específicos
```bash
# Verificar apenas Instagram e Twitter
holehe email@exemplo.com --sites instagram twitter
```

### Usar Proxy
```bash
holehe email@exemplo.com --proxy http://proxy:8080
```

### Timeout Personalizado
```bash
holehe email@exemplo.com --timeout 10
```

### Modo Verboso
```bash
holehe email@exemplo.com -v
```

---

## 🔍 Casos de Uso

### 1. Investigação OSINT
- Mapear presença digital de uma pessoa
- Identificar contas esquecidas ou abandonadas
- Verificar vazamentos de dados

### 2. Segurança Pessoal
- Auditar suas próprias contas online
- Identificar contas criadas sem seu conhecimento
- Verificar exposição de e-mail em breaches

### 3. Investigação Jornalística
- Verificar autenticidade de fontes
- Mapear conexões entre pessoas
- Investigar atividades online

### 4. Pentest e Red Team
- Reconnaissance de alvos
- Identificar vetores de ataque
- Mapear superfície de ataque

---

## 🚨 Considerações Legais e Éticas

### ✅ Uso Permitido
- Verificar suas próprias contas
- Investigação com consentimento
- Pesquisa acadêmica ética
- Jornalismo investigativo legítimo

### ❌ Uso Proibido
- Stalking ou assédio
- Violação de privacidade
- Atividades maliciosas
- Uso sem consentimento para fins pessoais

### 📋 Boas Práticas
1. **Sempre obtenha consentimento** quando aplicável
2. **Respeite a privacidade** das pessoas
3. **Use apenas para fins legítimos**
4. **Não abuse da ferramenta** (evite spam/rate limiting)
5. **Mantenha os dados seguros** e não os compartilhe

---

## 🛠️ Solução de Problemas

### Erro: "holehe: command not found"
```bash
# Verifique se Python está no PATH
python -m pip install holehe

# Ou use diretamente
python -m holehe email@exemplo.com
```

### Erro: "Permission denied"
```bash
# Use --user para instalação local
pip install --user holehe
```

### Rate Limiting
Se você receber muitos bloqueios:
1. Use delays entre verificações
2. Configure um proxy
3. Verifique menos sites por vez

### Timeout Errors
```bash
# Aumente o timeout
holehe email@exemplo.com --timeout 30
```

---

## 📈 Dicas de Eficiência

### 1. Automatização
Crie scripts para verificações em lote:
```bash
#!/bin/bash
for email in $(cat lista_emails.txt); do
    echo "Verificando: $email"
    holehe $email > "resultado_${email//[@.]/_}.txt"
    sleep 2  # Delay para evitar rate limiting
done
```

### 2. Filtragem de Resultados
```bash
# Mostrar apenas contas encontradas
holehe email@exemplo.com | grep "\[+\]"

# Contar quantas contas foram encontradas
holehe email@exemplo.com | grep -c "\[+\]"
```

### 3. Integração com Outras Ferramentas
```bash
# Combinar com outras ferramentas OSINT
holehe email@exemplo.com > holehe_results.txt
phoneinfoga scan -n +5511999999999 > phone_results.txt
```

---

## 🔄 Atualizações

### Verificar Versão Atual
```bash
holehe --version
```

### Atualizar Holehe
```bash
pip install --upgrade holehe
```

### Changelog
O Holehe é atualizado regularmente com:
- Novos sites suportados
- Correções de bugs
- Melhorias de performance
- Novos recursos

---

## 📚 Recursos Adicionais

### Links Úteis
- **Repositório GitHub**: https://github.com/megadose/holehe
- **Documentação Oficial**: https://github.com/megadose/holehe/wiki
- **Issues e Suporte**: https://github.com/megadose/holehe/issues

### Ferramentas Complementares
- **SpiderFoot**: OSINT automático completo
- **PhoneInfoga**: Investigação de números de telefone
- **Maltego**: Análise visual de conexões
- **theHarvester**: Coleta de e-mails e subdomínios

---

## 💡 Resumo Rápido

```bash
# Instalação
pip install holehe

# Uso básico
holehe email@exemplo.com

# Salvar resultados
holehe email@exemplo.com > resultados.txt

# Verificar apenas sites específicos
holehe email@exemplo.com --sites instagram twitter github
```

**O Holehe é uma ferramenta poderosa para mapear a presença digital através de endereços de e-mail. Use sempre de forma ética e responsável!** 🕵️‍♂️