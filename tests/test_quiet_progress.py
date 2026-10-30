"""No blinking consoles, non-animated, factual campaign progress."""
from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from koa_audit import campaigns, evidence_collector, windows_process, profiles

ROOT = Path(__file__).resolve().parents[1]


class QuietProgressTests(unittest.TestCase):
    def test_progress_captures_actual_repository_counts_and_final_verification(self):
        progress = []
        with tempfile.TemporaryDirectory() as td:
            with patch.dict(os.environ, {"LOCALAPPDATA": str(Path(td)/'local')}):
                target = campaigns.create_campaign(
                    ROOT, "Campagne sans animation", store=Path(td)/'campaigns',
                    git_probe=False, progress=lambda done, total, text: progress.append((done, total, text)))
            self.assertTrue(target.exists())
        n = len(profiles.inventory(ROOT))
        self.assertEqual(progress[0][:2], (0, n+4))
        self.assertEqual(progress[-1][:2], (n+4, n+4))
        self.assertIn("vérifiée", progress[-1][2])
        self.assertEqual([p[0] for p in progress if 1 <= p[0] <= n],
                         list(range(1,n+1)) + [n]) # same count for attachment phase
        self.assertEqual([p[0] for p in progress], sorted(p[0] for p in progress))

    def test_failed_campaign_never_claims_complete_progress(self):
        observations=[]
        with tempfile.TemporaryDirectory() as td:
            with patch.object(campaigns, 'MAX_CAMPAIGN', 100), \
                 patch.dict(os.environ, {'LOCALAPPDATA':str(Path(td)/'state')}):
                with self.assertRaises(ValueError):
                    campaigns.create_campaign(ROOT, 'Campagne invalide', store=Path(td)/'campaigns',
                        git_probe=False, progress=lambda *args: observations.append(args))
        self.assertFalse(observations and observations[-1][0] == observations[-1][1])

    def test_non_windows_process_has_no_platform_specific_flags(self):
        with patch.object(windows_process, 'os', SimpleNamespace(name='posix')):
            self.assertEqual(windows_process.hidden_console_kwargs(), {})

    def test_windows_process_is_hidden_without_shell(self):
        class Startup:
            def __init__(self):
                self.dwFlags=0
                self.wShowWindow=-1
        with patch.object(windows_process, 'os', SimpleNamespace(name='nt')), \
             patch.object(windows_process.subprocess, 'STARTUPINFO', Startup, create=True), \
             patch.object(windows_process.subprocess, 'STARTF_USESHOWWINDOW', 1, create=True), \
             patch.object(windows_process.subprocess, 'CREATE_NO_WINDOW', 0x08000000, create=True):
            options=windows_process.hidden_console_kwargs()
        self.assertEqual(options['creationflags'], 0x08000000)
        self.assertEqual(options['startupinfo'].dwFlags, 1)
        self.assertEqual(options['startupinfo'].wShowWindow, 0)

    def test_git_and_optional_tool_invocations_pass_visibility_flags(self):
        sentinel={'creationflags':0x08000000}
        with patch('koa_audit.campaigns.hidden_console_kwargs', return_value=sentinel), \
             patch('koa_audit.campaigns.subprocess.run') as call:
            call.return_value.returncode=0
            call.return_value.stdout='head123\n'
            self.assertEqual(campaigns._git_cmd(Path('.'),'rev-parse','HEAD'), 'head123')
            self.assertEqual(call.call_args.kwargs['creationflags'],0x08000000)
        with patch('koa_audit.evidence_collector.hidden_console_kwargs',return_value=sentinel), \
             patch('koa_audit.evidence_collector.subprocess.run') as call:
            call.return_value.returncode=0
            call.return_value.stdout=None
            result=evidence_collector._run(['git','--version'], 2)
            self.assertEqual(result['status'], 'ok')
            self.assertEqual(call.call_args.kwargs['creationflags'],0x08000000)

if __name__ == '__main__':
    unittest.main()
