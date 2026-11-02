/* kOA Graph · owner-pinned, path-focused architecture explorer.
 * Views consume a frozen JSON publication. No live GitHub API and no private evidence.
 */
(() => {
  'use strict';
  const root = document.getElementById('focus-graph');
  if (!root) return;
  const $ = id => document.getElementById(id);
  const ui = {
    fr: {
      waiting: 'Chargement des parcours datés…', missing: 'Parcours non encore publiés. Dans GitHub Actions, publie le mode all après avoir poussé le registre source et le collecteur.',
      actions: 'Ouvrir la publication', pathways: 'Choisir un parcours', above: 'Environnement et appuis', below: 'Circuits complémentaires',
      status: 'État du lien', contract: 'Contrat / interface', evidence: 'Document de référence', scope: 'Portée et limite', owner: 'Dépôt propriétaire',
      frozen: 'Copie documentaire datée', pinned: 'Source au commit figé', source: 'Source GitHub', path: 'Parcours',
      noProof: 'Un parcours architectural n’atteste ni un déploiement ni une exécution globale en production.',
      more: 'Afficher les branches', fewer: 'Masquer les branches', click: 'Choisir une étape, une branche ou un contrat pour consulter son contexte.',
      provenance: 'Référentiel kOA figé au commit', statuses: {
        qualified_local: 'Qualifié localement', implemented_owner: 'Implémenté côté propriétaire', documented: 'Documenté',
        candidate: 'Candidat / à qualifier', optional: 'Facultatif / non imposé'
      },
    },
    en: {
      waiting: 'Loading dated architecture paths…', missing: 'Paths are not yet published. In GitHub Actions, publish mode all after pushing the owner registry and collector.',
      actions: 'Open publication workflow', pathways: 'Choose a path', above: 'Supporting systems', below: 'Complementary circuits',
      status: 'Relationship status', contract: 'Contract / interface', evidence: 'Source document', scope: 'Scope and limits', owner: 'Owner repository',
      frozen: 'Frozen documentation copy', pinned: 'Pinned commit source', source: 'GitHub source', path: 'Path',
      noProof: 'An architectural path does not prove a global production deployment or execution.',
      more: 'Show branches', fewer: 'Hide branches', click: 'Select a step, branch or contract to inspect its context.',
      provenance: 'kOA owner registry pinned at commit', statuses: {
        qualified_local: 'Qualified locally', implemented_owner: 'Implemented by owner', documented: 'Documented',
        candidate: 'Candidate / requires qualification', optional: 'Optional / not mandatory'
      }
    }
  };
  let data = null, manifest = null, pathId = null, chosen = null, branchesVisible = true;
  const t = obj => obj?.[language()] || obj?.fr || '';
  const language = () => window.kOA_I18N?.language === 'en' ? 'en' : 'fr';
  const labels = () => ui[language()];
  const elem = (tag, cls, text) => {
    const el = document.createElement(tag);
    if (cls) el.className = cls;
    if (text != null) el.textContent = text;
    return el;
  };
  const add = (container, ...children) => { children.forEach(x => container.appendChild(x)); return container; };
  const uniqueStatus = status => labels().statuses[status] || status;
  const safeRepo = repo => typeof repo === 'string' && /^[\w.-]+\/[\w.-]+$/.test(repo);
  const safePath = path => typeof path === 'string' && /^(?:docs|doc|documentation)\/[\w .\/-]+\.(?:md|mdx|txt|rst|adoc)$|^README\.md$/.test(path) && !path.split('/').includes('..');
  function evidenceLink(source) {
    if (!source || !safeRepo(source.repo) || !safePath(source.path)) return null;
    const record = manifest?.repos?.find(item => item.repo === source.repo);
    const d = record?.documents?.find(item => item.path === source.path && typeof item.page === 'string' &&
      item.page.startsWith('releases/' + manifest.release_id + '/repos/') && !item.page.includes('..'));
    if (d) return { href: 'publications/' + d.page, label: labels().frozen };
    const sha = (/^[a-f0-9]{40}$/.test(record?.revision || '') && record.revision) ||
      (source.repo === data?.owner_repository && data.owner_commit) || 'main';
    return { href: 'https://github.com/' + source.repo + '/blob/' + sha + '/' + source.path.split('/').map(encodeURIComponent).join('/'),
      label: sha === 'main' ? labels().source : labels().pinned };
  }
  function makeSource(source, parent) {
    const link = evidenceLink(source);
    if (!link) return;
    const a = elem('a','focus-source-link', link.label + ' ↗');
    a.href = link.href;
    a.target = '_blank'; a.rel = 'noopener noreferrer';
    const code = elem('code','',source.repo.split('/').pop() + ' / ' + source.path);
    add(parent, a, code);
  }
  // Navigation to owner records remains scoped to the application/validation view.
  // Do not equate a repository page with a proof of deployment.
  function linkToLocalView(parent, hash, value, repoName) {
    const a=elem('a','focus-context-link',value);
    a.href=hash;
    if (repoName) a.addEventListener('click',()=>{
      setTimeout(()=>{
        const search = document.getElementById(hash==='#validations'?'validation-search':'search');
        if(search){search.value=repoName;search.dispatchEvent(new Event('input',{bubbles:true}));}
      },30);
    });
    parent.appendChild(a);
  }
  function makeContextLinks(parent,repo) {
    const row=elem('div','focus-context-actions');
    const name=safeRepo(repo)?repo.split('/')[1]:'';
    linkToLocalView(row,'#apps',language()==='fr'?'Fiche application →':'Application profile →',name);
    linkToLocalView(row,'#validations',language()==='fr'?'Validations →':'Evidence checks →',name);
    const release=elem('a','focus-context-link',language()==='fr'?'Publications datées ↗':'Frozen publications ↗');
    release.href='publications/index.html';row.appendChild(release);
    parent.appendChild(row);
  }
  function renderDetails(path) {
    const holder = $('focus-detail'); holder.replaceChildren();
    const details = chosen?.value;
    const isBranch=chosen?.kind==='branch', isNode=chosen?.kind==='node';
    add(holder,elem('span','focus-eyebrow',language()==='fr'?'EXPLORER / ACCÉDER':'EXPLORE / OPEN'),
      elem('h3','',details?t(details.label):t(path.title)));
    if(!details){
      add(holder,elem('p','',t(path.summary)),elem('p','focus-caution',labels().click));
      makeContextLinks(holder,null);
      add(holder,elem('p','focus-caution',labels().noProof));
      return;
    }
    if(isNode){
      add(holder,elem('p','',t(details.description)),elem('p','focus-caution',labels().noProof));
      if(safeRepo(details.repo)){
        const a=elem('a','focus-source-link',details.repo+' ↗');
        a.href='https://github.com/'+details.repo;a.target='_blank';a.rel='noopener noreferrer';
        add(holder,elem('h4','',labels().owner),a);
      }
      const adjacent=path.spine_links.filter(l=>l.from===details.id||l.to===details.id);
      if(adjacent.length){holder.appendChild(elem('h4','',labels().evidence));adjacent.forEach(l=>makeSource(l.evidence,holder));}
      makeContextLinks(holder,details.repo);
      return;
    }
    holder.appendChild(elem('p','focus-status focus-'+details.status,uniqueStatus(details.status)));
    add(holder,elem('p','',t(details.description||details.label)),elem('p','focus-caution',labels().noProof));
    if(isBranch){
      const steps=elem('div','focus-detail-steps');
      for(const step of details.steps){
        const line=elem('div','focus-detail-step');
        add(line,elem('strong','',t(step.label)),elem('small','',t(step.description)));
        if(safeRepo(step.repo)){
          const a=elem('a','focus-source-link',language()==='fr'?'Dépôt ↗':'Repository ↗');
          a.href='https://github.com/'+step.repo;a.target='_blank';a.rel='noopener noreferrer';line.appendChild(a);
        }
        steps.appendChild(line);
      }
      holder.appendChild(steps);
    }
    if(details.contract){add(holder,elem('h4','',labels().contract),elem('code','focus-contract',details.contract));}
    add(holder,elem('h4','',labels().evidence));makeSource(details.evidence,holder);
    const repo = isBranch ? (details.steps.find(step=>safeRepo(step.repo))||{}).repo : null;
    makeContextLinks(holder,repo);
  }
  function focusButton(value, cls, kind, path) {
    const button=elem('button',cls);
    button.type='button';
    button.setAttribute('aria-pressed',String(chosen?.kind===kind && chosen?.value===value));
    button.addEventListener('click',()=>{chosen={kind,value}; renderPath(path);});
    return button;
  }
  function renderBranch(branch,path) {
    const btn=focusButton(branch,'focus-branch focus-'+branch.status,'branch',path);
    add(btn,elem('span','focus-status focus-'+branch.status,uniqueStatus(branch.status)),
      elem('strong','',t(branch.label)),elem('small','',branch.steps.map(n=>t(n.label)).join(' → ')));
    return btn;
  }
  function renderPath(path) {
    const routes=$('focus-route-chooser');routes.replaceChildren();
    routes.appendChild(elem('span','focus-eyebrow',labels().pathways));
    const choices=elem('div','focus-route-cards');
    data.paths.forEach((p,index)=>{
      const btn=elem('button','focus-route-button'+(p.id===path.id?' active':''));
      btn.type='button';btn.setAttribute('aria-pressed',String(p.id===path.id));
      add(btn,elem('span','focus-route-number',String(index+1).padStart(2,'0')),
        elem('strong','',t(p.title)),elem('small','',t(p.summary)));
      btn.addEventListener('click',()=>{
        pathId=p.id;chosen=null;
        const url=new URL(location.href);
        url.searchParams.set('parcours',p.id);
        try{history.replaceState(null,'',url.pathname+url.search+'#cartographie');}catch(_){/* restricted previews */}
        renderPath(p);
      });
      choices.appendChild(btn);
    });
    routes.appendChild(choices);
    $('focus-title').textContent=t(path.title);
    $('focus-summary').textContent=t(path.summary);
    $('focus-disclosure').textContent=branchesVisible?labels().fewer:labels().more;
    $('focus-disclosure').setAttribute('aria-pressed',String(branchesVisible));
    const board=$('focus-board');board.replaceChildren();
    path.spine.forEach((node,i)=>{
      const stage=elem('div','focus-vertical-stage');
      const left=elem('div','focus-vertical-branches focus-left');
      const right=elem('div','focus-vertical-branches focus-right');
      if(branchesVisible){
        path.branches.filter(b=>b.anchor===i&&b.side==='above').forEach(b=>left.appendChild(renderBranch(b,path)));
        path.branches.filter(b=>b.anchor===i&&b.side==='below').forEach(b=>right.appendChild(renderBranch(b,path)));
      }
      const core=elem('div','focus-vertical-core');
      const btn=focusButton(node,'focus-spine-node','node',path);
      add(btn,elem('span','focus-spine-index',String(i+1).padStart(2,'0')),
        elem('strong','',t(node.label)),elem('small','',t(node.description)));
      core.appendChild(btn);
      add(stage,left,core,right);board.appendChild(stage);
      const link=path.spine_links[i];
      if(link){
        const flow=elem('div','focus-vertical-flow');
        const edge=focusButton(link,'focus-flow-link focus-'+link.status,'link',path);
        add(edge,elem('span','focus-down','↓'),elem('span','focus-flow-label',t(link.label)),
          elem('small','',link.contract||uniqueStatus(link.status)));
        flow.appendChild(edge);board.appendChild(flow);
      }
    });
    const legend=$('focus-legend');legend.replaceChildren();
    ['qualified_local','implemented_owner','documented','candidate','optional'].forEach(status=>
      legend.appendChild(elem('span','focus-status focus-'+status,uniqueStatus(status))));
    renderDetails(path);
  }
  // Frozen source paths win. Local add-ons are clearly identified as previews.
  // No commit, backend mutation, or hidden writes are performed by this reader.
  let localOverlayIds = [], referencePreview = false;
  function addGraphNavigation() {
    const apps = document.querySelector('.rail a[data-nav="applications"]');
    if (!apps || document.querySelector('[data-graph-nav]')) return;
    const link = elem('a','workspace-nav','');
    link.href='#cartographie';link.dataset.graphNav='true';
    link.append(elem('span','', '⬡'));
    link.append(document.createTextNode(' '));
    link.append(elem('span','',language()==='fr'?'Graphe':'Graph'));
    link.setAttribute('aria-label',language()==='fr'?'Explorer les cinq parcours kOA':'Explore five kOA paths');
    const first = document.querySelector('.rail a[data-nav="validations"]');
    if(first)first.insertAdjacentElement('beforebegin',link);else apps.insertAdjacentElement('afterend',link);
    const appsNav=document.querySelector('.rail a[data-nav="applications"]');
    const update = () => {
      const active = location.hash==='#cartographie';
      // The audit's asynchronous refresh can reselect Applications after
      // this menu has initialized. Keep one active entry for this route.
      if (link.classList.contains('active') !== active) link.classList.toggle('active',active);
      if (active) {
        if (link.getAttribute('aria-current')!=='page') link.setAttribute('aria-current','page');
        if (appsNav?.classList.contains('active')) appsNav.classList.remove('active');
        if (appsNav?.hasAttribute('aria-current')) appsNav.removeAttribute('aria-current');
      } else if (link.hasAttribute('aria-current')) {
        link.removeAttribute('aria-current');
      }
    };
    // Observe only Applications, avoiding changes to the audit engine.
    // Idempotent updates prevent observer loops.
    if (appsNav) new MutationObserver(update).observe(appsNav, {
      attributes:true, attributeFilter:['class','aria-current']
    });
    window.addEventListener('hashchange',update);
    update();
  }
  function provenanceText(){
    const fr=language()==='fr';
    const base = data?.owner_commit
      ? labels().provenance+' '+data.owner_commit.slice(0,12)+' · '+data.source_date
      : (fr?'Aperçu local des parcours de référence (non figé)':'Local reference paths preview (not frozen)');
    return base+(localOverlayIds.length
      ? (fr?' · Parcours additionnels non figés : ':' · Additional non-frozen paths: ')+localOverlayIds.join(', ')
      : '')+(referencePreview?(fr?' · Référence locale':' · Local reference'):'');
  }
  async function getJson(path) {
    try{const r=await fetch(path,{cache:'no-store'});return r.ok?await r.json():null;}catch(_){return null;}
  }
  const validPath = p => p && typeof p.id==='string' && /^(?:decision|knowledge|publication|koali|ekole)$/.test(p.id)
       && p.title?.fr && p.title?.en && Array.isArray(p.spine) && p.spine.length>=3
       && Array.isArray(p.spine_links) && p.spine_links.length===p.spine.length-1
       && Array.isArray(p.branches);
  async function load(){
    addGraphNavigation();
    const status=$('focus-loading'); status.textContent=labels().waiting;
    const [frozen,preview,koali,ekole]=await Promise.all([
      getJson('data/focus-paths.json'),
      getJson('inventory/graph-paths-local-base.v1.json'),
      getJson('inventory/graph-path-koali.v1.json'),
      getJson('inventory/graph-path-ekole.v1.json')
    ]);
    const validFrozen=frozen?.format==='koa.graph.focus.public.v1'
      && Array.isArray(frozen.paths) && /^[a-f0-9]{40}$/.test(frozen.owner_commit);
    if (validFrozen) data={...frozen,paths:frozen.paths.filter(validPath)};
    else if(preview?.format==='koa.graph.focus.preview.v1' && Array.isArray(preview.paths)){
      data={format:'koa.graph.focus.preview.v1',owner_commit:null,source_date:'2026-11-01',
        paths:preview.paths.filter(validPath)};
      referencePreview=true;
    } else data={format:'koa.graph.focus.preview.v1',owner_commit:null,source_date:'2026-11-01',paths:[]};
    for(const candidate of [koali,ekole]){
      if (validPath(candidate) && !data.paths.some(p=>p.id===candidate.id)) {
        data.paths.push(candidate);localOverlayIds.push(candidate.id);
      }
    }
    if(!data.paths.length){
      status.textContent=labels().missing;return;
    }
    if(validFrozen){
      try{
        const pointer=await getJson('data/publication-current.json');
        if (/^[0-9]{8}T[0-9]{6}Z(?:-[0-9]+(?:-[0-9]+)?)?$/.test(pointer?.release_id||'')) {
          const m=await getJson('publications/releases/'+pointer.release_id+'/manifest.json');
          if(m?.release_id===pointer.release_id)manifest=m;
        }
      }catch(_){/* Dated source links remain optional. */}
    }
    status.textContent=provenanceText();
    $('focus-interactive').hidden=false;
    const requested=new URLSearchParams(location.search).get('parcours');
    pathId=data.paths.some(p=>p.id===requested)?requested:data.paths[0].id;
    renderPath(data.paths.find(p=>p.id===pathId));
  }
  $('focus-disclosure')?.addEventListener('click',()=>{
    branchesVisible=!branchesVisible;
    const path=data?.paths.find(p=>p.id===pathId);
    if(path)renderPath(path);
  });
  window.addEventListener('koa:languagechange',()=>{
    const nav=document.querySelector('[data-graph-nav]');
    if(nav){nav.lastElementChild.textContent=language()==='fr'?'Graphe':'Graph';nav.setAttribute('aria-label',language()==='fr'?'Explorer les cinq parcours kOA':'Explore five kOA paths');}
    if(data){$('focus-loading').textContent=provenanceText();
      const path=data.paths.find(p=>p.id===pathId);if(path)renderPath(path);}
  });
  load();
})();
