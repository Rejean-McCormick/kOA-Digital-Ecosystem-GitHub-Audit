"""Conservative, AST-based Python TLS-verification heuristic.

Never executes imported modules, project code or network calls.  A bare
``verify=False`` is NOT sufficient: it commonly means artifact validation.
Only surface calls identifiable as HTTP/TLS libraries or SSL trust bypasses.
This is not a full TLS data-flow analysis.
"""
from __future__ import annotations

import ast

_REQUEST_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "request"}
_HTTPX_CLIENTS = {"Client", "AsyncClient"}


def tls_verification_disabled_lines(content: str) -> set[int]:
    """Return 1-based line numbers of recognizable disabled TLS checks."""
    try:
        tree = ast.parse(content)
    except (SyntaxError, ValueError):
        return set()

    # Import aliases are resolved solely from syntax, not executed imports.
    aliases: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                if item.name in ("requests", "httpx", "ssl", "urllib3"):
                    aliases[item.asname or item.name] = item.name
        elif isinstance(node, ast.ImportFrom) and node.module:
            package = node.module.split(".", 1)[0]
            if package in ("requests", "httpx", "ssl", "urllib3"):
                for item in node.names:
                    aliases[item.asname or item.name] = f"{node.module}.{item.name}"

    def dotted(node: ast.AST) -> str | None:
        if isinstance(node, ast.Name):
            return aliases.get(node.id, node.id)
        if isinstance(node, ast.Attribute):
            base = dotted(node.value)
            return f"{base}.{node.attr}" if base else None
        if isinstance(node, ast.Call):
            return dotted(node.func)
        return None

    def is_http_call(name: str | None) -> bool:
        if not name:
            return False
        parts = name.split(".")
        if parts[0] == "requests":
            return (parts[-1] in _REQUEST_METHODS and
                    (len(parts) == 2 or "Session" in parts or "sessions" in parts))
        if parts[0] == "httpx":
            return (len(parts) == 2 and parts[-1] in _REQUEST_METHODS | _HTTPX_CLIENTS) or (
                parts[-1] in _REQUEST_METHODS and any(p in _HTTPX_CLIENTS for p in parts))
        return False

    # Keep only typed client variables inferred from clear constructors.
    session_vars: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            if not isinstance(value, ast.Call):
                continue
            ctor = dotted(value.func)
            if ctor not in {"requests.Session", "requests.session", "requests.sessions.Session",
                            "httpx.Client", "httpx.AsyncClient"}:
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    session_vars.add(target.id)

    found: set[int] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = dotted(node.func)
            if name in {"ssl._create_unverified_context"}:
                found.add(node.lineno)
                continue
            # verified by named keyword on requests/httpx HTTP client calls only
            disabled = any(kw.arg == "verify" and isinstance(kw.value, ast.Constant)
                           and kw.value.value is False for kw in node.keywords)
            if disabled and (is_http_call(name) or (
                isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id in session_vars
                and node.func.attr in _REQUEST_METHODS)):
                found.add(node.lineno)
            # Explicit semantic TLS-disabling keywords are not interchangeable
            # with generic `verify=False` (artifact validation, test fixtures, ...).
            if any(kw.arg in {"verify_tls", "verify_ssl", "ssl_verify"}
                   and isinstance(kw.value, ast.Constant) and kw.value.value is False
                   for kw in node.keywords):
                found.add(node.lineno)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            value = node.value
            if not isinstance(value, ast.Constant) or value.value is not False:
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Attribute) and target.attr == "verify":
                    if isinstance(target.value, ast.Name) and target.value.id in session_vars:
                        found.add(node.lineno)
    return found
