"""Archive the local emission 4 and transfer its diagnostic campaign to Audit."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

CLI = "Diagnostic-kOA-Digital-Ecosystem-CLI.py"
CONFIG = "koa-ecosystem-diag.config.json"
LOCAL_CONFIG = "koa-ecosystem-diag.config.local.json"
JOURNEY = "konnaxion-orgo-decision-impact"
ORIGINALS = {
    "konnaxion.json": "2ec1696eb6b7eb51eea7d92a0a653b3f7278c308c310996f7435772e6ee2d393",
    "orgo.json": "f187e464e1f33d40df2674ebd2fa92aea2a8766662a0cc49884a341d48c5c6f9",
}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def archive_files(source, destination):
    originals = {}
    for name, expected in ORIGINALS.items():
        path = source / name
        if not path.is_file():
            path = destination / name
        data = path.read_bytes()
        if digest(data) != expected:
            raise ValueError(f"Le fichier diffère de l'export original de l'émission 4 : {path}")
        originals[name] = data

    kx = json.loads(originals["konnaxion.json"].decode("utf-8-sig"))
    orgo = json.loads(originals["orgo.json"].decode("utf-8-sig"))
    outbound, impact = kx["outbound"], kx["impact"]
    decision = dict(
        journey_id=JOURNEY, source_repo="Konnaxion", target_repo="Orgo",
        contract="governance.decision.execute/1.0.0",
        attempt_id=outbound["interaction_id"], correlation_id=outbound["correlation_id"],
    )
    callback = dict(
        journey_id=JOURNEY, source_repo="Orgo", target_repo="Konnaxion",
        contract="accountability.impact.publish/1.0.0",
        attempt_id=impact["interaction_id"], correlation_id=impact["correlation_id"],
    )
    # Keep the correlation actually observed for each hop. The operation ID
    # documents the association without standing in for an end-to-end ID.
    normalized = {
        "konnaxion-observations-natives.json": json_bytes([
            dict(decision, phase="sent", timestamp=outbound["envelope_time"]),
            dict(callback, phase="received", timestamp=impact["published_at"]),
        ]),
        "orgo-observations-natives.json": json_bytes([
            dict(decision, phase="received", timestamp=orgo["received_at"]),
            dict(callback, phase="sent", timestamp=orgo["started_at"]),
        ]),
    }
    files = originals | normalized
    for name, data in files.items():
        path = destination / name
        if path.exists() and path.read_bytes() != data:
            raise ValueError(f"Archive existante différente : {path}")

    destination.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        path = destination / name
        try:
            with path.open("xb") as stream:
                stream.write(data)
        except FileExistsError:
            if path.read_bytes() != data:
                raise ValueError(f"Archive existante différente : {path}") from None
    return normalized


def trace_override(diag, root, destination, normalized):
    entries = []
    for filename in (CONFIG, LOCAL_CONFIG):
        path = diag / filename
        if path.is_file():
            configured = json.loads(path.read_text(encoding="utf-8-sig"))
            entries = configured.get("interrepo", {}).get("exchange_trace_files", entries)
    if not isinstance(entries, list):
        raise ValueError("interrepo.exchange_trace_files doit être une liste.")

    current = []
    for owner in ("Konnaxion", "Orgo"):
        name = f"{owner.lower()}-observations-natives.json"
        path = destination / name
        current.append({
            "path": path.relative_to(root).as_posix(),
            "owner_repo": owner,
            "mode": "non_renseigne",
            "sha256": digest(normalized[name]),
        })

    # Replace only this emission's previous descriptors during this run.
    old_sources = (destination, root / "preuves" / destination.name)
    replaced_paths = {
        (folder / f"{owner}-observations.json").resolve()
        for folder in old_sources for owner in ("konnaxion", "orgo")
    }
    replaced_paths.update((root / item["path"]).resolve() for item in current)

    def already_added(entry):
        value = entry.get("path") if isinstance(entry, dict) else entry
        return isinstance(value, str) and (root / value).resolve() in replaced_paths

    return {"interrepo": {"exchange_trace_files": [
        entry for entry in entries if not already_added(entry)
    ] + current}}


def run(cwd, arguments, marker=None):
    env = os.environ | {"PYTHONIOENCODING": "utf-8"}
    result = None
    with subprocess.Popen(
        [sys.executable, *map(str, arguments)], cwd=cwd, env=env,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        encoding="utf-8", errors="replace",
    ) as process:
        for line in process.stdout:
            print(line, end="", flush=True)
            if marker and line.startswith(marker):
                result = Path(line.removeprefix(marker).strip())
        return process.wait(), result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(r"C:\mycode"))
    parser.add_argument("--audit", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--diag", type=Path)
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    audit = args.audit.resolve()
    diag = (args.diag or root / "kOA_Digital_Ecosystem" / "kOADiag").resolve()
    source = (args.source or root / "preuves" / "konnaxion-orgo-emission-4").resolve()
    destination = (audit / "private_evidence" / "konnaxion-orgo-emission-4").resolve()
    for path in (audit / "koa_audit" / "__main__.py", diag / CLI, diag / CONFIG):
        if not path.is_file():
            raise ValueError(f"Installation introuvable : {path}")
    if not destination.is_relative_to(root) or not destination.is_relative_to(audit):
        raise ValueError(f"Le dossier d'archive doit se trouver sous {root} dans le dépôt Audit.")

    print(f"[1/4] Archiver les exports dans {destination}", flush=True)
    normalized = archive_files(source, destination)
    override = trace_override(diag, root, destination, normalized)

    print("[2/4] kOADiag — validation intégrale avec les exports passifs", flush=True)
    with tempfile.TemporaryDirectory(prefix="koa-emission-4-") as temporary:
        config = Path(temporary) / "observations.json"
        config.write_bytes(json_bytes(override))
        code, summary = run(diag, [CLI, "run", "validation-integrale", "--root", root,
                                   "--config", config], "SUMMARY=")
        if summary is None or summary.name != "summary.json" or not summary.is_file():
            raise ValueError(f"kOADiag n'a produit aucun résumé exploitable (code {code}).")
        campaign = json.loads(summary.read_text(encoding="utf-8-sig"))
        print(f"Verdict kOADiag : {campaign['verdict']} (code {code})", flush=True)

        print("[3/4] Exporter les métadonnées de cette campagne", flush=True)
        bundle = Path(temporary) / "campaign.zip"
        export_code, _ = run(diag, [CLI, "export-audit", "--run-root", summary.parent,
                                    "--out", bundle])
        if export_code or not bundle.is_file():
            raise ValueError(f"Export Audit impossible (code {export_code}). Résumé : {summary}")

        print("[4/4] Importer la campagne dans GitHub Audit", flush=True)
        import_code, _ = run(audit, ["-m", "koa_audit", "ecosystem-diag-import", "--input", bundle])
        if import_code:
            raise ValueError(f"Import Audit impossible (code {import_code}). Résumé : {summary}")

    print(f"Campagne {campaign['run_id']} importée. Résumé kOADiag : {summary}", flush=True)
    return code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as error:
        sys.exit(f"[ARRÊT] {error}")
