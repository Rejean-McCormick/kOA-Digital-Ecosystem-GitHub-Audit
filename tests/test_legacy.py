import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from koa_audit.legacy import normalize_legacy, ingest, load_normalized_directory, SCHEMAS


class LegacyTest(unittest.TestCase):
    def test_families_normalize_metadata_only(self):
        for tool, schema in SCHEMAS.items():
            with self.subTest(tool=tool):
                data = json.dumps({"schema": schema, "verdict": "WARN", "run_id": "r01",
                    "levels": [{"id": "K00", "verdict": "PASS", "findings": [{"message": "SECRET_VALUE"}]}],
                    "findings": [{"message": "SECRET_VALUE"}],
                    "target_repo_root": "C:/private/path", "evidence_digest": "d"*64,
                    "subject": {"git": {"commit": "1"*40}, "subject_digest": "e"*64}}).encode()
                normalized = normalize_legacy(tool, "owner/repo", data, label="summary.json")
                self.assertEqual(normalized["source_schema"], schema)
                self.assertEqual(normalized["verdict"], "WARN")
                self.assertEqual(normalized["levels"][0]["findings_count"], 1)
                self.assertNotIn("SECRET_VALUE", json.dumps(normalized))
                self.assertNotIn("C:/private/path", json.dumps(normalized))
                self.assertFalse(normalized["evidence_independently_verified"])
                self.assertEqual(normalized["current_security_conclusion"], "NOT_ASSESSED")

    def test_schema_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "schema"):
            normalize_legacy("KorDiag", "a/b", b'{"schema":"other","verdict":"PASS","levels":[]}', label="x")

    def test_zip_explicit_member_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            zip_path = Path(tmp) / "source.zip"
            with zipfile.ZipFile(zip_path, "w") as z:
                z.writestr("runs/summary.json", json.dumps({"schema": "kordiag.summary.v1",
                    "verdict": "FAIL", "levels": []}))
            record = ingest("KorDiag", "owner/repo", zip_path, member="runs/summary.json")
            self.assertEqual(record["verdict"], "FAIL")
            with self.assertRaises(ValueError):
                ingest("KorDiag", "owner/repo", zip_path, member="../summary.json")

    def test_invalid_directory_record_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp)/"bad.json").write_text('{"format":"other"}')
            records, errors = load_normalized_directory(Path(tmp))
            self.assertEqual(records, [])
            self.assertEqual(errors, ["bad.json"])


if __name__ == "__main__": unittest.main()
