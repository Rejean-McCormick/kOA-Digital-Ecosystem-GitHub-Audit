"""Explicit, bounded, read-only local engineering measurement.

No source repository modification, no Git fetch, no test execution, no shell.
Results are *observations*, never a compliance score or a certification.
Source files and filenames are not copied into the report.
"""
from __future__ import annotations

import csv
import io
import json
import os
import shutil
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .campaigns import _git_observation, _hash, _dump, _origin_matches, _git_cmd

MAX_TRACKED = 25000
MAX_TOOL_BYTES = 8_000_000
TOOL_TIMEOUT = 75
EXTENSIONS = {'.py':'Python', '.ps1':'PowerShell', '.pyw':'Python', '.js':'JavaScript',
              '.jsx':'JavaScript', '.ts':'TypeScript', '.tsx':'TypeScript', '.go':'Go',
              '.rs':'Rust', '.cs':'C#', '.c':'C', '.cpp':'C++', '.h':'C/C++',
              '.java':'Java', '.json':'JSON', '.md':'Markdown', '.html':'HTML',
              '.css':'CSS', '.sh':'Shell', '.yml':'YAML', '.yaml':'YAML', '.toml':'TOML'}


def _run(argv: list[str], timeout: int) -> dict:
    """Read-only subprocess, bounded output to disk and fixed time limit."""
    import tempfile
    start = datetime.now(timezone.utc)
    with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
        try:
            p = subprocess.run(argv, stdout=output, stderr=errors, timeout=timeout,
                 check=False, stdin=subprocess.DEVNULL,
                 env={**os.environ, 'GIT_TERMINAL_PROMPT':'0', 'GIT_OPTIONAL_LOCKS':'0',
                      'NO_COLOR':'1'}, shell=False)
        except subprocess.TimeoutExpired:
            return {'status':'timeout','timeout_seconds':timeout}
        except OSError:
            return {'status':'unavailable'}
        size = output.tell()
        if size > MAX_TOOL_BYTES:
            return {'status':'output_too_large', 'bytes':size}
        output.seek(0)
        data = output.read()
        if p.returncode:
            return {'status':'tool_error', 'return_code':p.returncode}
        return {'status':'ok', 'data':data}


def _tracked_filenames(folder: Path) -> tuple[list[str], str]:
    output = _run(['git', '-c', 'core.fsmonitor=false', '-C', str(folder),
                   'ls-files', '-z', '--cached'], 30)
    if output['status'] != 'ok':
        return [], output['status']
    names = output['data'].split(b'\x00')
    if len(names) > MAX_TRACKED + 1:
        return [], 'tracked_file_count_limit'
    return [x.decode('utf-8','replace') for x in names if x], 'ok'


