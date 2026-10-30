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
  let atlas=null, localAudit=null, qualification=null, kristal=null, activeRepo=null, activeGroup='all', searchText='', detailTab='overview', mapMode='contracts', mapTouched=false;
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
  function kristalByRepo(name){return kristal?.repositories?.find(r=>r.repo===name)||null;}
  function humanRole(value){
    const names={
      unqualified_inventory:'Responsabilité à préciser',
      mapped:'Cartographié',
      mapped_support:'Support documenté',
      primary:'Application principale',
      primary_reference_implementation:'Implémentation de référence',
      canonical_system_map:'Carte canonique des systèmes',
      diagnostic_suite:'Diagnostics',
      companion:'Projet associé',
    };
    return names[value]||String(value||'Non précisé').replaceAll('_',' ');
  }
  function humanPredicate(value){
    const names={part_of:'fait partie de',connects_to:'se relie à',uses_contract:'utilise un contrat',
      conforms_to:'se conforme à',participates_in:'participe à',realizes_or_supports:'réalise ou soutient'};
    return names[value]||String(value||'relation').replaceAll('_',' ');
  }
  function drawKristal(){
    const holder=$('kristal-constellation');holder.replaceChildren();
    if(!kristal||kristal.state!=='ready'){
      holder.append(el('p','empty','Le référentiel Kristal local est indisponible. Choisis ou vérifie son dossier dans l’application Windows. La carte intégrée et les Engineering Profiles restent disponibles.'));
      return;
    }
    const groups=new Map();
    for(const item of kristal.repositories){
      const key=item.found ? (item.membership||'not_classified') : 'not_mapped';
      if(!groups.has(key))groups.set(key,[]);
      groups.get(key).push(item);
    }
    const labels={
      mapped:'Cartographiés',mapped_support:'Support documenté',mapped_research:'Recherche cartographiée',
      unqualified_inventory:'À situer dans le graphe',
      documentation_companion:'Documentation associée',
      not_mapped:'Non rapprochés',
      supporting_ecosystem_not_koa_member:'Écosystème de soutien distinct',
      not_classified:'Classement non spécifié',
    };
    for(const [id,items] of groups){
      const card=el('section','kristal-group');
      const title=el('h3','',labels[id]||id.replaceAll('_',' '));
      title.append(el('small','',`${items.length} dépôt${items.length>1?'s':''}`));card.append(title);
      const itemsBox=el('div','kristal-group-items');
      for(const item of items){
        const r=repoByName(item.repo);if(!r)continue;
        const button=el('button','kristal-repo'+(item.repo===activeRepo?' selected':''));button.type='button';button.dataset.repo=item.repo;
        button.append(el('strong','',r.name));
        if(item.components?.length)button.append(el('small','',item.components.length+' association(s) explicite(s)'));
        else if(item.candidates?.length)button.append(el('small','suggestion-label',item.candidates.length+' proposition(s) à confirmer'));
        else button.append(el('small','',humanRole(item.role)||'Aucune association proposée'));
        button.addEventListener('click',()=>{detailTab='kristal';selectRepo(item.repo,true,true);});itemsBox.append(button);
      }
      card.append(itemsBox);holder.append(card);
    }
  }
  function kristalInfo(section, repoName){
    const item=kristalByRepo(repoName);
    if(!kristal||kristal.state!=='ready'){
      section.append(el('p','profile-copy','Le catalogue Kristal n’est accessible qu’en aperçu local avec le dossier source configuré. Aucun statut n’est inféré en son absence.'));
      return;
    }
    if(!item?.found){
      section.append(el('p','profile-copy','Ce dépôt n’a pas de correspondance exacte dans le catalogue Kristal lu. Il reste dans les 49 dépôts officiels.'));
      return;
    }
    section.append(el('p','profile-copy',item.description||'Aucune description canonique fournie.'));
    const grid=el('div','detail-grid');
    grid.append(metricCell('Rôle du catalogue',humanRole(item.role)),metricCell('Cartographie',humanRole(item.membership)),metricCell('Associations explicites',count(item.components?.length||0)),metricCell('Associations proposées',count(item.candidates?.length||0)));
    section.append(grid);
    if(item.components?.length){section.append(el('h4','',`Composants liés explicitement (${item.components.length})`));}
    for(const comp of item.components||[]){
      const card=el('div','kristal-card');card.append(el('h4','',comp.label),el('p','',comp.description||comp.kind||'Composant référencé'));
      card.append(el('small','kristal-status-note','Lien par repository_ref · assertion '+(comp.evidence==='claimed'?'déclarée':comp.evidence==='sourced'?'sourcée':'non classée')+' · pas une intégration certifiée'));
      section.append(card);
    }
    if(item.candidates?.length){
      section.append(el('h4','',`Associations proposées à confirmer (${item.candidates.length})`));
      for(const candidate of item.candidates){
        const card=el('div','kristal-card candidate-card');
        card.append(el('h4','',candidate.label||candidate.id));
        card.append(el('p','','Identifiant du composant : '+candidate.id));
        const reason=candidate.reason==='EXACT_NAME_OR_CANONICAL_ID'?'Nom ou identifiant canonique concordant':'Source GitHub spécifique commune';
        card.append(el('small','kristal-status-note','Suggestion non validée · '+reason+' · '+count(candidate.source_count||0)+' référence(s) de catalogue'));
        section.append(card);
      }
      if(item.candidate_relations?.length){
        const details=el('details','candidate-relations');
        const summary=el('summary','','Voir '+count(item.candidate_relations.length)+' relations sémantiques liées aux candidats (non validées)');
        details.append(summary);
        for(const rel of item.candidate_relations){
          const line=el('div','kristal-card candidate-card');
          line.append(el('p','',`${rel.subject} → ${humanPredicate(rel.predicate)} → ${rel.object}`));
          line.append(el('small','kristal-status-note','Relation de catalogue '+(rel.evidence==='sourced'?'sourcée':'déclarée')+' · attribution du composant au dépôt non validée'));
          details.append(line);
        }
        section.append(details);
      }
    }else if(!item.components?.length){
      section.append(el('p','profile-copy','Aucune association proposée. Cela ne dit rien de la qualité ou de la maturité du dépôt.'));
    }
    if(item.relations?.length){
      section.append(el('h4','',`Relations sémantiques associées (${item.relations.length})`));
      for(const rel of item.relations){
        const card=el('div','kristal-card');card.append(el('p','',`${rel.subject} → ${humanPredicate(rel.predicate)} → ${rel.object}`));
        card.append(el('small','kristal-status-note',rel.evidence==='claimed'?'Déclarée (non certifiée)':'Sourcée (pas une intégration testée)'));
        section.append(card);
      }
    }
    section.append(el('p','profile-copy','Source : catalogues canoniques Kristal locaux. Un dépôt et une composante sont des entités distinctes. Les relations ne prouvent ni des CI réussies ni un déploiement.'));
  }
  function switchMap(mode){
    mapMode=mode;
    $('map-scroller').hidden=mode!=='contracts';
    $('constellation').hidden=mode!=='all';
    $('kristal-constellation').hidden=mode!=='kristal';
    for(const [id,selected] of [['view-contracts',mode==='contracts'],['view-all',mode==='all'],['view-kristal',mode==='kristal']]){
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
    for(const [id,label] of [['overview','Aperçu'],['report','Ingénierie'],['stages','Qualification'],['kristal','Kristal (local)']]){
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
      if(kristalByRepo(r.repo)?.found){const entry=kristalByRepo(r.repo);section.append(el('p','profile-copy','Kristal : '+(entry.description||humanRole(entry.role))+'. Les relations se trouvent dans l’onglet Kristal (local).'));}
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
    }else if(detailTab==='kristal'){
      kristalInfo(section,r.repo);
    }else{
      for(const [id,label] of stages){const row=el('div','stage-detail-row');row.append(el('span','',label),statusBadge(statusFor(r.repo,id)));section.append(row);}
      section.append(el('p','profile-copy',qualification?'États manuels lus dans le registre local. Pour modifier une évaluation, ouvre « Certification & profils » dans l’application Windows.':'Aucun verdict manuel n’est publié sur GitHub Pages. Ouvre l’aperçu depuis l’application Windows pour voir tes évaluations locales.'));
    }
    holder.append(section);
    document.querySelectorAll('.map-node,.constellation-item').forEach(x=>x.classList.toggle('selected',x.dataset.repo===activeRepo));
  }
  function selectRepo(repo,fromMap=false,keepTab=false){
    if(!repoByName(repo))return;
    activeRepo=repo;if(!keepTab)detailTab='overview';directory();renderDetail();drawKristal();
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
      const [newAtlas, audit, local, source]=await Promise.all([
        getJSON('data/ecosystem.json?at='+Date.now()),
        getJSON('data/dashboard.json?at='+Date.now(),true),
        getJSON('data/local-qualification.json?at='+Date.now(),true),
        getJSON('/api/kristal/atlas?at='+Date.now(),true),
      ]);
      if(newAtlas.format!=='koa_ecosystem.atlas.v1'||!Array.isArray(newAtlas.repositories)||newAtlas.repositories.length!==49){throw new Error('Inventaire invalide');}
      atlas=newAtlas;localAudit=audit;qualification=local?.format==='koa_qualification.public_status.v1'?local:null;
      $('historique-campagnes').hidden = !qualification;
      kristal=source?.format==='koa_audit.kristal_local.v1'&&source.state==='ready'?source:null;
      $('kristal-banner').classList.toggle('missing',!kristal);
      if(kristal){
        $('kristal-banner').textContent=`Kristal local · ${kristal.matched}/${kristal.inventory} dépôts identifiés · ${kristal.explicit_repositories} liens explicites · ${kristal.candidate_repositories} suggestions à confirmer · ${kristal.unlinked_repositories} sans proposition` ;
        const displayCount=n=>Number.isInteger(n)?count(n):'—';
        $('kristal-catalog-note').textContent=`Catalogues : ${count(kristal.catalog_components)} composants · ${displayCount(kristal.catalog_contracts)} contrats · ${displayCount(kristal.catalog_capabilities)} capacités · ${count(kristal.catalog_relations)} relations sémantiques. Présence documentaire, pas qualification.`;
        $('kristal-source-title').textContent='Kristal kOA Ecosystem · local';
        $('kristal-source-note').textContent='Lecture en direct des catalogues canoniques. Aucun changement ni publication automatique.';
      }else{
        $('kristal-banner').textContent=String.raw`Kristal local indisponible · la carte intégrée reste accessible. Configure C:\mycode\Kristal\locals\Kristal-kOA-Ecosystem dans l’application Windows.`;
        $('kristal-catalog-note').textContent='La carte intégrée et les Engineering Profiles restent consultables hors ligne. Aucune certification n’est déduite.';
        $('kristal-source-title').textContent='Carte publique kOA';
        $('kristal-source-note').textContent='Pour consulter Kristal en direct, ouvre le centre depuis le launcher Windows.';
      }
      const measured=atlas.repositories.filter(r=>r.report).length;
      $('kpi-total').textContent=count(atlas.total);
      $('kpi-profiles').textContent=`${count(measured)} / ${count(atlas.total)}`;
      $('kpi-profiles-note').textContent=`${Math.round(measured/atlas.total*100)} % de dépôts avec profil mesuré`;
      $('bar-profiles').style.width=measured/atlas.total*100+'%';
      const scans=(localAudit?.snapshots||[]).filter(x=>x.mode==='LOCAL_OBSERVE').sort((a,b)=>a.at.localeCompare(b.at));
      const latest=scans[scans.length-1];
      $('kpi-audited').textContent=latest?`${count(latest.inventory_scanned)} / ${count(atlas.total)}`:'Non publié';
      $('bar-audited').style.width=latest?Math.min(100,100*latest.inventory_scanned/atlas.total)+'%':'0%';
      if(kristal&&!mapTouched)mapMode='kristal';
      createStageBars();drawMap();drawConstellation();drawKristal();switchMap(mapMode);filters();directory();
      if(!activeRepo){const requested=new URLSearchParams(location.search).get('app');const r=atlas.repositories.find(x=>x.slug===requested);
        activeRepo=r?.repo||atlas.repositories.find(x=>x.slug==='Konnaxion')?.repo||atlas.repositories[0]?.repo;}
      renderDetail();$('load-status').textContent='Données disponibles';
    }catch(e){$('load-status').textContent='Données indisponibles';$('repo-list').replaceChildren(el('div','empty','Impossible de lire l’inventaire du tableau de bord. Lance l’aperçu depuis l’application Windows.'));}
  }
  $('search').addEventListener('input',e=>{searchText=e.target.value.trim().toLocaleLowerCase();directory();});
  $('refresh').addEventListener('click',refresh);
  $('view-contracts').addEventListener('click',()=>{mapTouched=true;switchMap('contracts');});
  $('view-all').addEventListener('click',()=>{mapTouched=true;switchMap('all');});
  $('view-kristal').addEventListener('click',()=>{mapTouched=true;switchMap('kristal');});
  refresh();
})();
