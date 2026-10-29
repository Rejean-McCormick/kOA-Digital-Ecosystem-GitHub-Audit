(() => {
  'use strict';
  const $ = (id) => document.getElementById(id);
  let snapshots = [];
  let mode = 'LOCAL_OBSERVE';
  const labels = {
    WORKFLOW_UNPINNED_ACTION:'Références Actions par tags (piste de durcissement)',
    LARGE_FILE_NOT_INSPECTED:'Gros fichiers hors inspection (limite du scan)',
    SENSITIVE_FILENAME:'Noms de configuration à vérifier (pas un incident)',
    PYTHON_SHELL_TRUE:'Utilisations de shell=True',
    PYTHON_PICKLE_LOAD:'Utilisations de pickle.load',
    PRIVATE_KEY_MATERIAL:'Motif de clé privée potentielle',
    PYTHON_SSL_VERIFY_DISABLED:'Ancienne règle TLS (faux positifs connus possibles)',
    PYTHON_TLS_BYPASS:'Contournement TLS potentiel'
  };

  function text(id, value) { const el=$(id); if(el) el.textContent = String(value); }
  function dom(tag, cls, value) { const el = document.createElement(tag); if(cls)el.className=cls; if(value !== undefined)el.textContent=String(value); return el; }
  function number(n) {return Number(n || 0).toLocaleString('fr-CA');}
  function shortBytes(bytes){ const mb=(Number(bytes||0)/1000000); return mb>=100 ? Math.round(mb)+' MB' : mb.toFixed(1)+' MB'; }
  function day(s) {try{return new Intl.DateTimeFormat('fr-CA',{dateStyle:'medium',timeStyle:'short',timeZone:'America/Toronto'}).format(new Date(s));}catch(e){return s;}}
  function selected(){return snapshots.filter(s=>s.mode===mode).sort((a,b)=>a.at.localeCompare(b.at));}
  function latest(){const arr=selected();return arr.length?arr[arr.length-1]:null;}
  function metric(i,label,value,extra){text('metric-label-'+i,label);text('metric-'+i,value); if(i>1) text('metric-extra-'+i,extra || '');}
  function row(parent,label,value){const r=dom('div','coverage-row');r.append(dom('span','',label),dom('strong','',number(value)));parent.append(r);}
  function ring(percent,caption){$('ring').style.setProperty('--pct',Math.max(0,Math.min(100,percent))+'%');text('ring-value',percent+' %');text('ring-caption',caption);}

  function statRows(targetId, rows){
    const target=$(targetId); target.replaceChildren();
    if(!rows.length){ target.append(dom('div','empty-state','Aucune donnée.')); return; }
    rows.forEach(([label,val])=>{
      const r=dom('div','stat-row');
      r.append(dom('span','',label), dom('strong','',val));
      target.append(r);
    });
  }

  function miniBars(targetId, items){
    const target=$(targetId); target.replaceChildren();
    if(!items.length){ return; }
    const max=Math.max(1,...items.map(i=>i.value));
    items.forEach(item=>{
      const row=dom('div','mini-bar-row');
      row.append(dom('span','',item.label), dom('strong','',number(item.value)));
      const track=dom('div','mini-bar-track');
      const fill=dom('div','mini-bar-fill');
      fill.style.width=(100*item.value/max)+'%';
      track.append(fill); row.append(track); target.append(row);
    });
  }

  function bars(items){
    const target=$('signal-list'); target.replaceChildren();
    if(!items.length){target.append(dom('div','empty-state','Aucune donnée pour cette catégorie.'));return;}
    const max=Math.max(1,...items.map(i=>i.count));
    items.forEach(item=>{const e=dom('div','signal'),top=dom('div','signal-top'),tr=dom('div','bar-track'),fill=dom('div','bar-fill');top.append(dom('span','',item.name),dom('strong','',number(item.count)));fill.style.width=(100*item.count/max)+'%';tr.append(fill);e.append(top,tr);target.append(e);});
  }

  function trend(data,read,label){
    text('history-count',data.length+' campagne'+(data.length>1?'s':''));text('trend-legend-title',label);
    const place=$('trend-visual');place.replaceChildren();
    if(!data.length){place.append(dom('div','empty-state','Aucune campagne publiée dans cette catégorie.'));return;}
    const w=640,h=215,padX=36,padY=26,vals=data.map(read),ceiling=Math.max(1,...vals);const x=i=>padX+(w-2*padX)*(data.length===1?.5:i/(data.length-1));const y=v=>h-padY-(h-2*padY)*v/ceiling;
    const ns='http://www.w3.org/2000/svg';const svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox',`0 0 ${w} ${h}`);svg.setAttribute('role','img');svg.setAttribute('aria-label',label+' : '+vals.join(', '));
    for(let i=0;i<4;i++){let value=ceiling*i/3;const line=document.createElementNS(ns,'line');line.setAttribute('x1',padX);line.setAttribute('x2',w-padX);line.setAttribute('y1',y(value));line.setAttribute('y2',y(value));line.setAttribute('stroke','#355a56');line.setAttribute('stroke-dasharray','4 5');svg.append(line);const tx=document.createElementNS(ns,'text');tx.textContent=Math.round(value).toString();tx.setAttribute('x','1');tx.setAttribute('y',y(value)+4);tx.setAttribute('fill','#7ca09b');tx.setAttribute('font-size','11');svg.append(tx);} 
    const poly=document.createElementNS(ns,'polyline');poly.setAttribute('points',vals.map((v,i)=>`${x(i)},${y(v)}`).join(' '));poly.setAttribute('fill','none');poly.setAttribute('stroke','#68c4bd');poly.setAttribute('stroke-width','3');poly.setAttribute('stroke-linejoin','round');svg.append(poly);
    vals.forEach((v,i)=>{const c=document.createElementNS(ns,'circle');c.setAttribute('cx',x(i));c.setAttribute('cy',y(v));c.setAttribute('r',data.length<24?'5':'3');c.setAttribute('fill','#9ce1db');c.setAttribute('stroke','#0f1b1a');c.setAttribute('stroke-width','2');const title=document.createElementNS(ns,'title');title.textContent=day(data[i].at)+' : '+v;c.append(title);svg.append(c);});
    [0,data.length-1].filter((v,i,a)=>a.indexOf(v)===i).forEach(i=>{const tx=document.createElementNS(ns,'text');tx.textContent=new Date(data[i].at).toLocaleDateString('fr-CA',{month:'short',day:'numeric',year:'numeric',timeZone:'UTC'});tx.setAttribute('x',x(i));tx.setAttribute('y',h-3);tx.setAttribute('text-anchor',i===0&&data.length>1?'start':i===data.length-1&&data.length>1?'end':'middle');tx.setAttribute('fill','#90aba7');tx.setAttribute('font-size','11');svg.append(tx);});place.append(svg);
  }

  function renderLocal(d){
    const statuses=d.statuses||{};
    const controls=d.controls||{};
    const size=d.size||{};
    const quality=d.quality||{};
    const structuring=d.structuring||{};
    const findingsTotal=Object.values(d.findings||{}).reduce((a,b)=>a+b,0);
    metric(1,'Dépôts de référence',number(d.declared), '');
    metric(2,'Présents et audités',`${number(d.inventory_scanned)} / ${number(d.declared)}`,'Couverture réelle de l’inventaire');
    metric(3,'Profils ingénierie disponibles',`${number(d.engineering_profiles||0)} / ${number(d.declared)}`,'Mesures issues de snapshots');
    metric(4,'Dépôts avec workflows',number(controls.workflows||0),'Configuration détectée, pas test exécuté');

    text('coverage-title','État des inspections');
    ring(d.declared?Math.round(100*d.inventory_scanned/d.declared):0,'inventaire audité');
    const side=$('coverage-list');side.replaceChildren();
    row(side,'Inspection limitée',statuses.PARTIAL||0); row(side,'Pistes à interpréter',statuses.REVIEW||0); row(side,'Observations informatives',statuses.OBSERVED_INFORMATIONAL||0); row(side,'Aucun motif détecté',statuses.INSPECTED_NO_PATTERN_MATCH||0); row(side,'Copies locales multiples',d.ambiguous||0);
    text('coverage-note','Les copies locales et les limites d’inspection ne réduisent pas la qualité d’un dépôt.');

    statRows('completion-list',[
      ['Repos de l’inventaire présents localement', `${number(d.inventory_scanned)} / ${number(d.declared)}`],
      ['Profils d’ingénierie disponibles', number(d.engineering_profiles||0)],
      ['Dépôts avec workflows détectés', number(controls.workflows||0)],
      ['Dépôts avec manifests de dépendances', number(controls.dependency_manifests||0)],
    ]);
    text('completion-note','Ces nombres décrivent les preuves disponibles, pas un taux de complétion ni un certificat.');

    statRows('size-list',[
      ['Fichiers trouvés dans les dépôts audités', number(size.files_enumerated||0)],
      ['Fichiers effectivement inspectés', number(size.files_inspected||0)],
      ['Volume inspecté', shortBytes(size.bytes_inspected||0)],
      ['Taille médiane par dépôt', number(size.median_repo_files||0)+' fichiers'],
    ]);
    miniBars('size-buckets',[
      {label:'Micro (<100 fichiers)', value:((size.size_buckets||{}).micro||0)},
      {label:'Moyen (100–299)', value:((size.size_buckets||{}).medium||0)},
      {label:'Grand (300–999)', value:((size.size_buckets||{}).large||0)},
      {label:'Très grand (1000+)', value:((size.size_buckets||{}).xlarge||0)},
    ]);

    statRows('quality-list',[
      ['Workflows détectés', number(controls.workflows||0)],
      ['Manifestes de dépendances', number(controls.dependency_manifests||0)],
      ['Dependabot configuré', number(controls.dependabot||0)],
      ['CodeQL configuré localement', number(controls.codeql||0)],
    ]);
    miniBars('quality-buckets',[
      {label:'Workflows', value:(controls.workflows||0)},
      {label:'Dépendances', value:(controls.dependency_manifests||0)},
      {label:'Dependabot', value:(controls.dependabot||0)},
      {label:'CodeQL', value:(controls.codeql||0)},
    ]);

    text('signals-title','Observations techniques à interpréter');
    text('signal-note','Les noms, doublons, tailles et motifs de scan ne sont jamais des conclusions négatives par eux-mêmes. Les faux positifs historiques restent des pistes non qualifiées.');
    bars(Object.entries(d.findings||{}).sort((a,b)=>b[1]-a[1]).map(([name,count])=>({name:labels[name]||'Catégorie contrôlée',count})));
    text('caveat',`Ce rapport contient ${number(findingsTotal)} motifs heuristiques historiques, non des failles confirmées. Une certification exige des preuves et une validation par portée.`);
    text('mode-description','LOCAL_OBSERVE · Mesures d’ingénierie factuelles · aucune notation automatique');
    trend(selected(),s=>s.inventory_scanned||0,'Dépôts audités (inventaire)');
  }

  function renderRemote(d){
    const vis=d.visibility||{};
    const flows=d.flows||{};
    const alerts=d.alerts||{};
    const quality=d.quality||{};
    metric(1,'Dépôts de référence',number(d.declared), '');
    metric(2,'Métadonnées GitHub visibles',`${number(d.observed)} / ${number(d.declared)}`,'Selon la disponibilité de l’API');
    metric(3,'CI récentes en échec',number((d.ci||{}).failure||0),'Échantillon observé');
    metric(4,'Workflows observables',number(flows.workflows_visible||0),'Configurations présentes dans les réponses');

    text('coverage-title','Accès à GitHub');
    ring(d.declared?Math.round(100*d.observed/d.declared):0,'métadonnées observées');
    const side=$('coverage-list');side.replaceChildren();
    row(side,'Métadonnées accessibles',d.observed||0); row(side,'Statut inconnu',d.unknown||0); row(side,'CI réussies',((d.ci||{}).success||0)); row(side,'CI en échec',((d.ci||{}).failure||0));
    text('coverage-note','Une couverture API incomplète signifie qu’une partie de l’écosystème reste non qualifiée.');

    statRows('completion-list',[
      ['Dépôts observés via GitHub', `${number(vis.observed||d.observed||0)} / ${number(d.declared)}`],
      ['Dépôts encore inconnus', number(vis.unknown||d.unknown||0)],
      ['Workflows visibles', number(flows.workflows_visible||0)],
      ['Runs récents visibles', number(flows.runs_visible||0)],
    ]);
    text('completion-note','Cette vue mesure surtout la visibilité GitHub, pas la qualité intrinsèque du code.');

    statRows('size-list',[
      ['Alertes Dependabot observées (minimum)', number((alerts.dependabot||{}).observed_minimum||0)],
      ['Alertes code scanning observées (minimum)', number((alerts.code_scanning||{}).observed_minimum||0)],
      ['Alertes secret scanning observées (minimum)', number((alerts.secret_scanning||{}).observed_minimum||0)],
      ['CodeQL au statut inconnu', number(d.codeql_unknown||0)],
    ]);
    miniBars('size-buckets',[
      {label:'Dépôts observés', value:(vis.observed||d.observed||0)},
      {label:'Dépôts inconnus', value:(vis.unknown||d.unknown||0)},
      {label:'Workflows visibles', value:(flows.workflows_visible||0)},
      {label:'Runs visibles', value:(flows.runs_visible||0)},
    ]);

    statRows('quality-list',[
      ['CI récentes réussies', number((d.ci||{}).success||0)],
      ['CI récentes en échec', number((d.ci||{}).failure||0)],
      ['Sources d’alertes à couverture complète', number(quality.alerts_complete||0)],
      ['Sources d’alertes à couverture partielle', number(quality.alerts_partial||0)],
    ]);
    miniBars('quality-buckets',[
      {label:'Dependabot complet', value:(alerts.dependabot||{}).complete ? 1 : 0},
      {label:'Code scanning complet', value:(alerts.code_scanning||{}).complete ? 1 : 0},
      {label:'Secret scanning complet', value:(alerts.secret_scanning||{}).complete ? 1 : 0},
    ]);

    text('signals-title','Alertes de sécurité : visibilité disponible');
    text('signal-note','Les nombres présentés ci-dessous sont seulement des minimums observés. Un zéro n’implique pas l’absence d’alertes.');
    bars([
      {name:'Dependabot · '+((alerts.dependabot||{}).complete?'complet':'partiel / inconnu'), count:(alerts.dependabot||{}).observed_minimum||0},
      {name:'Code scanning · '+((alerts.code_scanning||{}).complete?'complet':'partiel / inconnu'), count:(alerts.code_scanning||{}).observed_minimum||0},
      {name:'Secret scanning · '+((alerts.secret_scanning||{}).complete?'complet':'partiel / inconnu'), count:(alerts.secret_scanning||{}).observed_minimum||0},
    ]);
    text('caveat','La vue GitHub dépend de la disponibilité de l’API. Les zéros et « inconnu » reflètent souvent un manque de visibilité, pas une absence de problèmes.');
    text('mode-description','OBSERVE · Visibilité GitHub et éléments de qualification, non certificatifs');
    trend(selected(),s=>s.observed||0,'Métadonnées accessibles');
  }

  function clearInsightPanels(){
    ['completion-list','size-list','quality-list','size-buckets','quality-buckets'].forEach(id=>$(id).replaceChildren());
  }

  function render(){
    const d=latest();
    document.querySelectorAll('.mode-toggle button').forEach(b=>{const active=b.id===(mode==='LOCAL_OBSERVE'?'mode-local':'mode-github');b.classList.toggle('is-active',active);b.setAttribute('aria-pressed',String(active));});
    if(!d){
      for(let i=1;i<=4;i++)metric(i,'Données indisponibles','—','');
      text('updated','Aucun rapport dans cette catégorie');
      $('trend-visual').replaceChildren(dom('div','empty-state','Publie un rapport pour commencer.'));
      $('signal-list').replaceChildren(); $('coverage-list').replaceChildren(); clearInsightPanels();
      ring(0,'aucun rapport'); return;
    }
    text('updated','Rapport du '+day(d.at));
    if(mode==='LOCAL_OBSERVE') renderLocal(d); else renderRemote(d);
    text('footer-version','Format v1 · dashboard enrichi');
  }

  async function refresh(){
    text('connection','Chargement…');
    try{
      const r=await fetch('data/dashboard.json?time='+Date.now(),{cache:'no-store'});
      if(!r.ok) throw Error('HTTP '+r.status);
      const data=await r.json();
      if(data.format!=='koa_audit.dashboard.v1'||!Array.isArray(data.snapshots)) throw Error('Format inconnu');
      snapshots=data.snapshots.filter(x=>x&&(x.mode==='LOCAL_OBSERVE'||x.mode==='OBSERVE'));
      text('connection','Données publiées');
      render();
    }catch(error){
      text('connection','Données indisponibles'); text('updated','Erreur de chargement');
      const tip=dom('div','error-note','Impossible de charger les données. En aperçu local, utilise le bouton intégré de l’application.');
      $('trend-visual').replaceChildren(tip); clearInsightPanels();
    }
  }

  $('mode-local').addEventListener('click',()=>{mode='LOCAL_OBSERVE';render();});
  $('mode-github').addEventListener('click',()=>{mode='OBSERVE';render();});
  $('refresh').addEventListener('click',refresh);
  refresh();
  setInterval(refresh,180000);
})();
