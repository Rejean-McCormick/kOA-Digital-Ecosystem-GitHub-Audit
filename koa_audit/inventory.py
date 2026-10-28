"""Load provenance-aware scopes without promoting inventory to an execution grant."""
from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

from .github_client import GitHubClient, ApiError

REPO_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
INVENTORY_PATH = "docs/inventory/repositories.json"


def check_repo(name: str) -> str:
    if not isinstance(name, str) or not REPO_PATTERN.fullmatch(name) or ".." in name:
        raise ValueError(f"Invalid repository identifier: {str(name)[:90]}")
    return name


def parse_inventory(payload: bytes) -> tuple[list[dict], str]:
    if len(payload) > 2_000_000:
        raise ValueError("Inventory too large")
    content = json.loads(payload)
    if not isinstance(content, list):
        raise ValueError("Expected JSON inventory array")
    found: set[str] = set()
    clean: list[dict] = []
    for item in content:
        if not isinstance(item, dict):
            raise ValueError("Invalid inventory entry")
        name = check_repo(item.get("github_repo"))
        if name.lower() in found:
            raise ValueError(f"Duplicate repository: {name}")
        found.add(name.lower())
        clean.append({"github_repo": name, "scope": str(item.get("scope", "UNSPECIFIED")),
                      "source_status": str(item.get("source_status", item.get("status", "unspecified")))})
    if not clean:
        raise ValueError("Inventory is empty")
    return clean, hashlib.sha256(payload).hexdigest()


def bundled_inventory(path: Path) -> tuple[list[dict], dict]:
    data = path.read_bytes()
    rows, digest = parse_inventory(data)
    return rows, {"kind": "bundled_snapshot", "sha256": digest, "git_commit": None,
                  "authoritative_live": False}


def remote_inventory(client: GitHubClient, source_repo: str) -> tuple[list[dict], dict]:
    """Pin the owner inventory read to a specific commit, never floating HEAD."""
    source_repo = check_repo(source_repo)
    repo_path = "/repos/" + source_repo
    metadata, _ = client.get(repo_path)
    default_branch = metadata.get("default_branch")
    if not isinstance(default_branch, str) or not default_branch:
        raise ValueError("Missing inventory default branch")
    head, _ = client.get(repo_path + "/commits/" + quote(default_branch, safe=""))
    commit = head.get("sha")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", commit):
        raise ValueError("Missing inventory commit SHA")
    content, _ = client.get(repo_path + "/contents/" + INVENTORY_PATH, {"ref": commit})
    if not isinstance(content, dict) or content.get("encoding") != "base64":
        raise ValueError("Expected base64 inventory content")
    try:
        raw = base64.b64decode(content["content"], validate=False)
    except (ValueError, KeyError) as exc:
        raise ValueError("Invalid encoded inventory") from exc
    rows, digest = parse_inventory(raw)
    return rows, {"kind": "github_repository", "repository": source_repo,
                  "path": INVENTORY_PATH, "git_commit": commit, "sha256": digest,
                  "authoritative_live": True}


def owner_public_discovery(client: GitHubClient, owner: str) -> tuple[set[str], bool]:
    if not re.fullmatch(r"[A-Za-z0-9-]{1,39}", owner):
        raise ValueError("Invalid account owner")
    # Public API only. Not a complete inventory of private repositories.
    try:
        rows, truncated = client.list_items("/users/" + owner + "/repos", max_pages=10,
                                             params={"type": "owner", "sort": "full_name"})
    except ApiError:
        return set(), True
    return {item["full_name"] for item in rows if isinstance(item.get("full_name"), str)}, truncated
