"""events.log and Windows toast notifications."""
from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

CREATE_NO_WINDOW = 0x08000000 if os.name == "nt" else 0

_TOAST_PS = r"""
$ErrorActionPreference = 'SilentlyContinue'
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$t = [System.Security.SecurityElement]::Escape($env:G2G_TITLE)
$b = [System.Security.SecurityElement]::Escape($env:G2G_BODY)
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml("<toast><visual><binding template='ToastGeneric'><text>$t</text><text>$b</text></binding></visual></toast>")
$app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($app).Show([Windows.UI.Notifications.ToastNotification]::new($xml))
"""


class Notifier:
    def __init__(self, events_log: Path, toast: bool = True):
        self.events_log = events_log
        self.toast_enabled = toast and os.name == "nt"

    def event(self, kind: str, msg: str, toast: bool = False):
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')}\t{kind}\t{msg}\n"
        self.events_log.parent.mkdir(parents=True, exist_ok=True)
        with open(self.events_log, "a", encoding="utf-8") as f:
            f.write(line)
        print(line, end="", flush=True)
        if toast:
            self.toast(f"G2G eval: {kind}", msg)

    def toast(self, title: str, body: str):
        if not self.toast_enabled:
            return
        env = dict(os.environ, G2G_TITLE=title[:120], G2G_BODY=body[:240])
        try:
            subprocess.Popen(["powershell", "-NoProfile", "-NonInteractive", "-Command", _TOAST_PS], env=env,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_NO_WINDOW)
        except OSError:
            pass
