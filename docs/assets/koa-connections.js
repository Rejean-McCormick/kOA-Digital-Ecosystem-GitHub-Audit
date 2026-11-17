(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  let language = params.get('lang') === 'en' ? 'en' : 'fr';
  let tab = 'all';
  let rows = [];
  const labels = {
    all: ['Tout','All'], journeys: ['Parcours','Journeys'], applications: ['Applications','Applications'], architecture: ['Chaînes fonctionnelles','Functional chains'], evidence: ['Preuves','Evidence'],
  };
  const translate = (fr, en) => language === 'en' ? en : fr;
  const el = (tag, className, value) => {
    const n = document.createElement(tag);
    if (className) n.className = className;
    if (value !== undefined) n.textContent = String(value);
    return n;
  };
  function link(text, href, external = false) {
    const a = el('a', '', text); a.href = href;
    if (external) { a.target = '_blank'; a.rel = 'noopener noreferrer'; }
    return a;
  }
  function setLanguage(lang) {
    language = lang === 'en' ? 'en' : 'fr';
    document.documentElement.lang = language;
    const url = new URL(location.href); url.searchParams.set('lang', language);
    try { history.replaceState(null, '', url.pathname + url.search + url.hash); } catch (_) { /* file and sandbox previews */ }
    document.querySelectorAll('[data-lang]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.lang === language)));
    $('back-graph').href = `index.html?lang=${language}#cartographie`;
    renderFilters(); renderCards();
  }
  function renderFilters() {
    const box = $('bridge-filters'); box.replaceChildren();
    for (const [key, [fr, en]] of Object.entries(labels)) {
      const button = el('button', '', translate(fr, en)); button.type = 'button';
      button.setAttribute('aria-pressed', String(key === tab));
      button.addEventListener('click', () => { tab = key; renderFilters(); renderCards(); });
      box.append(button);
    }
  }
  function renderCards() {
    const search = $('bridge-search').value.toLocaleLowerCase().trim();
    const items = rows.filter(item => (tab === 'all' || item.kind === tab) && (`${item.title} ${item.description} ${item.tags}`.toLocaleLowerCase().includes(search)));
    $('bridge-count').textContent = translate(`${items.length} correspondances`, `${items.length} connections`);
    const container = $('bridge-records'); container.replaceChildren();
    for (const item of items) {
      const card = el('article','bridge-card');
      card.append(el('span','kind',translate(...labels[item.kind])));
      card.append(el('h2','',item.title));card.append(el('p','',item.description));
      card.append(el('p','status',item.status));
      const actions = el('div','actions');
      actions.append(link(translate(item.external?'Voir la fiche ↗':'Voir la chaîne →',item.external?'Open record ↗':'Open chain →'),item.href,item.external));
      if (item.siteLink) actions.append(link(translate('Contexte sur initkoa.org ↗','Context on initkoa.org ↗'),item.siteLink,true));
      card.append(actions);
      if (item.related?.length) {
        const related = el('div','crosswalk',translate('Correspondances éditoriales proposées : ','Proposed editorial crosswalks: '));
        item.related.forEach(x => related.append(link(x.label,x.href,x.external)));
        card.append(related);
      }
      container.append(card);
    }
    if (!items.length) container.append(el('p','',translate('Aucun résultat.','No matching connections.')));
  }
  fetch('data/koa-connections.json', {cache:'no-store'}).then(response => {
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  }).then(data => {
    if(data.schema !== 'koa.connections.public-navigation.v1') throw new Error('Registry schema mismatch');
    const aliasByUrl = new Map(data.aliases.map(alias=>[alias.target,alias.path]));
    const repoById = new Map(data.repositories.map(repo=>[repo.id,repo]));
    rows = [
      ...data.paths.map(p => ({kind:'journeys',title:p.title_en,description:p.summary_en,
        status:translate('Parcours daté · pas une preuve d’exécution','Dated path · not execution evidence'),
        href:p.audit_url,external:true,tags:p.spine_repositories.join(' '),siteLink:`https://initkoa.org/connections?type=journeys&q=${encodeURIComponent(p.id.replace('path:',''))}`,
        related:data.crosswalks.filter(c=>c.to===p.id).map(c=>({label:c.from.replace('chain:',''),href:`https://initkoa.org/ecosystem/functional-chains/${c.from.replace('chain:','')}`,external:true}))
      })),
      ...data.repositories.map(r => ({kind:'applications',title:r.name,description:r.target_role||r.repository,
        status:r.in_audit_reference_inventory?translate('Inventaire de référence de l’audit','Audit reference inventory'):translate('Conception cible seulement · hors inventaire de référence','Target design only · outside audit reference inventory'),
        href:r.audit_app_url||'https://initkoa.org/ecosystem', external:true, tags:`${r.repository} ${r.target_family} ${r.id}`,
        siteLink:`https://initkoa.org/connections?repo=${encodeURIComponent(r.name)}`
      })),
      ...data.chains.map(c=>({kind:'architecture',title:`${c.id.replace('chain:','')} — ${c.title_en}`,description:c.outcome,
        status:translate('Conception cible · non qualifiée','Target design · not qualified'),
        href:`https://initkoa.org${c.href}`,external:true,tags:`${c.id} ${c.status_raw}`,
        related:data.crosswalks.filter(x=>x.from===c.id).map(x=>{
          const p=data.paths.find(p=>p.id===x.to);
          return {label:`${p?.title_en||x.to} (proposed)`,href:p?.audit_url||'index.html#cartographie',external:!!p};
        })
      })),
      {kind:'evidence',title:translate('Validations publiques','Public evidence checks'),description:translate('Dossiers datés et leur portée','Dated records and their scope'),
        status:translate('Voir les preuves d’origine','Read evidence at its source'),href:'index.html#validations',external:false,tags:'evidence validations tests reports',siteLink:'https://initkoa.org/evidence'},
    ];
    setLanguage(language);
  }).catch(error=>{
    $('bridge-count').textContent=translate('Répertoire indisponible en aperçu fichier. Servir docs/ avec un serveur HTTP local.','Directory unavailable as a file preview. Serve docs/ with a local HTTP server.');
    console.error('kOA Connections',error);
  });
  $('bridge-search').value = params.get('q') || params.get('repo') || '';
  $('bridge-search').addEventListener('input',renderCards);
  document.querySelectorAll('[data-lang]').forEach(button=>button.addEventListener('click',()=>setLanguage(button.dataset.lang)));
  document.documentElement.lang=language;
})();
