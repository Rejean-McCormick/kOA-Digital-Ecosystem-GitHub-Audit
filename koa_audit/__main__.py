"""CLI: default local scans are offline; legacy remote observer remains optional."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from .audit import run_audit
from .github_client import GitHubClient, ApiError
from .inventory import bundled_inventory, remote_inventory, owner_public_discovery
from .legacy import SCHEMAS, ingest, load_normalized_directory
from .report import summarize, write_reports
from .local_scan import run_local_audit, write_local_reports, discover_repositories

DEFAULT_INVENTORY = Path(__file__).resolve().parent.parent / "data" / "initial_inventory.json"
SOURCE_REPO = "Rejean-McCormick/kOA-Digital-Ecosystem"


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m koa_audit", description="Read-only ecosystem audit")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("plan", "audit"):
        p = sub.add_parser(name, help="Inventory plan / GitHub observation")
        p.add_argument("--inventory-source", choices=("bundled", "github"), default="bundled")
        p.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY,
                       help="Path to bundled inventory when source=bundled")
        p.add_argument("--source-repo", default=SOURCE_REPO)
        p.add_argument("--limit", type=int, default=0)
        p.add_argument("--require-auth", action="store_true")
        if name == "audit":
            p.add_argument("--workers", type=int, default=3)
            p.add_argument("--max-age-days", type=int, default=30)
            p.add_argument("--out", type=Path, default=Path("reports"))
            p.add_argument("--legacy-dir", type=Path)
            p.add_argument("--discover-public-owner", action="store_true",
                           help="Compare inventory to public repositories; never automatically add them")
    for name in ("local-plan", "local-audit"):
        p = sub.add_parser(name, help="Offline inspection of local Git working trees (no API token)")
        p.add_argument("--root", type=Path, action="append", required=True,
                       help="Top-level folder containing local repositories; repeatable")
        p.add_argument("--max-depth", type=int, default=4)
        p.add_argument("--limit", type=int, default=0, help="0 = all")
        if name == "local-audit":
            p.add_argument("--out", type=Path, default=Path("reports"))
            p.add_argument("--legacy-dir", type=Path)
            p.add_argument("--max-files", type=int, default=6000)
            p.add_argument("--only-inventory", action="store_true",
                           help="Skip local Git repositories outside bundled inventory")
    p = sub.add_parser("import-legacy", help="Import a historical summary JSON as metadata-only evidence")
    p.add_argument("--tool", choices=sorted(SCHEMAS), required=True)
    p.add_argument("--repo", required=True, help="Explicit owner/repository binding")
    p.add_argument("--input", required=True, type=Path, help="JSON file or ZIP containing exact member")
    p.add_argument("--member", help="Exact ZIP member path; no ZIP extraction")
    p.add_argument("--out", type=Path, required=True)
    return parser


def execute(args: argparse.Namespace) -> int:
    if args.command in ("local-plan", "local-audit"):
        if args.limit < 0 or not 0 <= args.max_depth <= 10:
            raise ValueError("Invalid local scan limits")
        for root in args.root:
            if not root.expanduser().is_dir():
                raise ValueError(f"Local source folder does not exist: {root}")
        if args.command == "local-plan":
            folders, meta = discover_repositories(args.root, max_depth=args.max_depth)
            print(json.dumps({"mode": "LOCAL_OBSERVE", "repositories_found": len(folders),
                              "folders": [str(p) for p in folders[:args.limit or None]],
                              "discovery": meta}, indent=2, ensure_ascii=False))
            return 0
        if not 1 <= args.max_files <= 100000:
            raise ValueError("--max-files must be between 1 and 100000")
        report = run_local_audit(args.root, inventory_path=DEFAULT_INVENTORY,
                                 max_depth=args.max_depth, max_files=args.max_files,
                                 include_unlisted=not args.only_inventory, limit=args.limit,
                                 progress=lambda line: print(line, flush=True))
        if args.legacy_dir:
            legacy, errors = load_normalized_directory(args.legacy_dir)
            selected = {r["repository"].lower() for r in report["repositories"]}
            report["historical_legacy"] = [r for r in legacy if r["repository"].lower() in selected]
            report["legacy_ingestion"] = {"invalid_filenames": errors,
                                          "out_of_scope_count": len(legacy) - len(report["historical_legacy"])}
        else:
            report["historical_legacy"] = []
        write_local_reports(args.out, report)
        print(json.dumps({"repositories_discovered": report["local_repositories_discovered"],
                          "repositories_scanned": report["repositories_scanned"],
                          "finding_patterns": report["findings_by_type"],
                          "missing_locally": len(report["inventory_repositories_missing_locally"]),
                          "reports": str(args.out.resolve())}, indent=2, ensure_ascii=False))
        return 0
    if args.command == "import-legacy":
        result = ingest(args.tool, args.repo, args.input, member=args.member)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("Imported historical metadata only:", args.out)
        return 0
    if args.limit < 0:
        raise ValueError("--limit must be >= 0")
    client = GitHubClient()
    if args.require_auth and not client.token:
        raise ValueError("No read-only API token configured (KOA_AUDIT_TOKEN or GH_TOKEN)")
    if args.inventory_source == "github":
        rows, origin = remote_inventory(client, args.source_repo)
    else:
        rows, origin = bundled_inventory(args.inventory)
    if args.limit:
        rows = rows[:args.limit]
    if args.command == "plan":
        print(json.dumps({"count": len(rows), "inventory_source": origin,
                          "repositories": [r["github_repo"] for r in rows]}, indent=2))
        return 0
    legacy = []
    legacy_errors = []
    if args.legacy_dir:
        legacy, legacy_errors = load_normalized_directory(args.legacy_dir)
    results = run_audit(client, rows, workers=args.workers, max_age_days=args.max_age_days)
    selected = {r["github_repo"].lower() for r in rows}
    matched_legacy = [x for x in legacy if x["repository"].lower() in selected]
    unbound_count = len(legacy) - len(matched_legacy)
    discovery = {"status": "not_requested", "scope": "public_only"}
    if args.discover_public_owner:
        owner = rows[0]["github_repo"].split("/")[0]
        if all(r["github_repo"].split("/")[0].lower() == owner.lower() for r in rows):
            found, incomplete = owner_public_discovery(client, owner)
            discovery = {"status": "partial_or_unknown" if incomplete else "ok",
                         "scope": "public_only", "unlisted_public_repositories": sorted(
                             r for r in found if r.lower() not in selected)}
        else:
            discovery = {"status": "skipped", "reason": "multiple_owners"}
    report = {
        "format": "koa_audit.observation.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mode": "OBSERVE", "mutations_performed": False,
        "inventory": origin, "selected_repositories": len(rows),
        "summary": summarize(results, matched_legacy),
        "repositories": results,
        "historical_legacy": matched_legacy,
        "legacy_ingestion": {"invalid_filenames": legacy_errors, "out_of_scope_count": unbound_count},
        "public_discovery": discovery,
        "caveats": ["No GitHub settings or repository contents changed.",
                    "No scans were triggered. GitHub alert counts reflect existing detections only.",
                    "Lack of alerts does not establish code scanning coverage.",
                    "Historical imports are not revalidated nor authority-bearing."],
    }
    write_reports(args.out, report)
    print(json.dumps(report["summary"], indent=2))
    print("Reports saved to", args.out)
    return 0


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    try:
        return execute(args)
    except (ValueError, OSError, json.JSONDecodeError, ApiError, KeyError) as exc:
        print("Audit error:", exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
