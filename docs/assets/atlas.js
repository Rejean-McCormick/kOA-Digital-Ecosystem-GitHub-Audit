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
  let atlas=null, localAudit=null, qualification=null, kristal=null, privateCampaigns=null, privateReview=null, activeRepo=null, activeGroup='all', searchText='', detailTab='overview', mapMode='contracts', mapTouched=false;
  let validationBoard=null, validationRepo=null, validationCategory='Fonctionnalités', validationSearch='', validationFilter='all';
  // One workspace per user intent (UX-01/05/15/16). Keep older anchors working.
  let workspace='validations', mapExpanded=false;
  function workspaceForHash(hash){
    if(hash==='#cartographie')return 'applications';
    if(hash==='#apps')return 'applications';
    if(hash==='#historique-campagnes'||hash==='#qualification')return 'campagnes';
    return 'validations';
  }
  function setWorkspace(mode, anchor=''){
    workspace=['validations','applications','campagnes'].includes(mode)?mode:'validations';
    if(anchor==='#cartographie')mapExpanded=true;
    else if(mode==='applications'&&anchor==='#apps')mapExpanded=false;
    document.querySelectorAll('[data-workspace]').forEach(section=>{
      const isVisible=section.dataset.workspace===workspace;
      section.hidden=!isVisible || (section.id==='cartographie'&&!mapExpanded);
    });
    for(const item of document.querySelectorAll('[data-nav]')){
      const active=item.dataset.nav===workspace;
      item.classList.toggle('active',active);
      if(active)item.setAttribute('aria-current','page');else item.removeAttribute('aria-current');
    }
    const publicNote=$('campaign-public-note');
    if(publicNote)publicNote.hidden=workspace!=='campagnes'||!!qualification;
    if(workspace==='applications' && mapExpanded && atlas)requestAnimationFrame(()=>drawMap());
  }
  function activateRoute(){setWorkspace(workspaceForHash(location.hash),location.hash);}
  function validationRepoData(name){return validationBoard?.repositories?.find(x=>x.repo===name);}
  function validationMetric(value, caption){const d=el('div','validation-metric');d.append(el('strong','',value),el('small','',caption));return d;}
  function sourceProvenance(sources, tests){
    const holder=el('details','spec-evidence');
    const files=[...(sources||[]).map(x=>({...x,kind:'Code / contrat'})),...(tests||[]).map(x=>({...x,kind:'Test défini, non exécuté'}))];
    if(!files.length)return holder;
    holder.append(el('summary','','Sources et empreintes · '+files.length+' fichier(s)'));
    for(const item of files){
      const entry=el('div','spec-source');
      entry.append(el('span','',item.kind+' · '+item.path),el('code','',`SHA-256 ${item.sha256}`));
      holder.append(entry);
    }
    return holder;
  }
  function renderSpecsheetDetail(detail,current,technical){
    const spec=current.specsheet||{};
    const heading=technical?'Technologies et composants':'Fonctionnalités de l’application';
    detail.append(el('h4','',heading));
    if(spec.state!=='snapshot_reviewed'){
      detail.append(el('p','validation-explain',spec.notice||'Pas de snapshot fonctionnel examiné pour ce dépôt. Ses fonctions ne sont pas considérées absentes.'));
      const report=atlas?.repositories?.find(x=>x.repo===current.repo)?.report;
      if(report)detail.append(link(report,'↗ Engineering Profile disponible (mesures, pas fonctionnalités validées)',''));
      return;
    }
    detail.append(el('p','spec-overview',spec.overview));
    const meta=el('p','spec-meta','Source : '+spec.snapshot+' · SHA-256 '+spec.snapshot_sha256.slice(0,20)+'… · commit non attesté. Aucune exécution de test démontrée par ce ZIP.');
    detail.append(meta);
    const items=technical?spec.technical:spec.features;
    const groups=[...new Set(items.map(x=>x.group))];
    const summary=el('div','spec-summary');
    summary.append(el('strong','',String(items.length)),el('span','',technical?'technologies repérées':'fonctions observées ou spécifiées'),el('strong','',String(current.targeted_test_run?.passed||0)),el('span','','tests unitaires ciblés PASS sur ce ZIP · pas validation de toutes les fonctions'));
    detail.append(summary);
    for(const group of groups){
      const box=el('details','spec-group');box.open=true;
      box.append(el('summary','',`${group} · ${items.filter(x=>x.group===group).length} élément(s)`));
      for(const item of items.filter(x=>x.group===group)){
        const row=el('article','spec-feature');
        const head=el('div','spec-feature-head');head.append(el('strong','',item.title));
        const state=item.execution_verified?'✓ Test réussi et vérifié':item.status==='specification_only'?'Spécifié · fonctionnement non validé':'Implémentation repérée · validation à établir';
        head.append(el('span',item.execution_verified?'spec-state spec-success':'spec-state',state));row.append(head);
        row.append(el('p','',item.description));
        if(item.technologies?.length){const tags=el('div','spec-tech-tags');
          item.technologies.forEach(t=>tags.append(el('span','',t)));row.append(tags);}
        if(item.test_definitions?.length){
          const run=current.targeted_test_run;
          const matched=run?.test_files?.filter(t=>item.test_definitions.some(d=>d.path===t.path && d.sha256===t.sha256))||[];
          if(matched.length){
            const check=el('div','spec-unit-success');check.append(el('span','','✓ '+run.passed+' tests unitaires ciblés PASS pour '+matched.map(x=>x.path).join(', ')));
            check.append(link(run.junit_link,'↗ Rapport JUnit daté (snapshot uniquement)',''));
            row.append(check);
          }else row.append(el('p','spec-tests',`${item.test_definitions.length} fichier(s) de tests présent(s) · exécution non attestée`));
        }
        row.append(sourceProvenance(item.sources,item.test_definitions));box.append(row);
      }
      detail.append(box);
    }
    detail.append(el('p','validation-explain','La présence d’une implémentation, d’un framework, d’un fichier pytest ou d’un scénario ne donne pas un crochet vert. Les tests doivent avoir un journal de succès et une provenance compatibles avec la version.'));
  }
  function renderValidationBoard(){
    const holder=$('validation-metrics'), listing=$('validation-list'), detail=$('validation-detail');
    holder.replaceChildren();listing.replaceChildren();detail.replaceChildren();
    if(!validationBoard){
      $('validation-source').textContent='Données privées indisponibles sur cette page';
      holder.append(validationMetric('49','Dépôts de l’inventaire'),validationMetric('—','Résultats locaux non publiés'),validationMetric('—','Tests vérifiés non publiés'),validationMetric('—','Contrôles de sécurité non publiés'));
      listing.append(el('p','validation-no-data','Ouvre le dashboard depuis le lanceur Windows pour voir les résultats réels et les pièces confidentielles. Aucun verdict n’est déduit ici.'));
      detail.append(el('p','','Les données privées de qualification ne sont pas copiées sur GitHub Pages. Les 49 fiches et les Engineering Profiles publics restent accessibles plus bas.'));
      return;
    }
    $('validation-source').textContent='Registre privé local · sources contrôlées';
    const entries=validationBoard.repositories;
    const evaluated=entries.reduce((n,r)=>n+r.assessed_practices,0);
    holder.append(validationMetric(String(entries.length),'Applications dans le périmètre'),
      validationMetric(String(validationBoard.functional_specsheets_reviewed||0),'Fiches fonctionnelles vérifiées par source'),
      validationMetric(String(validationBoard.targeted_unit_tests_passed||0),'Tests unitaires ciblés PASS · snapshots datés'),
      validationMetric(String(validationBoard.source_checked_documentary_jalons),'Jalons documentaires étayés · périmètre limité'));
    if(evaluated)holder.append(validationMetric(String(evaluated),'Pratiques examinées, non certifiées'));
    const query=validationSearch.trim().toLocaleLowerCase();
    // Evidence-first orientation, NOT quality ranking: grouped by availability of
    // actually verified documentation, then alphabetical for predictable browsing.
    const filtered=entries.filter(r=>(!query||r.slug.toLocaleLowerCase().includes(query))&&
      (validationFilter==='all'||(validationFilter==='verified'&&r.verified_stages>0)||
       (validationFilter==='reviewed'&&r.assessed_practices>0)||
       (validationFilter==='specs'&&r.specsheet?.state==='snapshot_reviewed')))
      .sort((a,b)=>Number(b.verified_stages||0)-Number(a.verified_stages||0)||
        a.slug.localeCompare(b.slug,'fr'));
    if(!validationRepo||!filtered.some(r=>r.repo===validationRepo))validationRepo=filtered[0]?.repo||null;
    if(!filtered.length)listing.append(el('p','validation-no-data','Aucune application pour ce filtre (ce n’est pas une non-conformité).'));
    for(const r of filtered){
      const b=el('button','validation-repo'+(r.repo===validationRepo?' selected':''));b.type='button';
      const name=el('span');name.append(el('strong','',r.slug));
      name.append(el('small','',r.verified_stages?`${r.verified_stages} jalon(s) documenté(s) · périmètre limité`:
        r.specsheet?.state==='snapshot_reviewed'?`${r.specsheet.features.length} fonctions décrites · tests : ${r.targeted_test_run?.passed||0} PASS ciblés`:'Aucune pièce qualifiante vérifiée dans le registre'));
      b.append(name,el('span',r.verified_stages?'proof-tick':'proof-unknown',r.verified_stages?'✓ '+r.verified_stages:'—'));
      b.addEventListener('click',()=>{validationRepo=r.repo;validationCategory='Fonctionnalités';renderValidationBoard();});listing.append(b);
    }
    const current=validationRepoData(validationRepo);
    if(!current){detail.append(el('p','validation-no-data','Aucune fiche sélectionnée.'));return;}
    detail.append(el('small','detail-eyebrow','VALIDATION DÉTAILLÉE · APPLICATION'),el('h3','',current.slug));
    detail.append(el('p','','Fiche technique et fonctions détectées dans les snapshots : une implémentation visible n’est pas un test réussi. Les coches vertes restent réservées aux preuves vérifiées et datées.'));
    const categories=el('div','validation-categories');
    const componentInfo=kristalByRepo(current.repo);
    for(const category of [{label:'Fonctionnalités',verified_count:0,practice_count:0,evaluated_practices:0}, {label:'Technologies',verified_count:0,practice_count:0,evaluated_practices:0}, ...current.categories, {label:'Composants',verified_count:0,practice_count:0,evaluated_practices:0}]){
      const b=el('button','validation-category'+(category.label===validationCategory?' selected':''));b.type='button';
      b.append(el('strong','',category.label),el('span','',category.label==='Composants'?
        (componentInfo?.components?.length ? `${componentInfo.components.length} lien(s) explicite(s)` : componentInfo?.candidates?.length ? `${componentInfo.candidates.length} suggestion(s)` : 'Rattachement non documenté') : category.label==='Tests'&&current.targeted_test_run?`${current.targeted_test_run.passed} tests unitaires ciblés PASS` :
        category.label==='Sécurité'&&current.targeted_test_run?.test_files?.some(x=>x.path.includes('test_security_gate.py'))?`${current.targeted_test_run.passed} tests gate PASS · 53 critères non certifiés` :
        category.label==='Fonctionnalités'?
        (current.specsheet?.state==='snapshot_reviewed'? `${current.specsheet.features.length} fonctions identifiées · validation globale non attestée`:'Snapshot à examiner') : category.label==='Technologies'?
        (current.specsheet?.state==='snapshot_reviewed'? `${current.specsheet.technical.length} composants observés`:'Source à examiner') : category.verified_count?`✓ ${category.verified_count} preuve(s) datée(s)`:
        category.practice_count?`${category.practice_count} critères du référentiel · ${category.evaluated_practices} évalués manuellement`:'Aucune pièce vérifiée'));
      b.addEventListener('click',()=>{validationCategory=category.label;renderValidationBoard();});categories.append(b);
    }
    detail.append(categories);
    if(validationCategory==='Fonctionnalités'||validationCategory==='Technologies'){
      renderSpecsheetDetail(detail,current,validationCategory==='Technologies');return;
    }
    const selected=current.categories.find(c=>c.label===validationCategory)||current.categories[0];
    if(validationCategory==='Composants'){
      detail.append(el('h4','','Composants du catalogue Kristal'));
      if(!kristal||kristal.state!=='ready'){detail.append(el('p','','Kristal local non accessible : aucun rattachement de composant n’est inventé.'));}
      else if(!componentInfo?.components?.length&&!componentInfo?.candidates?.length){detail.append(el('p','','Aucun rattachement de composant documenté pour ce dépôt. Cela ne dit rien de la qualité du système.'));}
      else {
        for(const comp of componentInfo.components||[]){
          const row=el('div','validation-control'),left=el('div');left.append(el('strong','',comp.label||comp.id),el('small','',comp.description||comp.kind||'Composant du catalogue'));
          row.append(left,el('span','control-status','Lien explicite dans Kristal · pas une certification'));detail.append(row);
        }
        for(const comp of componentInfo.candidates||[]){
          const row=el('div','validation-control'),left=el('div');left.append(el('strong','',comp.label||comp.id),el('small','',comp.reason==='EXACT_NAME_OR_CANONICAL_ID'?'Nom ou identifiant concordant':'Référence de source commune'));
          row.append(left,el('span','control-status','Association proposée · non validée'));detail.append(row);
        }
      }
      const r=atlas?.repositories?.find(x=>x.repo===current.repo);if(r?.report)detail.append(link(r.report,'↗ Engineering Profile mesuré et provenance',''));
      detail.append(el('p','validation-explain','Les composants proviennent du registre Kristal local. Un nom similaire, une relation sémantique ou un lien de responsabilité ne constitue pas un test d’intégration réussi.'));
      return;
    }
    detail.append(el('h4','',selected.label+(selected.practice_count?` · ${selected.practice_count} critères du catalogue`:'')));
    for(const stage of selected.stages){
      const row=el('div','validation-control');const left=el('div');left.append(el('strong','',stage.label));
      if(stage.scope)left.append(el('small','',stage.scope));
      if(stage.source_verified){left.append(link(stage.source_link,'↗ Consulter la pièce originale et son empreinte',''));
        left.append(el('small','','SHA-256 '+stage.source_sha256.slice(0,16)+'… · version du clone non attestée'));}
      row.append(left,el('span','control-status'+(stage.source_verified?' checked':''),stage.display));detail.append(row);
    }
    if((selected.label==='Tests'||selected.label==='Sécurité')&&current.targeted_test_run){
      const run=current.targeted_test_run;
      if(selected.label==='Tests'||run.test_files.some(x=>x.path.includes('test_security_gate.py'))){
        const row=el('div','validation-control'),left=el('div');
        left.append(el('strong','','✓ '+run.passed+'/'+run.passed+' tests unitaires ciblés réussis sur un snapshot ZIP'));
        left.append(el('small','',run.scope+' SHA du ZIP '+run.snapshot_sha256.slice(0,16)+'… · commit Git non attesté'));
        left.append(link(run.junit_link,'↗ Voir le rapport JUnit original validé par SHA-256',''));
        row.append(left,el('span','control-status checked','PASS vérifié · suite ciblée seulement'));detail.append(row);
      }
    }
    if(selected.label==='Tests'){
      const ci=current.historical_ci;
      const row=el('div','validation-control'),left=el('div');left.append(el('strong','','Exécution CI historique · GitHub Actions'));
      if(ci?.run_at)left.append(el('small','','Exécution observée : '+ci.run_at+' · SHA '+(ci.run_head_sha||'inconnu')));
      if(ci?.source_snapshot_sha256)left.append(el('small','','Observation archivée et datée · SHA-256 du fichier '+ci.source_snapshot_sha256.slice(0,16)+'…'));
      const status=ci?.success_observed?'Succès CI observé · portée du workflow inconnue':
        ci?.conclusion==='success'?'Succès historique sur un autre SHA':
        ci?.conclusion==='failure'?'Échec observé de ce workflow (pas une évaluation globale)':
        'Aucun résultat CI attestable dans le snapshot';
      row.append(left,el('span','control-status'+(ci?.success_observed?' checked':''),status));detail.append(row);
      if(ci?.success_observed)detail.append(el('p','validation-explain','La conclusion « success » a été observée via l’API GitHub le 28 octobre 2026 au SHA du snapshot. Le contenu des tests du workflow n’est pas fourni, et le SHA de ta version actuelle n’est pas vérifié.'));
    }
    if(selected.practices.length){
      const collection=el('details','validation-practices'),heading=el('summary','',
        `Consulter les ${selected.practices.length} critères du catalogue · états individuels`);
      collection.append(heading);
      for(const item of selected.practices){
        const row=el('div','validation-control'),left=el('div');
        left.append(el('strong','',item.id+' · '+item.title),el('small','',item.section));
        const right=el('span','control-status',item.display);row.append(left,right);collection.append(row);
      }
      detail.append(collection);
    }
    detail.append(el('p','validation-explain',selected.label==='Sécurité'? 'Aucun contrôle de sécurité du catalogue ne reçoit automatiquement un crochet vert : une analyse statique ou la présence d’un fichier ne démontre pas qu’un contrôle passe un test. Un journal ciblé et vérifiable est nécessaire.':
      selected.label==='Tests'?'Un même rapport E2E historique peut concerner deux applications. Cela ne correspond pas à deux campagnes de tests indépendantes ni à un succès CI du commit actuel.':'Les preuves historiques documentent seulement le périmètre et la date indiqués, pas la préparation globale du dépôt.'));
    const app=atlas?.repositories?.find(x=>x.repo===current.repo);
    if(app){const actions=el('p');actions.append(link('#apps','↗ Ouvrir la fiche de cette application',''));actions.querySelector('a').addEventListener('click',()=>selectRepo(current.repo,false));detail.append(actions);}
  }
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
      const pending=counts['À documenter'];
      const evidenced=counts['Étayé par preuve'];
      const other=[];
      if(counts['Non évalué'])other.push(`${counts['Non évalué']} non évalués`);
      if(counts['Non applicable'])other.push(`${counts['Non applicable']} non applicables`);
      const metaLabel=qualification?[`${evidenced}/${total} étayés`,`${pending} à documenter`,...other].join(' · '):'Non publié / non évalué';
      const meta=el('div','stage-meta',metaLabel);
      row.append(left,meter,meta);holder.append(row);
    });
    if(qualification){
      let examined=0,evidenced=0,pending=0,notEvaluated=0,notApplicable=0;
      for(const r of data){for(const [key] of stages){
        const status=statusFor(r.repo,key);
        if(status!=='Non évalué')examined++;
        if(status==='Étayé par preuve')evidenced++;
        else if(status==='À documenter')pending++;
        else if(status==='Non applicable')notApplicable++;
        else notEvaluated++;
      }}
      // Only source-supported, scope-limited stages count as evidenced; reviewing a case is NOT certification.
      $('kpi-qualification').textContent=`${count(evidenced)} / ${count(total*5)}`;
      const parts=[`${count(pending)} à documenter`,`${count(examined)}/${count(total*5)} dossiers examinés`];
      if(notEvaluated)parts.push(`${count(notEvaluated)} non évalués`);
      if(notApplicable)parts.push(`${count(notApplicable)} non applicables`);
      $('kpi-qualification-note').textContent=parts.join(' · ');
      $('qual-mode').textContent='Registre actuel · qualifications limitées à leur portée et à leur date, non à l’application entière';
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
    if(privateReview)actions.append(link('/local/review/app/'+encodeURIComponent(r.slug),'↗ Voir les 5 dossiers de preuves','secondary-link'));
    actions.append(link('https://github.com/'+encodeURI(r.repo),'Ouvrir le dépôt GitHub','secondary-link'));
    if(privateCampaigns?.available && privateCampaigns.latest.repositories?.[r.repo]){
      const cid=privateCampaigns.latest.id;
      actions.append(link('/local/campaigns/'+cid+'/app/'+encodeURIComponent(r.slug),
                   '↗ Fiche figée · dernière campagne','secondary-link'));
    }
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
    setWorkspace('applications','#apps');
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
      const [newAtlas, audit, local, source, campaignSummary, reviewSummary, board]=await Promise.all([
        getJSON('data/ecosystem.json?at='+Date.now()),
        getJSON('data/dashboard.json?at='+Date.now(),true),
        getJSON('data/local-qualification.json?at='+Date.now(),true),
        getJSON('/api/kristal/atlas?at='+Date.now(),true),
        getJSON('/api/campaigns/summary?at='+Date.now(),true),
        getJSON('/api/review/summary?at='+Date.now(),true),
        getJSON('/api/validation/board?at='+Date.now(),true),
      ]);
      if(newAtlas.format!=='koa_ecosystem.atlas.v1'||!Array.isArray(newAtlas.repositories)||newAtlas.repositories.length!==49){throw new Error('Inventaire invalide');}
      validationBoard=board?.format==='koa.validation_board.private.v1'&&board.local_only?board:null;
      atlas=newAtlas;localAudit=audit;qualification=local?.format==='koa_qualification.public_status.v1'?local:null;
      privateCampaigns = campaignSummary?.format==='koa_certification.latest_summary.v1'?campaignSummary:null;
      privateReview = reviewSummary?.format==='koa.evidence_review.summary.v1'?reviewSummary:null;
      const reviewLink=$('review-private-link'); if(reviewLink)reviewLink.hidden=!privateReview;
      const historyLink=$('campaigns-local-link'); if(historyLink)historyLink.hidden=!qualification;
      // Historic panels are private; the route remains navigable even on public Pages.
      setWorkspace(workspace,location.hash);
      const latestPanel = $('latest-campaign');latestPanel.replaceChildren();
      if(qualification){
        if(privateCampaigns?.available){
          const c=privateCampaigns.latest;
          latestPanel.append(el('p','',`Campagne figée du ${c.frozen_at.slice(0,10)} (état historique) · ${count(c.engineering_profiles)}/${count(c.repository_count)} profils figés · ${count(c.proof_files)} pièces jointes · ${count(c.practice_reviews)} pratiques examinées.`));
          const frozenEvidenced=stages.reduce((sum,[key])=>sum+(Number(c.stages_evidenced?.[key])||0),0);
          const totalPossible=atlas.repositories.length*stages.length;
          const currentEvidenced=atlas.repositories.reduce((sum,r)=>sum+stages.filter(([id])=>statusFor(r.repo,id)==='Étayé par preuve').length,0);
          latestPanel.append(el('p','campaign-scope-note',`Jalons étayés — campagne figée : ${count(frozenEvidenced)}/${count(totalPossible)} · registre actuel : ${count(currentEvidenced)}/${count(totalPossible)}. Les décisions postérieures à la campagne n’en modifient pas le contenu.`));
          if(currentEvidenced!==frozenEvidenced){
            latestPanel.append(el('p','campaign-scope-note','Pour conserver l’état actuel, crée une nouvelle campagne dans l’application Windows. Aucune ancienne campagne n’est réécrite.'));
          }
          const list=el('div','campaign-bars');
          for(const [id,label] of stages){
            const n=c.stages_evidenced?.[id]||0,row=el('div','stage-row');
            row.append(el('span','',label+` · ${n}/${c.repository_count} étayés`));
            const meter=el('div','stage-meter'),fill=el('span','stage-evidence');
            fill.style.width=(100*n/Math.max(1,c.repository_count))+'%';meter.append(fill);row.append(meter);list.append(row);
          }
          latestPanel.append(list);
          if(privateCampaigns.previous_id)latestPanel.append(link('/local/campaigns/compare/'+privateCampaigns.previous_id+'--'+c.id,'Comparer les deux dernières campagnes ↗','small-button'));
        }else latestPanel.append(el('p','','Aucune campagne locale encore créée. Le registre de qualification reste disponible dans l’application Windows.'));
      }
      kristal=source?.format==='koa_audit.kristal_local.v1'&&source.state==='ready'?source:null;
      renderValidationBoard();
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
  $('validation-search').addEventListener('input',e=>{validationSearch=e.target.value;renderValidationBoard();});
  $('validation-filter').addEventListener('change',e=>{validationFilter=e.target.value;renderValidationBoard();});
  $('search').addEventListener('input',e=>{searchText=e.target.value.trim().toLocaleLowerCase();directory();});
  $('refresh').addEventListener('click',refresh);
  window.addEventListener('hashchange',activateRoute);
  // Update immediately on ordinary in-page clicks, even in restricted previews
  // where a hashchange event can be suppressed.
  document.addEventListener('click',event=>{
    const a=event.target.closest?.('a[href^="#"]');
    if(!a)return;
    const anchor=a.getAttribute('href');
    if(['#validations','#apps','#cartographie','#qualification','#historique-campagnes'].includes(anchor))
      setWorkspace(workspaceForHash(anchor),anchor);
  });
  activateRoute();
  $('view-contracts').addEventListener('click',()=>{mapTouched=true;switchMap('contracts');});
  $('view-all').addEventListener('click',()=>{mapTouched=true;switchMap('all');});
  $('view-kristal').addEventListener('click',()=>{mapTouched=true;switchMap('kristal');});
  refresh();
})();
