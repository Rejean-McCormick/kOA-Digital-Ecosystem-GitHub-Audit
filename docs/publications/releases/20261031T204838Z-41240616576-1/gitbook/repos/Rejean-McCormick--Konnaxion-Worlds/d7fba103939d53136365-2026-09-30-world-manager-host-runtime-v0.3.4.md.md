<!-- Frozen source: https://github.com/Rejean-McCormick/Konnaxion-Worlds/blob/0e8d47c147d13a5721c5ae8e4b1dd7968def51fb/docs/status/2026-09-30-world-manager-host-runtime-v0.3.4.md | commit: 0e8d47c147d13a5721c5ae8e4b1dd7968def51fb | SHA-256: 794915810bc530555e6c48d19d04df1400f305505607577f5d40f2e9237ca94c -->

# World Manager host runtime v0.3.4

The Windows Manager now auto-selects the sibling Konnaxion host runtime when available. The previous v0.3.3 startup could finish the standalone `.venv` bootstrap and then appear frozen while an implicit standalone `migrate`/registry refresh ran silently against the production-shaped database.

Hosted mode uses `../Konnaxion/backend/.venv/Scripts/python.exe` and `../Konnaxion/backend/manage.py`, which preserves Konnaxion-owned seed roots, scenario importers, fixture loaders and settings. A GUI refresh is read-only and never runs host migrations.

Standalone mode remains supported as a fallback; its control-plane migration runs once per Manager process and setup can inherit a detected database URL without placing credentials in process arguments.
