# Mr.Holmes — investigação com interface gráfica

**Pasta:** `osint/Mr.Holmes/` · **Site:** https://github.com/Lucksi/Mr.Holmes ·
**Instalação (Windows):** `Install.cmd` · **Uso:** `python MrHolmes.py`

> Use apenas com alvos próprios/autorizados.

## O que é e como funciona

Investigação OSINT com **GUI** (claro/escuro/alto contraste) + CLI. Entrada
(`MrHolmes.py` → `Core/Support/Menu`) chama os buscadores de `Core/`:

| Módulo (`Core/`) | Função |
|---|---|
| `Searcher_website.py` | domínios: WHOIS, DNS, tecnologias, links |
| `Searcher.py` | usernames em dezenas de sites |
| `Searcher_phone.py` | telefones: operadora, região, mensageiros |
| `Searcher_person.py` | pessoas: agrega e gera hipóteses sobre o alvo |
| `E_Mail.py` | e-mail lookup silencioso |
| `Dork.py` | Google Dorks prontas contra o alvo |
| `Port_Scanner.py` | portas do host |
| `PDF_Converter.py` | exporta o dossiê em PDF |
| `Transfer.py` + `QRCodes/` | transfere resultados via QR Code |
| `Decoder.py` | decodifica hashes/encodings |
| `Proxies/` | proxies anônimos; `Useragents/` rotaciona user-agent |

Config em `Configuration/Configuration.ini` (ex.: chave WhoIS
https://whois.whoisxmlapi.com); idiomas em `Lang/`; sessões e evidências em
`Logs/`, `Temp/`, `Transfer/`.

## Uso

```bash
cd osint/Mr.Holmes
Install.cmd        # só na primeira vez (Windows)
python MrHolmes.py # menu → Domínio / Username / Telefone / Pessoa / Dork
```

Siga o menu: informe o alvo, revise mapas/gráficos/hipóteses e exporte o PDF.
