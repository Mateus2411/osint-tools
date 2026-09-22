# Holehe — descoberta de contas por e-mail

**Pasta:** `osint/holohe/` · **Site:** https://github.com/megadose/holehe ·
**Instalação:** `pip install holehe` (já instalado aqui: v1.61)

> Use apenas com e-mails próprios ou com consentimento.

## O que é e como funciona

O Holehe testa um e-mail contra **+100 sites** (Instagram, Twitter, Adobe,
Gravatar etc.) usando a função "esqueci a senha"/registro de cada um: se o
site diz que o e-mail existe, a conta existe. Não quebra senha nem invade
nada — só revela **onde há cadastro**. Roda local, sem API key.

## Uso

```bash
holehe email@alvo.com.br
holehe a@mail.com b@mail.com --only-used   # só onde tem conta
holehe email@mail.com -C                    # exporta CSV
holehe email@mail.com -T 20                 # timeout 20s por site
```

| Flag | Efeito |
|---|---|
| `--only-used` | mostra só sites com conta encontrada |
| `--no-color` / `--no-clear` | saída simples, sem limpar a tela |
| `-NP` | não tenta recuperação de senha |
| `-C` | gera CSV com os resultados |
| `-T` | timeout por site (padrão 10s) |

## Saída

Tabela no terminal (`[+]` conta encontrada) ou CSV com `-C`. Combine com o
SpiderFoot (e-mails do domínio) e o theHarvester para encadear a investigação.
