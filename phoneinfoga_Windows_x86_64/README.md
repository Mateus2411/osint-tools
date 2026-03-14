# PhoneInfoga - Investigação de Números de Telefone

<sub style="color:gray;">
Ferramenta avançada para investigar números de telefone e obter informações detalhadas sobre operadoras, localização e muito mais.
</sub>

---

## 📋 Sobre o PhoneInfoga

O PhoneInfoga é uma das ferramentas OSINT mais poderosas para investigação de números de telefone. Ele coleta informações de múltiplas fontes para fornecer dados abrangentes sobre qualquer número telefônico.

### 🎯 O que o PhoneInfoga pode descobrir:
- **Informações da Operadora**: Nome, país, tipo de linha
- **Localização Geográfica**: País, região, cidade
- **Tipo de Número**: Móvel, fixo, VoIP, toll-free
- **Validação**: Se o número é válido e ativo
- **Formatação**: Diferentes formatos internacionais
- **Reputação**: Verificação em bases de spam/fraude
- **Redes Sociais**: Possíveis contas associadas

---

## 🔧 Instalação

### Método 1: Download Direto (Recomendado para Windows)

1. **Baixar o executável**:
   - Acesse: https://github.com/sundowndev/phoneinfoga/releases
   - Baixe: `phoneinfoga_Windows_x86_64.tar.gz`

2. **Extrair arquivos**:
   ```bash
   # Extrair na pasta desejada
   tar -xzf phoneinfoga_Windows_x86_64.tar.gz
   
   # Ou extrair para pasta específica
   mkdir C:\osint\phoneinfoga
   tar -xzf phoneinfoga_Windows_x86_64.tar.gz -C C:\osint\phoneinfoga
   ```

3. **Verificar instalação**:
   ```bash
   ./phoneinfoga.exe version
   ```

### Método 2: Instalação via Go (Avançado)
```bash
go install github.com/sundowndev/phoneinfoga/v2@latest
```

---

## 🚀 Como Usar

### Comando Básico
```bash
./phoneinfoga.exe scan -n +5511999999999
```

### Exemplos Práticos

#### 1. Scan Básico (Número Brasileiro)
```bash
# Formato internacional
./phoneinfoga.exe scan -n +5511999999999

# Formato nacional
./phoneinfoga.exe scan -n 11999999999
```

#### 2. Scan com Saída Detalhada
```bash
./phoneinfoga.exe scan -n +5511999999999 --verbose
```

#### 3. Salvar Resultados em JSON
```bash
./phoneinfoga.exe scan -n +5511999999999 --output json > resultado.json
```

#### 4. Scan de Múltiplos Números
```bash
# Criar arquivo numeros.txt com um número por linha
./phoneinfoga.exe scan -i numeros.txt
```

#### 5. Usar Servidor Web (Interface Gráfica)
```bash
# Iniciar servidor web
./phoneinfoga.exe serve

# Acessar no navegador: http://localhost:5000
```

---

## 📊 Interpretando os Resultados

### Informações Básicas
```json
{
  "valid": true,
  "number": "+5511999999999",
  "local_format": "(11) 99999-9999",
  "international_format": "+55 11 99999-9999",
  "country_prefix": "+55",
  "country": "Brazil",
  "country_code": "BR",
  "location": "São Paulo"
}
```

### Informações da Operadora
```json
{
  "carrier": "Vivo",
  "line_type": "mobile",
  "mcc": "724",
  "mnc": "11"
}
```

### Verificações de Segurança
```json
{
  "reputation": {
    "spam_score": 0,
    "is_spam": false,
    "reports": []
  }
}
```

---

## 🌐 Interface Web

### Iniciar Servidor Web
```bash
./phoneinfoga.exe serve --port 5000
```

### Recursos da Interface Web
- **Dashboard intuitivo** para inserir números
- **Visualização gráfica** dos resultados
- **Histórico de pesquisas**
- **Exportação de dados** em múltiplos formatos
- **API REST** para integração

### Acessar Interface
1. Abra o navegador
2. Vá para: `http://localhost:5000`
3. Digite o número no campo de pesquisa
4. Clique em "Scan"

---

## 🔍 Formatos de Número Suportados

### Formatos Aceitos
```bash
# Internacional (recomendado)
+5511999999999
+1234567890
+447700900123

# Nacional
11999999999
(11) 99999-9999
11 99999-9999

# Com códigos de país
0055 11 99999-9999
```

### Países Suportados
- **Brasil**: +55
- **Estados Unidos**: +1
- **Reino Unido**: +44
- **França**: +33
- **Alemanha**: +49
- **E mais de 200 países...**

---

## ⚙️ Opções Avançadas

### Configuração de Scanner
```bash
# Timeout personalizado
./phoneinfoga.exe scan -n +5511999999999 --timeout 30

# Usar proxy
./phoneinfoga.exe scan -n +5511999999999 --proxy http://proxy:8080

# Desabilitar verificações específicas
./phoneinfoga.exe scan -n +5511999999999 --no-reputation
```

### Configuração do Servidor
```bash
# Porta personalizada
./phoneinfoga.exe serve --port 8080

# Bind em interface específica
./phoneinfoga.exe serve --host 0.0.0.0 --port 5000

# Modo debug
./phoneinfoga.exe serve --debug
```

