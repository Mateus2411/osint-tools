# Utilitários de linha de comando

Scripts da raiz do SET (rodar no WSL, dentro de `~/setoolkit`). Parte de
[INDICE.md](INDICE.md).

## setoolkit

O launcher interativo: checa root (`geteuid`), prepara
`/etc/setoolkit/set.config` (regrava se `CONFIG_VERSION` mudou), cria
`~/.set/reports` e `set.options`, aceita os termos 1 vez
(`src/agreement4`), mostra o banner e entra no loop do menu.

## seautomate `<arquivo>`

Roda o SET sem digitar, via **pexpect**: abre o menu em subprocesso e envia
**uma resposta por linha** do arquivo. Regras do arquivo:

- linha vazia = aperta Enter (aceita o padrão)
- palavra `CONTROL-C-HERE` = envia Ctrl+C
- no fim, devolve o terminal para você (`child.interact()`)

Exemplo (harvester automático no lab):

```
1
2
3
2
127.0.0.1
http://localhost:8000/login
```

## seproxy

Configura proxy: pergunta servidor/usuário/senha e grava
`export http_proxy=...` em `~/.set/proxy.config`; depois mata processos presos
nas portas 80/443. Só em Linux.

## seupdate

Atualiza sem abrir o menu: chama `core.update_set()` (`git pull` do oficial).
