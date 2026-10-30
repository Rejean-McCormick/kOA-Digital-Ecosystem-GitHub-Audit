"""Regression: no-console Windows pythonw must serve a real HTTP response."""
from __future__ import annotations

import functools
import http.server
import runpy
import sys
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.request import urlopen

SCRIPT = Path(__file__).resolve().parents[1] / "kOA_GitHub_Audit_Launcher.pyw"
ROOT = SCRIPT.parent


class DashboardPreviewTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = runpy.run_path(str(SCRIPT))
        cls.handler = cls.module["_NoConsolePreviewHandler"]

    def test_preview_serves_html_css_js_json_with_no_stderr(self):
        handler = functools.partial(self.handler, directory=str(ROOT / "docs"))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        server.daemon_threads = True
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            # Emulate pythonw.exe: no stderr and no console.
            with patch.object(sys, "stderr", None):
                for name, expected in (("", b"<!doctype html>"),
                                       ("assets/dashboard.css", b"body"),
                                       ("assets/dashboard.js", b"fetch"),
                                       ("data/dashboard.json", b"snapshots")):
                    with self.subTest(url=name):
                        with urlopen(f"http://127.0.0.1:{server.server_port}/{name}", timeout=5) as r:
                            self.assertEqual(r.status, 200)
                            self.assertIn(expected, r.read())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)

    def test_handler_is_quiet_in_no_console_mode(self):
        self.assertIs(self.handler.log_message.__code__.co_consts[-1], None)

    def test_gui_method_uses_fixed_handler(self):
        import inspect
        method = self.module["AuditLauncher"]._preview_dashboard
        source = inspect.getsource(method)
        helper = inspect.getsource(self.module["AuditLauncher"]._ensure_preview_server)
        self.assertIn("_ensure_preview_server", source)
        self.assertIn("_NoConsolePreviewHandler", helper)
        self.assertIn("127.0.0.1", helper)


if __name__ == "__main__":
    unittest.main()
