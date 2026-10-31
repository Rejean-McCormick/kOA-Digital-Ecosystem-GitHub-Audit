/* kOA Graph — Frozen publication viewer. Reuses the local dashboard's directory/detail UI.
 * Source: an immutable publication manifest, never a live repository API.
 */
(() => {
  'use strict';
  const root = document.getElementById('publication-viewer');
  if (!root) return;
  const $ = id => document.getElementById(id);
  const release = /^[0-9]{8}T[0-9]{6}Z(?:-[0-9]+(?:-[0-9]+)?)?$/;
  const repoPattern = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;
  const state = { manifest: null, selected: null, status: 'all', query: '' };
  const element = (tag, cls, text) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = String(text);
    return node;
  };
  const text = (id, value) => { const node = $(id); if (node) node.textContent = String(value); };
  const localized = (fr, en) => {
    const span = element('span');
    const a = element('span', 'fr', fr), b = element('span', 'en', en);
    span.append(a, b); return span;
  };
  const link = (href, label, cls) => {
    const a = element('a', cls, label); a.href = href; return a;
  };
  const selectedRepo = () => state.manifest?.repos.find(r => r.repo === state.selected);
  const status = s => s === 'captured' ? ['Capturé', 'Captured'] :
    ['fallback', 'retained'].includes(s) ? ['Conservé', 'Retained'] : ['Indisponible', 'Unavailable'];
  const safePage = path => {
    if (typeof path !== 'string' || !/^releases\/[0-9A-Za-z-]+\/repos\/[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+\.html$/.test(path)) return null;
    const id = path.split('/')[1];
    return release.test(id) ? root.dataset.pagesPrefix + path : null;
  };
  function select(repo) {
    if (!repoPattern.test(repo) || !state.manifest.repos.some(r => r.repo === repo)) return;
    state.selected = repo;
    renderList(); renderDetail();
  }
  function renderList() {
    const list = $('published-repo-list'); list.replaceChildren();
    let count = 0;
    const q = state.query.toLocaleLowerCase();
    for (const r of state.manifest.repos) {
      if (state.status !== 'all' && (state.status === 'retained' ? !['fallback','retained'].includes(r.status) : r.status !== state.status)) continue;
      if (q && !(r.repo.toLocaleLowerCase().includes(q) || (r.documents || []).some(d => d.path.toLocaleLowerCase().includes(q)))) continue;
      count++;
      const b = element('button', 'repo-entry' + (r.repo === state.selected ? ' active' : ''));
      b.type = 'button'; b.setAttribute('aria-pressed', String(r.repo === state.selected));
      const name = element('span'); name.append(element('strong', '', r.repo.split('/')[1]), element('small', '', r.repo));
      const badge = element('span', 'repo-badge'); badge.append(localized(...status(r.status)));
      b.append(name, badge); b.addEventListener('click', () => select(r.repo)); list.append(b);
    }
    text('published-count', count + ' / ' + state.manifest.repos.length);
    if (!count) list.append(element('p', 'empty', 'Aucun dépôt correspondant.'));
  }
  function renderDetail() {
    const host = $('published-detail'); host.replaceChildren();
    const r = selectedRepo();
    if (!r) { host.append(element('p', 'detail-placeholder', 'Choisis un dépôt pour consulter sa documentation publiée.')); return; }
    host.append(element('div', 'detail-eyebrow', 'DOCUMENTATION FIGÉE · VERSION DATÉE'));
    host.append(element('h3', '', r.repo.split('/')[1]));
    const role = element('p', 'detail-role'); role.append(localized(...status(r.status)));
    role.append(document.createTextNode(' · ' + (r.documents || []).length + ' documents · ' + (r.captured_at || '—')));
    host.append(role);
    const actions = element('div', 'detail-links');
    actions.append(link('https://github.com/' + r.repo, '↗ GitHub', 'primary-link'));
    actions.append(link('https://github.com/' + r.repo + '/wiki', '↗ Wiki GitHub', 'secondary-link'));
    host.append(actions);
    const provenance = element('div', 'publication-provenance');
    provenance.append(element('p', '', 'Commit source : ' + (r.revision || '—')));
    if (r.wiki_revision) provenance.append(element('p', '', 'Commit wiki : ' + r.wiki_revision));
    if (r.note) provenance.append(element('p', '', r.note));
    host.append(provenance);
    if (!r.documents?.length) { host.append(element('p', 'empty', 'Aucune copie documentaire disponible pour ce dépôt.')); return; }
    const field = element('div', 'publication-doc-search');
    const label = element('label', '', 'Filtrer les documents de cette application');
    label.htmlFor = 'published-doc-search';
    const search = element('input'); search.id='published-doc-search'; search.type='search'; search.placeholder='README, architecture, contrat…';
    field.append(label, search); host.append(field);
    const groups = element('div', 'publication-doc-groups'); host.append(groups);
    const buckets = [
      ['README', d => d.kind === 'repo' && /^readme/i.test(d.path.split('/').pop())],
      ['Documentation', d => d.kind === 'repo' && !/^readme/i.test(d.path.split('/').pop())],
      ['Wiki', d => d.kind === 'wiki'],
    ];
    const drawDocs = () => {
      groups.replaceChildren();
      const q = search.value.trim().toLocaleLowerCase();
      let total = 0;
      for (const [label, test] of buckets) {
        const all = r.documents.filter(test);
        if (!all.length) continue;
        const docs = all.filter(d => d.path.toLocaleLowerCase().includes(q));
        total += docs.length;
        if (q && !docs.length) continue;
        const details = element('details', 'publication-doc-group');
        details.open = !!q || label === 'README';
        const summary = element('summary'); summary.append(element('strong', '', label), element('span', 'repo-badge', docs.length + ' / ' + all.length));
        details.append(summary);
        const list = element('div', 'publication-doc-scroll');
        for (const d of docs) {
          const page = safePage(d.page); if (!page) continue;
          const row = element('div', 'publication-doc-row');
          row.append(link(page, d.path, 'publication-document-link'));
          row.append(element('small', '', 'SHA-256 ' + (d.sha256 || '').slice(0,16)));
          list.append(row);
        }
        details.append(list); groups.append(details);
      }
      if (!total) groups.append(element('p', 'empty', 'Aucun document correspondant.'));
    };
    search.addEventListener('input', drawDocs); drawDocs();
    const note = element('p', 'publication-disclaimer');
    note.append(localized('Une copie documentaire datée n’atteste ni test réussi ni certification.', 'A dated documentation copy does not prove passing tests or certification.'));
    host.append(note);
  }
  function filters() {
    const panel = $('published-filters'); panel.replaceChildren();
    for (const [id,fr,en] of [['all','Tous','All'],['captured','Capturés','Captured'],['retained','Conservés','Retained'],['unavailable','Indisponibles','Unavailable']]) {
      const btn = element('button','filter' + (state.status === id ? ' active' : ''));
      btn.type = 'button'; btn.setAttribute('aria-pressed', String(state.status === id));
      btn.append(localized(fr,en));
      btn.addEventListener('click', () => {state.status=id;filters();renderList();}); panel.append(btn);
    }
  }
  async function getJson(uri) {
    const response = await fetch(uri, {cache:'no-store'});
    if (!response.ok) throw new Error('HTTP ' + response.status);
    return response.json();
  }
  async function load() {
    try {
      let locationOfManifest = root.dataset.manifestUrl;
      if (root.dataset.pointerUrl) {
        const pointer = await getJson(root.dataset.pointerUrl);
        if (!release.test(pointer.release_id)) throw new Error('Invalid published release');
        locationOfManifest = 'releases/' + pointer.release_id + '/manifest.json';
      }
      const data = await getJson(locationOfManifest);
      if (!release.test(data.release_id) || !Array.isArray(data.repos)) throw new Error('Invalid snapshot manifest');
      state.manifest = data;
      text('published-id', data.release_id);
      text('published-date', data.published_at || '—');
      text('published-total', data.repos.length);
      text('published-selected', (data.selected || []).length);
      const first = new URLSearchParams(location.search).get('repo');
      const found = data.repos.find(r => r.repo === first || r.repo.split('/')[1].toLowerCase() === (first || '').toLowerCase());
      state.selected = found?.repo || data.repos.find(r => r.status === 'captured')?.repo || data.repos[0]?.repo;
      filters(); renderList(); renderDetail();
      text('published-load', 'Version publiée disponible');
    } catch (e) {
      text('published-load', 'Impossible de lire la version figée. Vérifie le déploiement GitHub Pages.');
      $('published-repo-list').append(element('p','empty','Manifeste indisponible.'));
    }
  }
  $('published-repo-search').addEventListener('input', event => { state.query=event.target.value.trim(); renderList(); });
  load();
})();
