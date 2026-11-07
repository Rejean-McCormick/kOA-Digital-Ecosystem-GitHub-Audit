"""Keep owner-provided evidence out of the public test run."""
import os
import unittest


requires_private_evidence = unittest.skipIf(
    os.environ.get("KOA_PUBLIC_TESTS") == "1",
    "Requires local private_evidence/ fixtures",
)
