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
    global ROOT, SCHEMAS, make_plan_args, make_audit_args, make_legacy_args, make_local_args, make_triage_args
    # Do not search arbitrary installed modules if the selected folder is incomplete.
    if not _valid_project_dir(folder):
        raise FileNotFoundError("Le dépôt n'est pas extrait complètement.")
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
    from koa_audit.launcher_support import (
        make_plan_args as plan, make_audit_args as audit, make_legacy_args as legacy,
        make_local_args as local, make_triage_args as triage,
    )
    from koa_audit.legacy import SCHEMAS as schemas
    ROOT = folder
    SCHEMAS = schemas
    make_plan_args, make_audit_args, make_legacy_args = plan, audit, legacy
    make_local_args = local
    make_triage_args = triage
BG = "#f5f7fa"
NAVY = "#17324d"
MUTED = "#596879"
ACCENT = "#16659b"


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
        self.root.title("kOA — Audit local des dépôts")
        self.root.geometry("1040x760")
        self.root.minsize(830, 640)
        self.root.configure(bg=BG)
        self._events: queue.Queue[tuple] = queue.Queue()
        self._process: subprocess.Popen[str] | None = None
        self._running = False
        self._cancelled = False
        self._action = ""
        self._action_buttons: list[ttk.Button] = []

        default_workspace = Path("C:/mycode") if Path("C:/mycode").is_dir() else ROOT.parent
        self.workspace = StringVar(value=str(default_workspace))
        self.depth = StringVar(value="4")
        self.limit = StringVar(value="0")
        self.max_files = StringVar(value="6000")
        self.out_dir = StringVar(value=str(ROOT / "reports"))
        self.only_inventory = BooleanVar(value=False)
        self.use_legacy = BooleanVar(value=(ROOT / ".legacy").is_dir())
        self.legacy_dir = StringVar(value=str(ROOT / ".legacy"))
        self.tool = StringVar(value="LevelUpDiag-Orgo")
        self.target_repo = StringVar(value="Rejean-McCormick/Orgo")
        self.source_file = StringVar()
        self.zip_member = StringVar(value="verification/embedded/summary.json")
        self.legacy_out = StringVar(value=str(ROOT / ".legacy"))
        self.triage_input = StringVar(value=str(ROOT / "reports" / "audit.json"))
        self.triage_output = StringVar(value=str(ROOT / "reports"))
        self.status = StringVar(value="Prêt — aucun audit exécuté dans cette session")
        self.token_status = StringVar(value="100 % local · Aucun jeton")

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
        style.map("Primary.TButton", background=[("active", "#0f4c79"), ("disabled", "#8aa8bb")])
        style.configure("TNotebook", background=BG)
        style.configure("TNotebook.Tab", font=("Segoe UI", 10), padding=(14, 9))

    def _build_ui(self) -> None:
        outer = ttk.Frame(self.root, padding=(18, 14))
        outer.pack(fill="both", expand=True)
        header = ttk.Frame(outer)
        header.pack(fill="x", pady=(0, 10))
        ttk.Label(header, text="kOA  /  Audit local", style="Title.TLabel").pack(anchor="w")
        ttk.Label(header, text="LOCAL_OBSERVE — audit des dossiers Git · sans jeton ni connexion réseau",
                  style="Muted.TLabel").pack(anchor="w", pady=(3, 0))

        self.tabs = ttk.Notebook(outer)
        self.tabs.pack(fill="both", expand=True)
        audit_tab = ttk.Frame(self.tabs, padding=14)
        legacy_tab = ttk.Frame(self.tabs, padding=14)
        reports_tab = ttk.Frame(self.tabs, padding=14)
        triage_tab = ttk.Frame(self.tabs, padding=14)
        self.tabs.add(audit_tab, text="  Audit local  ")
        self.tabs.add(legacy_tab, text="  Import historique  ")
        self.tabs.add(reports_tab, text="  Rapports  ")
        self.tabs.add(triage_tab, text="  Vérification + ZIP  ")
        self._build_audit(audit_tab)
        self._build_legacy(legacy_tab)
        self._build_reports(reports_tab)
        self._build_triage(triage_tab)

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
        options = ttk.LabelFrame(tab, text="Dossiers Git locaux — aucun jeton requis", style="Card.TLabelframe", padding=12)
        options.grid(row=0, column=0, sticky="ew")
        options.columnconfigure(1, weight=1)
        self._input_row(options, 0, "Racine des projets", self.workspace,
                        browse=self._browse_workspace, width=55)
        self._input_row(options, 1, "Profondeur (0 à 10)", self.depth)
        self._input_row(options, 2, "Nombre de dépôts (0 = tous)", self.limit)
        self._input_row(options, 3, "Max fichiers par dépôt", self.max_files)
        self._input_row(options, 4, "Dossier des rapports", self.out_dir, browse=self._browse_report_folder)
        self._input_row(options, 5, "Diagnostics historiques", self.legacy_dir,
                        browse=self._browse_legacy_folder)
        flags = ttk.Frame(options)
        flags.grid(row=6, column=0, columnspan=3, sticky="w", pady=(8, 0))
        ttk.Checkbutton(flags, text="Limiter aux dépôts de l'inventaire kOA (49)",
                        variable=self.only_inventory).pack(anchor="w")
        ttk.Checkbutton(flags, text="Inclure les diagnostics historiques déjà importés",
                        variable=self.use_legacy).pack(anchor="w")

        controls = ttk.Frame(tab)
        controls.grid(row=1, column=0, sticky="ew", pady=(14, 8))
        self._action_button(controls, "Découvrir les dépôts locaux", self._run_plan).pack(side="left", padx=(0, 9))
        self._action_button(controls, "Scanner localement", self._run_audit, primary=True).pack(side="left")
        self.cancel_button = ttk.Button(controls, text="Annuler", command=self._cancel, state="disabled")
        self.cancel_button.pack(side="right")
        self.progress = ttk.Progressbar(tab, mode="indeterminate")
        self.progress.grid(row=2, column=0, sticky="ew", pady=(3, 8))
        ttk.Label(tab, text="Résultats heuristiques hors ligne (sans exécution du code cible)",
                  style="Muted.TLabel").grid(row=3, column=0, sticky="w", pady=(2, 5))
        self.console = ScrolledText(tab, height=10, font=("Consolas", 9), wrap="word",
                                    state="disabled", bg="white", fg=NAVY, relief="solid", borderwidth=1)
        self.console.grid(row=4, column=0, sticky="nsew")
        tab.rowconfigure(4, weight=1)
        self._log("Choisissez votre dossier de projets (ex. C:\\mycode), puis cliquez sur Scanner localement.")
        self._log("Aucune connexion GitHub, aucun jeton, aucune modification de dépôt.")

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
            "Après l'import, revenir à « Audit local » et cocher « Inclure les diagnostics historiques normalisés »."
        ), style="Muted.TLabel", wraplength=780).grid(row=2, column=0, sticky="w")

    def _build_triage(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        panel = ttk.LabelFrame(tab, text="Contre-vérification des observations locales", style="Card.TLabelframe", padding=14)
        panel.grid(row=0, column=0, sticky="ew")
        panel.columnconfigure(1, weight=1)
        self._input_row(panel, 0, "Audit JSON existant", self.triage_input,
                        browse=self._browse_triage_input, width=58)
        self._input_row(panel, 1, "Destination des ZIP", self.triage_output,
                        browse=self._browse_triage_output, width=58)
        ttk.Label(panel, text="Racine analysée : identique à celle de l'onglet Audit local.",
                  style="Muted.TLabel").grid(row=2, column=0, columnspan=3, sticky="w", pady=(7, 4))
        self._action_button(panel, "Contre-vérifier et créer le ZIP", self._run_triage, primary=True).grid(
            row=3, column=1, sticky="w", pady=(12, 9))
        ttk.Label(tab, text=(
            "Reprend les signalements de audit.json : présence des motifs aux lignes indiquées, "
            "fichiers sensibles suivis par Git, références des GitHub Actions, gros fichiers "
            "non inspectés et copies Git en doublon. Aucun code ni secret brut dans le ZIP. "
            "Un motif retrouvé n'est PAS une vulnérabilité confirmée."
        ), style="Muted.TLabel", wraplength=780, justify="left").grid(
            row=1, column=0, sticky="w", pady=(14, 8))
        ttk.Button(tab, text="Ouvrir le dossier des ZIP", command=self._open_triage_folder).grid(
            row=2, column=0, sticky="w", pady=(7, 0))

    def _build_reports(self, tab: ttk.Frame) -> None:
        tab.columnconfigure(0, weight=1)
        buttons = ttk.Frame(tab)
        buttons.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        ttk.Button(buttons, text="Actualiser", command=self._refresh_report).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir SUMMARY.md", command=lambda: self._open_report("SUMMARY.md")).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir audit.csv", command=lambda: self._open_report("audit.csv")).pack(side="left", padx=(0, 9))
        ttk.Button(buttons, text="Ouvrir audit.json", command=lambda: self._open_report("audit.json")).pack(side="left")
        ttk.Button(buttons, text="Ouvrir dossier", command=self._open_folder).pack(side="right")
        ttk.Label(tab, text="Aperçu du dernier rapport local",
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
            self.triage_input.set(str(Path(value) / "audit.json"))
            self.triage_output.set(value)
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

    def _browse_triage_input(self) -> None:
        selected = filedialog.askopenfilename(title="Choisir le rapport audit.json", initialdir=self.out_dir.get(),
                                               filetypes=[("Rapports JSON", "*.json"), ("Tous les fichiers", "*.*")])
        if selected:
            self.triage_input.set(selected)

    def _browse_triage_output(self) -> None:
        selected = filedialog.askdirectory(title="Destination du ZIP de preuves", initialdir=self.out_dir.get())
        if selected:
            self.triage_output.set(selected)

    def _open_triage_folder(self) -> None:
        folder = Path(self.triage_output.get()).expanduser()
        folder.mkdir(parents=True, exist_ok=True)
        self._open_file(folder)

    def _run_triage(self) -> None:
        try:
            args = make_triage_args(root=Path(self.workspace.get()),
                                    audit_json=Path(self.triage_input.get()),
                                    out_dir=Path(self.triage_output.get()), depth=self.depth.get())
        except (ValueError, OSError) as error:
            messagebox.showerror("Vérification locale", str(error))
            return
        self._start(args, "Contre-vérification + ZIP")

    def _browse_workspace(self) -> None:
        value = filedialog.askdirectory(title="Choisir la racine des dépôts Git",
                                         initialdir=self.workspace.get() if Path(self.workspace.get()).is_dir() else ROOT)
        if value:
            self.workspace.set(value)

    def _update_token_label(self) -> None:
        self.token_status.set("100 % local · Aucun jeton")

    def _run_plan(self) -> None:
        try:
            args = make_local_args(command="local-plan", root=Path(self.workspace.get()),
                                   depth=self.depth.get(), limit=self.limit.get())
        except (ValueError, OSError) as error:
            messagebox.showerror("Options invalides", str(error))
            return
        self._start(args, "Découverte locale")

    def _run_audit(self) -> None:
        try:
            args = make_local_args(command="local-audit", root=Path(self.workspace.get()),
                                   depth=self.depth.get(), limit=self.limit.get(),
                                   max_files=self.max_files.get(), out=Path(self.out_dir.get()),
                                   only_inventory=self.only_inventory.get(),
                                   legacy_dir=Path(self.legacy_dir.get()) if self.use_legacy.get() else None)
        except (ValueError, OSError) as error:
            messagebox.showerror("Options invalides", str(error))
            return
        self._start(args, "Audit local OBSERVE")

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
        self._log("Inspection hors ligne — aucune requête GitHub / aucun jeton.")
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
            if self._action == "Audit local OBSERVE":
                self.triage_input.set(str(self._report_path("audit.json")))
                self.triage_output.set(str(Path(self.out_dir.get()).expanduser().resolve()))
                self._refresh_report()
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
                      "Lancer d'abord un audit depuis l'onglet « Audit local ».\n"
                      "Aucune analyse de vulnérabilités par base CVE n'a été effectuée.")
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
