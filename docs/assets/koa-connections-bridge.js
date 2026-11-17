/* Optional, nonintrusive contextual backlink for the public audit application profile. */
(() => {
  'use strict';
  const appData = fetch('data/koa-connections.json', { cache:'no-store' }).then(r=>r.ok?r.json():null).catch(()=>null);
  const language = () => document.documentElement.lang === 'en' ? 'en' : 'fr';
  const links = document.querySelectorAll('a[data-koa-connections-link]');
  links.forEach(link => link.addEventListener('click',()=>{
    link.href = `connections.html?lang=${language()}`;
  }));
  appData.then(data=>{
    if (!data || !Array.isArray(data.repositories)) return;
    const detail = document.getElementById('detail');
    if (!detail) return;
    const apply = () => {
      const heading=detail.querySelector('h3');
      const actions=detail.querySelector('.detail-links');
      if (!heading || !actions || actions.querySelector('[data-koa-context]')) return;
      const name=heading.textContent.trim().toLowerCase();
      const repo=data.repositories.find(r=>r.name.toLowerCase()===name || r.audit_slug?.toLowerCase()===name);
      if (!repo) return;
      const a=document.createElement('a');
      a.href=`https://initkoa.org/connections?repo=${encodeURIComponent(repo.name)}`;
      a.target='_blank';a.rel='noopener noreferrer';a.className='secondary-link';
      a.dataset.koaContext='true';
      a.textContent=language()==='en'?'↗ Explore context in The kOA Initiative':'↗ Explorer le contexte dans The kOA Initiative';
      actions.append(a);
    };
    const observer=new MutationObserver(apply);observer.observe(detail,{childList:true,subtree:true});
    apply();
  });
})();
