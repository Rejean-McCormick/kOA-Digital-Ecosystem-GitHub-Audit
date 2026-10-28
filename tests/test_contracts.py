import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ContractsTest(unittest.TestCase):
    def test_json_contract_files_load(self):
        for name in ("observation.schema.json", "legacy-record.schema.json"):
            doc = json.loads((ROOT / "schemas" / name).read_text())
            self.assertEqual(doc["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertTrue(doc["properties"])

    def test_no_mutating_github_methods(self):
        source = (ROOT / "koa_audit/github_client.py").read_text()
        self.assertIn('method="GET"', source)
        for method in ('method="POST"', 'method="PATCH"', 'method="DELETE"', 'method="PUT"'):
            self.assertNotIn(method, source)


if __name__ == "__main__": unittest.main()
