const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{
  const b=await chromium.launch(); const pg=await b.newPage({viewport:{width:1280,height:720}});
  const files=fs.readdirSync(__dirname+'/../..').filter(f=>/^hari\d.*\.html$/.test(f)).sort();
  for(const f of files){
    await pg.goto('file://'+__dirname+'/../../'+f); await pg.waitForTimeout(400);
    const data=await pg.evaluate(()=>{
      const D=window.DECK, out=[]; const cls=['shown','on','hl','focus','pick','chg','m','used'];
      const snap=(sl)=>{const set=new Map();sl.querySelectorAll('*').forEach(e=>{if(e.closest('.notes'))return;
        if(cls.some(c=>e.classList.contains(c))&&e.children.length<4){const t=(e.textContent||'').replace(/\s+/g,' ').trim();if(t)set.set(e,t)}});return set};
      D.slides.forEach((sl,i)=>{
        D.show(i,0,'fwd'); const max=sl._max||0; const steps=[]; let prev=snap(sl); const prevTexts=new Set([...prev.values()]);
        for(let s=1;s<=max;s++){D.show(i,s,'fwd');const cur=snap(sl);const apps=[];cur.forEach((t,e)=>{if(!prevTexts.has(t)&&!apps.includes(t))apps.push(t)});cur.forEach(t=>prevTexts.add(t));steps.push({s,appear:apps.slice(0,8)})}
        const h=sl.querySelector('h1,h2,.big-title,.sec-title');
        const nt=sl.querySelector('.notes');
        out.push({n:i+1,cls:sl.className.replace(/\s*(active|entering|leaving)\b/g,'').trim(),title:(sl.dataset.title||(h&&h.textContent)||'').trim(),max,notes:nt?nt.textContent.replace(/\s+/g,' ').trim():'',steps,
          text:[...sl.querySelectorAll('h1,h2,p,li,td,th,pre.code')].filter(e=>!e.closest('.notes')).map(e=>e.textContent.replace(/\s+/g,' ').trim()).filter(Boolean).slice(0,40)});
      });
      return out});
    fs.writeFileSync(__dirname+'/struktur/'+f.replace('.html','.json'),JSON.stringify(data,null,1));
    console.log(f,data.length,data.reduce((a,s)=>a+s.max,0)+' steps');
  }
  await b.close();
})();
