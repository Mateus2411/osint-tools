# Third Party Modules — menu 1 → 10 and menu 3

Community modules loaded dynamically by `src/core/module_handler.py`. Part of
[INDICE.en.md](INDICE.en.md).

## Bundled ones

| File in `modules/` | Purpose |
|---|---|
| `ratte_module.py` / `ratte_only_module.py` | RATTE payload with/without menu (HTTP tunneling) |
| `google_analytics_attack.py` | vector via Google Analytics |
| `test_module.example` | new-module template |
| `test_module.readme`, `readme.txt` | packaging how-to (details in `readme/User_Manual.pdf`) |

## How to write your own

1. Copy `test_module.example` to `my_module.py` in the `modules/` folder
2. Keep the required fields and entry function:

```python
import src.core.setcore as core

MAIN = "   My module"
AUTHOR = "   Your name"

def main():
    core.java_applet_attack("https://test-target.local", "443", "reports/")
```

3. It shows up in the menu automatically — `module_handler` imports every
   `.py` in the folder following the `MAIN`/`AUTHOR`/`main()` convention.
