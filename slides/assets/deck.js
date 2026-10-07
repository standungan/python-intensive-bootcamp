/* ===== Deck engine — Python Intensive Bootcamp (tanpa dependensi) ===== */
(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var NS='http://www.w3.org/2000/svg';
function el(tag,cls,html){var e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function svgEl(tag,attrs){var e=document.createElementNS(NS,tag);for(var k in attrs)e.setAttribute(k,attrs[k]);return e}
function maxOf(a){return a.reduce(function(m,v){return v>m?v:m},0)}

/* ---------- penyorot sintaks Python ---------- */
var KW={};'def class return if elif else for while in not and or is import from as try except finally raise with pass break continue lambda None True False global yield assert del'.split(' ').forEach(function(k){KW[k]=1});
var BI={};'print len range int float str bool list dict set tuple sum min max sorted open input type isinstance enumerate zip map filter abs round super self'.split(' ').forEach(function(k){BI[k]=1});
function hlLine(line,st){
  if(st.lang==='text')return esc(line);
  if(st.lang==='bash'){return esc(line).replace(/^(\$ ?)/,'<span class="t-k">$1</span>').replace(/(#.*)$/,'<span class="t-c">$1</span>')}
  var out='',i=0,n=line.length,prevKw='';
  if(st.tq){var e=line.indexOf(st.tq);if(e<0)return '<span class="t-s">'+esc(line)+'</span>';out+='<span class="t-s">'+esc(line.slice(0,e+3))+'</span>';i=e+3;st.tq=null}
  while(i<n){
    var r=line.slice(i),m;
    if((m=/^#.*/.exec(r))){out+='<span class="t-c">'+esc(m[0])+'</span>';i+=m[0].length;continue}
    if((m=/^[fFrRbB]?("""|''')/.exec(r))){var q=m[1],rest=r.slice(m[0].length),e2=rest.indexOf(q);
      if(e2<0){out+='<span class="t-s">'+esc(r)+'</span>';st.tq=q;i=n;continue}
      var len=m[0].length+e2+3;out+='<span class="t-s">'+esc(r.slice(0,len))+'</span>';i+=len;continue}
    if((m=/^[fFrRbB]?"(?:\\.|[^"\\])*"/.exec(r))||(m=/^[fFrRbB]?'(?:\\.|[^'\\])*'/.exec(r))){out+='<span class="t-s">'+esc(m[0])+'</span>';i+=m[0].length;continue}
    if((m=/^\d[\d_]*(?:\.\d+)?/.exec(r))){out+='<span class="t-n">'+m[0]+'</span>';i+=m[0].length;continue}
    if((m=/^[A-Za-z_][A-Za-z0-9_]*/.exec(r))){var w=m[0],cls='';
      if(KW[w])cls='t-k';else if(prevKw==='def'||prevKw==='class')cls='t-f';else if(BI[w]&&w!=='self')cls='t-b';else if(/^\s*\(/.test(r.slice(w.length)))cls='t-f';
      out+=cls?'<span class="'+cls+'">'+w+'</span>':w;prevKw=KW[w]?w:'';i+=w.length;continue}
    out+=esc(r[0]);i++;if(!/\s/.test(r[0]))prevKw='';
  }
  return out;
}

/* ---------- komponen kode ---------- */
function initCode(pre){
  var lang=pre.dataset.lang||'py';
  var raw=pre.textContent.replace(/\n$/,'').split('\n');
  var reveal=JSON.parse(pre.dataset.reveal||'[]'),focus=JSON.parse(pre.dataset.focus||'{}');
  var st={lang:lang,tq:null};pre.textContent='';
  var lines=raw.map(function(l){var s=el('span','ln');s.innerHTML=hlLine(l,st)||'&nbsp;';pre.appendChild(s);return s});
  if(lang!=='py')pre.appendChild(el('span','lang',lang==='bash'?'terminal':lang));
  var fkeys=Object.keys(focus).map(Number).sort(function(a,b){return a-b});
  var steps=Math.max(maxOf(reveal),maxOf(fkeys));var prev=-1;
  return {steps:steps,set:function(s){
    var fk=null;fkeys.forEach(function(k){if(k<=s)fk=k});
    var fset=fk!=null?focus[fk]:null;
    lines.forEach(function(ln,i){
      var vis=(reveal[i]||0)<=s,was=!ln.classList.contains('hide');
      ln.classList.toggle('hide',!vis);
      if(vis&&!was&&prev>=0&&s>prev){ln.classList.remove('enter');void ln.offsetWidth;ln.classList.add('enter')}
      ln.classList.toggle('focus',!!fset&&fset.indexOf(i)>=0);
      ln.classList.toggle('dim',!!fset&&fset.indexOf(i)<0);
    });
    prev=s;
  }};
}

/* ---------- registri widget ---------- */
var W={},uid=0;

W.boxes=function(host,c){
  host.classList.add('w-boxes');var items=c.items;
  var els=items.map(function(it){var b=el('div','b','<div class="nm">'+esc(it.name)+'</div><div class="v">'+esc(it.val)+'</div>'+(it.type?'<div class="ty">'+esc(it.type)+'</div>':''));host.appendChild(b);return b});
  var steps=0;items.forEach(function(it){steps=Math.max(steps,it.at||0);(it.changes||[]).forEach(function(ch){steps=Math.max(steps,ch.at)})});
  return {steps:steps,set:function(s){items.forEach(function(it,i){
    var b=els[i];b.classList.toggle('on',s>=(it.at||0));var val=it.val,ty=it.type;
    (it.changes||[]).forEach(function(ch){if(s>=ch.at){val=ch.val;if(ch.type)ty=ch.type}});
    var v=$('.v',b);if(v.textContent!==String(val)){v.textContent=val;v.classList.add('flash');setTimeout(function(){v.classList.remove('flash')},650)}
    var t=$('.ty',b);if(t&&ty!=null)t.textContent=ty;
  })}};
};

W.flow=function(host,c){
  host.classList.add('w-flow');host.style.width=c.w+'px';host.style.height=c.h+'px';
  var id=++uid,svg=svgEl('svg',{width:c.w,height:c.h});
  var defs=svgEl('defs',{});[['dim','var(--line)'],['on','var(--acc)'],['bad','var(--bad)']].forEach(function(m){
    var mk=svgEl('marker',{id:'mk'+id+m[0],viewBox:'0 0 12 12',refX:'11',refY:'6',markerWidth:'12',markerHeight:'12',markerUnits:'userSpaceOnUse',orient:'auto'});
    mk.appendChild(svgEl('path',{d:'M0,1 L11,6 L0,11 z',style:'fill:'+m[1]}));defs.appendChild(mk)});
  svg.appendChild(defs);host.appendChild(svg);
  var nodes={};
  c.nodes.forEach(function(n){var d=el('div','nd k-'+(n.k||'p'),esc(n.t).replace(/\n/g,'<br>'));
    d.style.cssText='left:'+n.x+'px;top:'+n.y+'px;width:'+n.w+'px;height:'+(n.h||56)+'px';host.appendChild(d);nodes[n.id]={n:n,d:d}});
  function pt(n,tx,ty){var cx=n.x+n.w/2,cy=n.y+(n.h||56)/2,dx=tx-cx,dy=ty-cy,hw=n.w/2,hh=(n.h||56)/2;
    var sc=Math.min(dx?hw/Math.abs(dx):1e9,dy?hh/Math.abs(dy):1e9);return [cx+dx*sc,cy+dy*sc]}
  function ats(x){return x==null?[]:(Array.isArray(x)?x:[x])}
  function mn(x){var a=ats(x);return a.length?Math.min.apply(null,a):null}
  var eds=(c.edges||[]).map(function(e){
    var a=nodes[e.a].n,b=nodes[e.b].n,ac=[a.x+a.w/2,a.y+(a.h||56)/2],bc=[b.x+b.w/2,b.y+(b.h||56)/2];
    var p1=pt(a,bc[0],bc[1]),p2=pt(b,ac[0],ac[1]),d;
    if(e.bend){var mx=(p1[0]+p2[0])/2,my=(p1[1]+p2[1])/2,dx=p2[0]-p1[0],dy=p2[1]-p1[1],L=Math.sqrt(dx*dx+dy*dy)||1;
      d='M'+p1[0]+','+p1[1]+' Q'+(mx-dy/L*e.bend)+','+(my+dx/L*e.bend)+' '+p2[0]+','+p2[1]}
    else d='M'+p1[0]+','+p1[1]+' L'+p2[0]+','+p2[1];
    var path=svgEl('path',{d:d,'class':'ed','marker-end':'url(#mk'+id+'dim)'});svg.appendChild(path);
    var lab=null;if(e.l){var bx=e.bend?(p1[0]+p2[0])/2-(p2[1]-p1[1])/(Math.sqrt(Math.pow(p2[0]-p1[0],2)+Math.pow(p2[1]-p1[1],2))||1)*e.bend/2:(p1[0]+p2[0])/2,
      by=e.bend?(p1[1]+p2[1])/2+(p2[0]-p1[0])/(Math.sqrt(Math.pow(p2[0]-p1[0],2)+Math.pow(p2[1]-p1[1],2))||1)*e.bend/2:(p1[1]+p2[1])/2;
      lab=svgEl('text',{x:bx+(e.lx||8),y:by+(e.ly||-8),'class':'el'});lab.textContent=e.l;svg.appendChild(lab)}
    return {e:e,path:path,lab:lab}});
  var steps=0;c.nodes.forEach(function(n){ats(n.at).forEach(function(v){steps=Math.max(steps,v)})});(c.edges||[]).forEach(function(e){ats(e.at).forEach(function(v){steps=Math.max(steps,v)})});
  return {steps:steps,set:function(s){
    c.nodes.forEach(function(n){var d=nodes[n.id].d;d.classList.remove('act','done','bad');
      var A=ats(n.at);if(!A.length)return;var m=Math.min.apply(null,A);if(s<m)return;
      if(A.indexOf(s)>=0)d.classList.add(n.bad?'bad':'act');else d.classList.add(n.bad?'bad':'done')});
    eds.forEach(function(x){var m=mn(x.e.at),on=m!=null&&s>=m;x.path.classList.toggle('on',on&&!x.e.bad);x.path.classList.toggle('bad',on&&!!x.e.bad);
      x.path.setAttribute('marker-end','url(#mk'+id+(on?(x.e.bad?'bad':'on'):'dim')+')');if(x.lab)x.lab.classList.toggle('on',on)});
  }};
};

function cellsOf(spec,R,C){
  if(Array.isArray(spec))return [spec];var out=[],m,r,c;
  if(spec==='all'){for(r=0;r<R;r++)for(c=0;c<C;c++)out.push([r,c]);return out}
  if((m=/^r:(\d+)(?:-(\d+))?$/.exec(spec))){var a=+m[1],b=m[2]!=null?+m[2]:a;for(r=a;r<=b;r++)for(c=0;c<C;c++)out.push([r,c]);return out}
  if((m=/^c:(\d+)(?:-(\d+))?$/.exec(spec))){var a2=+m[1],b2=m[2]!=null?+m[2]:a2;for(c=a2;c<=b2;c++)for(r=0;r<R;r++)out.push([r,c]);return out}
  return out;
}
W.grid=function(host,c){
  host.classList.add('w-grid');if(c.cw)host.style.setProperty('--cw',c.cw+'px');if(c.ch)host.style.setProperty('--ch',c.ch+'px');if(c.gf)host.style.setProperty('--gf',c.gf+'px');
  var t=el('table');var rows=c.rows,R=rows.length,C=rows[0].length,cells=[],base=[];
  if(c.head){var tr=el('tr');if(c.idx)tr.appendChild(el('th'));c.head.forEach(function(h){tr.appendChild(el('th','ch',esc(h)))});t.appendChild(tr)}
  rows.forEach(function(row,r){var tr=el('tr');if(c.idx)tr.appendChild(el('th',null,esc(c.idx[r])));cells[r]=[];base[r]=[];
    row.forEach(function(v,cc){var td=el('td',null,esc(v));tr.appendChild(td);cells[r][cc]=td;base[r][cc]=String(v)});t.appendChild(tr)});
  var app=(c.append||[]).map(function(a){var tr=el('tr','app off');if(c.idx)tr.appendChild(el('th',null,esc(a.label||'')));
    a.row.forEach(function(v,cc){var td=el('td','g',esc(v));tr.appendChild(td)});t.appendChild(tr);return {a:a,tr:tr}});
  host.appendChild(t);
  var steps=0;(c.hl||[]).concat(c.vals||[],c.append||[]).forEach(function(h){steps=Math.max(steps,h.at)});
  var cur=[];for(var r=0;r<R;r++){cur[r]=[];for(var cc=0;cc<C;cc++)cur[r][cc]=base[r][cc]}
  return {steps:steps,set:function(s){
    for(var r=0;r<R;r++)for(var k=0;k<C;k++){cells[r][k].className='';}
    (c.hl||[]).forEach(function(h){if(h.at>s)return;if(h.clear){for(var r=0;r<R;r++)for(var k=0;k<C;k++)cells[r][k].className='';return}
      (h.cells||[]).forEach(function(sp){cellsOf(sp,R,C).forEach(function(p){if(cells[p[0]]&&cells[p[0]][p[1]])cells[p[0]][p[1]].className=h.cls||'a'})})});
    for(var r2=0;r2<R;r2++)for(var k2=0;k2<C;k2++)cells[r2][k2].textContent=base[r2][k2];
    (c.vals||[]).forEach(function(x){if(x.at>s)return;(x.cells||[]).forEach(function(sp){cellsOf(sp,R,C).forEach(function(p){
      var td=cells[p[0]][p[1]];td.textContent=x.text;if(x.at===s){td.classList.add('chg')}})})});
    app.forEach(function(x){x.tr.classList.toggle('off',s<x.a.at)});
  }};
};

W.conv=function(host,c){
  host.classList.add('w-conv');var keep=c.keep||c.items.map(function(){return true});
  var lab1=el('div','lab',esc(c.lin||'input')),laneIn=el('div','lane'),fn=el('div','fn',esc(c.fn)),lab2=el('div','lab',esc(c.lout||'hasil')),laneOut=el('div','lane');
  var ins=c.items.map(function(v){var d=el('div','it',esc(v));laneIn.appendChild(d);return d});
  var outs=[],map=[];
  c.items.forEach(function(v,i){if(keep[i]){var o=el('div','it out-it',esc((c.out||c.items)[outs.length]));laneOut.appendChild(o);map[i]=outs.length;outs.push(o)}});
  [lab1,laneIn,el('div','arrow','↓'),fn,el('div','arrow','↓'),lab2,laneOut].forEach(function(e){host.appendChild(e)});
  return {steps:c.items.length,set:function(s){
    ins.forEach(function(d,i){d.classList.remove('pick','used','drop');
      if(i<s-1)d.classList.add(keep[i]?'used':'drop');else if(i===s-1)d.classList.add(keep[i]?'pick':'drop')});
    outs.forEach(function(o,j){var idx=map.indexOf(j);o.classList.toggle('on',idx<s)});
    if(s>0){fn.classList.add('pulse');setTimeout(function(){fn.classList.remove('pulse')},450)}
  }};
};

W.chart=function(host,c){
  host.classList.add('w-chart');var w=c.w||900,h=c.h||380,m={l:70,r:30,t:c.title?58:24,b:c.xl?72:48};
  host.style.width=w+'px';host.style.height=h+'px';
  var svg=svgEl('svg',{viewBox:'0 0 '+w+' '+h});host.appendChild(svg);
  var iw=w-m.l-m.r,ih=h-m.t-m.b,kind=c.kind||'bar',series=c.series;
  var all=[];series.forEach(function(s){all=all.concat(s.data)});
  var ymax=c.ymax||(function(){var mx=Math.max.apply(null,all),p=Math.pow(10,Math.floor(Math.log10(mx||1)));return Math.ceil(mx*1.1/p*2)/2*p})();
  function Y(v){return m.t+ih-(v/ymax)*ih}
  var g0=svgEl('g',{'class':'fade'});svg.appendChild(g0);
  for(var i=0;i<=4;i++){var yy=m.t+ih-ih*i/4;g0.appendChild(svgEl('line',{x1:m.l,x2:w-m.r,y1:yy,y2:yy,'class':'gl'}));
    var tx=svgEl('text',{x:m.l-12,y:yy+6,'text-anchor':'end'});tx.textContent=Math.round(ymax*i/4*10)/10;g0.appendChild(tx)}
  g0.appendChild(svgEl('line',{x1:m.l,x2:m.l,y1:m.t,y2:m.t+ih,'class':'ax'}));g0.appendChild(svgEl('line',{x1:m.l,x2:w-m.r,y1:m.t+ih,y2:m.t+ih,'class':'ax'}));
  var n=(c.labels||[]).length||series[0].data.length,slot=iw/n;
  (c.labels||[]).forEach(function(l,i){var tx=svgEl('text',{x:m.l+slot*(i+.5),y:m.t+ih+28,'text-anchor':'middle'});tx.textContent=l;g0.appendChild(tx)});
  var data=[],gD=svgEl('g',{});svg.appendChild(gD);
  if(kind==='bar'||kind==='hist'){var ns=series.length,bw=kind==='hist'?slot-3:Math.min(80,slot*.7/ns);
    series.forEach(function(s,si){s.data.forEach(function(v,i){
      var x=m.l+slot*i+(slot-bw*ns)/2+bw*si;var r=svgEl('rect',{x:x,width:bw,y:m.t+ih,height:0,rx:kind==='hist'?0:6,'class':'bar s'+si});gD.appendChild(r);
      var t=svgEl('text',{x:x+bw/2,y:Y(v)-8,'class':'val fade'});t.textContent=v;if(kind!=='hist')gD.appendChild(t);data.push({r:r,v:v,t:t})})})}
  else if(kind==='line'){series.forEach(function(s,si){var pts=s.data.map(function(v,i){return [m.l+slot*(i+.5),Y(v)]});
    var p=svgEl('path',{d:'M'+pts.map(function(p){return p.join(',')}).join(' L'),'class':'ln s'+si,pathLength:1,'stroke-dasharray':1,'stroke-dashoffset':1});gD.appendChild(p);
    var dots=pts.map(function(q){var d=svgEl('circle',{cx:q[0],cy:q[1],r:0,'class':'pt',style:si?'fill:var(--acc2)':''});gD.appendChild(d);return d});data.push({p:p,dots:dots})})}
  else if(kind==='scatter'){series.forEach(function(s){(c.xs||[]).forEach(function(xv,i){var d=svgEl('circle',{cx:m.l+iw*xv/(c.xmax||1),cy:Y(s.data[i]),r:0,'class':'pt',style:'transition-delay:'+(i*40)+'ms'});gD.appendChild(d);data.push({d:d})})})}
  var gT=svgEl('g',{'class':'fade'});svg.appendChild(gT);
  if(c.title){var t=svgEl('text',{x:w/2,y:30,'text-anchor':'middle','class':'ttl'});t.textContent=c.title;gT.appendChild(t)}
  if(c.xl){var t2=svgEl('text',{x:m.l+iw/2,y:h-14,'text-anchor':'middle'});t2.textContent=c.xl;gT.appendChild(t2)}
  if(c.yl){var t3=svgEl('text',{x:18,y:m.t+ih/2,'text-anchor':'middle',transform:'rotate(-90 18 '+(m.t+ih/2)+')'});t3.textContent=c.yl;gT.appendChild(t3)}
  var gL=svgEl('g',{'class':'fade'});svg.appendChild(gL);
  if(series.length>1||c.note){var lx=w-m.r-10;series.forEach(function(s,si){var y=m.t+14+si*26;
    gL.appendChild(svgEl('rect',{x:lx-170,y:y-12,width:18,height:18,rx:4,style:'fill:'+(si?'var(--acc2)':'var(--acc)')}));
    var tx=svgEl('text',{x:lx-144,y:y+3});tx.textContent=s.name||('seri '+(si+1));gL.appendChild(tx)});
    if(c.note){var nt=svgEl('text',{x:m.l+iw/2,y:m.t+ih/2,'text-anchor':'middle',style:'font-size:24px;fill:var(--acc2);font-weight:700'});nt.textContent=c.note;gL.appendChild(nt)}}
  var steps=(series.length>1||c.note)?4:3;
  return {steps:steps,set:function(s){
    g0.classList.toggle('on',s>=1);gT.classList.toggle('on',s>=3);gL.classList.toggle('on',s>=4);
    data.forEach(function(d,i){
      if(d.r){var on=s>=2;d.r.setAttribute('y',on?Y(d.v):m.t+ih);d.r.setAttribute('height',on?m.t+ih-Y(d.v):0);d.r.style.transitionDelay=(i*70)+'ms';d.t.classList.toggle('on',on)}
      if(d.p){d.p.setAttribute('stroke-dashoffset',s>=2?0:1);d.dots.forEach(function(q,j){q.setAttribute('r',s>=2?6:0);q.style.transitionDelay=s>=2?(900+j*60)+'ms':'0ms'})}
      if(d.d){d.d.setAttribute('r',s>=2?7:0);d.d.style.opacity=s>=2?.85:0}
    });
  }};
};

W.seq=function(host,c){
  host.classList.add('w-seq');host.style.width=c.w+'px';host.style.height=c.h+'px';
  c.actors.forEach(function(a){var d=el('div','act',esc(a.n));d.style.left=a.x+'px';host.appendChild(d);var l=el('div','life');l.style.left=a.x+'px';host.appendChild(l)});
  var msgs=c.msgs.map(function(m){var xf=c.actors[m.f].x,xt=c.actors[m.t].x,rev=xt<xf;
    var d=el('div','msg'+(rev?' rev':'')+(m.bad?' bad':''),'<div class="lbl">'+esc(m.l)+'</div><div class="ar"></div>');
    d.style.left=Math.min(xf,xt)+8+'px';d.style.width=Math.abs(xt-xf)-16+'px';d.style.top=m.y+'px';host.appendChild(d);return {m:m,d:d}});
  return {steps:maxOf(c.msgs.map(function(m){return m.at})),set:function(s){msgs.forEach(function(x){x.d.classList.toggle('on',s>=x.m.at)})}};
};

W.tree=function(host,c){
  host.classList.add('w-tree');var IC={dir:'▾',file:'▪',cls:'◆',node:'▸'};
  var rows=c.nodes.map(function(n){var d=el('div','tn '+(n.k||'file'),'<span class="ic">'+(n.ic||IC[n.k||'file'])+'</span><span class="tt">'+esc(n.t)+'</span>'+(n.n?'<span class="nt">'+esc(n.n)+'</span>':''));
    d.style.marginLeft=(n.d||0)*34+'px';host.appendChild(d);return {n:n,d:d}});
  return {steps:maxOf(c.nodes.map(function(n){return Math.max(n.at||0,n.hl||0)})),set:function(s){
    rows.forEach(function(x){x.d.classList.toggle('on',s>=(x.n.at||0));x.d.classList.toggle('hl',x.n.hl!=null&&s===x.n.hl)})}};
};

W.venn=function(host,c){
  host.classList.add('w-venn');var w=c.w||700,h=c.h||300;host.style.width=w+'px';host.style.height=h+'px';
  var d=h-20,ov=d*.42,lx=(w-(2*d-ov))/2;
  var ca=el('div','c');ca.style.cssText='left:'+lx+'px;top:10px;width:'+d+'px;height:'+d+'px';
  var cb=el('div','c b');cb.style.cssText='left:'+(lx+d-ov)+'px;top:10px;width:'+d+'px;height:'+d+'px';host.appendChild(ca);host.appendChild(cb);
  var na=el('div','nm acc',esc(c.a.n));na.style.cssText='left:'+(lx+d*.18)+'px;top:-6px';var nb=el('div','nm acc2',esc(c.b.n));nb.style.cssText='left:'+(lx+d*1.62-ov)+'px;top:-6px';host.appendChild(na);host.appendChild(nb);
  var cx=w/2;function reg(items,x,y){var r=el('div','reg',items.map(esc).join('<br>'));r.style.cssText='left:'+(x-70)+'px;top:'+y+'px;width:140px';host.appendChild(r);return r}
  var ra=reg(c.a.only,lx+(d-ov)/2,d*.3),rb=reg(c.b.only,lx+d-ov+ov+(d-ov)/2,d*.3),rc=reg(c.both,cx,d*.3);
  var cap=el('div','',''),capH=el('div','sm mut');cap.style.cssText='position:absolute;left:0;right:0;bottom:-34px;text-align:center';cap.appendChild(capH);host.appendChild(cap);
  var map={a_only:[ra],b_only:[rb],both:[rc],union:[ra,rb,rc],a:[ra,rc],b:[rb,rc]};
  return {steps:maxOf(c.steps.map(function(x){return x.at})),set:function(s){
    var cur=null;c.steps.forEach(function(x){if(x.at<=s)cur=x});
    [ra,rb,rc].forEach(function(r){r.classList.remove('hl','dm')});
    if(cur){var hs=map[cur.hl]||[];[ra,rb,rc].forEach(function(r){r.classList.add(hs.indexOf(r)>=0?'hl':'dm')});capH.innerHTML=cur.label||''}else capH.innerHTML='';
  }};
};

W.cards=function(host,c){
  host.classList.add('w-cards');
  var bp=el('div','bp','<h4>'+esc(c.bp.t)+'</h4>'+(c.bp.attrs?'<div>'+c.bp.attrs.map(esc).join('<br>')+'</div>':'')+(c.bp.methods?'<div style="margin-top:8px;color:var(--acc2)">'+c.bp.methods.map(esc).join('<br>')+'</div>':''));
  var stk=el('div','stk');var ins=c.ins.map(function(i){var d=el('div','ins','<h4>'+esc(i.t)+'</h4><div>'+i.vals.map(function(v){return esc(v[0])+' = <b>'+esc(v[1])+'</b>'}).join('<br>')+'</div>');stk.appendChild(d);return d});
  host.appendChild(bp);host.appendChild(el('div','mid','→'));host.appendChild(stk);
  return {steps:c.ins.length,set:function(s){ins.forEach(function(d,i){d.classList.toggle('on',s>=(c.ins[i].at||i+1))})}};
};

W.nest=function(host,c){
  host.classList.add('w-nest');var rootEl=host,lv=[];
  c.levels.forEach(function(l,i){var d=el('div','lv','<div class="lt">'+esc(l.t)+'</div>');
    var vars=(l.vars||[]).map(function(v){var s=el('span','vr',esc(v.t));d.appendChild(s);return {v:v,s:s}});
    rootEl.appendChild(d);rootEl=d;lv.push({l:l,d:d,vars:vars})});
  return {steps:maxOf([].concat.apply([],c.levels.map(function(l){return [l.at||0].concat((l.hl||[]),(l.vars||[]).map(function(v){return Math.max(v.at||0,v.hl||0)}))}))),set:function(s){
    lv.forEach(function(x){x.d.classList.toggle('on',s>=(x.l.at||0));x.d.classList.toggle('hl',(x.l.hl||[]).indexOf(s)>=0);
      x.vars.forEach(function(y){y.s.style.display=s>=(y.v.at||0)?'inline-block':'none';y.s.classList.toggle('hl',y.v.hl===s)})})}};
};

W.merge=function(host,c){
  host.classList.add('w-merge');
  function tbl(t,keyIdx){var tb=el('div','','<div class="ti">'+esc(t.t)+'</div>');var tt=el('table');
    var tr=el('tr');t.head.forEach(function(h,i){tr.appendChild(el('th',i===keyIdx?'key':'',esc(h)))});tt.appendChild(tr);
    var trs=t.rows.map(function(r){var q=el('tr');r.forEach(function(v,i){q.appendChild(el('td',i===keyIdx?'key':'',esc(v)))});tt.appendChild(q);return q});
    tb.appendChild(tt);return {box:tb,trs:trs,ths:$$('th',tt),tds:$$('td.key',tt)}}
  var L=tbl(c.left,c.left.key),Rr=tbl(c.right,c.right.key),Z=tbl(c.res,-1);
  var op=el('div','op','⋈');Z.box.classList.add('res');
  host.appendChild(L.box);host.appendChild(el('div','op','+'));host.appendChild(Rr.box);host.appendChild(op);host.appendChild(Z.box);
  return {steps:3,set:function(s){
    $$('th.key',host).forEach(function(e){e.classList.toggle('on',s>=1)});$$('td.key',host).forEach(function(e){e.classList.toggle('on',s>=1)});
    L.trs.forEach(function(r,i){var m=c.matches.some(function(x){return x[0]===i});r.className=s>=2?(m?'m':'u'):''});
    Rr.trs.forEach(function(r,i){var m=c.matches.some(function(x){return x[1]===i});r.className=s>=2?(m?'m':'u'):''});
    op.classList.toggle('on',s>=3);Z.box.classList.toggle('on',s>=3)}};
};

W.timeline=function(host,c){
  host.classList.add('w-tl');var tot=c.items.reduce(function(a,b){return a+b.m},0);
  var bar=el('div','bar'),leg=el('div','legend');
  var COL=['var(--acc)','var(--acc2)','var(--ok)','var(--pur)','var(--bad)','#7dd3fc'];
  var segs=c.items.map(function(it,i){var s=el('div','seg',esc(it.t));s.style.cssText='width:'+(it.m/tot*100)+'%;background:'+(it.c||COL[i%COL.length]);bar.appendChild(s);
    var l=el('div','',esc(it.m)+' '+(c.unit||'mnt'));l.style.width=(it.m/tot*100)+'%';leg.appendChild(l);return s});
  host.appendChild(bar);host.appendChild(leg);
  return {steps:c.items.length,set:function(s){segs.forEach(function(x,i){x.classList.toggle('on',s>=i+1)})}};
};

W.timer=function(host,c){
  host.classList.add('w-timer');var total=(c.m||10)*60,left=total,iv=null;
  var tm=el('div','tm'),bt=el('div','bt'),b1=el('button','','▶ Mulai'),b2=el('button','','⟲ Reset');bt.appendChild(b1);bt.appendChild(b2);host.appendChild(tm);host.appendChild(bt);
  function draw(){var m=Math.floor(left/60),s=left%60;tm.textContent=(m<10?'0':'')+m+':'+(s<10?'0':'')+s;host.classList.toggle('low',left<=60&&left>0)}
  function stop(){clearInterval(iv);iv=null;b1.textContent='▶ Mulai'}
  b1.onclick=function(e){e.stopPropagation();if(iv){stop();return}if(left<=0)left=total;b1.textContent='⏸ Jeda';iv=setInterval(function(){left--;draw();if(left<=0)stop()},1000)};
  b2.onclick=function(e){e.stopPropagation();stop();left=total;draw()};
  draw();return {steps:0,set:function(){},leave:stop,toggle:function(){b1.click()}};
};

/* ---------- mesin slide ---------- */
var params=new URLSearchParams(location.search),PRINT=params.has('print');
var stage=$('#stage'),deckEl=$('#deck'),slides=$$('.slide',deckEl),N=slides.length;
var cur=-1,step=0,ui={};
slides.forEach(function(sl,i){
  var ws=[];
  $$('.w',sl).forEach(function(h){var f=W[h.dataset.w];if(!f){console.error('widget tidak dikenal',h.dataset.w);return}ws.push(f(h,JSON.parse(h.dataset.cfg||'{}')))});
  $$('pre.code',sl).forEach(function(p){ws.push(initCode(p))});
  $$('.stagger',sl).forEach(function(p){Array.prototype.forEach.call(p.children,function(ch,k){if(ch.hasAttribute('data-anim')&&!ch.hasAttribute('data-step'))ch.style.setProperty('--d',(0.12+k*0.09)+'s')})});
  sl._ws=ws;
  sl._max=Math.max(0,maxOf($$('[data-step]',sl).map(function(e){return +e.dataset.step})),maxOf($$('[data-step-out]',sl).map(function(e){return +e.dataset.stepOut})),maxOf(ws.map(function(w){return w.steps||0})));
  sl._title=sl.dataset.title||(($('h1,h2',sl)||{}).textContent||('Slide '+(i+1))).replace(/\s+/g,' ').trim();
});
function applyStep(sl,s){
  $$('[data-step]',sl).forEach(function(e){e.classList.toggle('shown',s>=+e.dataset.step)});
  $$('[data-step-out]',sl).forEach(function(e){e.classList.toggle('gone',s>=+e.dataset.stepOut)});
  sl._ws.forEach(function(w){w.set(s)});
}
function fit(){var k=Math.min(innerWidth/1280,innerHeight/720);stage.style.transform='translate(-50%,-50%) scale('+k+')'}
function updateUI(){
  ui.cnt.textContent=(cur+1)+' / '+N;var sl=slides[cur];
  ui.prog.style.width=((cur+(sl._max?step/sl._max:0)*0.999)/Math.max(1,N-1)*100)+'%';
  var nt=$('.notes',sl);ui.notes.innerHTML=nt?nt.innerHTML:'<i>(tidak ada catatan)</i>';
  try{history.replaceState(null,'','#'+(cur+1)+(step?'.'+step:''))}catch(e){}
}
function show(i,s,dir){
  i=Math.max(0,Math.min(N-1,i));var prev=cur;
  if(i!==prev){
    var nx=slides[i],type='t-'+(nx.dataset.transition||deckEl.dataset.transition||'slide');
    if(prev>=0){var ps=slides[prev];ps.classList.remove('active','entering');ps._ws.forEach(function(w){w.leave&&w.leave()});
      ps.className=ps.className.replace(/\bt-\w+|\bfwd\b|\bback\b/g,'').trim();
      ps.classList.add('leaving',type,dir||'fwd');(function(p){setTimeout(function(){p.classList.remove('leaving','fwd','back')},450)})(ps)}
    nx.className=nx.className.replace(/\bt-\w+|\bfwd\b|\bback\b|\bleaving\b/g,'').trim();
    nx.classList.add('active','entering',type,dir||'fwd');(function(p){setTimeout(function(){p.classList.remove('entering')},700)})(nx);
    cur=i;
  }
  step=Math.max(0,Math.min(s||0,slides[cur]._max));applyStep(slides[cur],step);updateUI();
}
function next(){var sl=slides[cur];if(step<sl._max){step++;applyStep(sl,step);updateUI()}else if(cur<N-1)show(cur+1,0,'fwd')}
function prev(){if(step>0){step--;applyStep(slides[cur],step);updateUI()}else if(cur>0)show(cur-1,slides[cur-1]._max,'back')}

function buildUI(){
  var p=el('div');p.id='prog';document.body.appendChild(p);ui.prog=p;
  var n=el('div');n.id='notes';document.body.appendChild(n);ui.notes=n;
  var t=el('div');t.id='timer';t.textContent='00:00';document.body.appendChild(t);ui.timer=t;
  var h=el('div');h.id='help';h.innerHTML='<b>Pintasan</b><br><kbd>→</kbd><kbd>Space</kbd> maju &nbsp; <kbd>←</kbd> mundur<br><kbd>Home</kbd><kbd>End</kbd> awal / akhir<br><kbd>O</kbd> daftar slide &nbsp; <kbd>N</kbd> catatan<br><kbd>T</kbd> timer sesi &nbsp; <kbd>L</kbd> tema terang/gelap<br><kbd>F</kbd> layar penuh &nbsp; <kbd>C</kbd> mulai/jeda timer latihan<br><kbd>?</kbd> bantuan';document.body.appendChild(h);ui.help=h;
  var o=el('div');o.id='overview';document.body.appendChild(o);ui.ov=o;
  var u=el('div');u.id='ui';u.innerHTML='<div class="bar"><button data-a="prev" title="Mundur (←)">◀</button><button data-a="next" title="Maju (→)">▶</button><button data-a="ov" title="Daftar slide (O)">☰</button><button data-a="notes" title="Catatan (N)">📝</button><button data-a="timer" title="Timer sesi (T)">⏱</button><button data-a="theme" title="Tema (L)">◐</button><button data-a="fs" title="Layar penuh (F)">⛶</button><button data-a="help" title="Bantuan (?)">?</button></div><div class="cnt"></div>';
  document.body.appendChild(u);ui.bar=u;ui.cnt=$('.cnt',u);
  u.addEventListener('click',function(e){var a=e.target.getAttribute&&e.target.getAttribute('data-a');if(!a)return;e.stopPropagation();act(a)});
}
var t0=null,tiv=null;
function act(a){
  if(a==='next')next();else if(a==='prev')prev();
  else if(a==='ov')toggleOv();else if(a==='notes')ui.notes.classList.toggle('on');
  else if(a==='help')ui.help.classList.toggle('on');
  else if(a==='theme'){document.documentElement.classList.toggle('light');try{localStorage.setItem('deckTheme',document.documentElement.classList.contains('light')?'light':'dark')}catch(e){}}
  else if(a==='fs'){if(!document.fullscreenElement)document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();else document.exitFullscreen()}
  else if(a==='timer'){ui.timer.classList.toggle('on');if(!tiv){t0=Date.now();tiv=setInterval(function(){var s=Math.floor((Date.now()-t0)/1000);ui.timer.textContent=('0'+Math.floor(s/60)).slice(-2)+':'+('0'+s%60).slice(-2)},1000)}}
  else if(a==='ctimer'){slides[cur]._ws.forEach(function(w){w.toggle&&w.toggle()})}
}
function toggleOv(){
  if(ui.ov.classList.contains('on')){ui.ov.classList.remove('on');return}
  ui.ov.innerHTML='<h3>Daftar slide — klik untuk lompat (Esc untuk menutup)</h3><div class="gr">'+slides.map(function(s,i){return '<div class="it'+(i===cur?' cur':'')+'" data-i="'+i+'"><small>'+(i+1)+'</small>'+esc(s._title)+'</div>'}).join('')+'</div>';
  ui.ov.classList.add('on');var c=$('.cur',ui.ov);c&&c.scrollIntoView({block:'center'});
}
function init(){
  try{if(localStorage.getItem('deckTheme')==='light')document.documentElement.classList.add('light')}catch(e){}
  if(params.get('theme')==='light')document.documentElement.classList.add('light');
  if(PRINT){document.documentElement.classList.add('print');slides.forEach(function(sl){sl.classList.add('active');sl._ws.forEach(function(w){w.set(sl._max)});applyStep(sl,sl._max)});document.title+=' (cetak)';return}
  buildUI();fit();addEventListener('resize',fit);
  var m=/^#(\d+)(?:\.(\d+))?/.exec(location.hash),i0=m?(+m[1]-1):0,s0=m&&m[2]?+m[2]:0;
  show(Math.max(0,Math.min(N-1,i0)),s0,'fwd');
  slides[cur].classList.remove('entering');
  addEventListener('keydown',function(e){
    if(e.ctrlKey||e.metaKey||e.altKey)return;var k=e.key;
    if(ui.ov.classList.contains('on')){if(k==='Escape'||k==='o'||k==='O'){toggleOv()}return}
    if(k==='ArrowRight'||k==='ArrowDown'||k===' '||k==='PageDown'||k==='Enter'){e.preventDefault();next()}
    else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev()}
    else if(k==='Home'){show(0,0,'back')}else if(k==='End'){show(N-1,0,'fwd')}
    else if(k==='o'||k==='O'||k==='Escape')toggleOv();else if(k==='n'||k==='N')act('notes');else if(k==='t'||k==='T')act('timer');
    else if(k==='l'||k==='L')act('theme');else if(k==='f'||k==='F')act('fs');else if(k==='c'||k==='C')act('ctimer');else if(k==='?')act('help');
  });
  ui.ov.addEventListener('click',function(e){var it=e.target.closest&&e.target.closest('.it');if(it){var i=+it.dataset.i;toggleOv();show(i,0,i>cur?'fwd':'back')}});
  stage.addEventListener('click',function(e){if(e.target.closest('button,a,.w-timer'))return;var r=stage.getBoundingClientRect();(e.clientX-r.left)<r.width*.28?prev():next()});
  var tx=null;addEventListener('touchstart',function(e){tx=e.touches[0].clientX},{passive:true});
  addEventListener('touchend',function(e){if(tx==null)return;var dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)(dx<0?next:prev)();tx=null},{passive:true});
  var idle=null;function wake(){ui.bar.classList.remove('idle');document.body.style.cursor='';clearTimeout(idle);idle=setTimeout(function(){ui.bar.classList.add('idle');document.body.style.cursor='none'},2800)}
  addEventListener('mousemove',wake);wake();
  addEventListener('hashchange',function(){var m=/^#(\d+)(?:\.(\d+))?/.exec(location.hash);if(m){var i=+m[1]-1;if(i!==cur||(+m[2]||0)!==step)show(i,+m[2]||0,i>=cur?'fwd':'back')}});
}
window.DECK={next:next,prev:prev,show:show,slides:slides,get state(){return {cur:cur,step:step,max:slides[cur]._max}}};
init();
})();