### Arquivo de Configuração
Crie `config.yml`:
```yaml
scanners:
  timeout: 30
  reputation: true
  
server:
  host: "127.0.0.1"
  port: 5000
  
output:
  format: "json"
  file: "results.json"
```

---

## 🔍 Casos de Uso

### 1. Investigação OSINT
```bash
# Verificar informações básicas
./phoneinfoga.exe scan -n +5511999999999

# Análise completa com reputação
./phoneinfoga.exe scan -n +5511999999999 --verbose
```

### 2. Verificação de Spam/Fraude
```bash
# Verificar reputação do número
./phoneinfoga.exe scan -n +5511999999999 --reputation-only
```

### 3. Validação de Dados
```bash
# Verificar se números são válidos
./phoneinfoga.exe validate -n +5511999999999
```

### 4. Análise em Lote
```bash
# Processar lista de números
./phoneinfoga.exe scan -i lista_numeros.txt -o resultados.json
```

---

## 🛡️ Considerações de Privacidade

### ✅ Uso Ético
- Investigação de números próprios
- Verificação de spam/fraude
- Pesquisa acadêmica autorizada
- Investigação jornalística legítima

### ❌ Uso Inadequado
- Stalking ou assédio
- Violação de privacidade
- Coleta não autorizada de dados
- Atividades maliciosas

### 📋 Boas Práticas
1. **Obtenha consentimento** quando necessário
2. **Respeite leis locais** de privacidade
3. **Use apenas fontes públicas**
4. **Não armazene dados sensíveis**
5. **Mantenha logs seguros**

---

## 🛠️ Solução de Problemas

### Erro: "Invalid phone number"
```bash
# Certifique-se de usar formato internacional
./phoneinfoga.exe scan -n +5511999999999

# Não use:
./phoneinfoga.exe scan -n 11999999999  # Sem código do país
```

### Erro: "Connection timeout"
```bash
# Aumente o timeout
./phoneinfoga.exe scan -n +5511999999999 --timeout 60

# Use proxy se necessário
./phoneinfoga.exe scan -n +5511999999999 --proxy http://proxy:8080
```

### Erro: "Rate limited"
```bash
# Adicione delay entre requests
sleep 5 && ./phoneinfoga.exe scan -n +5511999999999
```

### Interface Web não carrega
```bash
# Verifique se a porta está livre
netstat -an | grep :5000

# Use porta diferente
./phoneinfoga.exe serve --port 8080
```

---

## 📈 Integração com Outras Ferramentas

### 1. Combinar com Holehe
```bash
# Primeiro, obter informações do telefone
./phoneinfoga.exe scan -n +5511999999999

# Depois, verificar e-mails relacionados
holehe email@encontrado.com
```

### 2. Usar com SpiderFoot
```bash
# Adicionar número como target no SpiderFoot
# O SpiderFoot pode usar PhoneInfoga como módulo
```

### 3. Exportar para Maltego
```bash
# Exportar em formato compatível
./phoneinfoga.exe scan -n +5511999999999 --output csv > maltego_import.csv
```

---

## 📊 API REST

### Endpoints Disponíveis
```bash
# Informações básicas
GET /api/numbers/{number}

# Scan completo
POST /api/scan
{
  "number": "+5511999999999"
}

# Histórico
GET /api/history

# Status do servidor
GET /api/health
```

### Exemplo de Uso da API
```bash
# Usando curl
curl -X POST http://localhost:5000/api/scan \
  -H "Content-Type: application/json" \
  -d '{"number": "+5511999999999"}'
```

---

## 🔄 Atualizações

### Verificar Versão
```bash
./phoneinfoga.exe version
```

### Baixar Nova Versão
1. Acesse: https://github.com/sundowndev/phoneinfoga/releases
2. Baixe a versão mais recente
3. Substitua o executável antigo

### Changelog
- **v2.10+**: Interface web melhorada
- **v2.9+**: Suporte a mais operadoras
- **v2.8+**: API REST completa
- **v2.7+**: Verificação de reputação

---

## 📚 Recursos Adicionais

### Links Úteis
- **Repositório GitHub**: https://github.com/sundowndev/phoneinfoga
- **Documentação**: https://sundowndev.github.io/phoneinfoga/
- **Wiki**: https://github.com/sundowndev/phoneinfoga/wiki
- **Issues**: https://github.com/sundowndev/phoneinfoga/issues

### Ferramentas Complementares
- **Holehe**: Descoberta de contas por e-mail
- **SpiderFoot**: OSINT automático completo
- **Maltego**: Visualização de conexões
- **TrueCaller**: Identificação de chamadas

---

## 💡 Resumo Rápido

```bash
# Instalação (Windows)
# 1. Baixar phoneinfoga_Windows_x86_64.tar.gz
# 2. Extrair arquivos
# 3. Executar

# Uso básico
./phoneinfoga.exe scan -n +5511999999999

# Interface web
./phoneinfoga.exe serve
# Acessar: http://localhost:5000

# Salvar resultados
./phoneinfoga.exe scan -n +5511999999999 --output json > resultado.json
```

**O PhoneInfoga é uma ferramenta essencial para investigação de números de telefone. Use sempre respeitando a privacidade e legalidade!** 📞🕵️‍♂️