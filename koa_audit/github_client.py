"""Minimal GET-only GitHub REST client; no target repository mutations."""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ApiError(Exception):
    status: int
    category: str

    def __str__(self) -> str:
        # Do not disclose API response bodies, which may contain sensitive data.
        return f"GitHub API {self.category} (HTTP {self.status})"


def status_category(status: int) -> str:
    if status in (401, 403):
        return "access_denied_or_feature_unavailable"
    if status == 404:
        return "not_found_or_feature_unavailable"
    if status == 422:
        return "not_supported_or_invalid"
    if status == 429:
        return "rate_limited"
    if status >= 500:
        return "upstream_error"
    return "api_error"


class GitHubClient:
    def __init__(self, token: str | None = None, *, retries: int = 2, timeout: int = 20,
                 base_url: str = "https://api.github.com") -> None:
        self.token = token if token is not None else (
            os.environ.get("KOA_AUDIT_TOKEN") or os.environ.get("GH_TOKEN") or None
        )
        self.retries = retries
        self.timeout = timeout
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, params: dict[str, str | int] | None = None) -> tuple[Any, dict[str, str]]:
        if not path.startswith("/") or path.startswith("//") or "?" in path or "#" in path:
            raise ValueError("Expected a GitHub API path, not an arbitrary URL")
        url = self.base_url + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "koa-github-audit/0.1",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        for attempt in range(self.retries + 1):
            req = urllib.request.Request(url, headers=headers, method="GET")
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as res:
                    payload = res.read(12_000_001)
                    if len(payload) > 12_000_000:
                        raise ApiError(0, "response_too_large")
                    return json.loads(payload), dict(res.headers.items())
            except urllib.error.HTTPError as err:
                if err.code in (429, 500, 502, 503, 504) and attempt < self.retries:
                    time.sleep(min(2 ** attempt, 4))
                    continue
                # Prevent response-body leakage into logs/artifacts.
                raise ApiError(err.code, status_category(err.code)) from None
            except (urllib.error.URLError, TimeoutError):
                if attempt < self.retries:
                    time.sleep(min(2 ** attempt, 4))
                    continue
                raise ApiError(0, "network_error") from None
            except ValueError:
                raise ApiError(0, "invalid_json") from None
        raise ApiError(0, "unknown_error")

    def list_items(self, path: str, key: str | None = None, *, max_pages: int = 10,
                   params: dict[str, str | int] | None = None) -> tuple[list[dict], bool]:
        """Return items and whether results were truncated by the page limit."""
        if not 1 <= max_pages <= 100:
            raise ValueError("max_pages out of range")
        query = dict(params or {})
        query["per_page"] = 100
        items: list[dict] = []
        for page in range(1, max_pages + 1):
            query["page"] = page
            payload, headers = self.get(path, query)
            rows = payload.get(key) if key is not None and isinstance(payload, dict) else payload
            if not isinstance(rows, list):
                raise ApiError(0, "unexpected_response_shape")
            items.extend(x for x in rows if isinstance(x, dict))
            link = headers.get("Link", headers.get("link", ""))
            has_next = any(part.strip().endswith('rel="next"') for part in link.split(","))
            if not has_next:
                return items, False
        return items, True
