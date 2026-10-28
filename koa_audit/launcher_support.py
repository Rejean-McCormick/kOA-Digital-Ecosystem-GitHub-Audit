"""Pure argument builders for the optional Windows GUI (no Tk dependencies).

Every command invokes this repository's OBSERVE-only CLI; no shell, repo
mutations, remote code execution or token-handling behavior lives here.
"""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from .inventory import check_repo
from .legacy import SCHEMAS


INVENTORY_SOURCES = ("bundled", "github")


def _integer(value: object, *, label: str, minimum: int, maximum: int) -> str:
    raw = str(value).strip()
    if not re.fullmatch(r"[0-9]+", raw):
        raise ValueError(f"{label} : entrer un entier entre {minimum} et {maximum}.")
    number = int(raw)
    if not minimum <= number <= maximum:
        raise ValueError(f"{label} : entrer un entier entre {minimum} et {maximum}.")
    return str(number)


def make_plan_args(*, source: str, limit: object) -> list[str]:
    if source not in INVENTORY_SOURCES:
        raise ValueError("Source d'inventaire inconnue")
    return ["-m", "koa_audit", "plan", "--inventory-source", source,
            "--limit", _integer(limit, label="Limite", minimum=0, maximum=100000)]


def make_audit_args(*, source: str, limit: object, workers: object,
                    max_age_days: object, out: Path, require_auth: bool,
                    discover_public_owner: bool, legacy_dir: Path | None) -> list[str]:
    args = make_plan_args(source=source, limit=limit)
    args[2] = "audit"
    args += ["--workers", _integer(workers, label="Workers", minimum=1, maximum=8),
             "--max-age-days", _integer(max_age_days, label="Ancienneté", minimum=1, maximum=3650),
             "--out", str(out.expanduser().resolve())]
    if require_auth:
        args.append("--require-auth")
    if discover_public_owner:
        args.append("--discover-public-owner")
    if legacy_dir is not None:
        folder = legacy_dir.expanduser().resolve()
        if not folder.is_dir():
            raise ValueError("Le dossier de diagnostics historiques est introuvable.")
        args += ["--legacy-dir", str(folder)]
    return args


def default_legacy_filename(tool: str, repo: str, *, now: datetime | None = None) -> str:
    if tool not in SCHEMAS:
        raise ValueError("Famille de diagnostic inconnue")
    check_repo(repo)
    timestamp = (now or datetime.now()).strftime("%Y%m%d-%H%M%S-%f")
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", f"{tool}-{repo.replace('/', '-')}").lower()
    return f"{slug}-{timestamp}.json"


def make_legacy_args(*, tool: str, repo: str, source_path: Path,
                     member: str, out_dir: Path, now: datetime | None = None) -> list[str]:
    if tool not in SCHEMAS:
        raise ValueError("Famille de diagnostic inconnue")
    check_repo(repo)
    source_path = source_path.expanduser().resolve()
    if not source_path.is_file():
        raise ValueError("Fichier historique introuvable")
    suffix = source_path.suffix.lower()
    member = member.strip()
    if suffix == ".json" and member:
        raise ValueError("Le champ membre ZIP doit être vide pour un JSON")
    if suffix == ".zip" and (not member or member.startswith("/") or ".." in member.split("/")):
        raise ValueError("Indiquer un chemin interne ZIP exact et sûr (ex. verification/embedded/summary.json)")
    if suffix not in (".json", ".zip"):
        raise ValueError("Choisir un fichier .json ou .zip")
    out_path = out_dir.expanduser().resolve() / default_legacy_filename(tool, repo, now=now)
    if out_path.exists():
        raise ValueError("Un import portant ce nom existe déjà : réessayer.")
    args = ["-m", "koa_audit", "import-legacy", "--tool", tool,
            "--repo", repo, "--input", str(source_path), "--out", str(out_path)]
    if member:
        args += ["--member", member]
    return args


def make_local_args(*, command: str, root: Path, depth: object, limit: object,
                    max_files: object = "6000", out: Path | None = None,
                    only_inventory: bool = False, legacy_dir: Path | None = None) -> list[str]:
    """No-token, offline command builder. Never sends or executes code remotely."""
    if command not in ("local-plan", "local-audit"):
        raise ValueError("Mode local inconnu")
    folder = root.expanduser().resolve()
    if not folder.is_dir():
        raise ValueError(f"Dossier source introuvable : {folder}")
    args = ["-m", "koa_audit", command, "--root", str(folder),
            "--max-depth", _integer(depth, label="Profondeur", minimum=0, maximum=10),
            "--limit", _integer(limit, label="Limite", minimum=0, maximum=100000)]
    if command == "local-audit":
        if out is None:
            raise ValueError("Choisir le dossier des rapports")
        args.extend(["--max-files", _integer(max_files, label="Fichiers par dépôt", minimum=1, maximum=100000),
                     "--out", str(out.expanduser().resolve())])
        if only_inventory:
            args.append("--only-inventory")
        if legacy_dir is not None:
            folder = legacy_dir.expanduser().resolve()
            if not folder.is_dir():
                raise ValueError("Dossier des rapports historiques introuvable")
            args.extend(["--legacy-dir", str(folder)])
    return args
