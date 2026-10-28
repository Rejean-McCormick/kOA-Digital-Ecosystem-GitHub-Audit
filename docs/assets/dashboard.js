(() => {
  'use strict';
  const $ = (id) => document.getElementById(id);
  let snapshots = [];
  let mode = 'LOCAL_OBSERVE';
  const labels = {
    WORKFLOW_UNPINNED_ACTION:'Actions GitHub non figées par SHA',
    LARGE_FILE_NOT_INSPECTED:'Fichiers volumineux non inspectés',
    SENSITIVE_FILENAME:'Noms de fichiers sensibles',
    PYTHON_SHELL_TRUE:'Utilisations de shell=True',
    PYTHON_PICKLE_LOAD:'Utilisations de pickle.load',
    PRIVATE_KEY_MATERIAL:'Motif de clé privée potentielle',
    PYTHON_SSL_VERIFY_DISABLED:'Ancienne règle TLS (à requalifier)',
    PYTHON_TLS_BYPASS:'Contournement TLS potentiel'
  };
  function text(id, value) { $(id).textContent = String(value); }
  function dom(tag, cls, value) { const el = document.createElement(tag); if(cls)el.className=cls; if(value !== undefined)el.textContent=String(value); return el; }
  function number(n) {return Number(n || 0).toLocaleString('fr-CA');}
  function day(s) {try{return new Intl.DateTimeFormat('fr-CA',{dateStyle:'medium',timeStyle:'short',timeZone:'America/Toronto'}).format(new Date(s));}catch(e){return s;}}
  function selected(){return snapshots.filter(s=>s.mode===mode).sort((a,b)=>a.at.localeCompare(b.at));}
  function latest(){const arr=selected();return arr.length?arr[arr.length-1]:null;}
  function metric(i,label,value,extra){text('metric-label-'+i,label);text('metric-'+i,value);if(i>1)text('metric-extra-'+i,extra);}
  function row(parent,label,value){const r=dom('div','coverage-row');r.append(dom('span','',label),dom('strong','',number(value)));parent.append(r);}
  function ring(percent,caption){$('ring').style.setProperty('--pct',Math.max(0,Math.min(100,percent))+'%');text('ring-value',percent+' %');text('ring-caption',caption);}
  function renderLocal(d){
    const sum=Object.values(d.findings||{}).reduce((a,b)=>a+b,0);
    metric(1,'Dépôts déclarés',number(d.declared),'');
    metric(2,'Dépôts inspectés',number(d.scanned),'Scan statique local');
    metric(3,'Observations à examiner',number(sum),'Motifs, non vulnérabilités');
    metric(4,'Couverture',d.declared ? Math.round(100*d.inventory_scanned/d.declared)+' %':'—','Dépôts de l’inventaire inspectés');
    text('coverage-title','État des inspections');ring(d.declared?Math.round(100*d.inventory_scanned/d.declared):0,'audités / déclarés');
    const side=$('coverage-list');side.replaceChildren();
    row(side,'Inspection partielle',(d.statuses||{}).PARTIAL||0);row(side,'À examiner',(d.statuses||{}).REVIEW||0);row(side,'Aucun motif détecté',(d.statuses||{}).INSPECTED_NO_PATTERN_MATCH||0);row(side,'Doublons ambigus',d.ambiguous||0);
    text('coverage-note','« Aucun motif » ne signifie pas « sécurité garantie ». Les copies ambiguës limitent la couverture.');
    text('signals-title','Signaux détectés sur le disque');
    text('signal-note','Les règles TLS des anciennes campagnes pouvaient contenir des faux positifs. Les données de ce site ne réévaluent pas le code.');
    bars(Object.entries(d.findings||{}).sort((a,b)=>b[1]-a[1]).map(([name,count])=>({name:labels[name]||'Catégorie contrôlée',count})));
    text('caveat','Aucun scan CVE, CodeQL ni test CI n’a été exécuté par l’auditeur local.');
    text('mode-description','LOCAL_OBSERVE · Inspection du disque · métadonnées agrégées');
    trend(selected(),s=>Object.values(s.findings||{}).reduce((a,b)=>a+b,0),'Observations heuristiques');
  }
  function renderRemote(d){
    metric(1,'Dépôts déclarés',number(d.declared),'');
    metric(2,'Métadonnées obtenues',number(d.observed),'API publique partiellement accessible');
    metric(3,'CI récentes en échec',number((d.ci||{}).failure),'Selon l’échantillon observé');
    metric(4,'Couverture API',d.declared?Math.round(100*d.observed/d.declared)+' %':'—','Les autres états sont inconnus');
    text('coverage-title','Accès à GitHub');ring(d.declared?Math.round(100*d.observed/d.declared):0,'observés / déclarés');
    const side=$('coverage-list');side.replaceChildren();row(side,'Métadonnées accessibles',d.observed||0);row(side,'Statut inconnu',d.unknown||0);row(side,'CI récentes réussies',(d.ci||{}).success||0);row(side,'CI récentes en échec',(d.ci||{}).failure||0);
    text('coverage-note','Un échec CI ne signifie pas qu’un dépôt est compromis. Les accès API incomplets limitent les conclusions.');
    text('signals-title','Alertes de sécurité : visibilité disponible');
    text('signal-note','Les nombres présentés sont seulement des minimums observés. Lorsque la couverture API est incomplète, zéro ne signifie pas absence d’alertes.');
    const keys={dependabot:'Dependabot',code_scanning:'Code scanning',secret_scanning:'Secret scanning'};
    bars(Object.entries(keys).map(([k,name])=>({name:name+' · '+((d.alerts||{})[k]?.complete?'complet':'inconnu / partiel'),count:(d.alerts||{})[k]?.observed_minimum||0})));
    text('caveat','CodeQL, Dependabot et Secret Scanning ne sont pas évaluables globalement ici : restrictions API / rate limits possibles.');
    text('mode-description','OBSERVE · État GitHub constaté · disponibilité API variable');
    trend(selected(),s=>(s.ci||{}).failure||0,'Dernières CI en échec');
  }
  function bars(items){const target=$('signal-list');target.replaceChildren();if(!items.length){target.append(dom('div','empty-state','Aucune donnée pour cette catégorie.'));return;}
    const max=Math.max(1,...items.map(i=>i.count));items.forEach(item=>{const e=dom('div','signal'),top=dom('div','signal-top'),tr=dom('div','bar-track'),fill=dom('div','bar-fill');top.append(dom('span','',item.name),dom('strong','',number(item.count)));fill.style.width=(100*item.count/max)+'%';tr.append(fill);e.append(top,tr);target.append(e);});
  }
  function trend(data,read,label){text('history-count',data.length+' campagne'+(data.length>1?'s':''));text('trend-legend-title',label);const place=$('trend-visual');place.replaceChildren();if(!data.length){place.append(dom('div','empty-state','Aucune campagne publiée dans cette catégorie.'));return;}
    const w=640,h=215,padX=36,padY=26,vals=data.map(read),ceiling=Math.max(1,...vals);const x=i=>padX+(w-2*padX)*(data.length===1?.5:i/(data.length-1));const y=v=>h-padY-(h-2*padY)*v/ceiling;
    const ns='http://www.w3.org/2000/svg';const svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox',`0 0 ${w} ${h}`);svg.setAttribute('role','img');svg.setAttribute('aria-label',label+' : '+vals.join(', '));
    for(let i=0;i<4;i++){let value=ceiling*i/3;const line=document.createElementNS(ns,'line');line.setAttribute('x1',padX);line.setAttribute('x2',w-padX);line.setAttribute('y1',y(value));line.setAttribute('y2',y(value));line.setAttribute('stroke','#29374d');line.setAttribute('stroke-dasharray','4 5');svg.append(line);const tx=document.createElementNS(ns,'text');tx.textContent=Math.round(value).toString();tx.setAttribute('x','1');tx.setAttribute('y',y(value)+4);tx.setAttribute('fill','#7187a3');tx.setAttribute('font-size','11');svg.append(tx);}
    const poly=document.createElementNS(ns,'polyline');poly.setAttribute('points',vals.map((v,i)=>`${x(i)},${y(v)}`).join(' '));poly.setAttribute('fill','none');poly.setAttribute('stroke','#61dfbf');poly.setAttribute('stroke-width','3');poly.setAttribute('stroke-linejoin','round');svg.append(poly);
    vals.forEach((v,i)=>{const c=document.createElementNS(ns,'circle');c.setAttribute('cx',x(i));c.setAttribute('cy',y(v));c.setAttribute('r',data.length<24?'5':'3');c.setAttribute('fill','#86f2d7');c.setAttribute('stroke','#101827');c.setAttribute('stroke-width','2');const title=document.createElementNS(ns,'title');title.textContent=day(data[i].at)+' : '+v;c.append(title);svg.append(c);});
    [0,data.length-1].filter((v,i,a)=>a.indexOf(v)===i).forEach(i=>{const tx=document.createElementNS(ns,'text');tx.textContent=new Date(data[i].at).toLocaleDateString('fr-CA',{month:'short',day:'numeric',year:'numeric',timeZone:'UTC'});tx.setAttribute('x',x(i));tx.setAttribute('y',h-3);tx.setAttribute('text-anchor',i===0&&data.length>1?'start':i===data.length-1&&data.length>1?'end':'middle');tx.setAttribute('fill','#8296b0');tx.setAttribute('font-size','11');svg.append(tx);});place.append(svg);
  }
  function render(){const d=latest();document.querySelectorAll('.mode-toggle button').forEach(b=>{const active=b.id===(mode==='LOCAL_OBSERVE'?'mode-local':'mode-github');b.classList.toggle('is-active',active);b.setAttribute('aria-pressed',String(active));});if(!d){for(let i=1;i<=4;i++)metric(i,'Données indisponibles','—','');text('updated','Aucun rapport dans cette catégorie');$('trend-visual').replaceChildren(dom('div','empty-state','Publie un rapport pour commencer.'));$('signal-list').replaceChildren();$('coverage-list').replaceChildren();ring(0,'aucun rapport');return;}text('updated','Rapport du '+day(d.at));if(mode==='LOCAL_OBSERVE')renderLocal(d);else renderRemote(d);}
  async function refresh(){text('connection','Chargement…');try{const r=await fetch('data/dashboard.json?time='+Date.now(),{cache:'no-store'});if(!r.ok)throw Error('HTTP '+r.status);const data=await r.json();if(data.format!=='koa_audit.dashboard.v1'||!Array.isArray(data.snapshots))throw Error('Format inconnu');snapshots=data.snapshots.filter(x=>x&&(x.mode==='LOCAL_OBSERVE'||x.mode==='OBSERVE'));text('connection','Données publiées');render();}catch(error){text('connection','Données indisponibles');text('updated','Erreur de chargement');const tip=dom('div','error-note','Impossible de charger les données. En aperçu local, utilise un serveur HTTP (voir README).');$('trend-visual').replaceChildren(tip);}}
  $('mode-local').addEventListener('click',()=>{mode='LOCAL_OBSERVE';render();});$('mode-github').addEventListener('click',()=>{mode='OBSERVE';render();});$('refresh').addEventListener('click',refresh);refresh();setInterval(refresh,180000);
})();
