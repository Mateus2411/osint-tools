# theHarvester — coleta de e-mails e subdomínios

**Pasta:** `osint/theHarvester/` · **Site:** https://github.com/laramies/theHarvester ·
**Instalação:** `pip install theHarvester`

> Use apenas em domínios próprios/autorizados.

## O que é e como funciona

Coleta passiva: consulta buscadores e APIs e extrai **e-mails, subdomínios,
hosts, IPs e URLs** ligados a um domínio. Cada fonte é um plugin em
`theHarvester/discovery/` (google, bing, crtsh, github, shodan, virustotal,
dnssearch, haveibeenpwned… — dezenas); `parsers/` limpa os resultados e
`lib/` centraliza requisições/keys (`~/.theHarvester/api-keys.yaml` para as
fontes que exigem chave).

## Uso

```bash
theHarvester -d alvo.com -b google
theHarvester -d alvo.com -b google,bing,crtsh,github -l 200
theHarvester -d alvo.com -b all -f resultado   # salva HTML/XML
theHarvester -d alvo.com -b dnssearch          # brute-force de DNS
```

| Flag | Efeito |
|---|---|
| `-d` | domínio alvo (obrigatório) |
| `-b` | fontes separadas por vírgula, ou `all` |
| `-l` | limite de resultados por fonte |
| `-f` | prefixo dos relatórios (HTML + XML) |
| `-c` | brute-force de DNS com dicionário |
| `-e` | DNS extra (AXFR/shuffle) |

## Saída

No terminal: e-mails, hosts e IPs agrupados por fonte; com `-f`, relatórios
para encadear com Holehe (e-mails) e SpiderFoot (domínio).
