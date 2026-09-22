# Command-line utilities

SET root scripts (run from WSL, inside `~/setoolkit`). Part of
[INDICE.en.md](INDICE.en.md).

## setoolkit

The interactive launcher: checks root (`geteuid`), prepares
`/etc/setoolkit/set.config` (rewrites when `CONFIG_VERSION` changed), creates
`~/.set/reports` and `set.options`, accepts the terms once
(`src/agreement4`), shows the banner and enters the menu loop.

## seautomate `<file>`

Runs SET without typing, via **pexpect**: spawns the menu as a subprocess and
sends **one answer per file line**. File rules:

- empty line = presses Enter (accepts the default)
- the word `CONTROL-C-HERE` = sends Ctrl+C
- at the end, hands the terminal back to you (`child.interact()`)

Example (automatic harvester in the lab):

```
1
2
3
2
127.0.0.1
http://localhost:8000/login
```

## seproxy

Configures a proxy: asks server/user/password and writes
`export http_proxy=...` to `~/.set/proxy.config`; then kills processes stuck
on ports 80/443. Linux only.

## seupdate

Updates without opening the menu: calls `core.update_set()` (`git pull` from
upstream).