def collect(folder: Path, repo: str, *, static_tools: bool = False,
            timeout: int = TOOL_TIMEOUT) -> dict:
    """Measure a selected local clone; never executes project code.

    Optional scc and Lizard parse source from disk; opt-in only.  They are not
    executed automatically when campaigns are created.
    """
    folder=Path(folder)
    if not folder.is_dir() or folder.is_symlink():
        raise ValueError('Dossier source absent ou lien symbolique')
    git=_git_observation(folder, repo)
    if git.get('status') != 'verified_git_origin':
        raise ValueError('Origine GitHub non vérifiée : collecte refusée pour éviter une mauvaise attribution')
    names, status = _tracked_filenames(folder)
    if status != 'ok':
        raise ValueError('Inventaire Git non disponible : ' + status)
    extensions = Counter()
    docs = Counter()
    actions = 0
    tracked_bytes = 0
    size_known = 0
    for name in names:
        rel = Path(name.replace('\\','/'))
        if rel.is_absolute() or '..' in rel.parts:
            continue
        ext = rel.suffix.lower()
        if ext in EXTENSIONS:
            extensions[EXTENSIONS[ext]] += 1
        basename=rel.name.casefold()
        if basename in ('readme.md','architecture.md','contributing.md','security.md','license','pyproject.toml', 'package.json'):
            docs[basename] += 1
        if len(rel.parts) >= 3 and rel.parts[0] == '.github' and rel.parts[1] == 'workflows' and ext in ('.yml','.yaml'):
            actions += 1
        file=folder/rel
        try:
            if not file.is_symlink() and file.is_file():
                tracked_bytes += file.stat().st_size
                size_known += 1
        except OSError:
            pass
    data = {'format':'koa_evidence.static_metadata.v1',
            'captured_at':datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'repository':repo,
            'git':git,
            'scope': 'Fichiers suivis Git (chemin et contenu non exportés). Métadonnées seulement.',
            'tracked_files':len(names), 'tracked_files_sized':size_known,
            'tracked_bytes':tracked_bytes,
            'languages_by_extension': dict(extensions.most_common(25)),
            'documentation_markers':dict(docs),
            'github_workflow_files':actions,
            'optional_tools': {},
            'limitations':['Fichiers non suivis, ignorés, sous-modules et résultats de CI non inspectés.',
                           'Présence d’un fichier ne prouve pas sa qualité ni son exécution.',
                           'Les données du répertoire de travail peuvent différer de HEAD.',
                           'Aucune pratique ni qualification n’est validée automatiquement.']}
    if static_tools:
        if git.get('worktree') != 'tracked_files_clean_untracked_not_checked':
            data['optional_tools']['note']='Mesures de code effectuées sur une copie présentant des changements suivis; pas liées au SHA.'
        exe=shutil.which('scc')
        if exe:
            result=_run([exe, '--format', 'json', str(folder)], timeout)
            if result['status']=='ok':
                try:
                    parsed=json.loads(result['data'])
                    if not isinstance(parsed, list): raise ValueError('Format scc différent')
                    rows=[]
                    for item in parsed:
                        if not isinstance(item, dict): continue
                        rows.append({'language':str(item.get('Name',''))[:60],
                                     'files':int(item.get('Count',0)),
                                     'code_lines':int(item.get('Code',0)),
                                     'comment_lines':int(item.get('Comment',0))})
                    data['optional_tools']['scc']={'status':'measured','languages':rows[:60],
                                                   'note':'Mesure scc locale, non interprétée comme qualité.'}
                except (TypeError,ValueError,KeyError):
                    data['optional_tools']['scc']={'status':'unrecognized_output'}
            else: data['optional_tools']['scc']={'status':result['status']}
        else: data['optional_tools']['scc']={'status':'not_installed'}
        exe=shutil.which('lizard')
        if exe:
            result=_run([exe,'-V','--csv',str(folder)], timeout)
            if result['status']=='ok':
                try:
                    csvdata=io.StringIO(result['data'].decode('utf-8','replace'))
                    reader=csv.reader(csvdata)
                    header=next(reader,None)
                    if not header or 'CCN' not in header: raise ValueError('CSV header not recognized')
                    index=header.index('CCN'); n=0; total=0.0; mx=0.0
                    for row in reader:
                        if len(row)<=index: continue
                        ccn=float(row[index]); n+=1; total+=ccn; mx=max(mx,ccn)
                    data['optional_tools']['lizard']={'status':'measured', 'functions':n,
                        'mean_ccn':round(total/n,2) if n else None, 'max_ccn':mx if n else None,
                        'note':'Complexité cyclomatique mesurée; pas un verdict.'}
                except (TypeError,ValueError,StopIteration):
                    data['optional_tools']['lizard']={'status':'unrecognized_output'}
            else: data['optional_tools']['lizard']={'status':result['status']}
        else: data['optional_tools']['lizard']={'status':'not_installed'}
        exe=shutil.which('ctags')
        if exe:
            # Explicit -f - prevents a tags file being written into the source.
            # --options=NONE disables executable/user/project-specific config.
            # Universal Ctags only; other ctags variants return an error safely.
            result=_run([exe,'--options=NONE','--output-format=json','-f','-','-R',str(folder)],timeout)
            if result['status']=='ok':
                try:
                    tags=0; kinds=Counter(); languages=Counter()
                    for line in result['data'].splitlines():
                        if not line: continue
                        obj=json.loads(line)
                        if not isinstance(obj,dict) or obj.get('_type')!='tag': continue
                        tags+=1
                        kinds[str(obj.get('kind','unknown'))[:50]]+=1
                        languages[str(obj.get('language','unknown'))[:50]]+=1
                    data['optional_tools']['ctags']={'status':'measured','symbols':tags,
                        'kinds':dict(kinds.most_common(20)),'languages':dict(languages.most_common(20)),
                        'note':'Symboles indexés dans la copie locale. Ce chiffre ne reflète ni qualité ni tests réussis.'}
                except (ValueError,TypeError):
                    data['optional_tools']['ctags']={'status':'unrecognized_output'}
            else:
                data['optional_tools']['ctags']={'status':result['status'],
                    'note':'Universal Ctags avec sortie JSON requis; aucun tags fichier n’a été créé.'}
        else:
            data['optional_tools']['ctags']={'status':'not_installed'}
    else:
        data['optional_tools']['status']='not_requested'
    return data


def write_report(report: dict, dest: Path) -> Path:
    """Store a small, private report atomically. Does not modify source folder."""
    dest = Path(dest)
    payload=_dump(report)
    if len(payload) > 2_000_000:
        raise ValueError('Rapport de métadonnées trop volumineux')
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() or dest.is_symlink():
        raise FileExistsError('Ne pas écraser une preuve existante')
    with dest.open('xb') as f:
        f.write(payload)
    return dest
