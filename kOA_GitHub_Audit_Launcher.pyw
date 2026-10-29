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
        self.dashboard_local = StringVar(value=str(ROOT / "reports" / "local" / "audit.json"))
        self.dashboard_github = StringVar(value="")
        self.triage_input = StringVar(value=str(ROOT / "reports" / "local" / "audit.json"))
        self._preview_server = None
        self.profile_repo = StringVar(value="Rejean-McCormick/Konnaxion")
        self.profile_kind = StringVar(value="ENGINEERING_PROFILE.md")
        self.profile_family = StringVar(value="Tous")
        self.profile_status = StringVar(value="Non évalué")
        self.profile_note = StringVar(value="")
        self.profile_overview = StringVar(value="")
        self.profile_audit_context = StringVar(value="")
        self.profile_catalog_items = {}
        self.profile_current_id = None
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

        self._styles()
        self._build_ui()
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
        style.configure("TNotebook", background=BG)
        style.configure("TNotebook.Tab", font=("Segoe UI", 10), padding=(14, 9))

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=(18, 14))
        outer.pack(fill="both", expand=True)
        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 10))
        ttk.Label(header, text="kOA  /  GitHub Audit", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="LOCAL_OBSERVE — scanner local · Vérification ZIP · Dashboard GitHub Pages · sans jeton personnel",
                  style="Muted.TLabel").pack(anchor="w", pady=(3, 0))

        self.tabs = ttk.Notebook(outer)
        self.tabs.pack(fill="both", expand=True)
        local_tab = ttk.Frame(self.tabs, padding=14)
        triage_tab = ttk.Frame(self.tabs, padding=14)
        dashboard_tab = ttk.Frame(self.tabs, padding=14)
        reports_tab = ttk.Frame(self.tabs, padding=14)
        profiles_tab = ttk.Frame(self.tabs, padding=14)
        legacy_tab = ttk.Frame(self.tabs, padding=14)
        audit_tab = ttk.Frame(self.tabs, padding=14)
        self.tabs.add(local_tab, text="  Audit local  ")
        self.tabs.add(triage_tab, text="  Vérification + ZIP  ")
        self.tabs.add(dashboard_tab, text="  Tableau de bord  ")
        self.tabs.add(reports_tab, text="  Rapports  ")
        self.tabs.add(profiles_tab, text="  Profils & conformité  ")
        self.tabs.add(legacy_tab, text="  Import historique  ")
        self.tabs.add(audit_tab, text="  GitHub (optionnel)  ")
        self._build_audit(audit_tab)
        self._build_local(local_tab)
        self._build_triage(triage_tab)
        self._build_dashboard(dashboard_tab)
        self._build_reports(reports_tab)
        self._build_profiles(profiles_tab)
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
        self.progress = ttk.Progressbar(tab, mode="indeterminate")
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
        frame = ttk.LabelFrame(tab, text="Bilan global pour GitHub Pages (données agrégées uniquement)", padding=15)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)
        self._input_row(frame, 0, "Rapport local (JSON)", self.dashboard_local,
                        browse=lambda: self._choose_json(self.dashboard_local), width=57)
        self._input_row(frame, 1, "Rapport GitHub (optionnel)", self.dashboard_github,
                        browse=lambda: self._choose_json(self.dashboard_github), width=57)
        btns=ttk.Frame(frame)
        btns.grid(row=2, column=0, columnspan=3, sticky="w", pady=(14, 5))
        self._action_button(btns, "Mettre à jour le tableau de bord", self._run_dashboard, primary=True).pack(side="left", padx=(0, 9))
        self._action_button(btns, "Publier sur GitHub (1 clic)", self._sync_dashboard, primary=True).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Aperçu dans le navigateur", command=self._preview_dashboard).pack(side="left", padx=(0, 9))
        ttk.Button(btns, text="Ouvrir le dossier docs", command=lambda: self._open_file(ROOT / "docs")).pack(side="left")
        note=("« Publier sur GitHub » envoie uniquement le bilan agrégé dans le dépôt d'audit. "
              "Aucun jeton à saisir, aucun nouvel audit, aucun code source ou secret publié. "
              "Git pour Windows utilise votre connexion GitHub existante. Le bouton local d'aperçu ne publie rien.")
        ttk.Label(tab, text=note, wraplength=910, justify="left", style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=14)
        ttk.Label(tab, text="Une seule configuration GitHub peut être nécessaire : Settings > Pages > Source : GitHub Actions. "
                  "Ensuite, le site se déploie automatiquement après chaque publication. Ne pas utiliser le bouton d'audit distant.",
                  wraplength=910, justify="left").grid(row=2, column=0, sticky="w", pady=8)

    def _build_profiles(self, tab: ttk.Frame) -> None:
        """Read standardized files and let the user review architecture/security patterns."""
        from koa_audit import profiles
        inventory = profiles.inventory(ROOT)
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

    def _profiles_refresh(self) -> None:
        from koa_audit import profiles
        repo = self.profile_repo.get()
        progress = profiles.progress(ROOT, repo)
        self.profile_overview.set(
            f"{repo}  |  Pratiques : {progress['reviewed']}/{progress['total']} examinées  |  "
            f"Appliqué : {progress['Appliqué']}  |  À améliorer : {progress['À améliorer']}  |  "
            f"Non applicable : {progress['Pas applicable']}")
        report = Path(self.dashboard_local.get()).expanduser()
        try:
            ctx = profiles.audit_context(ROOT, repo, report)
            if ctx:
                self.profile_audit_context.set(
                    f"Dernier audit JSON choisi : {ctx['status']} · "
                    f"{ctx['files_inspected']}/{ctx['files_enumerated']} fichiers inspectés · "
                    f"{ctx['findings']} observations · commit {ctx['head']}")
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

    def _preview_dashboard(self) -> None:
        try:
            dashboard_dir = ROOT / "docs"
            if not (dashboard_dir / "index.html").is_file():
                raise FileNotFoundError(
                    "Le tableau de bord n'est pas dans le dossier docs/. "
                    "Décompressez le ZIP complet avant de lancer l'application."
                )
            if self._preview_server is None:
                handler = functools.partial(_NoConsolePreviewHandler,
                                            directory=str(dashboard_dir))
                server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
                server.daemon_threads = True
                threading.Thread(target=server.serve_forever, daemon=True,
                                 name="koa-dashboard-preview").start()
                self._preview_server = server
            # Loopback only: nothing is sent to GitHub or to a remote server.
            webbrowser.open(f"http://127.0.0.1:{self._preview_server.server_port}/")
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
        self.progress.start(12)
        self._log("\n" + "─" * 54)
        self._log(f"▶ {label}")
        self._log("Publication d'agrégats vers le seul dépôt d'audit." if label == "Publication du tableau de bord"
                  else "Lecture seule — exécution locale de koa_audit.")
        thread = threading.Thread(target=self._worker, args=(args,), daemon=True)
        thread.start()

    def _worker(self, args: list[str]) -> None:
        flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0
        try:
            # Never invoke a shell or interpolate a user-supplied command line.
            proc = subprocess.Popen(
                [child_python(), "-u", *args], cwd=str(ROOT),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL, text=True, encoding="utf-8",
                errors="replace", bufsize=1, creationflags=flags,
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
        except queue.Empty:
            pass
        self.root.after(150, self._poll)

    def _finish(self, exit_code: int) -> None:
        if not self._running:
            return
        self._running = False
        self.progress.stop()
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
