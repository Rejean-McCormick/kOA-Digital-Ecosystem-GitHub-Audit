"""kOA GitHub Audit — interface Windows locale (Python 3.11+, Tkinter).

Double-cliquer sur ce .pyw à la racine du dépôt. Toutes les opérations passent
par la CLI de lecture seule et ne modifient aucun dépôt GitHub cible.
"""
from __future__ import annotations

import os
import queue
import subprocess
import sys
import tempfile
import threading
import traceback
import functools
import http.server
import html
import json
import re
import zipfile
from urllib.parse import urlsplit, unquote, quote
import webbrowser
from datetime import datetime, timezone
from pathlib import Path

# Delay project imports until after selecting the extracted repository folder.
# pythonw.exe hides stderr: a missing koa_audit package previously closed silently.
try:
    from tkinter import END, StringVar, BooleanVar, Tk, messagebox, filedialog, ttk
    from tkinter.scrolledtext import ScrolledText
    TK_ERROR = None
except Exception as error:
    TK_ERROR = error

ROOT = Path(__file__).resolve().parent
SCHEMAS = ()


class _NoConsolePreviewHandler(http.server.SimpleHTTPRequestHandler):
    """Serve dashboard assets even under pythonw.exe (where sys.stderr is None).

    BaseHTTPRequestHandler logs every response to sys.stderr *before* sending
    headers. On Windows pythonw.exe, this raises AttributeError and Chrome
    displays ERR_EMPTY_RESPONSE. An HTTP preview must not depend on a console.
    """

    def log_message(self, format: str, *args: object) -> None:
        # Preview is loopback-only. Never write HTTP logs to a missing stderr.
        pass

    def do_GET(self) -> None:
        """Serve local qualification states and full reports only on loopback.

        These URLs do NOT exist in GitHub Pages and are never written into docs/.
        No free-form evidence, file paths or notes are exported through JSON.
        """
        route = urlsplit(self.path).path
        if (route not in ("/data/local-qualification.json", "/api/kristal/atlas", "/api/campaigns/summary", "/api/review/summary")
                and not route.startswith(("/local/engineering/", "/local/campaigns", "/local/review"))):
            return super().do_GET()
        if (self.client_address[0] not in ("127.0.0.1", "::1")
                or self.headers.get("Sec-Fetch-Site", "same-origin") == "cross-site"
                or self.headers.get("Origin") not in (None, "", f"http://127.0.0.1:{self.server.server_port}")):
            self.send_error(403)
            return
        try:
            from koa_audit import profiles, qualification
            if route == "/data/local-qualification.json":
                claims = qualification.load_state().get("claims", {})
                allowed = set(qualification.STATES)
                result = {}
                for repo in profiles.inventory(ROOT):
                    entries = claims.get(repo, {})
                    result[repo] = {
                        stage: (entries.get(stage, {}).get("status")
                                if isinstance(entries.get(stage), dict)
                                and entries[stage].get("status") in allowed else "Non évalué")
                        for stage in qualification.STAGE_IDS
                    }
                payload = json.dumps({"format": "koa_qualification.public_status.v1", "repositories": result},
                                     ensure_ascii=False).encode("utf-8")
                kind = "application/json; charset=utf-8"
            elif route == "/api/review/summary":
                from koa_audit import evidence_review
                result = evidence_review.report_counts(ROOT)
                result["format"] = "koa.evidence_review.summary.v1"
                payload = json.dumps(result, ensure_ascii=False).encode("utf-8")
                kind = "application/json; charset=utf-8"
            elif route.startswith("/local/review"):
                from koa_audit import evidence_review
                payload = evidence_review.render_page(ROOT, route).encode("utf-8")
                kind = "text/html; charset=utf-8"
            elif route == "/api/kristal/atlas":
                from koa_audit import kristal_source
                root = getattr(self.server, "kristal_source", kristal_source.get_source_root())
                try:
                    source = kristal_source.build_local_kristal_view(root, profiles.inventory(ROOT))
                except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError):
                    source = {
                        "format": kristal_source.FORMAT, "state": "missing", "matched": 0,
                        "repositories": [],
                        "notice": "Source Kristal locale indisponible ou non lisible. "
                                  "Vérifier le dossier dans l'application Windows.",
                    }
                payload = json.dumps(source, ensure_ascii=False).encode("utf-8")
                kind = "application/json; charset=utf-8"
            elif route == "/api/campaigns/summary":
                from koa_audit import campaigns
                payload = json.dumps(campaigns.latest_summary(), ensure_ascii=False).encode("utf-8")
                kind = "application/json; charset=utf-8"
            elif route.startswith("/local/campaigns"):
                from koa_audit import campaigns
                segments=route.strip("/").split("/")
                if (len(segments)==5 and segments[:2]==["local","campaigns"]
                        and segments[3:]==["review","download"]):
                    payload = campaigns.read_archived_review(segments[2])
                    kind = "application/octet-stream"
                    extra_disposition = 'attachment; filename="KOA-REVUE-HISTORIQUE-2026-10-30.zip"'
                elif (len(segments)==6 and segments[:2]==["local","campaigns"]
                        and segments[3]=="download" and segments[5].isdigit()):
                    info, payload=campaigns.read_proof(segments[2],unquote(segments[4]),int(segments[5]))
                    kind="application/octet-stream"
                    name=Path(info.get("name", "preuve")).name[:140]
                    safe=re.sub(r"[^A-Za-z0-9._-]", "_", name) or "preuve"
                    extra_disposition=f'attachment; filename="{safe}"; filename*=UTF-8\'\'{quote(name)}'
                else:
                    payload = campaigns.render_local_page(route).encode("utf-8")
                    kind = "text/html; charset=utf-8"
            else:
                slug = unquote(route[len("/local/engineering/"):])
                if not re.fullmatch(r"[A-Za-z0-9_.-]{1,120}", slug):
                    self.send_error(404); return
                repo = next((r for r in profiles.inventory(ROOT)
                            if r.split("/", 1)[-1].casefold() == slug.casefold()), None)
                if repo is None:
                    self.send_error(404); return
                profile = profiles.get_profile(ROOT, repo, "ENGINEERING_PROFILE.md")
                if profile is None:
                    self.send_error(404); return
                payload = ("<!doctype html><html lang='fr'><head><meta charset='utf-8'>"
                           "<meta name='viewport' content='width=device-width,initial-scale=1'>"
                           "<title>Engineering Profile · " + html.escape(slug) + "</title>"
                           "<link rel='stylesheet' href='/assets/profile-report.css'></head>"
                           "<body><header><a href='/index.html?app=" + slug + "#apps'>← Revenir à la carte</a>"
                           "<span>kOA · PROFIL ORIGINAL LOCAL</span></header><main>"
                           "<h1>Engineering Profile — " + html.escape(slug) + "</h1>"
                           "<p class='lead'>Profil Markdown original, consultable localement. "
                           "Ce document et son contenu ne sont pas publiés sur GitHub Pages.</p>"
                           "<pre style='white-space:pre-wrap;overflow-wrap:anywhere;background:white;"
                           "padding:24px;border-radius:12px;border:1px solid #d3e6e1'>"
                           + html.escape(profile) + "</pre></main></body></html>").encode("utf-8")
                kind = "text/html; charset=utf-8"
            self.send_response(200)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'")
            if 'extra_disposition' in locals():
                self.send_header("Content-Disposition", extra_disposition)
            self.end_headers()
            self.wfile.write(payload)
        except (OSError, ValueError, TypeError, KeyError) as error:
            diagnostic_log(error)
            self.send_error(500, "Registre local indisponible")


def diagnostic_log(error: BaseException) -> Path | None:
    """Persist startup failures outside Git and without reading API credentials."""
    base = Path(os.environ.get("LOCALAPPDATA") or tempfile.gettempdir()) / "kOA-GitHub-Audit"
    try:
        base.mkdir(parents=True, exist_ok=True)
        path = base / "launcher-startup.log"
        with path.open("a", encoding="utf-8") as stream:
            stream.write(f"\n[{datetime.now(timezone.utc).isoformat()}] "
                         f"Python={sys.version.split()[0]} exe={sys.executable!r} "
                         f"script={str(Path(__file__).resolve())!r}\n")
            stream.write("".join(traceback.format_exception(type(error), error, error.__traceback__)))
        return path
    except OSError:
        return None


def _fatal_dialog(title: str, message: str) -> None:
    """A Windows native error remains visible even if tkinter is unavailable."""
    if os.name == "nt":
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(None, message, title, 0x10)
            return
        except Exception:
            pass
    try:
        from tkinter import Tk as ErrorTk, messagebox as error_messagebox
        popup = ErrorTk()
        popup.withdraw()
        error_messagebox.showerror(title, message, parent=popup)
        popup.destroy()
    except Exception:
        print(f"{title}: {message}", file=sys.stderr)


def _valid_project_dir(folder: Path) -> bool:
    return ((folder / "koa_audit" / "__main__.py").is_file()
            and (folder / "koa_audit" / "launcher_support.py").is_file()
            and (folder / "data" / "initial_inventory.json").is_file())


def _choose_project_root(root: Tk) -> Path:
    """Support both full-repository and separately downloaded .pyw files."""
    current = Path(__file__).resolve().parent
    for folder in (current, current.parent, Path.cwd()):
        if _valid_project_dir(folder):
            return folder
    messagebox.showwarning(
        "Dossier du projet introuvable",
        "Le lanceur ne trouve pas le dossier koa_audit.\n\n"
        "Le fichier .pyw seul ne contient pas le moteur d'audit.\n"
        "Décompressez le ZIP complet puis choisissez le dossier contenant "
        "koa_audit/ et data/.\n\n"
        "Aucune opération GitHub n'a été exécutée.", parent=root,
    )
    selected = filedialog.askdirectory(
        title="Choisir le dossier extrait de kOA-Digital-Ecosystem-GitHub-Audit",
        initialdir=str(current), parent=root,
    )
    if not selected:
        raise FileNotFoundError("Aucun dossier projet sélectionné. Décompressez le ZIP complet.")
    folder = Path(selected).resolve()
    if not _valid_project_dir(folder):
        raise FileNotFoundError(
            f"Dossier invalide : {folder}\n"
            "Il faut koa_audit/__main__.py, koa_audit/launcher_support.py "
            "et data/initial_inventory.json."
        )
    return folder


def _initialize_project(folder: Path) -> None:
    global ROOT, SCHEMAS, make_plan_args, make_audit_args, make_legacy_args
    # Do not search arbitrary installed modules if the selected folder is incomplete.
    if not _valid_project_dir(folder):
        raise FileNotFoundError("Le dépôt n'est pas extrait complètement.")
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    from koa_audit.launcher_support import (
        make_plan_args as plan, make_audit_args as audit, make_legacy_args as legacy,
    )
    from koa_audit.legacy import SCHEMAS as schemas
    ROOT = folder
    SCHEMAS = schemas
    make_plan_args, make_audit_args, make_legacy_args = plan, audit, legacy
BG = "#f5f7fa"
NAVY = "#154c49"
MUTED = "#596879"
ACCENT = "#1e6864"


def child_python() -> str:
    """Use console Python for piped output; hide its console on Windows."""
    current = Path(sys.executable)
    if current.name.lower() == "pythonw.exe":
        console = current.with_name("python.exe")
        if console.exists():
            return str(console)
    return sys.executable


def local_token_present() -> bool:
    """Only report presence; never read/display or store token values."""
    return bool(os.environ.get("KOA_AUDIT_TOKEN") or os.environ.get("GH_TOKEN"))


def _suggest_previous_local_audit() -> str:
    """Suggest an existing report only; never launch a new audit or network call."""
    preferred = ROOT / "reports" / "local" / "audit.json"
    if preferred.is_file():
        return str(preferred)
    downloads = Path.home() / "Downloads"
    try:
        from koa_audit.dashboard_sync import latest_reports
        for file in latest_reports(ROOT, downloads):
            # Only existing local-observation reports are usable for Git SHA
            # from the local scan; remote OBSERVE remains importable explicitly.
            if file.stat().st_size <= 30_000_000:
                obj=json.loads(file.read_text(encoding="utf-8-sig"))
                if obj.get("format") == "koa_audit.local_observation.v1":
                    return str(file)
    except (OSError, ValueError, TypeError):
        pass
    return ""


