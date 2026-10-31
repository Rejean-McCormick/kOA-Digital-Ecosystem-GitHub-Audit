<!-- Frozen source: https://github.com/Rejean-McCormick/Konstellation/wiki/Windows-Installation | commit: 01bfc9126e06db9560d1c84e4b315026a28690af | SHA-256: 48eb64117d39d630cd7c243248993d7730ae023e4976365f744db71fc142f30d -->

# Installing and Launching on Windows

## Recommended installation

The **root launcher for the neutral snapshot** is `Konstellation.cmd`, next to `package.json`. It selects `config/local-catalog.json` and starts the local Node server.

1. Back up the previous installation before applying a patch.
2. Extract the full package or copy the patch while preserving the directory structure.
3. Check versions:

```powershell
node --version
npm --version
```

4. Run `Konstellation.cmd` from Windows Explorer. Expected console output indicates **neutral selection in My Kristals** and the reader configuration file.
5. Open `http://127.0.0.1:4321`; keep the console window open during the session.

## Manual startup for developers

In the repository directory:

```powershell
npm ci
npm run build
$env:KONSTELLATION_DEPLOYMENT_PROFILE = 'local'
$env:KONSTELLATION_BACKEND_CONFIG = 'C:\mycode\Konstellation\Konstellation\config\local-catalog.json'
npm start
```

`npm ci` assumes a reproducible `package-lock.json` is present. The snapshot describes a release requirement for a lockfile: if it is missing, **do not claim `npm ci` has been validated**; prepare dependencies according to your repository's procedure.

## One visible launcher at the root

Keep **`Konstellation.cmd`** for everyday use. Archive older `Ouvrir_Kristal_Catho_v10.cmd`, `Ouvrir_Theophile_demo.cmd`, `Launch_My_Kristals.cmd`, and `Konstellation_Launcher.cmd`. `Test_Konstellation.cmd` and `Update_Biblical_Corpus.cmd` are development/maintenance utilities, not primary launchers.

If included, `tools/maintenance/Ranger_anciens_lanceurs.cmd` provides **reversible cleanup with confirmation**. Delete nothing until the neutral launcher works. Never use a launcher-cleanup script to remove a Kristal's `canon/`, `state/`, or `derived/` directories.

## Networking

The local profile normally listens on `127.0.0.1:4321`. Do not expose the local catalog or file paths to LAN/public networks. Profiles `lan`, `shared`, and `public` have different authentication requirements and **do not** provide access to the local-file reader.

See [[Security|Security-and-Privacy]] and [[Troubleshooting|Troubleshooting]].
