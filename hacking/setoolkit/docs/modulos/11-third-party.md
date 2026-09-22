# Third Party Modules — menu 1 → 10 e menu 3

Módulos da comunidade carregados dinamicamente por
`src/core/module_handler.py`. Parte de [INDICE.md](INDICE.md).

## Os que vêm juntos

| Arquivo em `modules/` | Função |
|---|---|
| `ratte_module.py` / `ratte_only_module.py` | payload RATTE com/sem menu (tunelamento HTTP) |
| `google_analytics_attack.py` | vetor via Google Analytics |
| `test_module.example` | modelo de módulo novo |
| `test_module.readme`, `readme.txt` | como empacotar (detalhes no `readme/User_Manual.pdf`) |

## Como criar o seu

1. Copie `test_module.example` para `meu_modulo.py` na pasta `modules/`
2. Mantenha os campos obrigatórios e a função de entrada:

```python
import src.core.setcore as core

MAIN = "   Meu módulo"
AUTHOR = "   Seu nome"

def main():
    core.java_applet_attack("https://alvo-teste.local", "443", "reports/")
```

3. Ele aparece no menu automaticamente — `module_handler` importa todo `.py`
   da pasta que siga a convenção `MAIN`/`AUTHOR`/`main()`.
