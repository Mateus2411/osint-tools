# RedTiger-Tools — pentest + OSINT all-in-one

**Pasta:** `hacking/RedTiger-Tools/` · **Site:** https://github.com/loxy0devlp/RedTiger-Tools ·
**Instalação:** `python setup.py` · **Uso:** `python redtiger.py`

> Use apenas em alvos próprios/autorizados.

## O que é e como funciona

Suite CLI + interativa com sistema de **plugins** (`Plugins/Example.py` como
modelo). Entrada `redtiger.py` despacha para `Program/` em 3 famílias:

| Prefixo | Família | Módulos |
|---|---|---|
| `NS*` | Network Scanner (pentest) | `NSAdvancedScanner`, `NSPortScanner`, `NSVulnerabilityScanner`, `NSUrlDiscoveryCrawler` (crawler de URLs), `NSHostDiscovery`, `NSIpPinger` (ping contínuo) |
| `O*` | OSINT | `ODorkingQueryEngine` (Google dorks), `OUsernameTracker`, `OEmailLookup`/`OEmailTracker`, `OIpLookup`, `OPhoneNumerLookup`, `OInstagramProfileLookup`, `OWalletTracker` (crypto) |
| `U*` | Utilidades | `UFileMetadataScanner`/`UFileMetadataDeleter`, `UWebsiteCloner` |
| `T*` | Sistema | `THelp`, `TSettingsUpdate`, `TVersion` |

Config em `Config/`, dados em `Data/`, resultados em `Ouput/`.

## Uso

```bash
cd hacking/RedTiger-Tools
python setup.py       # primeira vez
python redtiger.py    # menu interativo
python redtiger.py -pnl -p "+5511999999999"   # lookup de telefone direto
```

Combine: descubra e-mails com theHarvester → valide com Holehe → investigue
telefones/IPs aqui → varra portas do seu lab com `NSPortScanner`.
