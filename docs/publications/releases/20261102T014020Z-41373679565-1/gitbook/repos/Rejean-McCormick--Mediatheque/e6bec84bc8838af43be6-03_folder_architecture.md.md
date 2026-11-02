<!-- Frozen source: https://github.com/Rejean-McCormick/Mediatheque/blob/21e8d732e6690ab15ced87179eb5b152386fe716/docs/03_folder_architecture.md | commit: 21e8d732e6690ab15ced87179eb5b152386fe716 | SHA-256: 2cd99fdbe33892351f8d3499925b5522e2519af51ff3c65c8cdd01a6eb53918f -->

# Architecture des dossiers

```text
workspace/
├── mediatheque/
│   ├── 05_TOOLS/
│   ├── 06_GUI/
│   ├── schemas/sqlite/
│   ├── contracts/
│   ├── docs/
│   └── tests/
└── content/
    ├── 01_DB/
    ├── 02_STORAGE/
    ├── 03_IMPORTS/
    ├── 04_EXPORTS/
    ├── 07_BACKUPS/
    ├── 08_LOGS/
    ├── kristals/
    ├── documents/
    └── config.toml
```

`mediatheque/` est versionnable et ne contient pas de données privées. `content/` est l'état local et doit rester privé.
