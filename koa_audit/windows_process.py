"""Run child CLI tools without flashing terminal windows on Windows.

No shell and no mutation: this helper only configures subprocess visibility.
"""
from __future__ import annotations

import os
import subprocess


def hidden_console_kwargs() -> dict:
    """Supported by subprocess.run/Popen; portable and safe with pythonw.exe."""
    if os.name != "nt":
        return {}
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = getattr(subprocess, "SW_HIDE", 0)
    return {"creationflags": subprocess.CREATE_NO_WINDOW, "startupinfo": startupinfo}