class AuditLauncher:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("kOA — GitHub Ecosystem Audit")
        self.root.geometry("1110x790")
        self.root.minsize(830, 640)
        self.root.configure(bg=BG)
        self._events: queue.Queue[tuple] = queue.Queue()
        self._process: subprocess.Popen[str] | None = None
        self._running = False
        self._cancelled = False
        self._action = ""
        self._action_buttons: list[ttk.Button] = []

        self.inventory_source = StringVar(value="bundled")
        self.limit = StringVar(value="0")
        self.workers = StringVar(value="3")
        self.max_age = StringVar(value="30")
        self.out_dir = StringVar(value=str(ROOT / "reports" / "local"))
        self.remote_out_dir = StringVar(value=str(ROOT / "reports" / "github"))
        self.local_root = StringVar(value=r"C:\mycode" if Path(r"C:\mycode").exists() else str(Path.home()))
        self.local_depth = StringVar(value="4")
        self.local_limit = StringVar(value="0")
        from koa_audit.kristal_source import get_source_root
        self.kristal_root = StringVar(value=str(get_source_root()))
        self.kristal_status = StringVar(value="Source Kristal : lecture locale, sans modification")
        self.dashboard_local = StringVar(value=str(ROOT / "reports" / "local" / "audit.json"))
        self.dashboard_github = StringVar(value="")
        self.triage_input = StringVar(value=str(ROOT / "reports" / "local" / "audit.json"))
        self._preview_server = None
        self.campaign_title = StringVar(value="Bilan de qualification kOA")
        self.campaign_audit = StringVar(value=_suggest_previous_local_audit())
        self.campaign_repo = StringVar(value="Rejean-McCormick/Konnaxion")
        self.campaign_detail = StringVar(value="Aucune campagne encore sélectionnée")
        self.campaign_busy = False
        self.campaign_attached = {}
        self.campaign_expected_hashes = {}
        self.campaign_source = StringVar(value="")
        self.campaign_run_tools = BooleanVar(value=False)
        self.campaign_collection_cancel = threading.Event()
        self.campaign_progress_label = StringVar(value="Prêt · aucune opération en cours")
        self.review_repo = StringVar(value="Rejean-McCormick/Konnaxion")
        self.review_search = StringVar(value="")
        self.review_summary = StringVar(value="Revue documentaire datée : conclusions vérifiées et limites visibles")
        self.review_data = None
        self.profile_repo = StringVar(value="Rejean-McCormick/Konnaxion")
        self.profile_kind = StringVar(value="ENGINEERING_PROFILE.md")
        self.profile_family = StringVar(value="Tous")
        self.profile_status = StringVar(value="Non évalué")
        self.profile_note = StringVar(value="")
        self.profile_overview = StringVar(value="")
        self.profile_audit_context = StringVar(value="")
        self.profile_catalog_items = {}
        self.profile_current_id = None
        self.qual_stage = StringVar(value="Spécifié / architecturé")
        self.qual_status = StringVar(value="Non évalué")
        self.qual_evidence = StringVar(value="")
        self.qual_scope = StringVar(value="")
        self.qual_overview = StringVar(value="")
        self.require_auth = BooleanVar(value=False)
        self.discover = BooleanVar(value=False)
        self.use_legacy = BooleanVar(value=(ROOT / ".legacy").is_dir())
        self.legacy_dir = StringVar(value=str(ROOT / ".legacy"))
        self.tool = StringVar(value="LevelUpDiag-Orgo")
        self.target_repo = StringVar(value="Rejean-McCormick/Orgo")
        self.source_file = StringVar()
        self.zip_member = StringVar(value="verification/embedded/summary.json")
        self.legacy_out = StringVar(value=str(ROOT / ".legacy"))
        self.status = StringVar(value="Prêt — aucun audit exécuté dans cette session")
        self.token_status = StringVar()

        # Owner has requested a direct, source-checked documentary reconciliation.
        # Import only missing cases, preserve every existing local decision.
        try:
            from koa_audit import evidence_adjudication
            self._adjudication_import = evidence_adjudication.import_documentary_review(ROOT)
        except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile) as error:
            self._adjudication_import = {'error': str(error)}
        self._styles()
        self._build_ui()
        if self._adjudication_import.get('error'):
            self.status.set('Revue documentaire non intégrée : '+self._adjudication_import['error'])
        elif self._adjudication_import.get('added'):
            self.status.set(f"Revue des preuves : {self._adjudication_import['added']} jalons documentés ; "
                            "décisions antérieures conservées. Créer une nouvelle campagne pour les figer.")
        self._update_token_label()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self.root.after(150, self._poll)

    def _styles(self) -> None:
        style = ttk.Style(self.root)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("TFrame", background=BG)
        style.configure("TLabel", background=BG, foreground=NAVY, font=("Segoe UI", 10))
        style.configure("TCheckbutton", background=BG, foreground=NAVY, font=("Segoe UI", 10))
        style.configure("Title.TLabel", font=("Segoe UI Semibold", 19), foreground=NAVY)
        style.configure("Muted.TLabel", font=("Segoe UI", 9), foreground=MUTED)
        style.configure("Card.TLabelframe", background=BG, borderwidth=1)
        style.configure("Card.TLabelframe.Label", background=BG, foreground=NAVY,
                        font=("Segoe UI Semibold", 10))
        style.configure("TButton", font=("Segoe UI", 10), padding=(10, 7))
        style.configure("Primary.TButton", foreground="white", background=ACCENT)
        style.map("Primary.TButton", background=[("active", "#15504d"), ("disabled", "#8aa8bb")])
        style.configure("Calm.Horizontal.TProgressbar", troughcolor="#dce9e7",
                        background=ACCENT, bordercolor="#dce9e7", lightcolor=ACCENT,
                        darkcolor=ACCENT, thickness=15)
        style.configure("TNotebook", background=BG)
        style.configure("TNotebook.Tab", font=("Segoe UI", 10), padding=(14, 9))

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=(18, 14))
        outer.pack(fill="both", expand=True)
        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 10))
        ttk.Label(header, text="kOA  /  Centre de pilotage", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="Carte des 49 dépôts · Engineering Profiles cliquables · qualification par preuve · audit local optionnel",
                  style="Muted.TLabel").pack(anchor="w", pady=(3, 0))

        self.tabs = ttk.Notebook(outer)
        self.tabs.pack(fill="both", expand=True)
        local_tab = ttk.Frame(self.tabs, padding=14)
        triage_tab = ttk.Frame(self.tabs, padding=14)
        dashboard_tab = ttk.Frame(self.tabs, padding=14)
        reports_tab = ttk.Frame(self.tabs, padding=14)
        profiles_tab = ttk.Frame(self.tabs, padding=14)
        board_tab = ttk.Frame(self.tabs, padding=14)
        campaigns_tab = ttk.Frame(self.tabs, padding=14)
        review_tab = ttk.Frame(self.tabs, padding=14)
        legacy_tab = ttk.Frame(self.tabs, padding=14)
        audit_tab = ttk.Frame(self.tabs, padding=14)
        # Dominant journey first: Ecosystem -> application -> profile / evidence.
        # Advanced audit tools are retained but no longer occupy the initial view.
        self.tabs.add(dashboard_tab, text="  Écosystème  ")
        self.tabs.add(board_tab, text="  49 dépôts  ")
        self.tabs.add(review_tab, text="  Preuves 245  ")
        self.tabs.add(campaigns_tab, text="  Campagnes  ")
        self.tabs.add(profiles_tab, text="  Certification  ")
        self.tabs.add(reports_tab, text="  Rapports  ")
        self.tabs.add(local_tab, text="  Audit local  ")
        self.tabs.add(triage_tab, text="  Vérification  ")
        self.tabs.add(audit_tab, text="  GitHub  ")
        self.tabs.add(legacy_tab, text="  Historique  ")
        self._build_audit(audit_tab)
        self._build_local(local_tab)
        self._build_triage(triage_tab)
        self._build_dashboard(dashboard_tab)
        self._build_reports(reports_tab)
        self._build_profiles(profiles_tab)
        self._build_certification_board(board_tab)
        self._build_evidence_review(review_tab)
        self._build_campaigns(campaigns_tab)
        self._build_legacy(legacy_tab)

        line = ttk.Separator(outer)
        line.pack(fill="x", pady=(9, 6))
        footer = ttk.Frame(outer)
        footer.pack(fill="x")
        ttk.Label(footer, textvariable=self.status).pack(side="left", fill="x", expand=True)
        ttk.Label(footer, textvariable=self.token_status, style="Muted.TLabel").pack(side="right")

    def _input_row(self, parent: ttk.Widget, row: int, caption: str,
                   var: StringVar, *, browse=None, width: int = 22) -> ttk.Entry:
        ttk.Label(parent, text=caption).grid(row=row, column=0, sticky="w", pady=5, padx=(0, 9))
        entry = ttk.Entry(parent, textvariable=var, width=width)
        entry.grid(row=row, column=1, sticky="ew", pady=5)
        if browse:
            ttk.Button(parent, text="Parcourir…", command=browse).grid(row=row, column=2, padx=(8, 0))
        return entry

    def _build_audit(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        options = ttk.LabelFrame(tab, text="Périmètre et options", style="Card.TLabelframe", padding=12)
        options.grid(row=0, column=0, sticky="ew")
        options.columnconfigure(1, weight=1)
        ttk.Label(options, text="Source d'inventaire").grid(row=0, column=0, sticky="w", padx=(0, 9), pady=5)
        combo = ttk.Combobox(options, textvariable=self.inventory_source,
                             values=("bundled", "github"), state="readonly", width=20)
        combo.grid(row=0, column=1, sticky="w", pady=5)
        ttk.Label(options, text="bundled = copie locale (49) · github = référence distante",
                  style="Muted.TLabel").grid(row=0, column=2, sticky="w", padx=8)
        self._input_row(options, 1, "Nombre max de dépôts (0 = tous)", self.limit)
        self._input_row(options, 2, "Workers (1 à 8)", self.workers)
        self._input_row(options, 3, "Fraîcheur CodeQL (jours)", self.max_age)
        self._input_row(options, 4, "Dossier des rapports GitHub", self.remote_out_dir, browse=self._browse_remote_report_folder)
        self._input_row(options, 5, "Dossier des diagnostics", self.legacy_dir,
                        browse=self._browse_legacy_folder)
        flags = ttk.Frame(options)
        flags.grid(row=6, column=0, columnspan=3, sticky="w", pady=(8, 0))
        ttk.Checkbutton(flags, text="Exiger un jeton GitHub", variable=self.require_auth).pack(anchor="w")
        ttk.Checkbutton(flags, text="Comparer les dépôts publics du propriétaire", variable=self.discover).pack(anchor="w")
        ttk.Checkbutton(flags, text="Inclure les diagnostics historiques normalisés",
                        variable=self.use_legacy).pack(anchor="w")

        controls = ttk.Frame(tab)
        controls.grid(row=1, column=0, sticky="ew", pady=(14, 8))
        self._action_button(controls, "Prévisualiser le périmètre", self._run_plan).pack(side="left", padx=(0, 9))
        self._action_button(controls, "Lancer l'audit OBSERVE", self._run_audit, primary=True).pack(side="left")
        self.cancel_button = ttk.Button(controls, text="Annuler", command=self._cancel, state="disabled")
        self.cancel_button.pack(side="right")
        self.progress = ttk.Progressbar(tab, mode="determinate", maximum=100, value=0,
                                        style="Calm.Horizontal.TProgressbar")
        self.progress.grid(row=2, column=0, sticky="ew", pady=(3, 8))
        ttk.Label(tab, text="Journal d'exécution (aucune clé API n'est affichée)",
                  style="Muted.TLabel").grid(row=3, column=0, sticky="w", pady=(2, 5))
        self.console = ScrolledText(tab, height=10, font=("Consolas", 9), wrap="word",
                                    state="disabled", bg="white", fg=NAVY, relief="solid", borderwidth=1)
        self.console.grid(row=4, column=0, sticky="nsew")
        tab.rowconfigure(4, weight=1)
        self._log("Prêt. Utilisez d’abord « Audit local ». L’API GitHub est facultative.")

    def _build_local(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        frame = ttk.LabelFrame(tab, text="Inspection 100 % locale · aucune clé GitHub", padding=15)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)
        self._input_row(frame, 0, "Dossier de départ", self.local_root, browse=self._browse_local_root, width=57)
        self._input_row(frame, 1, "Dossier de rapports", self.out_dir, browse=self._browse_report_folder, width=57)
        self._input_row(frame, 2, "Profondeur max (0-10)", self.local_depth)
        self._input_row(frame, 3, "Dépôts max (0 = tous)", self.local_limit)
        actions = ttk.Frame(frame)
        actions.grid(row=4, column=0, columnspan=3, sticky="w", pady=(15, 4))
        self._action_button(actions, "Découvrir les dépôts", self._run_local_plan).pack(side="left", padx=(0, 10))
        self._action_button(actions, "Scanner localement", self._run_local_audit, primary=True).pack(side="left")
        ttk.Label(tab, text="Le scanner ne clone, ne télécharge et ne modifie aucun dépôt. Il n’exécute pas les CI ni CodeQL.",
                  style="Muted.TLabel", wraplength=900).grid(row=1, column=0, sticky="w", pady=14)

    def _build_triage(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        frame = ttk.LabelFrame(tab, text="Contre-vérification ciblée — sans scanner à nouveau les dépôts", padding=15)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)
        self._input_row(frame, 0, "Dossier local", self.local_root, browse=self._browse_local_root, width=57)
        self._input_row(frame, 1, "audit.json existant", self.triage_input, browse=self._browse_triage_json, width=57)
        self._action_button(frame, "Contre-vérifier et créer le ZIP", self._run_triage, primary=True).grid(row=2, column=1, sticky="w", pady=14)
        ttk.Label(tab, text="ZIP de métadonnées expurgées : aucun .env, aucune valeur secrète, aucun fichier source brut.",
                  style="Muted.TLabel", wraplength=900).grid(row=1, column=0, sticky="w", pady=14)

    def _build_dashboard(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        frame = ttk.LabelFrame(tab, text="Carte de l'écosystème, rapports d'ingénierie et progression des qualifications", padding=15)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)
        self._input_row(frame, 0, "Référentiel Kristal (local)", self.kristal_root,
                        browse=self._browse_kristal_root, width=57)
        ttk.Label(frame, textvariable=self.kristal_status, style="Muted.TLabel").grid(
            row=1, column=0, columnspan=3, sticky="w", pady=(0, 5))
        self._input_row(frame, 2, "Rapport local (JSON)", self.dashboard_local,
                        browse=lambda: self._choose_json(self.dashboard_local), width=57)
        self._input_row(frame, 3, "Rapport GitHub (optionnel)", self.dashboard_github,
                        browse=lambda: self._choose_json(self.dashboard_github), width=57)
        btns=ttk.Frame(frame)
        btns.grid(row=4, column=0, columnspan=3, sticky="w", pady=(14, 5))
        self._action_button(btns, "Ouvrir le centre de pilotage (carte + profils)", self._preview_dashboard, primary=True).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Vérifier Kristal", command=self._check_kristal_root).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Actualiser les rapports", command=self._run_dashboard).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Publier sur GitHub", command=self._sync_dashboard).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Ouvrir le dossier docs", command=lambda: self._open_file(ROOT / "docs")).pack(side="left")
        ttk.Button(frame, text="Consulter les 245 dossiers de preuves historiques →",
                   command=self._review_open_browser).grid(row=5, column=0, columnspan=3, sticky="w", pady=(5, 2))
        note=("La source Kristal est lue à chaque actualisation du navigateur local, sans changer les fichiers du référentiel. "
              "Les associations proposées restent distinctes des liens explicites ; elles ne sont ni des intégrations vérifiées ni des certifications. Elle ne part PAS sur GitHub Pages. « Publier sur GitHub » envoie les bilans autorisés, la carte publique et "
              "les profils d'ingénierie expurgés (avec noms publics des dépôts). "
              "Aucun jeton à saisir, aucun nouvel audit, aucun code source ou secret publié. "
              "Git pour Windows utilise votre connexion GitHub existante. Le bouton local d'aperçu ne publie rien.")
        ttk.Label(tab, text=note, wraplength=910, justify="left", style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=14)
        ttk.Label(tab, text="Parcours recommandé : ouvrir la carte → choisir un dépôt → cliquer « Engineering Profile » → suivre ses jalons. "
                  "L’aperçu local affiche les preuves évaluées sur ce PC; la version publique n'exporte jamais ce registre.",
                  wraplength=910, justify="left").grid(row=3, column=0, sticky="w", pady=9)
        ttk.Label(tab, text="Une seule configuration GitHub peut être nécessaire : Settings > Pages > Source : GitHub Actions. "
                  "Ensuite, le site se déploie automatiquement après chaque publication. Ne pas utiliser le bouton d'audit distant.",
                  wraplength=910, justify="left").grid(row=2, column=0, sticky="w", pady=8)

    def _build_campaigns(self, tab: ttk.Frame) -> None:
        from koa_audit import profiles, campaigns
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(3, weight=1)
        group = ttk.LabelFrame(tab, text="Créer une capture datée de conformité — preuves gelées sur ton PC", padding=14)
        group.grid(row=0, column=0, sticky="ew")
        group.columnconfigure(1, weight=1)
        self._input_row(group, 0, "Nom de la campagne", self.campaign_title, width=52)
        self._input_row(group, 1, "audit.json existant (facultatif)", self.campaign_audit,
                        browse=lambda: self._choose_json(self.campaign_audit), width=52)
        ttk.Label(group, text="Dépôt (preuve complémentaire facultative)").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Combobox(group, textvariable=self.campaign_repo, values=profiles.inventory(ROOT),
                     state="readonly", width=45).grid(row=2, column=1, sticky="w", pady=5)
        self._input_row(group, 3, "Clone local à mesurer (facultatif)", self.campaign_source,
                        browse=self._campaign_choose_clone, width=52)
        ttk.Checkbutton(group, text="Utiliser scc, Lizard et Universal Ctags si installés (analyse statique en lecture seule)",
                        variable=self.campaign_run_tools).grid(row=4, column=1, sticky="w", pady=4)
        controls = ttk.Frame(group)
        controls.grid(row=5, column=0, columnspan=3, sticky="w", pady=(10, 3))
        ttk.Button(controls, text="Joindre une preuve…", command=self._campaign_attach).pack(side="left", padx=(0, 8))
        ttk.Button(controls, text="Mesurer ce clone", command=self._campaign_measure_one).pack(side="left", padx=(0, 8))
        ttk.Button(controls, text="Mesurer clones de l'audit", command=self._campaign_measure_all).pack(side="left", padx=(0, 8))
        ttk.Button(controls, text="Annuler après le dépôt en cours", command=self._campaign_cancel_measure).pack(side="left", padx=(0, 8))
        controls2 = ttk.Frame(group)
        controls2.grid(row=6, column=0, columnspan=3, sticky="w", pady=(3, 10))
        ttk.Button(controls2, text="Trouver rapports de ce clone", command=self._campaign_discover_one).pack(side="left", padx=(0, 8))
        ttk.Button(controls2, text="Trouver rapports des clones de l'audit", command=self._campaign_discover_all).pack(side="left", padx=(0, 8))
        ttk.Button(controls2, text="Voir mesures enregistrées", command=self._campaign_open_collections).pack(side="left", padx=(0, 8))
        controls3 = ttk.Frame(group)
        controls3.grid(row=7, column=0, columnspan=3, sticky="w", pady=(3, 10))
        self.campaign_create_button = ttk.Button(controls3, text="Créer une campagne figée",
                                                 command=self._campaign_create, style="Primary.TButton")
        self.campaign_create_button.pack(side="left", padx=(0, 8))
        ttk.Button(controls3, text="Ouvrir le dossier des campagnes",
                   command=self._campaign_folder).pack(side="left")
        progress_row = ttk.Frame(tab)
        progress_row.grid(row=1, column=0, sticky="ew", pady=(5, 6))
        progress_row.columnconfigure(0, weight=1)
        self.campaign_progress = ttk.Progressbar(progress_row, mode="determinate",
                                                maximum=100, value=0,
                                                style="Calm.Horizontal.TProgressbar")
        self.campaign_progress.grid(row=0, column=0, sticky="ew")
        ttk.Label(progress_row, textvariable=self.campaign_progress_label,
                  style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=(3, 0))
        ttk.Label(tab, text="Les collectes utilisent Git en lecture seule et éventuellement scc/Lizard/Universal Ctags si tu les autorises. "
                  "Les recherches de rapports existants sont limitées à quelques emplacements connus; elles demandent ton accord avant toute copie. "
                  "Les rapports peuvent contenir des données sensibles et leur version Git n’est pas automatiquement vérifiée. "
                  "Les mesures créent un résumé privé, sans code source ni chemins de fichiers. "
                  "Aucun test, aucun script du dépôt et aucune action GitHub n'est exécuté. "
                  "Les liens Git et les preuves indépendantes ne constituent pas une certification.",
                  style="Muted.TLabel", wraplength=990, justify="left").grid(row=2, column=0, sticky="ew", pady=10)
        listing = ttk.LabelFrame(tab, text="Historique des campagnes (clic = détails · double-clic = navigateur)", padding=9)
        listing.grid(row=3, column=0, sticky="nsew")
        listing.columnconfigure(0, weight=1)
        listing.rowconfigure(0, weight=1)
        self.campaign_tree = ttk.Treeview(listing, columns=("name", "date", "count", "integrity"),
                                          show="headings", height=8, selectmode="browse")
        for key, caption, width in (("name", "Campagne", 370), ("date", "Date UTC", 190),
                                    ("count", "Dépôts", 85), ("integrity", "Intégrité", 130)):
            self.campaign_tree.heading(key, text=caption)
            self.campaign_tree.column(key, width=width, stretch=key == "name")
        self.campaign_tree.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(listing, orient="vertical", command=self.campaign_tree.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.campaign_tree.configure(yscrollcommand=scroll.set)
        self.campaign_tree.bind("<<TreeviewSelect>>", lambda _e: self._campaign_select())
        self.campaign_tree.bind("<Double-1>", lambda _e: self._campaign_open())
        bottom = ttk.Frame(tab)
        bottom.grid(row=4, column=0, sticky="ew", pady=(7, 0))
        ttk.Label(bottom, textvariable=self.campaign_detail, style="Muted.TLabel").pack(side="left", fill="x", expand=True)
        ttk.Button(bottom, text="Vérifier SHA-256", command=self._campaign_verify).pack(side="right", padx=4)
        ttk.Button(bottom, text="Voir la campagne", command=self._campaign_open).pack(side="right", padx=4)
        ttk.Button(bottom, text="Rafraîchir", command=self._campaign_refresh).pack(side="right", padx=4)
        self._campaign_refresh()

    def _campaign_folder(self) -> None:
        from koa_audit import campaigns
        folder=campaigns.root_path()
        folder.mkdir(parents=True, exist_ok=True)
        self._open_file(folder)

    def _campaign_open_collections(self) -> None:
        from koa_audit import campaigns
        folder=campaigns.root_path().parent/"evidence_runs"
        folder.mkdir(parents=True, exist_ok=True)
        self._open_file(folder)

    def _campaign_cancel_measure(self) -> None:
        if self.campaign_busy:
            self.campaign_collection_cancel.set()
            self.campaign_detail.set("Annulation demandée : arrêt après la mesure en cours (outil limité en temps).")

    def _campaign_choose_clone(self) -> None:
        chosen=filedialog.askdirectory(title="Sélectionner la copie locale exacte du dépôt",initialdir=self.local_root.get())
        if chosen:
            self.campaign_source.set(chosen)

    def _campaign_measure_one(self) -> None:
        folder=Path(self.campaign_source.get().strip())
        if not folder.is_dir():
            messagebox.showinfo("Choisir le clone", "Sélectionne d'abord un dossier Git local à mesurer.")
            return
        self._campaign_collect([(self.campaign_repo.get(),folder)])

    def _campaign_measure_all(self) -> None:
        from koa_audit import campaigns, profiles
        path=Path(self.campaign_audit.get().strip())
        if not path.is_file():
            messagebox.showinfo("Rapport local requis", "Choisis un audit.json existant contenant les emplacements des copies locales.")
            return
        try:
            paths=campaigns._source_lookup(campaigns._read_json(path))
        except (OSError,ValueError,TypeError) as error:
            messagebox.showerror("Rapport illisible",str(error)); return
        inventory=profiles.inventory(ROOT)
        selected=[(repo,paths[repo.casefold()]) for repo in inventory
                  if repo.casefold() in paths and paths[repo.casefold()].is_dir()]
        if not selected:
            messagebox.showinfo("Aucune copie accessible","Le rapport ne fournit aucun chemin Git local actuellement accessible.")
            return
        self._campaign_collect(selected)

    def _campaign_collect(self, selected: list[tuple[str,Path]]) -> None:
        if self.campaign_busy or self._running:
            messagebox.showinfo("Collecte occupée","Une autre opération est en cours."); return
        optional=self.campaign_run_tools.get()
        if not messagebox.askyesno("Mesure d'ingénierie locale",
                f"Mesurer {len(selected)} copie(s) avec Git"+(" + scc/Lizard/Universal Ctags (si installés)" if optional else "")+" ?\n\n"
                "Lecture seule : aucun test, aucun code du projet exécuté, aucun réseau. "
                "Les rapports privés seront joints à la prochaine campagne.\n"
                "Toute origine GitHub ne correspondant pas à l'inventaire sera ignorée."):
            return
        self.campaign_busy=True
        self.campaign_collection_cancel.clear()
        self.campaign_create_button.configure(state="disabled")
        self.campaign_progress.configure(maximum=len(selected), value=0)
        self.campaign_progress_label.set(f"Mesure : 0/{len(selected)} dépôts · 0 %")
        self.campaign_detail.set(f"Mesure en cours : {len(selected)} copie(s)…")
        def work():
            import uuid
            from koa_audit import evidence_collector, campaigns
            saved=[]; skipped=[]
            folder=campaigns.root_path().parent/"evidence_runs"
            for i,(repo,source) in enumerate(selected,1):
                if self.campaign_collection_cancel.is_set():
                    break
                try:
                    report=evidence_collector.collect(source,repo,static_tools=optional)
                    name=repo.split("/",1)[-1]
                    target=folder/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+"-"+name+"-"+uuid.uuid4().hex[:8]+".json")
                    saved.append((repo,evidence_collector.write_report(report,target)))
                except (OSError, ValueError, TypeError, KeyError) as error:
                    skipped.append(f"{repo} : {str(error)[:60]}")
                self._events.put(("campaign-measuring", i, len(selected), len(saved)))
            self._events.put(("campaign-measured",saved,skipped))
        threading.Thread(target=work,daemon=True,name="koa-static-collector").start()

    def _campaign_discover_one(self) -> None:
        folder = Path(self.campaign_source.get().strip())
        if not folder.is_dir():
            messagebox.showinfo("Choisir le clone", "Sélectionne d'abord un clone local.")
            return
        self._campaign_discover([(self.campaign_repo.get(), folder)])

    def _campaign_discover_all(self) -> None:
        from koa_audit import campaigns, profiles
        path = Path(self.campaign_audit.get().strip())
        if not path.is_file():
            messagebox.showinfo("Rapport local requis", "Choisis un audit.json avec chemins locaux existants.")
            return
        try:
            locations = campaigns._source_lookup(campaigns._read_json(path))
        except (OSError, ValueError, TypeError) as error:
            messagebox.showerror("Rapport illisible", str(error)); return
        selected = [(repo, locations[repo.casefold()]) for repo in profiles.inventory(ROOT)
                    if repo.casefold() in locations and locations[repo.casefold()].is_dir()]
        if not selected:
            messagebox.showinfo("Copies absentes", "Aucun clone de ce rapport n'est actuellement accessible.")
            return
        self._campaign_discover(selected)

    def _campaign_discover(self, selected: list[tuple[str, Path]]) -> None:
        if self.campaign_busy or self._running:
            messagebox.showinfo("Opération en cours", "Attends la fin de l'opération en cours."); return
        if not messagebox.askyesno("Découvrir les rapports existants",
                f"Examiner {len(selected)} clone(s) pour trouver uniquement JUnit, couverture et SARIF "
                "à des emplacements connus ?\n\n"
                "Les rapports ne seront ni exécutés, ni copiés avant ta confirmation. "
                "Une preuve existante n'est pas nécessairement celle du commit courant."):
            return
        self.campaign_busy = True
        self.campaign_collection_cancel.clear()
        self.campaign_create_button.configure(state="disabled")
        self.campaign_progress.configure(maximum=len(selected), value=0)
        self.campaign_progress_label.set(f"Recherche : 0/{len(selected)} dépôts · 0 %")
        self.campaign_detail.set("Recherche ciblée des rapports existants…")
        def work():
            from koa_audit import evidence_discovery
            found, skipped = [], []
            for done, (repo, folder) in enumerate(selected, 1):
                if self.campaign_collection_cancel.is_set():
                    break
                try:
                    found.extend(evidence_discovery.discover(folder, repo))
                except (OSError, ValueError, TypeError) as error:
                    skipped.append(f"{repo} : {str(error)[:65]}")
                self._events.put(("campaign-discovering", done, len(selected), len(found)))
            self._events.put(("campaign-discovered", found, skipped))
        threading.Thread(target=work, daemon=True, name="koa-evidence-discovery").start()

    def _campaign_attach(self) -> None:
        path = filedialog.askopenfilename(title="Choisir une preuve à figer dans la prochaine campagne",
                    filetypes=[("Rapport / preuve", "*.json *.xml *.sarif *.md *.txt *.pdf *.html"), ("Tous", "*.*")])
        if not path:
            return
        repo=self.campaign_repo.get()
        if not messagebox.askyesno("Inclure une preuve privée ?",
                "Ce fichier sera COPIÉ dans le ZIP privé de la prochaine campagne. Il peut contenir des informations sensibles.\n\n"
                f"Dépôt : {repo}\nFichier : {Path(path).name}\n\nConfirmer son inclusion ?"):
            return
        self.campaign_attached.setdefault(repo, []).append(Path(path))
        total=sum(map(len,self.campaign_attached.values()))
        self.campaign_detail.set(f"{total} preuve(s) ajoutée(s) pour la prochaine campagne (non publiées).")

    def _campaign_create(self) -> None:
        if self.campaign_busy or self._running:
            messagebox.showinfo("Opération en cours", "Termine d'abord l'opération actuelle.")
            return
        title=self.campaign_title.get().strip()
        raw=self.campaign_audit.get().strip()
        report=Path(raw).expanduser() if raw and Path(raw).expanduser().is_file() else None
        if raw and report is None:
            if not messagebox.askyesno("Rapport absent", "Le fichier audit.json indiqué est introuvable.\n\nCréer une campagne sans audit historique ?"):
                return
        attachment_count=sum(len(v) for v in self.campaign_attached.values())
        if not messagebox.askyesno("Geler une campagne",
                f"Créer une capture privée datée pour les 49 dépôts ?\n\n"
                f"Rapport historique : {'oui' if report else 'non'}\n"
                f"Pièces jointes explicites : {attachment_count}\n\n"
                "Les rapports joints ont une version Git non attestée sauf déclaration explicite du collecteur.\n"
                "Les certifications ne seront pas calculées automatiquement.\n"
                "Aucun dépôt Git ni GitHub ne sera modifié."):
            return
        self.campaign_busy = True
        self.campaign_create_button.configure(state="disabled")
        from koa_audit import profiles
        self.campaign_progress.configure(maximum=len(profiles.inventory(ROOT)) + 4, value=0)
        self.campaign_progress_label.set("Création : préparation des données…")
        self.campaign_detail.set("Création de la campagne (lecture seule)…")
        extras={k:list(v) for k,v in self.campaign_attached.items()}
        expected_hashes={p:d for p,d in self.campaign_expected_hashes.items()
                         if any(p in paths for paths in extras.values())}
        def work():
            try:
                from koa_audit import campaigns
                dest=campaigns.create_campaign(ROOT,title,report,extra_proofs=extras,
                    expected_proof_sha256=expected_hashes,
                    kristal_folder=Path(self.kristal_root.get().strip()).expanduser(),
                    progress=lambda done,total,caption: self._events.put(
                        ("campaign-progress",done,total,caption)))
                self._events.put(("campaign-created",str(dest)))
            except Exception as error:
                self._events.put(("campaign-failed",f"{type(error).__name__}: {str(error)[:250]}"))
        threading.Thread(target=work,daemon=True,name="koa-campaign-capture").start()

    def _campaign_refresh(self) -> None:
        from koa_audit import campaigns
        old=self._campaign_selected()
        self.campaign_tree.delete(*self.campaign_tree.get_children())
        for entry in campaigns.list_campaigns():
            self.campaign_tree.insert("", "end", iid=entry['id'], values=(entry['title'], entry['frozen_at'],
                                                  entry['repositories'],entry['integrity']))
        if old and self.campaign_tree.exists(old):
            self.campaign_tree.selection_set(old)
        self.campaign_detail.set(f"{len(self.campaign_tree.get_children())} campagne(s) locales")

    def _campaign_selected(self) -> str | None:
        selection=self.campaign_tree.selection()
        return selection[0] if selection else None

    def _campaign_select(self) -> None:
        key=self._campaign_selected()
        if not key:
            return
        self.campaign_detail.set("Campagne "+key+" · double-clic pour voir les preuves et versions GitHub")

    def _campaign_verify(self) -> None:
        from koa_audit import campaigns
        cid=self._campaign_selected()
        if cid is None:
            messagebox.showinfo("Campagne", "Sélectionne d'abord une campagne dans la liste.")
            return
        try:
            data=campaigns.read_campaign(cid)
            messagebox.showinfo("Intégrité vérifiée",f"Empreinte ZIP et preuves vérifiées.\n\n{data['title']}\n{data['frozen_at']}")
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            messagebox.showerror("Intégrité de la campagne",str(error))

    def _campaign_open(self) -> None:
        cid=self._campaign_selected()
        if cid is None:
            messagebox.showinfo("Campagnes", "Sélectionne d'abord une campagne.")
            return
        try:
            from koa_audit import campaigns
            campaigns.read_campaign(cid)
            server=self._ensure_preview_server()
            webbrowser.open(f"http://127.0.0.1:{server.server_port}/local/campaigns/{cid}")
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            messagebox.showerror("Campagne indisponible",str(error))

    def _build_certification_board(self, tab: ttk.Frame) -> None:
        from koa_audit import qualification
        ttk.Label(tab, text="Registre de qualification des 49 dépôts", style="Title.TLabel").pack(anchor="w")
        ttk.Label(tab, text="Spécifié ≠ implémenté ≠ qualifié ≠ intégré ≠ production. "
                  "Aucune case n'est cochée automatiquement, et un statut non évalué n'est pas un échec.",
                  style="Muted.TLabel", wraplength=900).pack(fill="x", pady=(4, 11))
        toolbar = ttk.Frame(tab)
        toolbar.pack(fill="x", pady=(0, 8))
        self.board_overview = StringVar(value="")
        ttk.Label(toolbar, textvariable=self.board_overview, style="Muted.TLabel").pack(side="left", fill="x", expand=True)
        ttk.Button(toolbar, text="Rafraîchir", command=self._refresh_certification_board).pack(side="right")
        ttk.Button(toolbar, text="Ouvrir la fiche sélectionnée", command=self._board_open_selected).pack(side="right", padx=(0, 10))
        frame = ttk.Frame(tab)
        frame.pack(fill="both", expand=True)
        cols = ("repo", "profile", "specified", "implemented", "qualified", "integrated", "production", "patterns", "improvements")
        self.board_tree = ttk.Treeview(frame, columns=cols, show="headings", selectmode="browse")
        headings = {"repo":"Dépôt", "profile":"Profil", "specified":"Spécifié", "implemented":"Implémenté",
                    "qualified":"Qualifié", "integrated":"Intégré", "production":"Production", "patterns":"Pratiques revues", "improvements":"Axes suivis"}
        for k in cols:
            self.board_tree.heading(k, text=headings[k])
            self.board_tree.column(k, width=255 if k == "repo" else 108 if k not in ("profile", "patterns") else 90,
                                   minwidth=70, stretch=(k == "repo"))
        self.board_tree.pack(side="left", fill="both", expand=True)
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.board_tree.yview)
        scroll.pack(side="right", fill="y")
        self.board_tree.configure(yscrollcommand=scroll.set)
        self.board_tree.bind("<Double-1>", lambda _e: self._board_open_selected())
        ttk.Label(tab, text="Une qualification n'est déclarée que si une preuve et sa portée ont été enregistrées. "
                  "Les 86 pratiques ne sont pas des obligations universelles : Pas applicable est neutre.",
                  style="Muted.TLabel", wraplength=950).pack(anchor="w", pady=(9, 0))
        self._refresh_certification_board()

    def _refresh_certification_board(self) -> None:
        from koa_audit import qualification
        entries = qualification.ecosystem_board(ROOT)
        self.board_tree.delete(*self.board_tree.get_children())
        evidenced = 0
        profiles_count = 0
        reviewed = 0
        for entry in entries:
            stages = entry["stages"]
            has_evidence = any(s == "Étayé par preuve" for s in stages.values())
            if has_evidence:
                evidenced += 1
            if entry["engineering_profile"]:
                profiles_count += 1
            counts = entry["practice_counts"]
            cnt_reviewed = sum(v for k, v in counts.items() if k != "Non évalué")
            reviewed += cnt_reviewed
            label = entry["repository"].split("/", 1)[-1]
            self.board_tree.insert("", "end", iid=entry["repository"], values=(
                label, "Mesuré" if entry["engineering_profile"] else "Non fourni",
                *(stages[k] for k in qualification.STAGE_IDS), f"{cnt_reviewed}/86",
                counts["À améliorer"] if cnt_reviewed else "—",
            ))
        self.board_overview.set(
            f"{len(entries)} dépôts · {profiles_count} profils mesurés · "
            f"{evidenced} dépôts avec ≥1 jalon étayé · {reviewed} pratiques évaluées manuellement")

    def _board_open_selected(self) -> None:
        selected = self.board_tree.selection()
        if not selected:
            messagebox.showinfo("Registre", "Choisis un dépôt dans le tableau.")
            return
        self.profile_repo.set(selected[0])
        self._profiles_refresh()
        for index in range(self.tabs.index("end")):
            if "Certification" in self.tabs.tab(index, "text"):
                self.tabs.select(index)
                break

    def _build_evidence_review(self, tab: ttk.Frame) -> None:
        """Review 245 sourced historical cases; NEVER turn suggestions into claims."""
        from koa_audit import evidence_review
        ttk.Label(tab, text="Revue des preuves historiques · 245 dossiers", style="Title.TLabel").pack(anchor="w")
        ttk.Label(tab, text="49 dépôts × 5 jalons. Les sources historiques sont consultables; aucune qualification n'est validée automatiquement.",
                  style="Muted.TLabel", wraplength=980).pack(anchor="w", pady=(2, 6))
        ttk.Label(tab, textvariable=self.review_summary, style="Muted.TLabel", wraplength=960).pack(fill="x", pady=(0, 6))
        toolbar=ttk.Frame(tab)
        toolbar.pack(fill="x", pady=(0, 8))
        ttk.Label(toolbar, text="Recherche").pack(side="left", padx=(0, 7))
        inp=ttk.Entry(toolbar, textvariable=self.review_search, width=27)
        inp.pack(side="left", padx=(0, 11))
        inp.bind('<KeyRelease>', lambda _e: self._review_filter())
        ttk.Button(toolbar, text="Ouvrir la revue dans le navigateur", command=self._review_open_browser).pack(side="left", padx=(0, 8))
        ttk.Button(toolbar, text="Relire les données", command=self._review_reload).pack(side="left")
        main=ttk.Panedwindow(tab, orient="horizontal")
        main.pack(fill="both", expand=True)
        left=ttk.Frame(main)
        right=ttk.Frame(main)
        main.add(left, weight=1)
        main.add(right, weight=3)
        ttk.Label(left, text="Applications").pack(anchor="w")
        self.review_repos=ttk.Treeview(left, columns=("name", "sources"), show="headings", selectmode="browse", height=14)
        self.review_repos.heading('name', text='Dépôt')
        self.review_repos.heading('sources', text='Jalons cités')
        self.review_repos.column('name', width=185)
        self.review_repos.column('sources', width=125, anchor='center')
        self.review_repos.pack(fill="both", expand=True)
        self.review_repos.bind('<<TreeviewSelect>>', lambda _e: self._review_repo_select())
        ttk.Label(right, text="Cinq jalons indépendants · sélectionner pour voir les preuves").pack(anchor="w")
        self.review_stages=ttk.Treeview(right, columns=('stage','level','sources'),show='headings',height=5,selectmode='browse')
        for col,title,width in [('stage','Jalon',150),('level','Type de constat historique',360),('sources','Références',75)]:
            self.review_stages.heading(col,text=('Conclusion' if col=='level' else title))
            self.review_stages.column(col,width=width,minwidth=55,stretch=(col=='level'))
        self.review_stages.pack(fill='x',pady=(5,8))
        self.review_stages.bind('<<TreeviewSelect>>',lambda _e:self._review_stage_select())
        buttons=ttk.Frame(right)
        buttons.pack(fill='x',pady=(3,8))
        ttk.Button(buttons,text="Voir ce jalon et ses sources",command=self._review_open_stage).pack(side='left',padx=(0,8))
        ttk.Button(buttons,text="Ouvrir la source sélectionnée",command=self._review_open_source).pack(side='left',padx=(0,8))
        ttk.Button(buttons,text="Voir / ajuster la qualification",style='Primary.TButton',
                   command=self._review_prepare).pack(side='left')
        self.review_details=ScrolledText(right,height=6,wrap='word',font=('Segoe UI',10),background='white',foreground=NAVY)
        self.review_details.pack(fill='both',expand=True)
        self.review_details.configure(state='disabled')
        ttk.Label(right, text="Documents historiques (double-cliquer pour consulter la source originale)",
                  style='Muted.TLabel').pack(anchor='w',pady=(8,3))
        self.review_sources=ttk.Treeview(right,columns=('source','availability'),show='headings',height=3,selectmode='browse')
        self.review_sources.heading('source',text='Référence / document')
        self.review_sources.heading('availability',text='Consultation')
        self.review_sources.column('source',width=540)
        self.review_sources.column('availability',width=130,stretch=False)
        self.review_sources.pack(fill='x')
        self.review_sources.bind('<Double-1>',lambda _e:self._review_open_source())
        self._review_reload()

    def _review_reload(self) -> None:
        from koa_audit import evidence_review
        try:
            self.review_data=evidence_review.load_review(ROOT)
            evidence_review.preserve_review_locally(ROOT)
            from koa_audit import evidence_adjudication
            counts=evidence_review.report_counts(ROOT)
            qualification_summary=evidence_adjudication.current_summary(ROOT)
            self.review_summary.set(f"{counts['repositories']} dépôts · {counts['cases']} dossiers · "
                f"Revue inscrite sur ce PC : {qualification_summary['evidenced']}/245 jalons étayés (portée spécifique), "
                f"{qualification_summary['to_document']} à documenter. Pièces privées, aucune production attestée.")
            self._review_filter()
        except (OSError, ValueError, zipfile.BadZipFile, KeyError) as error:
            self.review_data=None
            self.review_summary.set("Archive de revue privée indisponible ou invalide : "+str(error))

    def _review_filter(self) -> None:
        if not self.review_data:
            return
        search=self.review_search.get().casefold().strip()
        selected=self.review_repo.get()
        self.review_repos.delete(*self.review_repos.get_children())
        for item in self.review_data['repositories']:
            if search not in item['repository'].casefold():
                continue
            name=item['repository']
            self.review_repos.insert('', 'end', iid=name,values=(name.split('/')[-1],
                str(sum(bool(s.get('sources')) for s in item['stages']))+'/5'))
        if selected in self.review_repos.get_children():
            self.review_repos.selection_set(selected)
        elif self.review_repos.get_children():
            self.review_repos.selection_set(self.review_repos.get_children()[0])
        self._review_repo_select()

    def _review_repo_select(self) -> None:
        from koa_audit import qualification
        if not self.review_data:
            return
        selected=self.review_repos.selection()
        if not selected:
            return
        self.review_repo.set(selected[0])
        record=next(x for x in self.review_data['repositories'] if x['repository']==selected[0])
        self.review_stages.delete(*self.review_stages.get_children())
        for s in record['stages']:
            self.review_stages.insert('', 'end', iid=s['stage'],values=(s['title'],
                qualification.get_claim(ROOT,record['repository'],s['stage'])['status'],
                len(s['sources'])))
        self.review_stages.selection_set('specified')
        self._review_stage_select()

    def _review_stage_select(self) -> None:
        if not self.review_data or not self.review_stages.selection():
            return
        from koa_audit import evidence_review, qualification
        stage=self.review_stages.selection()[0]
        record=next(x for x in self.review_data['repositories'] if x['repository']==self.review_repo.get())
        s=next(x for x in record['stages'] if x['stage']==stage)
        claim=qualification.get_claim(ROOT,self.review_repo.get(),stage)
        detail=(f"Type de constat : {s['evidence_level']}\n"
                f"Conclusion enregistrée (revue documentaire ou décision locale) : {claim['status']}\n\n"
                f"Observation : {s['summary']}\n\n"
                f"Portée : {s['scope']}\n\n"
                f"Limites : {s['limitations']}\n\n"
                f"Prochaine étape : {s['next_action']}\n\n"
                "Une présence de code ou de CI n'est pas un résultat de qualification automatique.")
        self.review_details.configure(state='normal')
        self.review_details.delete('1.0', END)
        self.review_details.insert('1.0',detail)
        self.review_details.configure(state='disabled')
        self.review_sources.delete(*self.review_sources.get_children())
        from koa_audit import evidence_adjudication
        adjudication=evidence_adjudication.decision(ROOT,self.review_repo.get(),stage)
        primary=(adjudication.get('source') or {}).get('member')
        primary_seen=False
        for i,source in enumerate(s['sources']):
            ref=evidence_review.source_reference(ROOT,self.review_repo.get(),stage,i)
            if source == primary:
                primary_seen=True
            availability=('Pièce vérifiée SHA' if source==primary else
                          ('Consultable' if ref['available'] else 'Réf. extérieure'))
            self.review_sources.insert('','end',iid=str(i),values=(source,availability))
        if primary and not primary_seen:
            self.review_sources.insert('','end',iid='expert',values=(primary,'Pièce vérifiée SHA'))

    def _review_url(self, url: str) -> None:
        try:
            server=self._ensure_preview_server()
            webbrowser.open(f"http://127.0.0.1:{server.server_port}{url}")
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            messagebox.showerror('Revue historique',str(error))

    def _review_open_browser(self) -> None:
        self._review_url('/local/review')

    def _review_open_stage(self) -> None:
        if self.review_stages.selection():
            self._review_url('/local/review/app/'+quote(self.review_repo.get().split('/')[-1])+'/'+self.review_stages.selection()[0])

    def _review_open_source(self) -> None:
        if not self.review_sources.selection() or not self.review_stages.selection():
            return
        from koa_audit import evidence_review
        stage=self.review_stages.selection()[0]
        if self.review_sources.selection()[0]=='expert':
            self._review_url('/local/review/app/'+quote(self.review_repo.get().split('/')[-1])+'/'+stage+'/expert')
            return
        index=int(self.review_sources.selection()[0])
        ref=evidence_review.source_reference(ROOT,self.review_repo.get(),stage,index)
        if not ref['available']:
            messagebox.showinfo('Source historique non jointe',
                "Cette référence est citée dans le diagnostic mais le document n'était pas inclus dans l'archive. "
                "Aucune pièce n'a été inventée.")
            return
        self._review_url('/local/review/app/'+quote(self.review_repo.get().split('/')[-1])+'/'+stage+'/source/'+str(index))

    def _review_prepare(self) -> None:
        """Open the already-reviewed conclusion without resetting its status."""
        if not self.review_stages.selection():
            return
        from koa_audit import evidence_review, qualification
        stage=self.review_stages.selection()[0]
        try:
            suggestion=evidence_review.suggested_qualification(ROOT,self.review_repo.get(),stage)
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            messagebox.showerror('Revue documentaire',str(error)); return
        self.profile_repo.set(suggestion['repository'])
        self.qual_stage.set(next(title for key,title in qualification.STAGES if key==stage))
        self._profiles_refresh()
        current=qualification.get_claim(ROOT,self.review_repo.get(),stage)
        if current['status']=='Non évalué':
            self.qual_scope.set(suggestion['scope'])
            self.qual_evidence.set(suggestion['evidence'])
        else:
            self.qual_scope.set(current['scope'])
            self.qual_evidence.set(current['evidence'])
            self.qual_status.set(current['status'])
        for index in range(self.tabs.index('end')):
            if 'Certification' in self.tabs.tab(index,'text'):
                self.tabs.select(index)
                break
        self.status.set('Qualification documentaire affichée. Modifier seulement si une nouvelle preuve le justifie.')

    def _build_profiles(self, tab: ttk.Frame) -> None:
        """Read standardized files and let the user review architecture/security patterns."""
        from koa_audit import profiles
        inventory = profiles.profile_repositories(ROOT)
        top = ttk.Frame(tab)
        top.pack(fill="x", pady=(0, 9))
        ttk.Label(top, text="Dépôt", style="TLabel").pack(side="left", padx=(0, 8))
        repo_box = ttk.Combobox(top, textvariable=self.profile_repo, state="readonly",
                                values=inventory, width=39)
        repo_box.pack(side="left", padx=(0, 12))
        repo_box.bind("<<ComboboxSelected>>", lambda _e: self._profiles_refresh())
        ttk.Label(top, text="Famille").pack(side="left", padx=(0, 7))
        family_box = ttk.Combobox(top, textvariable=self.profile_family, state="readonly",
                                  values=["Tous", "Architecture", "Sécurité"], width=15)
        family_box.pack(side="left", padx=(0, 10))
        family_box.bind("<<ComboboxSelected>>", lambda _e: self._profiles_refresh())
        ttk.Button(top, text="Rafraîchir", command=self._profiles_refresh).pack(side="left")

        # Independent, evidence-scoped ecosystem qualification milestones.
        # An engineering profile, scan observation or filename can never mark a claim.
        from koa_audit import qualification
        qual = ttk.LabelFrame(tab, text="Qualification par preuve — aucune certification automatique",
                              style="Card.TLabelframe", padding=(9, 5))
        qual.pack(fill="x", pady=(0, 8))
        qr = ttk.Frame(qual)
        qr.pack(fill="x")
        ttk.Label(qr, text="Jalon").pack(side="left", padx=(0, 6))
        self.qual_stage_box = ttk.Combobox(qr, textvariable=self.qual_stage,
            state="readonly", width=29, values=[x[1] for x in qualification.STAGES])
        self.qual_stage_box.pack(side="left", padx=(0, 12))
        self.qual_stage_box.bind("<<ComboboxSelected>>", lambda _e: self._qual_refresh())
        ttk.Label(qr, text="État").pack(side="left", padx=(0, 6))
        ttk.Combobox(qr, textvariable=self.qual_status, state="readonly", width=19,
                     values=qualification.STATES).pack(side="left", padx=(0, 12))
        ttk.Button(qr, text="Enregistrer le jalon", command=self._qual_save).pack(side="left")
        qe = ttk.Frame(qual)
        qe.pack(fill="x", pady=(5, 0))
        ttk.Label(qe, text="Portée").pack(side="left", padx=(0, 5))
        ttk.Entry(qe, textvariable=self.qual_scope, width=31).pack(side="left", fill="x", expand=True, padx=(0, 10))
        ttk.Label(qe, text="Preuve / référence").pack(side="left", padx=(0, 5))
        ttk.Entry(qe, textvariable=self.qual_evidence, width=43).pack(side="left", fill="x", expand=True)
        ttk.Label(qual, textvariable=self.qual_overview, style="Muted.TLabel").pack(fill="x", pady=(3, 0))
        ttk.Label(qual, text="Une preuve peut qualifier une portée donnée (ex. test local) sans prouver une intégration ni une production.",
                  style="Muted.TLabel").pack(fill="x")

        ttk.Label(tab, textvariable=self.profile_overview, style="Muted.TLabel").pack(fill="x", pady=(0, 7))
        ttk.Label(tab, textvariable=self.profile_audit_context, style="Muted.TLabel").pack(fill="x", pady=(0, 8))
        panes = ttk.Panedwindow(tab, orient="horizontal")
        panes.pack(fill="both", expand=True)
        left = ttk.Frame(panes)
        right = ttk.Frame(panes)
        panes.add(left, weight=3)
        panes.add(right, weight=2)
        tree_area = ttk.Frame(left)
        tree_area.pack(fill="both", expand=True)
        self.profile_tree = ttk.Treeview(tree_area, columns=("pattern", "state"),
                                          show="headings", selectmode="browse")
        self.profile_tree.heading("pattern", text="Pratique (source fournie)")
        self.profile_tree.heading("state", text="Statut")
        self.profile_tree.column("pattern", width=370, minwidth=230, stretch=True)
        self.profile_tree.column("state", width=122, minwidth=100, stretch=False)
        self.profile_tree.pack(side="left", fill="both", expand=True)
        scroll = ttk.Scrollbar(tree_area, orient="vertical", command=self.profile_tree.yview)
        scroll.pack(side="right", fill="y")
        self.profile_tree.configure(yscrollcommand=scroll.set)
        self.profile_tree.bind("<<TreeviewSelect>>", self._profile_selected)
        ttk.Label(left, text="Sélectionne une pratique, puis son statut. Aucun statut n'est attribué automatiquement.",
                  style="Muted.TLabel", wraplength=480).pack(anchor="w", pady=7)
        chooser = ttk.Frame(left)
        chooser.pack(fill="x", pady=(3, 2))
        ttk.Label(chooser, text="Statut").pack(side="left", padx=(0, 6))
        self.profile_status_box = ttk.Combobox(chooser, textvariable=self.profile_status,
                            values=profiles.STATUSES, state="readonly", width=18)
        self.profile_status_box.pack(side="left")
        ttk.Button(chooser, text="Enregistrer", command=self._profile_save,
                   style="Primary.TButton").pack(side="left", padx=(12, 0))
        ttk.Label(left, text="Justification / preuve (facultatif, conservé sur ce PC)",
                  style="Muted.TLabel").pack(anchor="w", pady=(8, 2))
        ttk.Entry(left, textvariable=self.profile_note).pack(fill="x")

        ttk.Label(right, text="Profil standardisé", style="Card.TLabelframe.Label").pack(anchor="w")
        choose = ttk.Frame(right)
        choose.pack(fill="x", pady=7)
        kind = ttk.Combobox(choose, textvariable=self.profile_kind, state="readonly",
                            values=profiles.PROFILE_NAMES, width=28)
        kind.pack(side="left", padx=(0, 8))
        kind.bind("<<ComboboxSelected>>", lambda _e: self._profile_show_document())
        ttk.Button(choose, text="Importer .md", command=self._profile_import).pack(side="left")
        doc_tabs = ttk.Notebook(right)
        doc_tabs.pack(fill="both", expand=True)
        doc_page = ttk.Frame(doc_tabs)
        practice_page = ttk.Frame(doc_tabs)
        doc_tabs.add(doc_page, text="Rapport du dépôt")
        doc_tabs.add(practice_page, text="Fiche de pratique")
        self.profile_preview = ScrolledText(doc_page, height=23, wrap="word", font=("Consolas", 9),
                                             background="#ffffff", foreground="#223d3b")
        self.profile_preview.pack(fill="both", expand=True)
        self.profile_preview.configure(state="disabled")
        self.pattern_preview = ScrolledText(practice_page, height=23, wrap="word", font=("Consolas", 9),
                                             background="#ffffff", foreground="#223d3b")
        self.pattern_preview.pack(fill="both", expand=True)
        self.pattern_preview.configure(state="disabled")
        self.profile_doc_tabs = doc_tabs
        ttk.Button(right, text="Ouvrir le dossier de ce dépôt",
                   command=self._profile_open_folder).pack(anchor="w", pady=(8, 0))
        ttk.Label(right, text="Les documents restent dans profiles/repositories/ et ne sont pas envoyés au dashboard public.",
                  style="Muted.TLabel", wraplength=410).pack(anchor="w", pady=(6, 0))
        self._profiles_refresh()

    def _qual_refresh(self) -> None:
        from koa_audit import qualification
        stage = next(k for k, title in qualification.STAGES if title == self.qual_stage.get())
        data = qualification.get_claim(ROOT, self.profile_repo.get(), stage)
        self.qual_status.set(data["status"])
        self.qual_scope.set(data["scope"])
        self.qual_evidence.set(data["evidence"])
        counts = qualification.progress(ROOT, self.profile_repo.get())
        self.qual_overview.set(
            f"Jalons examinés : {counts['assessed']}/{counts['total']}  ·  "
            f"Jalons étayés par preuve : {counts['evidenced']}  ·  "
            "Aucun score global ni verdict automatique")

    def _qual_save(self) -> None:
        from koa_audit import qualification
        stage = next(k for k, title in qualification.STAGES if title == self.qual_stage.get())
        if self.qual_status.get() == 'Étayé par preuve':
            if not messagebox.askyesno('Valider explicitement la preuve',
                'As-tu consulté la pièce originale, confirmé sa portée ET vérifié que la version et le périmètre '
                'justifient ce jalon ?\n\nCette décision est manuelle et sera figée dans la PROCHAINE campagne. '
                'Les rapports anciens et les CI ne prouvent pas la production.'):
                return
        try:
            qualification.set_claim(ROOT, self.profile_repo.get(), stage,
                self.qual_status.get(), self.qual_evidence.get(), self.qual_scope.get())
        except (OSError, ValueError, TypeError) as error:
            messagebox.showerror("Qualification", str(error))
            return
        self._qual_refresh()
        self._refresh_certification_board()
        if self.review_data:
            self._review_repo_select()
        self.status.set("Jalon enregistré sur ce PC, sans modification Git ni publication")

    def _profiles_refresh(self) -> None:
        from koa_audit import profiles
        repo = self.profile_repo.get()
        progress = profiles.progress(ROOT, repo)
        self._qual_refresh()
        self.profile_overview.set(
            f"{repo}  |  Pratiques : {progress['reviewed']}/{progress['total']} examinées  |  "
            f"Appliqué : {progress['Appliqué']}  |  À améliorer : {progress['À améliorer']}  |  "
            f"Non applicable : {progress['Pas applicable']}")
        report = Path(self.dashboard_local.get()).expanduser()
        try:
            ctx = profiles.audit_context(ROOT, repo, report)
            if ctx:
                self.profile_audit_context.set(
                    f"Données techniques (non qualificatives) : "
                    f"{ctx['files_inspected']}/{ctx['files_enumerated']} fichiers inspectés · "
                    f"{ctx['findings']} motifs de scan à requalifier · commit {ctx['head']}")
            else:
                self.profile_audit_context.set("Aucun rapport d'audit local associé à ce dépôt (sélectionner audit.json dans Tableau de bord).")
        except (ValueError, OSError, TypeError):
            self.profile_audit_context.set("Rapport d'audit local non disponible ou invalide.")
        self.profile_current_id = None
        self.profile_note.set("")
        self.profile_status.set("Non évalué")
        self.profile_tree.delete(*self.profile_tree.get_children())
        self.profile_catalog_items = {p['id']:p for p in profiles.catalog(ROOT)}
        for item in self.profile_catalog_items.values():
            if self.profile_family.get() == "Architecture" and item["family"] != "architecture":
                continue
            if self.profile_family.get() == "Sécurité" and item["family"] != "security":
                continue
            status = profiles.get_assessment(ROOT, repo, item['id'])["status"]
            self.profile_tree.insert("", "end", iid=item["id"], values=(item['id']+" · "+item['title'],status))
        self._profile_show_document()
        self._profile_show_pattern()

    def _profile_selected(self, _event=None) -> None:
        from koa_audit import profiles
        ids = self.profile_tree.selection()
        if not ids:
            return
        self.profile_current_id = ids[0]
        data = profiles.get_assessment(ROOT, self.profile_repo.get(), self.profile_current_id)
        self.profile_status.set(data["status"])
        self.profile_note.set(data["note"])
        self._profile_show_pattern()

    def _profile_show_pattern(self) -> None:
        from koa_audit import profiles
        if self.profile_current_id:
            try:
                content=profiles.get_pattern_text(ROOT,self.profile_current_id)
            except (OSError,ValueError,UnicodeError) as error:
                content=str(error)
        else:
            content="Sélectionne une pratique à gauche pour lire sa fiche source complète."
        self.pattern_preview.configure(state="normal")
        self.pattern_preview.delete("1.0",END)
        self.pattern_preview.insert("1.0",content)
        self.pattern_preview.configure(state="disabled")

    def _profile_save(self) -> None:
        from koa_audit import profiles
        if not self.profile_current_id:
            messagebox.showinfo("Pratique", "Sélectionne une pratique dans la liste.")
            return
        try:
            dest = profiles.set_assessment(ROOT, self.profile_repo.get(),self.profile_current_id,
                                           self.profile_status.get(),self.profile_note.get())
        except (OSError,ValueError,TypeError) as error:
            messagebox.showerror("Enregistrement impossible", str(error))
            return
        self.profile_tree.set(self.profile_current_id, "state", self.profile_status.get())
        progress = profiles.progress(ROOT, self.profile_repo.get())
        self.profile_overview.set(
            f"{self.profile_repo.get()}  |  Pratiques : {progress['reviewed']}/{progress['total']} examinées  |  "
            f"Appliqué : {progress['Appliqué']}  |  À améliorer : {progress['À améliorer']}  |  "
            f"Non applicable : {progress['Pas applicable']}")
        self._refresh_certification_board()
        self.status.set(f"Évaluation enregistrée localement : {self.profile_current_id} (aucun Git push)")

    def _profile_show_document(self) -> None:
        from koa_audit import profiles
        try:
            text = profiles.get_profile(ROOT, self.profile_repo.get(), self.profile_kind.get())
            if text is None:
                text = "Aucun profil fourni pour ce dépôt.\n\nUtilise « Importer .md » lorsque le rapport standardisé sera prêt.\nAucun résultat n'est inventé."
        except (OSError, ValueError) as error:
            text = str(error)
        self.profile_preview.configure(state="normal")
        self.profile_preview.delete("1.0", END)
        self.profile_preview.insert("1.0", text)
        self.profile_preview.configure(state="disabled")

    def _profile_import(self) -> None:
        from koa_audit import profiles
        src = filedialog.askopenfilename(title="Importer un profil Markdown",
                                         filetypes=[("Markdown", "*.md"), ("Tous", "*.*")])
        if not src:
            return
        dest = profiles.profile_directory(ROOT,self.profile_repo.get()) / self.profile_kind.get()
        if dest.exists() and not messagebox.askyesno("Remplacer le profil ?",
                    f"Le profil existe déjà pour ce dépôt.\n\nRemplacer {dest.name} ?"):
            return
        try:
            profiles.install_profile(ROOT,self.profile_repo.get(),self.profile_kind.get(),Path(src))
            self._profile_show_document()
            self.status.set("Profil importé localement dans le dossier profiles/.")
        except (OSError, ValueError, UnicodeError) as error:
            messagebox.showerror("Import impossible",str(error))

    def _profile_open_folder(self) -> None:
        from koa_audit import profiles
        folder=profiles.profile_directory(ROOT,self.profile_repo.get())
        folder.mkdir(parents=True,exist_ok=True)
        self._open_file(folder)

    def _browse_local_root(self) -> None:
        folder = filedialog.askdirectory(title="Choisir la racine des dépôts locaux", initialdir=self.local_root.get())
        if folder: self.local_root.set(folder)

    def _choose_json(self, variable: StringVar) -> None:
        path=filedialog.askopenfilename(title="Choisir audit.json", filetypes=[("JSON", "*.json"), ("Tous", "*.*")])
        if path: variable.set(path)

    def _browse_triage_json(self) -> None:
        self._choose_json(self.triage_input)

    def _browse_remote_report_folder(self) -> None:
        folder=filedialog.askdirectory(title="Dossier des rapports d’observation GitHub", initialdir=str(ROOT))
        if folder: self.remote_out_dir.set(folder)

    def _local_flags(self) -> list[str]:
        root = Path(self.local_root.get()).expanduser()
        if not root.is_dir(): raise ValueError("Dossier local introuvable")
        depth = int(self.local_depth.get())
        limit = int(self.local_limit.get())
        if not 0 <= depth <= 10 or limit < 0: raise ValueError("Profondeur ou limite invalide")
        return ["--root", str(root), "--max-depth", str(depth), "--limit", str(limit)]

    def _run_local_plan(self) -> None:
        try: args=["-m", "koa_audit", "local-plan", *self._local_flags()]
        except ValueError as error:
            messagebox.showerror("Options invalides", str(error));return
        self._start(args, "Découverte locale")

    def _run_local_audit(self) -> None:
        try:
            args=["-m", "koa_audit", "local-audit", *self._local_flags(),
                  "--out", self.out_dir.get()]
        except ValueError as error:
            messagebox.showerror("Options invalides", str(error));return
        self._start(args, "Audit local")

    def _run_triage(self) -> None:
        try:
            source=Path(self.triage_input.get())
            root=Path(self.local_root.get())
            if not source.is_file() or not root.is_dir(): raise ValueError("Vérifier le rapport JSON et le dossier local")
            out=ROOT / "reports" / "triage" / ("kOA-triage-"+datetime.now().strftime("%Y%m%d-%H%M%S-%f")+".zip")
            args=["-m", "koa_audit", "local-triage", "--root", str(root),
                  "--audit-json", str(source), "--out", str(out)]
        except ValueError as error:
            messagebox.showerror("Options invalides", str(error));return
        self._start(args, "Vérification + ZIP")

    def _run_dashboard(self) -> None:
        sources=[Path(v.get()).expanduser() for v in (self.dashboard_local, self.dashboard_github) if v.get().strip()]
        if not sources or not all(src.is_file() for src in sources):
            messagebox.showerror("Rapports manquants", "Sélectionner un audit.json existant; le rapport GitHub est facultatif.")
            return
        args=["-m", "koa_audit", "dashboard-publish", "--out", str(ROOT / "docs")]
        for source in sources: args += ["--audit-json", str(source)]
        self._start(args, "Tableau de bord")

    def _sync_dashboard(self) -> None:
        if not messagebox.askyesno("Publier le bilan kOA",
                                  "Envoyer uniquement les statistiques agrégées sur le dépôt d'audit GitHub ?\n\n"
                                  "Aucun audit ne sera relancé. Aucun fichier .env ni code source ne sera envoyé."):
            return
        sources = []
        for variable in (self.dashboard_local, self.dashboard_github):
            name = variable.get().strip()
            if name and Path(name).expanduser().is_file():
                sources.extend(["--audit-json", str(Path(name).expanduser())])
        self._start(["-m", "koa_audit", "dashboard-sync", *sources], "Publication du tableau de bord")

    def _browse_kristal_root(self) -> None:
        selected = filedialog.askdirectory(title="Choisir Kristal-kOA-Ecosystem",
                                           initialdir=self.kristal_root.get() if Path(self.kristal_root.get()).is_dir() else str(Path.home()))
        if selected:
            self.kristal_root.set(selected)
            self._check_kristal_root()

    def _check_kristal_root(self) -> bool:
        from koa_audit import kristal_source, profiles
        folder = Path(self.kristal_root.get().strip()).expanduser()
        try:
            view = kristal_source.build_local_kristal_view(folder, profiles.inventory(ROOT))
            kristal_source.save_source_root(folder)
            if self._preview_server is not None:
                self._preview_server.kristal_source = folder
            self.kristal_status.set(f"Kristal chargé : {view['matched']}/49 dépôts · {view['explicit_repositories']} liens explicites · {view['candidate_repositories']} propositions · {view['unlinked_repositories']} sans suggestion")
            return True
        except (OSError, ValueError, TypeError, KeyError) as error:
            self.kristal_status.set("Source Kristal indisponible : vérifie le dossier sélectionné")
            messagebox.showwarning("Référentiel Kristal", "Les catalogues canoniques ne sont pas accessibles.\n\n"
                                   "Choisis le dossier contenant knowledge-base/sources/.\n"
                                   "Tu peux tout de même consulter la carte intégrée.")
            return False

    def _ensure_preview_server(self) -> http.server.ThreadingHTTPServer:
        dashboard_dir = ROOT / "docs"
        if not (dashboard_dir / "index.html").is_file():
            raise FileNotFoundError("Tableau de bord absent : décompresser le ZIP complet.")
        if self._preview_server is None:
            handler = functools.partial(_NoConsolePreviewHandler, directory=str(dashboard_dir))
            server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
            server.daemon_threads = True
            threading.Thread(target=server.serve_forever, daemon=True,
                             name="koa-dashboard-preview").start()
            self._preview_server = server
        self._preview_server.kristal_source = Path(self.kristal_root.get().strip()).expanduser()
        return self._preview_server

    def _preview_dashboard(self) -> None:
        try:
            # Rebuild only allowlisted public data, not local campaign evidence.
            from koa_audit.ecosystem import build_public_atlas
            build_public_atlas(ROOT, ROOT / "docs")
            server = self._ensure_preview_server()
            webbrowser.open(f"http://127.0.0.1:{server.server_port}/")
        except (OSError, RuntimeError) as error:
            diagnostic_log(error)
            messagebox.showerror("Aperçu indisponible", str(error))

    def _build_legacy(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        panel = ttk.LabelFrame(tab, text="Importer un verdict historique (métadonnées seulement)",
                               style="Card.TLabelframe", padding=14)
        panel.grid(row=0, column=0, sticky="ew")
        panel.columnconfigure(1, weight=1)
        ttk.Label(panel, text="Famille de diagnostic").grid(row=0, column=0, sticky="w", pady=7)
        ttk.Combobox(panel, textvariable=self.tool, values=sorted(SCHEMAS),
                     state="readonly").grid(row=0, column=1, sticky="ew", pady=7)
        self._input_row(panel, 1, "Dépôt cible (owner/repo)", self.target_repo, width=45)
        self._input_row(panel, 2, "Fichier JSON / ZIP", self.source_file, browse=self._browse_source, width=45)
        self._input_row(panel, 3, "Membre ZIP exact (ZIP seulement)", self.zip_member, width=45)
        self._input_row(panel, 4, "Dossier des imports normalisés", self.legacy_out,
                        browse=self._browse_import_folder, width=45)
        self._action_button(panel, "Importer les métadonnées", self._run_import, primary=True).grid(
            row=5, column=1, sticky="w", pady=14)
        ttk.Label(tab, text=(
            "Le dépôt cible doit être explicitement indiqué. Aucun rapport historique n'est assimilé "
            "à une preuve actuelle de sécurité. Pour un JSON, laisser « Membre ZIP » vide."
        ), wraplength=780, justify="left", style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=15)
        ttk.Label(tab, text=(
            "Après l'import, revenir à « Audit GitHub » et cocher « Inclure les diagnostics historiques normalisés »."
        ), style="Muted.TLabel", wraplength=780).grid(row=2, column=0, sticky="w")

    def _build_reports(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        buttons = ttk.Frame(tab)
        buttons.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        ttk.Button(buttons, text="Actualiser", command=self._refresh_report).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir SUMMARY.md", command=lambda: self._open_report("SUMMARY.md")).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir audit.csv", command=lambda: self._open_report("audit.csv")).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir audit.json", command=lambda: self._open_report("audit.json")).pack(side="left")
        ttk.Button(buttons, text="Ouvrir dossier", command=self._open_folder).pack(side="right")
        ttk.Label(tab, text="Aperçu du dernier résumé local (pas de données GitHub sans exécution)",
                  style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=(0, 7))
        self.report_view = ScrolledText(tab, wrap="word", font=("Consolas", 10),
                                        bg="white", fg=NAVY, state="disabled")
        self.report_view.grid(row=2, column=0, sticky="nsew")
        tab.rowconfigure(2, weight=1)
        self._refresh_report()

    def _action_button(self, parent: ttk.Widget, caption: str, callback,
                       *, primary: bool = False) -> ttk.Button:
        btn = ttk.Button(parent, text=caption, command=callback,
                         style="Primary.TButton" if primary else "TButton")
        self._action_buttons.append(btn)
        return btn

    def _browse_report_folder(self) -> None:
        value = filedialog.askdirectory(title="Choisir le dossier des rapports", initialdir=ROOT)
        if value:
            self.out_dir.set(value)
            self._refresh_report()

    def _browse_legacy_folder(self) -> None:
        value = filedialog.askdirectory(title="Choisir les rapports historiques normalisés", initialdir=ROOT)
        if value:
            self.legacy_dir.set(value)
            self.use_legacy.set(True)

    def _browse_source(self) -> None:
        value = filedialog.askopenfilename(title="Choisir un rapport historique", initialdir=ROOT,
                                           filetypes=[("Rapports JSON ou ZIP", "*.json *.zip"),
                                                      ("Tous les fichiers", "*.*")])
        if value:
            self.source_file.set(value)
            if Path(value).suffix.lower() == ".json":
                self.zip_member.set("")

    def _browse_import_folder(self) -> None:
        value = filedialog.askdirectory(title="Choisir le dossier des imports", initialdir=ROOT)
        if value:
            self.legacy_out.set(value)

    def _update_token_label(self) -> None:
        self.token_status.set("Local : aucun jeton requis" if not self.require_auth.get()
                              else ("Jeton API distant : présent" if local_token_present()
                                    else "Jeton API distant : absent"))

    def _run_plan(self) -> None:
        try:
            args = make_plan_args(source=self.inventory_source.get(), limit=self.limit.get())
        except ValueError as error:
            messagebox.showerror("Options invalides", str(error))
            return
        self._start(args, "Prévisualisation du périmètre")

    def _run_audit(self) -> None:
        self._update_token_label()
        if self.require_auth.get() and not local_token_present():
            messagebox.showwarning("Jeton GitHub absent", (
                "KOA_AUDIT_TOKEN ou GH_TOKEN n'est pas défini dans l'environnement de ce programme.\n\n"
                "L’observation GitHub est facultative; utilisez Audit local pour travailler sans jeton. "
                "Vous pouvez décocher « Exiger un jeton » pour un essai public, "
                "mais plusieurs contrôles resteront UNKNOWN."
            ))
            return
        try:
            if not self.out_dir.get().strip():
                raise ValueError("Choisir un dossier pour les rapports")
            args = make_audit_args(
                source=self.inventory_source.get(), limit=self.limit.get(),
                workers=self.workers.get(), max_age_days=self.max_age.get(),
                out=Path(self.remote_out_dir.get()), require_auth=self.require_auth.get(),
                discover_public_owner=self.discover.get(),
                legacy_dir=Path(self.legacy_dir.get()) if self.use_legacy.get() else None,
            )
        except (ValueError, OSError) as error:
            messagebox.showerror("Options invalides", str(error))
            return
        self._start(args, "Audit GitHub OBSERVE")

    def _run_import(self) -> None:
        try:
            if not self.source_file.get().strip() or not self.legacy_out.get().strip():
                raise ValueError("Choisir le fichier source et le dossier des imports")
            args = make_legacy_args(
                tool=self.tool.get(), repo=self.target_repo.get().strip(),
                source_path=Path(self.source_file.get()), member=self.zip_member.get(),
                out_dir=Path(self.legacy_out.get()),
            )
        except (ValueError, OSError) as error:
            messagebox.showerror("Import invalide", str(error))
            return
        self._start(args, "Import historique")

    def _start(self, args: list[str], label: str) -> None:
        if self._running:
            return
        self._running = True
        self._cancelled = False
        self._action = label
        self.status.set(f"En cours : {label}…")
        for button in self._action_buttons:
            button.configure(state="disabled")
        self.cancel_button.configure(state="normal")
        # No flashing/animated LED indicator: wait with a stable bar until
        # the CLI reports an actual measurable number of completed operations.
        self.progress.configure(value=0)
        self._log("\n" + "─" * 54)
        self._log(f"▶ {label}")
        self._log("Publication d'agrégats vers le seul dépôt d'audit." if label == "Publication du tableau de bord"
                  else "Lecture seule — exécution locale de koa_audit.")
        thread = threading.Thread(target=self._worker, args=(args,), daemon=True)
        thread.start()

    def _worker(self, args: list[str]) -> None:
        from koa_audit.windows_process import hidden_console_kwargs
        try:
            # Never invoke a shell or interpolate a user-supplied command line.
            proc = subprocess.Popen(
                [child_python(), "-u", *args], cwd=str(ROOT),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL, text=True, encoding="utf-8",
                errors="replace", bufsize=1, **hidden_console_kwargs(),
            )
            self._process = proc
            if self._cancelled and proc.poll() is None:
                proc.terminate()
            assert proc.stdout is not None
            for line in proc.stdout:
                self._events.put(("line", line.rstrip("\r\n")))
            return_code = proc.wait()
            self._events.put(("done", return_code))
        except Exception as error:
            # Error objects might include a local path but not an API token.
            self._events.put(("error", f"Démarrage impossible : {type(error).__name__}"))
        finally:
            self._process = None

    def _cancel(self) -> None:
        if not self._running:
            return
        self._cancelled = True
        self.status.set("Annulation demandée…")
        proc = self._process
        if proc and proc.poll() is None:
            try:
                proc.terminate()
            except OSError:
                pass
            threading.Thread(target=self._kill_if_needed, args=(proc,), daemon=True).start()

    @staticmethod
    def _kill_if_needed(proc: subprocess.Popen[str]) -> None:
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            try:
                proc.kill()
            except OSError:
                pass

    def _poll(self) -> None:
        try:
            while True:
                event = self._events.get_nowait()
                if event[0] == "line":
                    self._log(event[1])
                elif event[0] == "done":
                    self._finish(event[1])
                elif event[0] == "error":
                    self._log(event[1])
                    self._finish(2)
                elif event[0] == "campaign-measuring":
                    _, done, total, saved_count = event
                    self.campaign_progress.configure(maximum=total, value=done)
                    self.campaign_progress_label.set(
                        f"Mesure : {done}/{total} dépôts · {round(100 * done / total)} %")
                    self.campaign_detail.set(
                        f"{done}/{total} dépôts examinés · {saved_count} rapport(s) généré(s)")
                elif event[0] == "campaign-progress":
                    _, done, total, caption = event
                    self.campaign_progress.configure(maximum=total, value=done)
                    self.campaign_progress_label.set(
                        f"Création : {done}/{total} étapes · {caption}")
                elif event[0] == "campaign-discovering":
                    _, done, total, found_count = event
                    self.campaign_progress.configure(maximum=total, value=done)
                    self.campaign_progress_label.set(
                        f"Recherche : {done}/{total} dépôts · {round(100 * done / total)} %")
                    self.campaign_detail.set(f"Rapports reconnus : {found_count} · copies examinées : {done}")
                elif event[0] == "campaign-discovered":
                    self.campaign_busy = False
                    self.campaign_create_button.configure(state="normal")
                    discovered, skipped = event[1], event[2]
                    cancelled = self.campaign_collection_cancel.is_set()
                    self.campaign_collection_cancel.clear()
                    self.campaign_progress_label.set(
                        f"Recherche {'interrompue' if cancelled else 'terminée'} · "
                        f"{len(discovered)} rapport(s) reconnu(s) · {len(skipped)} clone(s) ignoré(s)")
                    if discovered:
                        samples = "\n".join(f"• {r['repository'].split('/')[-1]} : {r['name']}"
                                            for r in discovered[:12])
                        if len(discovered) > 12:
                            samples += f"\n… et {len(discovered)-12} autres"
                        if messagebox.askyesno("Confirmer l'import privé",
                                f"{len(discovered)} rapports existants trouvés :\n\n{samples}\n\n"
                                "Ils peuvent contenir des informations sensibles. "
                                "Ils seront COPIÉS uniquement dans le prochain ZIP privé; "
                                "aucun résultat de test n'est réexécuté.\n\nJoindre ces rapports ?"):
                            accepted = 0; already = 0
                            for result in discovered:
                                repo, path = result['repository'], result['path']
                                attached = self.campaign_attached.setdefault(repo, [])
                                if path not in attached and len(attached) < 15:
                                    attached.append(path); accepted += 1
                                    self.campaign_expected_hashes[path] = result['sha256']
                                else: already += 1
                            self.campaign_detail.set(
                                f"{accepted} rapport(s) préparé(s) pour la prochaine campagne · "
                                f"{already} déjà joints ou au-delà des limites · {len(skipped)} ignorés")
                        else:
                            self.campaign_detail.set("Rapports identifiés, aucun fichier importé (choix conservé).")
                    else:
                        self.campaign_detail.set(
                            f"Aucun rapport reconnu aux emplacements connus · {len(skipped)} clone(s) ignoré(s). "
                            "Ce n'est pas une non-conformité.")
                elif event[0] == "campaign-measured":
                    self.campaign_busy=False
                    self.campaign_create_button.configure(state="normal")
                    saved, skipped=event[1],event[2]
                    cancelled=self.campaign_collection_cancel.is_set()
                    self.campaign_collection_cancel.clear()
                    if cancelled:
                        self.campaign_progress_label.set(
                            "Mesure interrompue · progression conservée (sans nouvelle collecte)")
                    skipped_attach=0
                    for repo,path in saved:
                        if len(self.campaign_attached.get(repo, [])) < 15:
                            self.campaign_attached.setdefault(repo,[]).append(path)
                        else:
                            skipped_attach+=1
                    self.campaign_detail.set(f"{len(saved)-skipped_attach} rapport(s) joints · {len(skipped)} dépôt(s) ignoré(s) · {skipped_attach} au-delà de la limite de 15 preuves")
                    if not cancelled:
                        self.campaign_progress_label.set(
                            f"Mesure terminée · {len(saved)} rapport(s) généré(s) · "
                            f"{len(skipped)} ignoré(s)")
                elif event[0] in ("campaign-created", "campaign-failed"):
                    self.campaign_busy=False
                    self.campaign_create_button.configure(state="normal")
                    if event[0] == "campaign-created":
                        self.campaign_attached.clear()
                        self.campaign_expected_hashes.clear()
                        self._campaign_refresh()
                        self.campaign_detail.set("Campagne figée : " + Path(event[1]).name)
                        self.status.set("Campagne enregistrée sans modifier GitHub")
                        self.campaign_progress_label.set("Campagne créée et intégrité vérifiée · 100 %")
                    else:
                        self.campaign_progress_label.set("Création interrompue · archive non publiée")
                        self.campaign_detail.set("Erreur : " + event[1])
                        messagebox.showerror("Création impossible",event[1])
        except queue.Empty:
            pass
        self.root.after(150, self._poll)

    def _finish(self, exit_code: int) -> None:
        if not self._running:
            return
        self._running = False
        # No indeterminate animation. Only mark complete on a successful exit.
        self.progress.configure(value=100 if exit_code == 0 and not self._cancelled else 0)
        self.cancel_button.configure(state="disabled")
        for button in self._action_buttons:
            button.configure(state="normal")
        if self._cancelled:
            self.status.set("Opération annulée — vérifier les fichiers éventuellement partiels")
            self._log("■ Annulé. Vérifier le dossier de sortie avant utilisation.")
        elif exit_code == 0:
            self.status.set(f"Terminé : {self._action}")
            self._log("✓ Terminé.")
            if self._action == "Import historique":
                self.legacy_dir.set(self.legacy_out.get())
                self.use_legacy.set(True)
            if self._action == "Audit local":
                self.triage_input.set(str(self._report_path("audit.json")))
                self.dashboard_local.set(str(self._report_path("audit.json")))
                self._refresh_report()
            if self._action == "Audit GitHub OBSERVE":
                self.dashboard_github.set(str(Path(self.remote_out_dir.get()) / "audit.json"))
            if self._action == "Tableau de bord":
                self._log("Préparation locale terminée; utiliser Publier sur GitHub pour la mise en ligne.")
            if self._action == "Publication du tableau de bord":
                self._log("Voir le site GitHub Pages après activation (une seule fois).")
        else:
            self.status.set(f"Échec : {self._action} (code {exit_code})")
            self._log(f"✗ Échec (code {exit_code}).")

    def _log(self, line: str) -> None:
        if hasattr(self, "console"):
            self.console.configure(state="normal")
            self.console.insert(END, line + "\n")
            # Bound UI memory even for unusual command output.
            if int(self.console.index("end-1c").split(".")[0]) > 1800:
                self.console.delete("1.0", "300.0")
            self.console.see(END)
            self.console.configure(state="disabled")

    def _report_path(self, filename: str) -> Path:
        return Path(self.out_dir.get()).expanduser().resolve() / filename

    def _refresh_report(self) -> None:
        path = self._report_path("SUMMARY.md")
        try:
            report = path.read_text(encoding="utf-8")[:100_000]
        except OSError:
            report = ("Aucun résumé local trouvé.\n\n"
                      "Lancer d'abord un audit depuis l'onglet « Audit GitHub ».\n"
                      "Aucun rapport de sécurité réel n'a été généré par cette interface.")
        self.report_view.configure(state="normal")
        self.report_view.delete("1.0", END)
        self.report_view.insert("1.0", report)
        self.report_view.configure(state="disabled")

    @staticmethod
    def _open_file(path: Path) -> None:
        if os.name == "nt":
            os.startfile(str(path))  # type: ignore[attr-defined]
        else:
            webbrowser.open(path.as_uri())

    def _open_report(self, filename: str) -> None:
        path = self._report_path(filename)
        if not path.is_file():
            messagebox.showinfo("Rapport non disponible", f"Fichier introuvable :\n{path}")
            return
        try:
            self._open_file(path)
        except OSError as error:
            messagebox.showerror("Ouverture impossible", str(error))

    def _open_folder(self) -> None:
        path = Path(self.out_dir.get()).expanduser().resolve()
        if not path.is_dir():
            messagebox.showinfo("Dossier non disponible", "Aucun rapport n'a encore été produit.")
            return
        try:
            self._open_file(path)
        except OSError as error:
            messagebox.showerror("Ouverture impossible", str(error))

    def _on_close(self) -> None:
        if self._running:
            if not messagebox.askyesno("Fermer le lanceur", "Une opération est en cours. L'annuler et fermer ?"):
                return
            self._cancel()
        if self._preview_server is not None:
            self._preview_server.shutdown()
            self._preview_server.server_close()
        self.root.destroy()


def main() -> None:
    if TK_ERROR is not None:
        log = diagnostic_log(TK_ERROR)
        _fatal_dialog(
            "kOA GitHub Audit — Tkinter indisponible",
            "L'interface Tkinter ne peut pas démarrer. Installez Python 3.11+ "
            "avec Tcl/Tk (installateur officiel).\n\n"
            + (f"Journal : {log}" if log else "Journal impossible à écrire."),
        )
        return
    if sys.version_info < (3, 11):
        error = RuntimeError("Python 3.11 ou supérieur requis")
        log = diagnostic_log(error)
        _fatal_dialog("kOA GitHub Audit — Python incompatible",
                      f"Version détectée : {sys.version.split()[0]}. Python 3.11+ requis.\n"
                      + (f"Journal : {log}" if log else ""))
        return
    root = None
    try:
        root = Tk()
        root.withdraw()
        project = _choose_project_root(root)
        _initialize_project(project)
        AuditLauncher(root)
        root.deiconify()
        root.lift()
        root.mainloop()
    except Exception as error:
        log = diagnostic_log(error)
        text = (f"{type(error).__name__}: {error}\n\n"
                "Vérifiez que le ZIP complet a été décompressé.\n"
                "Sur Windows, vous pouvez aussi lancer DIAGNOSTIC_LAUNCHER.cmd.\n\n"
                + (f"Détails : {log}" if log else "Le journal d'erreur n'a pas pu être créé."))
        if root is not None:
            try:
                messagebox.showerror("kOA GitHub Audit — démarrage impossible", text, parent=root)
                root.destroy()
                return
            except Exception:
                pass
        _fatal_dialog("kOA GitHub Audit — démarrage impossible", text)


if __name__ == "__main__":
    main()
