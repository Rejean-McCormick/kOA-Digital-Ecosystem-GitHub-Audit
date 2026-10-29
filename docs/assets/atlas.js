(() => {
  'use strict';
  const $=id=>document.getElementById(id);
  const count=n=>Number(n||0).toLocaleString('fr-CA');
  const stages=[['specified','Spécifié'],['implemented','Implémenté'],['qualified','Qualifié'],['integrated','Intégré'],['production','Production']];
  const positions={
    konnaxion:[12,14],orgo:[37,14],encyklopedia:[37,37],daat:[59,37],
    kristal:[82,37],linux:[82,65],spaces:[82,88],ik:[12,70],
    architect:[37,88],orchestrator:[59,88],sentient:[59,13],skope:[12,37]
  };
  let atlas=null, localAudit=null, qualification=null, activeRepo=null, activeGroup='all', searchText='', detailTab='overview';
  function el(tag,cls,content){const x=document.createElement(tag);if(cls)x.className=cls;if(content!==undefined)x.textContent=String(content);return x;}
  function link(href,text,klass){const a=el('a',klass,text);a.href=href;return a;}
  function repoByName(name){return atlas.repositories.find(r=>r.repo===name);}
  function statusFor(repo,stage){return qualification?.repositories?.[repo]?.[stage]||'Non évalué';}
  function createStageBars(){
    const holder=$('stage-chart');holder.replaceChildren();
    const data=atlas?.repositories||[],total=data.length;
    stages.forEach(([id,label])=>{
      const counts={'Étayé par preuve':0,'À documenter':0,'Non applicable':0,'Non évalué':0};
      data.forEach(r=>{const v=statusFor(r.repo,id);counts[v in counts?v:'Non évalué']++;});
      const row=el('div','stage-row'),left=el('div','stage-label',label),meter=el('div','stage-meter');
      meter.setAttribute('aria-label',`${label} : ${counts['Étayé par preuve']} étayés par preuve sur ${total}, ${counts['À documenter']} à documenter`);
      for(const [key,klass] of [['Étayé par preuve','stage-evidence'],['À documenter','stage-pending'],['Non applicable','stage-na']]){
        const width=counts[key]*100/Math.max(1,total);
        if(width>0){const span=el('span',klass);span.style.width=width+'%';meter.append(span);}
      }
      const meta=el('div','stage-meta',qualification?`${counts['Étayé par preuve']} preuves · ${counts['Non évalué']} non évalués`:'Non publié / non évalué');
      row.append(left,meter,meta);holder.append(row);
    });
    if(qualification){
      let assessed=0,evidenced=0;
      for(const r of data){for(const [key] of stages){let status=statusFor(r.repo,key);if(status!=='Non évalué')assessed++;if(status==='Étayé par preuve')evidenced++;}}
      $('kpi-qualification').textContent=`${count(assessed)} / ${count(total*5)}`;
      $('kpi-qualification-note').textContent=`Jalons examinés · ${count(evidenced)} étayés par preuve (état local)`;
      $('qual-mode').textContent='Données de qualification locales, conservées sur ton PC';
    }else{
      $('kpi-qualification').textContent='Non publié';
      $('kpi-qualification-note').textContent='Ouvrir via l’application pour voir les états privés';
      $('qual-mode').textContent='Qualification privée non exportée sur GitHub Pages';
    }
  }
  function svgLine(from,to,proposed){
    const a=positions[from],b=positions[to];if(!a||!b)return null;
    const svgNS='http://www.w3.org/2000/svg', path=document.createElementNS(svgNS,'path');
    const x1=a[0]*11.5,y1=a[1]*6.4,x2=b[0]*11.5,y2=b[1]*6.4;
    // Keep connections behind interactive cards, curve to reveal branches.
    const my=(y1+y2)/2, mx=(x1+x2)/2;
    const d=Math.abs(y2-y1)>70?`M ${x1} ${y1} C ${x1} ${my}, ${x2} ${my}, ${x2} ${y2}`:`M ${x1} ${y1} C ${mx} ${y1}, ${mx} ${y2}, ${x2} ${y2}`;
    path.setAttribute('d',d);path.setAttribute('fill','none');path.setAttribute('stroke',proposed?'#d7b77c':'#5eaa9b');path.setAttribute('stroke-width',proposed?'2':'2.3');path.setAttribute('opacity',proposed?'.65':'.69');
    if(proposed)path.setAttribute('stroke-dasharray','6 6');
    path.setAttribute('marker-end',proposed?'url(#arrow-proposed)':'url(#arrow)');
    return path;
  }
  function drawMap(){
    const svg=$('map-lines'),holder=$('map-nodes');svg.replaceChildren();holder.replaceChildren();
    const svgNS='http://www.w3.org/2000/svg';const defs=document.createElementNS(svgNS,'defs');
    for(const [id,color] of [['arrow','#61baaa'],['arrow-proposed','#dbbb85']]){
      const marker=document.createElementNS(svgNS,'marker');marker.setAttribute('id',id);marker.setAttribute('markerWidth','7');marker.setAttribute('markerHeight','7');marker.setAttribute('refX','6');marker.setAttribute('refY','3.5');marker.setAttribute('orient','auto');
      const arrow=document.createElementNS(svgNS,'path');arrow.setAttribute('d','M 0 0 L 7 3.5 L 0 7 z');arrow.setAttribute('fill',color);marker.append(arrow);defs.append(marker);
    }
    svg.append(defs);
    for(const c of atlas.links){const path=svgLine(c.from,c.to,c.status==='proposed');if(path){const title=document.createElementNS(svgNS,'title');title.textContent=c.label+(c.status==='proposed'?' (proposé)':'');path.append(title);svg.append(path);}}
    for(const n of atlas.systems){
      const pt=positions[n.id];if(!pt)continue;
      const button=el('button','map-node');button.type='button';button.style.left=pt[0]+'%';button.style.top=pt[1]+'%';button.dataset.repo=n.repo;
      button.title=n.role+' — ouvrir la fiche';
      button.append(el('strong','',n.label),el('small','',n.role));
      const r=repoByName(n.repo);if(r?.report)button.append(el('span','profile-dot','● Profil'));
      button.addEventListener('click',()=>selectRepo(n.repo,true));holder.append(button);
    }
  }
  function drawConstellation(){
    const holder=$('constellation');holder.replaceChildren();
    for(const group of atlas.groups){
      const repos=atlas.repositories.filter(r=>r.group===group.id);
      if(!repos.length)continue;
      const section=el('section','constellation-group');
      const heading=el('h3','',group.label);heading.append(el('small','',`${repos.length} dépôts`));section.append(heading);
      const chips=el('div','constellation-items');
      for(const r of repos){
        const btn=el('button','constellation-item'+(r.repo===activeRepo?' selected':''));btn.type='button';btn.dataset.repo=r.repo;
        btn.append(document.createTextNode(r.name));
        if(r.report||r.has_local_profile)btn.append(el('span','star','●'));
        btn.title=(r.report?'Engineering Profile disponible · ':'')+'Ouvrir la fiche '+r.name;
        btn.addEventListener('click',()=>selectRepo(r.repo,true));chips.append(btn);
      }
      section.append(chips);holder.append(section);
    }
  }
  function switchMap(mode){
    const connections=mode==='contracts';
    $('map-scroller').hidden=!connections;$('constellation').hidden=connections;
    for(const [id,selected] of [['view-contracts',connections],['view-all',!connections]]){
      const btn=$(id);btn.classList.toggle('active',selected);btn.setAttribute('aria-pressed',String(selected));
    }
  }
  function filters(){
    const holder=$('group-filters');holder.replaceChildren();
    const groups=[{id:'all',label:'Tous'},...atlas.groups];
    for(const g of groups){
      const btn=el('button','filter'+(g.id===activeGroup?' active':''),g.label);btn.type='button';
      btn.addEventListener('click',()=>{activeGroup=g.id;filters();directory();});holder.append(btn);
    }
  }
  function directory(){
    const holder=$('repo-list');holder.replaceChildren();
    const matching=atlas.repositories.filter(r=>(activeGroup==='all'||r.group===activeGroup) &&
      (r.name.toLocaleLowerCase().includes(searchText)||r.role.toLocaleLowerCase().includes(searchText)));
    $('result-count').textContent=`${matching.length} / ${atlas.total} applications`;
    if(!matching.length){holder.append(el('div','empty','Aucune application ne correspond au filtre.'));return;}
    for(const r of matching){
      const btn=el('button','repo-entry'+(activeRepo===r.repo?' active':''));btn.type='button';
      const side=el('span');side.append(el('strong','',r.name),el('small','',r.role));btn.append(side);
      if(r.report)btn.append(el('span','repo-badge','Profil ↗'));
      else if(r.has_local_profile)btn.append(el('span','repo-badge','Profil local'));
      btn.addEventListener('click',()=>selectRepo(r.repo,false));holder.append(btn);
    }
  }
  function metricCell(title,value){const d=el('div','small-stat');d.append(el('strong','',value),el('span','',title));return d;}
  function detailTabs(){
    const tabs=el('div','detail-tabs');
    for(const [id,label] of [['overview','Aperçu'],['report','Ingénierie'],['stages','Qualification']]){
      const b=el('button',''+(detailTab===id?'active':''),label);b.type='button';b.addEventListener('click',()=>{detailTab=id;renderDetail();});tabs.append(b);
    }
    return tabs;
  }
  function statusBadge(status){return el('strong','state-pill'+(status==='Étayé par preuve'?' evidence':status==='À documenter'?' pending':status==='Non applicable'?' na':''),status);}
  function renderDetail(){
    const holder=$('detail');holder.replaceChildren();const r=repoByName(activeRepo);
    if(!r){holder.append(el('div','detail-placeholder','Choisis une application dans la carte ou la liste.'));return;}
    holder.append(el('div','detail-eyebrow','FICHE APPLICATION / '+(r.group==='other'?'INVENTAIRE':r.group.toUpperCase())),el('h3','',r.name),el('p','detail-role',r.role));
    const actions=el('div','detail-links');
    if(qualification && r.has_local_profile){actions.append(link('/local/engineering/'+encodeURIComponent(r.slug),'↗ Lire l’Engineering Profile original','primary-link'));}
    else if(r.report){actions.append(link(r.report,'↗ Voir l’Engineering Profile','primary-link'));}
    else if(r.has_local_profile){actions.append(el('span','disabled-link','Profil original local seulement'));}
    else actions.append(el('span','disabled-link','Engineering Profile non fourni'));
    // The repository name has been validated against the bundled inventory.
    actions.append(link('https://github.com/'+encodeURI(r.repo),'Ouvrir le dépôt GitHub','secondary-link'));
    holder.append(actions,detailTabs());
    const section=el('div');
    const m=r.engineering;
    if(detailTab==='overview'){
      const grid=el('div','detail-grid');
      grid.append(metricCell('Profil mesuré',m?'Disponible':'Non fourni'),metricCell('Fichiers actifs',m?count(m.counts.active_files):'—'),metricCell('Lignes source de production',m?count(m.counts.production_nonblank_lines):'—'));
      section.append(grid);
      section.append(el('p','profile-copy',m?'Ouvre le rapport pour consulter les langues, les contrôles, le périmètre, les dates et la provenance. Mesure ≠ certificat.':'Ce dépôt reste dans l’inventaire officiel : son absence de profil ne constitue pas une non-conformité.'));
    }else if(detailTab==='report'){
      if(!m){section.append(el('p','profile-copy','Aucune mesure d’ingénierie structurée n’a été fournie pour ce dépôt.'));
      if(qualification&&r.has_local_profile)section.append(link('/local/engineering/'+encodeURIComponent(r.slug),'Lire le document Markdown original ↗','primary-link'));}
      else{
        const grid=el('div','detail-grid');
        for(const [name,value] of [['Fichiers actifs',m.counts.active_files],['Sources production',m.counts.production_source_files],['Sources tests',m.counts.test_source_files],['Lignes de production',m.counts.production_nonblank_lines],['Tests statiques',m.static_test_declarations],['Documentation',m.counts.active_docs]])grid.append(metricCell(name,count(value)));
        section.append(grid);
        section.append(el('p','profile-copy','Les lignes non vides peuvent inclure des commentaires. Les tests ont été détectés, mais non exécutés.'));
        section.append(link(qualification?'/local/engineering/'+encodeURIComponent(r.slug):r.report,qualification?'Lire le rapport original local ↗':'Consulter le rapport public et la provenance ↗','primary-link'));
      }
    }else{
      for(const [id,label] of stages){const row=el('div','stage-detail-row');row.append(el('span','',label),statusBadge(statusFor(r.repo,id)));section.append(row);}
      section.append(el('p','profile-copy',qualification?'États manuels lus dans le registre local. Pour modifier une évaluation, ouvre « Certification & profils » dans l’application Windows.':'Aucun verdict manuel n’est publié sur GitHub Pages. Ouvre l’aperçu depuis l’application Windows pour voir tes évaluations locales.'));
    }
    holder.append(section);
    document.querySelectorAll('.map-node,.constellation-item').forEach(x=>x.classList.toggle('selected',x.dataset.repo===activeRepo));
  }
  function selectRepo(repo,fromMap=false){
    if(!repoByName(repo))return;
    activeRepo=repo;detailTab='overview';directory();renderDetail();
    if(fromMap){$('apps').scrollIntoView({behavior:'smooth',block:'start'});}
    const url=new URL(location.href);url.searchParams.set('app',repo.split('/').pop());
    history.replaceState(null,'',url.pathname+url.search+'#apps');
  }
  async function getJSON(url,optional=false){
    try{const response=await fetch(url,{cache:'no-store'});if(!response.ok)throw new Error('HTTP '+response.status);return await response.json();}
    catch(e){if(optional)return null;throw e;}
  }
  async function refresh(){
    $('load-status').textContent='Chargement…';
    try{
      const [newAtlas, audit, local]=await Promise.all([
        getJSON('data/ecosystem.json?at='+Date.now()),
        getJSON('data/dashboard.json?at='+Date.now(),true),
        getJSON('data/local-qualification.json?at='+Date.now(),true),
      ]);
      if(newAtlas.format!=='koa_ecosystem.atlas.v1'||!Array.isArray(newAtlas.repositories)||newAtlas.repositories.length!==49){throw new Error('Inventaire invalide');}
      atlas=newAtlas;localAudit=audit;qualification=local?.format==='koa_qualification.public_status.v1'?local:null;
      const measured=atlas.repositories.filter(r=>r.report).length;
      $('kpi-total').textContent=count(atlas.total);
      $('kpi-profiles').textContent=`${count(measured)} / ${count(atlas.total)}`;
      $('kpi-profiles-note').textContent=`${Math.round(measured/atlas.total*100)} % de dépôts avec profil mesuré`;
      $('bar-profiles').style.width=measured/atlas.total*100+'%';
      const scans=(localAudit?.snapshots||[]).filter(x=>x.mode==='LOCAL_OBSERVE').sort((a,b)=>a.at.localeCompare(b.at));
      const latest=scans[scans.length-1];
      $('kpi-audited').textContent=latest?`${count(latest.inventory_scanned)} / ${count(atlas.total)}`:'Non publié';
      $('bar-audited').style.width=latest?Math.min(100,100*latest.inventory_scanned/atlas.total)+'%':'0%';
      createStageBars();drawMap();drawConstellation();filters();directory();
      if(!activeRepo){const requested=new URLSearchParams(location.search).get('app');const r=atlas.repositories.find(x=>x.slug===requested);
        activeRepo=r?.repo||atlas.repositories.find(x=>x.slug==='Konnaxion')?.repo||atlas.repositories[0]?.repo;}
      renderDetail();$('load-status').textContent='Données disponibles';
    }catch(e){$('load-status').textContent='Données indisponibles';$('repo-list').replaceChildren(el('div','empty','Impossible de lire l’inventaire du tableau de bord. Lance l’aperçu depuis l’application Windows.'));}
  }
  $('search').addEventListener('input',e=>{searchText=e.target.value.trim().toLocaleLowerCase();directory();});
  $('refresh').addEventListener('click',refresh);
  $('view-contracts').addEventListener('click',()=>switchMap('contracts'));
  $('view-all').addEventListener('click',()=>switchMap('all'));
  refresh();
})();
