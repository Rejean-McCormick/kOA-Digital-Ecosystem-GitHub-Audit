"""Bounded discovery of *existing* machine reports in a verified local clone.

Never executes project code, searches arbitrary files, or copies contents to Git.
Only known report names/locations are considered.  Discovering != approving
attachment; the Windows UI asks the operator before staging any results.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
from typing import Any

from .campaigns import MAX_ATTACHMENT, _git_observation, describe_proof

# Exact allowlist, rather than a potentially expensive or privacy-invasive rglob.
REPORT_ROOTS = ("", "reports", "test-results", "test_results", "artifacts",
                "coverage", "build/reports", "build/test-results", "results")
REPORT_NAMES = ("junit.xml", "pytest.xml", "test-results.xml", "tests.xml",
                "coverage.xml", "coverage.json", "results.sarif", "report.sarif",
                "security.sarif", "codeql.sarif", "test-results.json")
RECOGNIZED = frozenset(("junit_xml_summary", "coverage_xml_summary", "coverage_json_summary",
                        "sarif_summary", "koa_static_metadata_summary"))
MAX_CANDIDATES = 8
MAX_REPORT_READ = min(MAX_ATTACHMENT, 2_000_000)


def discover(folder: Path, repo: str, *, max_results: int = MAX_CANDIDATES) -> list[dict[str, Any]]:
    """Return allowlisted report paths plus preview metadata; no raw contents.

    The Git remote identity is checked independently, so another clone cannot
    be silently attributed to a similarly named repository.  This does not
    verify that a pre-existing report was generated for the current Git HEAD.
    """
    folder = Path(folder)
    if not folder.is_dir() or folder.is_symlink():
        raise ValueError("Clone local indisponible ou lien symbolique")
    if _git_observation(folder, repo).get("status") != "verified_git_origin":
        raise ValueError("Origine GitHub du clone non vérifiée pour ce dépôt")
    root = folder.resolve(strict=True)
    results = []
    limit = max(0, min(int(max_results), MAX_CANDIDATES))
    for directory in REPORT_ROOTS:
        for filename in REPORT_NAMES:
            if len(results) >= limit:
                return results
            target = folder / directory / filename
            try:
                if not target.is_file() or target.is_symlink():
                    continue
                # Refuse symlinked ancestor directories and paths outside clone.
                resolved = target.resolve(strict=True)
                if not resolved.is_relative_to(root) or resolved != target.absolute():
                    continue
                size = target.stat().st_size
                if size == 0 or size > MAX_REPORT_READ:
                    continue
                # Reports only; never inspect arbitrary source or .env files.
                raw = target.read_bytes()
                if len(raw) != size:
                    continue
                summary = describe_proof(target, raw)
                if summary.get("recognition") not in RECOGNIZED:
                    continue
                results.append({"repository": repo, "path": target,
                                "name": target.relative_to(folder).as_posix(),
                                "size_bytes": size, "sha256": hashlib.sha256(raw).hexdigest(),
                                "summary": summary,
                                "version_relation": "unverified_preexisting_report"})
            except (OSError, ValueError):
                continue
    return results
