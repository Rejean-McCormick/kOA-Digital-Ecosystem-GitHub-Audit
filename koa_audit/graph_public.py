"""Validate the kOA owner's architecture registry for a dated, public graph.

No runtime integration, authorization or certification status is inferred.
The source repository and inventory are read only from the same pinned Git commit.
"""
from __future__ import annotations

import hashlib
import json
import re

REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
NODE = re.compile(r"^[a-z][a-z0-9_-]{1,63}$")
SHA = re.compile(r"^[a-f0-9]{40}$")


def compile_public_graph(registry_text: str, inventory_text: str, source_sha: str) -> dict:
    if not SHA.fullmatch(source_sha):
        raise ValueError("Source revision must be an immutable Git SHA")
    registry = json.loads(registry_text)
    inventory = json.loads(inventory_text)
    if not isinstance(registry, dict) or registry.get("format") != "koa.graph.registry.v1":
        raise ValueError("Unsupported owner graph format")
    if not isinstance(inventory, list) or len(inventory) != registry.get("reference_count"):
        raise ValueError("Owner inventory and graph source count disagree")
    owner = registry.get("owner_repository")
    if owner != "Rejean-McCormick/kOA-Digital-Ecosystem":
        raise ValueError("Unexpected owner registry")
    if registry.get("reference_inventory") != "docs/inventory/repositories.json":
        raise ValueError("Unexpected inventory source")
    official = {}
    for row in inventory:
        if not isinstance(row, dict) or row.get("scope") != "PUBLIC":
            raise ValueError("Only explicit public repositories are publishable")
        repo = row.get("github_repo", "")
        if not isinstance(repo, str) or not REPO.fullmatch(repo) or repo in official:
            raise ValueError("Duplicate or invalid official repository")
        official[repo] = {"repo":repo, "name":repo.split("/")[-1],
                          "admission":"reference", "role":"Not mapped in this registry",
                          "group":"other", "node_id":None}
    candidates = {}
    for row in registry.get("additional_repositories", []):
        if not isinstance(row, dict) or row.get("admission") != "discovered_not_admitted":
            raise ValueError("New repositories must remain explicit candidates")
        repo = row.get("github_repo", "")
        if not isinstance(repo, str) or not REPO.fullmatch(repo) or repo in official or repo in candidates:
            raise ValueError("Invalid or duplicate candidate repository")
        candidates[repo] = {"repo":repo, "name":repo.split("/")[-1],
                            "admission":"discovered_not_admitted", "role":"Discovered repository; authority to qualify",
                            "group":"other", "node_id":None}
    systems = []
    ids = set()
    for row in registry.get("systems", []):
        if not isinstance(row, dict):
            raise ValueError("Invalid system record")
        node_id, repo = row.get("id"), row.get("github_repo")
        if not isinstance(node_id, str) or not NODE.fullmatch(node_id) or node_id in ids:
            raise ValueError("Invalid or duplicate system node")
        if repo not in official or row.get("evidence_state") != "documented_responsibility":
            raise ValueError("System node lacks documented owner repository")
        if row.get("source") != "docs/1-Overview/Components.md":
            raise ValueError("System source must point to owner overview")
        label, role = row.get("label"), row.get("responsibility")
        if not isinstance(label,str) or not label.strip() or not isinstance(role,str) or not role.strip():
            raise ValueError("Empty system role")
        group = row.get("group")
        if group not in {"civic", "knowledge", "platform", "protocol", "language", "other"}:
            raise ValueError("Unknown system group")
        ids.add(node_id)
        official[repo].update(role=role, group=group, node_id=node_id)
        systems.append({"id":node_id, "label":label, "repo":repo, "role":role,
                        "group":group, "evidence_state":"documented_responsibility"})
    links = []
    seen_links = set()
    for row in registry.get("relations", []):
        if not isinstance(row,dict):raise ValueError("Invalid graph edge")
        source, dest, state = row.get("from"), row.get("to"), row.get("evidence_state")
        if source not in ids or dest not in ids or state not in {"proposed","documented_passage"}:
            raise ValueError("Undocumented relation endpoint or state")
        if row.get("verification") != "not_certified":
            raise ValueError("Cannot infer qualified integrations from architecture")
        if row.get("source") != "docs/1-Overview/Integration.md":
            raise ValueError("Relation must cite the integration overview")
        key=(source,dest)
        if key in seen_links:raise ValueError("Duplicate relation")
        seen_links.add(key)
        links.append({"from":source,"to":dest,"label":str(row.get("label") or ""),
                      "status":"proposed" if state=="proposed" else "documented",
                      "verification":"not_certified"})
    return {
        "format":"koa.graph.public.v1",
        "owner_repository":owner,
        "owner_commit":source_sha,
        "graph_sha256":hashlib.sha256(registry_text.encode()).hexdigest(),
        "inventory_sha256":hashlib.sha256(inventory_text.encode()).hexdigest(),
        "source_date":registry.get("source_date"),
        "reference_count":len(official),
        "candidate_count":len(candidates),
        "repositories":[*official.values(),*candidates.values()],
        "systems":systems,
        "links":links,
        "notice":"Architecture and discovery only; no repository or integration certification",
    }
