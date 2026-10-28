import base64
import hashlib
import json
import unittest
from pathlib import Path

from koa_audit.inventory import parse_inventory, bundled_inventory, remote_inventory


class InventoryTest(unittest.TestCase):
    def test_bundled_repositories(self):
        path = Path(__file__).resolve().parent.parent / "data/initial_inventory.json"
        rows, origin = bundled_inventory(path)
        self.assertEqual(len(rows), 49)
        self.assertFalse(origin["authoritative_live"])
        self.assertNotIn("local_root", rows[0])

    def test_duplicate_case_insensitive(self):
        raw = json.dumps([{"github_repo": "User/Repo"}, {"github_repo": "user/repo"}]).encode()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            parse_inventory(raw)

    def test_invalid_name(self):
        for name in ("evil/x/../../admin", "https://github.com/foo/bar", "a/../b", "", "a%2fb"):
            with self.assertRaises(ValueError):
                parse_inventory(json.dumps([{"github_repo": name}]).encode())

    def test_remote_pin(self):
        raw = json.dumps([{"github_repo": "a/b", "local_root": "SECRET"}]).encode()
        sha = "c" * 40
        class Fake:
            def __init__(self): self.calls = []
            def get(self, path, params=None):
                self.calls.append((path, params))
                if path == "/repos/a/b" and params is None: return {"default_branch": "main"}, {}
                if path.endswith("/commits/main"): return {"sha": sha}, {}
                return {"encoding": "base64", "content": base64.b64encode(raw).decode()}, {}
        client = Fake()
        rows, origin = remote_inventory(client, "a/b")
        self.assertEqual(origin["git_commit"], sha)
        self.assertEqual(client.calls[-1][1], {"ref": sha})
        self.assertEqual(rows[0]["github_repo"], "a/b")
        self.assertNotIn("local_root", rows[0])


if __name__ == "__main__": unittest.main()
