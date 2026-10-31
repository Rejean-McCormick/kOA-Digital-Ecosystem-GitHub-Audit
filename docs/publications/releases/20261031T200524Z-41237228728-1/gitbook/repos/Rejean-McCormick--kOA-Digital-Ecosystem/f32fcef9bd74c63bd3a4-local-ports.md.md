<!-- Frozen source: https://github.com/Rejean-McCormick/kOA-Digital-Ecosystem/blob/4ed4b8928665ebd723b68f8b3f2cb2f196d6374f/docs/2-Technical-Reference/40-integration/skope-ekole/local-ports.md | commit: 4ed4b8928665ebd723b68f8b3f2cb2f196d6374f | SHA-256: 91962efd40cba244cac76b29400ae2f22677edc4a35cddc85f59c37f5363402a -->

# Local development port matrix (as supplied / updated)

| Local app | URL | Evidence |
| --- | --- | --- |
| Ékole Core & Élève | `http://127.0.0.1:8765/` and `/eleve/` | Ékole `README.md`, `LANCER_EKOLE_3_APPS.bat` |
| Ékole Enseignant | `http://127.0.0.1:8766/` | Ékole `README_EKOLE_3_APPS_v8.md`, launch batch |
| Ékole OpsConsole | `http://127.0.0.1:8766/` | Ékole `opsconsole/README.md`, `opsconsole/ekole_ops.py` |
| Skope | `http://127.0.0.1:8767/` | Updated Skope `skope/config.py` default |

**Coexistence warning:** Enseignant and OpsConsole both default to `8766`; launching both with their defaults will collide. This update **does not patch Ékole**, only records the conflict. Skope supports `--port` override, e.g. `py -3 -m skope demo --port 8790`.

Commands:

```powershell
# Skope, from its repository root
py -3 -m skope demo
# Open http://127.0.0.1:8767/

# Ékole (separate repository)
py -3 tools\ekole.py preview
# Open http://127.0.0.1:8765/

# To use OpsConsole, avoid running Ékole Enseignant on the same default port
py -3 opsconsole\ekole_ops.py
# Open http://127.0.0.1:8766/
```

This is **developer-local** addressing, not network deployment, Koali onboarding, OIDC integration or public routing.
