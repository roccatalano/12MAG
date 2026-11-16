"""12MAG slide templates. Every slide is built from one of these, so the layout never moves.

Zones on every slide: header (pill = type · source, left; VCAA % badge, right) · title line · body · footer (citation).
Question slides (Do Now, APK, Worked example, You try, Exit): LEFT = what is given (question text, data, figure, MC options),
RIGHT = what is produced (numbered working steps, one per click, then the answer box at the bottom right).
Reveal order is always: question → steps → answer (+ % badge).

Use: from tpl import *; build S=[title(...), qslide(...), ...]; assemble(S, '<title>', OUT)."""
import json, os, re
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
KIND={'dn':'Do Now','apk':'APK','we':'Worked example','yt':'You try','ex':'Exit task','learn':'Learn','cas':'CAS'}

def J(o): return json.dumps(o).replace("'","&#39;")
def box(rid,cfg): return f'<div class="chart" id="{rid}" data-chart="box" data-cfg=\'{J(cfg)}\'></div>'
def hist(rid,cfg,extra=''): return f'<div class="chart" id="{rid}" data-chart="hist" data-cfg=\'{J(cfg)}\' {extra}></div>'
def norm(rid,cfg,extra=''):
    """normal curve (tpl.js drawNorm). cfg: m, s, rows ['x','z'], hide ['x','z','pct'], xl, W, h, fs, dec, sh [[a,b,col,label]] (z units).
    Frag attrs: data-nshade="#id|a,b|col|label" (label: _ for spaces) · data-nshow="#id|x,z,pct" · data-nmark="#id|z|label|col\""""
    return f'<div class="chart" id="{rid}" data-chart="norm" data-cfg=\'{J(cfg)}\' {extra}></div>'
def dot(rid,cfg): return f'<div class="chart" id="{rid}" data-chart="dot3" data-cfg=\'{J(cfg)}\'></div>'
def stem(rid,rows,key,fs=24):
    i=0; tr=''
    for st,lv in rows:
        sp=''
        for l in lv: sp+=f'<span class="lf2" data-i="{i}">{l}</span>'; i+=1
        tr+=f'<tr><td class="st">{st}</td><td class="lv">{sp}</td></tr>'
    return f'<div><div class="stemcap">{key}</div><table class="stem3" id="{rid}" style="font-size:{fs}px">{tr}</table></div>'

# ---------- formulas: write once, substitute values, solve (animated) ----------
def plist(items):
    """multi-part question parts, listed down the page: [('a','the median'), ...]"""
    return '<ol class="parts">'+''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a,b in items)+'</ol>'
def F(*toks):
    """Build formula html. Tokens: plain str · V(name, value) a variable that flips to its value · FR(num, den) a fraction (each a list/tuple of tokens)."""
    out=''
    for t in toks:
        if isinstance(t,str): out+=t
        elif t[0]=='v': out+=f'<span class="fv"><i>{t[1]}</i><b>{t[2]}</b></span>'
        elif t[0]=='fr': out+=f'<span class="frac"><span>{F(*t[1])}</span><span>{F(*t[2])}</span></span>'
    return out
def V(name,value): return ('v',name,value)
def FR(num,den):
    """fraction; num/den: a token or a list of tokens"""
    L=lambda x:x if isinstance(x,list) else [x]
    return ('fr',L(num),L(den))
def fx(name,lhs,rhs,result,attrs='',ra=''):
    """One working step that models a key formula: click 1 shows the formula, click 2 substitutes the values (variables flip),
    click 3 shows the result. ra: attributes for the result click (e.g. an annotation on the question). name should match the Key formulas slide; lhs=None lets the step name stand as the left-hand side."""
    l=f'<span class="lhs">{lhs}</span> ' if lhs else ''
    html=(f'<span class="fx">{l}= <span class="rhs">{rhs}</span>'
          f'<span class="frag fxs" data-fx="sub"></span><span class="frag fxr" {ra}> = <b>{result}</b></span></span>')
    return (name,html,attrs)

def _stat(stat):
    """stat: None · ('mc', 90) % answered correctly · ('mark', 84) % scored full marks · ('avg', 55) average % of marks · ('nht',) answers only"""
    if not stat: return ''
    k=stat[0]
    txt={'mc':'of students answered correctly','mark':'scored full marks','avg':'average mark'}.get(k)
    if k=='nht': return '<div class="stat">VCAA: NHT report gives answers only</div>'
    if k=='new': return '<div class="stat">VCAA: report not yet released</div>'
    return f'<div class="stat">VCAA: <b>?%</b> {txt}</div>'
def _frame(cls,pill,head,body,src,stat=None,cfu='qw',extra='',cmd=None):
    ct=f'<div class="cmdt"><b>{cmd[0].upper()}</b>{(" · "+cmd[2]) if len(cmd)>2 and cmd[2] else ""}</div>' if cmd else ''
    return (f'<section class="slide T {cls}" data-cfu="{cfu}"><div class="hd"><div class="pill">{pill}</div><div class="tiles">{ct}{_stat(stat)}{extra}</div></div>'
            f'<h2 class="tt">{head}</h2>{body}<div class="src">{src}</div></section>')

def qslide(kind,pill,head,given,steps,answer,src,stat=None,mc=None,key=None,dist=None,dis=None,made='',cfu=None,video=None,cmd=None,afig='',build=(),parts=()):
    """kind: dn | apk | we | yt | ex.
    given: question html, or (text before, figure, text after) so the figure sits in a fixed middle zone. mc: list of option texts (A, B, …).
    steps: list of (label, html) or (label, html, attrs) — one reveal each, numbered.
    made: a figure shown on the right under the steps (not the answer).
    parts: [(label, html[, attrs])] for a multi-part question: one green answer card that reveals one part per click (steps may be empty).
    afig + build: when the figure IS the answer (e.g. a boxplot), it sits in the green answer card; build = [(text, attrs)] lines
         revealed one per click inside the card (e.g. 'Box from Q1 to Q3', 'data-bx="#id|box"'). Hide the axis in the figure ('axis' in hide).
    answer: final answer html (bottom right, revealed last with the % badge).
    key/dist/dis: MC correct letter, % choosing each option, (letter, explanation) distractor — leave dis out when there is no real distractor.
    cmd: (command word, marks, what it needs) e.g. ('Explain',1,'a reason that refers to the data'). Highlighted yellow in the question;
         a tile beside the % badge (top right) says what it needs. MC: no command word.
    steps may include fx(...) steps: formula → substitute → solve. The answer is a concluding statement."""
    if isinstance(given,tuple):  # (text before, figure, text after): text blocks stay whole, figure fills the middle
        pre,fig,post=given; given=f'<div>{pre}</div><div class="fig">{fig}</div>'+(f'<div>{post}</div>' if post else '')
    else:
        i=given.find('<ol class="parts">')
        if parts and i>0: given=f'<span style="display:block">{given[:i]}</span>{given[i:]}'  # lead text stays one block when the parts fill the card
        given=f'<div>{given}</div>'
    if cmd and cmd[0]!='Multiple choice':  # highlight the command word where it appears in the question (last occurrence = the actual question line)
        rx=re.compile(r'(?<![\w-])('+re.escape(cmd[0])+r')(?![\w-])(?![^<]*>)',re.I)
        ms=list(rx.finditer(given))
        ms=[m for m in ms if given[:m.start()].count('‘')<=given[:m.start()].count('’')]  # not inside a quotation
        for m in reversed(ms):  # every occurrence of the command word (Rocco, 15 Nov)
            given=given[:m.start()]+f'<mark class="cw">{m.group(1)}</mark>'+given[m.end():]
    L='<div class="L"><div class="q">'+given
    if mc:
        d=f' data-dist="{",".join(map(str,dist))}"' if dist else ''
        L+=f'<div class="mc"{d}>'+''.join(f'<div data-o="{chr(65+i)}"><b>{chr(65+i)}.</b>{o}</div>' for i,o in enumerate(mc))+'</div>'
    L+='</div></div>'
    R='<div class="R"><ol class="wk" style="display:flex;flex-direction:column">'
    # steps: (label, html[, attrs]) · ('ANS', html[, attrs]) a green answer card in the flow ·
    # ('TMPL', html[, attrs]) an answer TEMPLATE card: shown dark at the start of its segment (the steps since the last
    # ANS/TMPL), filled in by those steps (data-fill / data-grow …), then turned green by one more click.
    segs=[[]]
    for st in steps:
        segs[-1].append(st)
        if st[0] in ('ANS','TMPL'): segs.append([])
    n=0; v=0; tk=0
    for seg in segs:
        tm=[x for x in seg if x[0]=='TMPL']
        if tm:  # template card first in the DOM (revealed first), shown last (css order)
            tk+=1; t=tm[0]; att=(t+('',))[2]
            R+=f'<li class="ans tmpl" data-tk="{tk}" style="order:{v+len(seg)}" {att}><span class="frag" data-tmpl="on"></span><span class="wn">✓</span><span class="sl">Answer</span>{t[1]}</li>'
        for st in seg:
            lab,txt,att=(st+('',))[:3]
            if lab=='TMPL': continue
            v+=1
            if lab=='ANS': R+=f'<li class="frag ans" style="order:{v}" {att}><span class="wn">✓</span><span class="sl">Answer</span>{txt}</li>'
            else:
                n+=1; R+=f'<li class="frag" style="order:{v}" {att}><span class="wn">{n}</span><span class="sl">{lab}</span>{txt}</li>'
        if tm: v+=1; R+=f'<li class="frag tdone" data-tmpl="done:{tk}" style="display:none" {(tm[0]+("","",""))[3]}></li>'  # 4th item: attrs for the click that turns it green (e.g. data-stat)
    if any('data-pk' in ((st+('',))[2] or '') for st in steps): R+='<li class="frag" data-pall="1" style="display:none"></li>'  # end: everything back in full
    R+='</ol>'+(f'<div class="made">{made}</div>' if made else '')+'<ol class="wk">'
    sa=f' data-stat="{stat[1]}"' if stat and len(stat)>1 else ''
    if mc:
        R+=f'<li class="frag ans" data-key="{key}"{sa}><span class="wn">✓</span><span class="sl">Answer · {key}</span>{answer}</li>'
        # click 1: answer · click 2: the distractor question · click 3: which option and why (option highlighted)
        if dis: R+=f'<li class="frag dis"><div class="dlab">What’s the distractor?</div><div class="frag" data-dis="{dis[0]}"><span class="dl">{dis[0]}</span> {dis[1]}</div></li>'
        if dist: R+='<span class="frag" data-pct="1"></span>'
    elif parts:  # multi-part question: one big answer card, one part per click
        pl=''.join(f'<div class="frag pa" data-pk="{k}" {(p+("",))[2]}><b class="pl">{p[0]}</b><span>{p[1]}</span></div>' for k,p in enumerate(parts))
        pl+='<span class="frag" data-pall="1"></span>'  # last click: every part back in full (for the static PDF)
        R+=f'<li class="frag ans big"{sa}><span class="wn">✓</span><span class="sl">Answers</span>{answer}{pl}</li>'
    elif answer=='' and not afig: pass  # the answer is already in the steps (ANS / TMPL cards)
    else:
        bl=''.join(f'<div class="frag bl" {a}>{t}</div>' for t,a in build)
        fig=f'<div class="afig">{afig}</div>' if afig else ''
        R+=f'<li class="frag ans"{sa}><span class="wn">✓</span><span class="sl">Answer</span>{answer}{bl}{fig}</li>'
    R+='</ol></div>'
    cls=kind+(' mcslide' if mc else '')+(' mp' if parts else '')
    v=f'<button class="vid" data-src="" data-label="{video}">▶ Video</button>' if video else ''
    return _frame(cls,pill,head,f'<div class="qg">{L}{R}</div>',src,stat,cfu or ('mc' if mc else 'cold' if kind=='we' else 'qw'),v,cmd if cmd and cmd[0]!='Multiple choice' else None)

def cfat(code,title,subs,marks,where):
    """CFAT slide (first slide after Today's lesson): how it runs + 20-minute timer (starts on the click)."""
    body=('<div class="row" style="gap:40px;align-items:stretch"><div class="key" style="flex:1"><h4>How it runs</h4><ul class="bul" style="font-size:26px;line-height:1.6;margin-left:30px">'
          f'<li>Individual, in silence</li><li>CAS and your bound reference allowed</li><li>Multiple choice + short answer · <b>{marks} marks</b></li><li>Covers {subs}</li><li>Pens down when the timer ends</li></ul></div>'
          '<div class="key" style="flex:.8;display:flex;flex-direction:column;justify-content:center"><h4 style="text-align:center">Time remaining</h4><div class="timer" id="cfatT">20:00</div>'
          '<p class="frag muted" data-act="timer" style="text-align:center;font-size:20px">Timer running</p></div></div>')
    return _frame('cfat',f'{code} · {subs}',f'{code}: {title}',body,where,cfu='qw')
def kcard(name,body,rule=''):
    """a key formula/definition card, same look as the Key definitions and formulas slide"""
    return f'<div class="kf"><span class="kn">{name}</span><span class="kx">{body}</span>'+(f'<span class="kr">{rule}</span>' if rule else '')+'</div>'
def learn(pill,head,rule,pic,tip,src,frags='',cards=()):
    """rule: html for the rule box (top left) · cards: related key formula/definition cards (top right, from kcard) ·
    pic: picture/animation (middle) · tip: one watch-out (bottom). frags: invisible step spans that drive the picture."""
    kc=f'<div class="kcs frag">{"".join(cards)}</div>' if cards else ''
    body=f'<div class="lrn"><div class="ltop"><div class="key frag">{rule}</div>{kc}</div><div class="pic">{pic}</div>{frags}<div class="tip frag">{tip}</div></div>'
    return _frame('learn',pill,head,body,src,cfu='disc')

def yt(title,vid,start=0):
    """an embedded YouTube video card"""
    st=f'?start={start}' if start else ''
    return f'<div class="ytc"><div class="ytf"><iframe src="https://www.youtube-nocookie.com/embed/{vid}{st}" title="{title}" allow="encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div><div class="ytt">{title}</div></div>'
def cas(pill,head,task,ti,cp,answer,src,videos=()):
    """task: question + data (left). ti/cp: TI-Nspire and ClassPad steps (two cards, right). answer: what to read off (green card).
    videos: yt(...) cards shown small under the step cards."""
    ol=lambda xs:'<ol>'+''.join(f'<li>{x}</li>' for x in xs)+'</ol>'
    vc=f'<div class="ytrow">{"".join(videos)}</div>' if videos else ''
    R=(f'<div class="R"><div class="cas2"><div class="key"><h4>TI-Nspire</h4>{ol(ti)}</div>'
       f'<div class="key"><h4>ClassPad</h4>{ol(cp)}</div></div>{vc}<ol class="wk" style="margin-top:12px"><li class="ans"><span class="wn">✓</span><span class="sl">Read off</span>{answer}</li></ol></div>')
    return _frame('kcas',pill,head,f'<div class="qg"><div class="L"><div class="q">{task}</div></div>{R}</div>',src,cfu='disc')

def title(lesson,topic,sub,code,flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')):
    """topic: the formal topic name (e.g. the Cambridge subchapter title) · sub: subchapter code(s) and textbook."""
    col={'CFAT':'#00838F','Do Now':'#00838F','APK':'var(--apk)','Learn':'var(--learn)','Worked examples':'var(--we)','You try':'var(--yt)','Exit tasks':'var(--exit)'}
    return (f'<section class="slide s-title"><div class="kicker"><i></i>Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson {lesson}</div><h1 style="font-size:84px">{topic}</h1><div class="sub">{"".join(f"<div>{x}</div>" for x in sub.split(" · "))}</div>'
            '<div class="flow">'+''.join(f'<div style="border-color:{col.get(f,"var(--ink)")}">{f}</div>' for f in flow)+
            f'</div><div class="foot"><span>12MAG · General Mathematics 3&amp;4</span><span>{code}</span></div></section>')

def today(li,sc,seq):
    """Three white cards: learning intentions · success criteria (tick boxes) · lesson sequence (text, small, colour or None)."""
    ul=lambda xs,c='':f'<ul class="{c}">'+''.join(f'<li>{x}</li>' for x in xs)+'</ul>'
    q=''.join(f'<li{' style="--c:'+c+'"' if c else ""}>{t} <small>{m}</small></li>' for t,m,c in seq)
    body=(f'<div class="col3"><div class="card3"><h3>Learning intentions</h3>{ul(li)}</div><div class="card3"><h3>Success criteria</h3>{ul(sc,"tick")}</div>'
          f'<div class="card3"><h3>Lesson sequence</h3><ol class="seq">{q}</ol></div></div>')
    return _frame('',"Today’s lesson","Today’s lesson",body,'',cfu='')

def keys(defs,forms,src):
    """Two columns: key definitions (term, meaning[, picture html]) · key formulas (name, formula html built with F[, rule line])."""
    d=''.join(f'<div class="kd"><div><b>{x[0]}</b><span>{x[1]}</span></div>'+(f'<div class="kpic">{x[2]}</div>' if len(x)>2 else '')+'</div>' for x in defs)
    f=''.join(f'<div class="kf"><span class="kn">{x[0]}</span><span class="kx">{x[1]}</span>'+(f'<span class="kr">{x[2]}</span>' if len(x)>2 else '')+'</div>' for x in forms)
    body=f'<div class="col2 keys"><div class="card3"><h3>Key definitions</h3>{d}</div><div class="card3"><h3>Key formulas</h3>{f}</div></div>'
    return _frame('',"Key ideas","Key definitions and formulas",body,src,cfu='')

def scgrid(sc):
    h=(len(sc)+1)//2
    return '<div class="lisc" style="grid-template-columns:1fr 1fr"><ul>'+''.join(f'<li>{x}</li>' for x in sc[:h])+'</ul><ul>'+''.join(f'<li>{x}</li>' for x in sc[h:])+'</ul></div>'
def checkin(sc):
    """one card, success criteria with tick boxes down the page (same look as Today's lesson)"""
    body=('<div class="card3 ci"><h3>Success criteria</h3><ul class="tick">'+''.join(f'<li>{x}</li>' for x in sc)+'</ul></div>'
          '<p class="muted" style="font-size:22px;margin-top:14px">Thumbs up, sideways or down for each one, then tick it on your worksheet: ✓ got it · ~ nearly · ✗ not yet</p>')
    return _frame('','Check-in','How did you go?',body,'',cfu='tf')
def coursework(subs):
    """one card per set (mirrors the planner's coursework card): (title, note line, [items]); items are tick boxes like the success criteria"""
    def card(t,q,items):
        li=items or ([q] if q else [])
        return (f'<div class="card3 cw"><h3>{t}</h3>'+(f'<p class="cwn">{q}</p>' if q and items else '')+
                '<ul class="tick">'+''.join(f'<li>{x}</li>' for x in li)+'</ul></div>')
    k=''.join(card(t,q,(x[0] if x else [])) for t,q,*x in subs)
    return _frame('','Coursework','Coursework',f'<div class="cwgrid">{k}</div>','',cfu='')
def videos(items=(),blank=8):
    """last slide of every deck: 'Videos that might help'. items: yt(...) cards; the rest are blank cards to fill later."""
    cards=''.join(items)+''.join('<div class="ytc blank"><div class="ytf"></div><div class="ytt">Video to add</div></div>' for _ in range(max(0,blank-len(items))))
    return _frame('','Videos','Videos that might help',f'<div class="ytgrid">{cards}</div>','',cfu='')

# Controls (Rocco, 16 Nov, as in the 10MA deck): click/tap = next step only (double click/tap = next slide) · → single = step,
# double → = next slide · ← single = back a step, double ← = previous slide, cleared · Backspace single = back a step, double = clear this slide.
# Clicks on interactive widgets (class "ia": sliders, card sort) never advance. Replayed steps (show(n,true), back()) run with IA.fast = 1 (no delays).
CONTROLS=[
 ("if(atEnd){steps(s).forEach(st=>doStep(s,st));step=steps(s).length}",
  "if(atEnd){IA.fast=1;steps(s).forEach(st=>doStep(s,st));IA.fast=0;step=steps(s).length}"),
 ("for(let k=0;k<n;k++){doStep(s,all[k]);step++}","IA.fast=1;for(let k=0;k<n;k++){doStep(s,all[k]);step++}IA.fast=0"),
 ("addEventListener('keydown',e=>{if(e.repeat)return;if(['ArrowRight','PageDown',' ','Enter','ArrowDown'].includes(e.key)){e.preventDefault();press(1)}if(['ArrowLeft','PageUp','ArrowUp','Backspace'].includes(e.key)){e.preventDefault();press(-1)}",
  "let lastBs={t:0,slide:0};function bksp(){const now=performance.now();if(now-lastBs.t<DBL){lastBs.t=0;show(lastBs.slide);return}lastBs={t:now,slide:i};back()}\n"
  "addEventListener('keydown',e=>{if(e.repeat)return;if(e.target.closest&&e.target.closest('input,textarea,select'))return;if(['ArrowRight','PageDown',' ','Enter','ArrowDown'].includes(e.key)){e.preventDefault();press(1)}if(['ArrowLeft','PageUp','ArrowUp'].includes(e.key)){e.preventDefault();press(-1)}if(e.key==='Backspace'){e.preventDefault();bksp()}"),
 ("stage.addEventListener('click',e=>{const vb=","stage.addEventListener('click',e=>{if(e.target.closest('.ia'))return;const vb="),
 ("stage.addEventListener('contextmenu',e=>{e.preventDefault();","stage.addEventListener('contextmenu',e=>{e.preventDefault();if(e.target.closest('.ia'))return;"),
]
def assemble(S,doc_title,out,base=f'{ROOT}/tools/deck/engine.html'):
    """Wrap slides in the slide engine (tools/deck/engine.html: CSS, charts, reveal engine) plus the template CSS/JS."""
    h=open(base,encoding='utf-8').read()
    head,tail=h.split('<!--SLIDES-->')
    head=re.sub(r'<title>.*?</title>',f'<title>{doc_title}</title>',head)
    i=head.find('</style>')  # after the title swap, so the insert point is not shifted
    css=open(f'{HERE}/tpl.css',encoding='utf-8').read()+open(f'{HERE}/ia.css',encoding='utf-8').read()
    head=head[:i]+css+head[i:]
    for x,y in [('s4apply(s,f);','s4apply(s,f);tplapply(s,f);iaapply(s,f);'),('s4reset(s);','s4reset(s);tplreset(s);iareset(s);')]+CONTROLS:
        assert tail.count(x)==1,x; tail=tail.replace(x,y)
    js=open(f'{HERE}/tpl.js',encoding='utf-8').read()+'\n'+open(f'{HERE}/ia.js',encoding='utf-8').read()
    tail=tail.replace('/* ---------- reveal engine ---------- */',js+'\n/* ---------- reveal engine ---------- */',1)
    open(out,'w',encoding='utf-8').write(head+'\n'.join(S)+tail); return len(S)

# ---------- SOCS: describing numerical data (Rocco, 15 Nov: "like a sock") ----------
# Shape · Outliers (present or not: goes with the shape) · Centre (mean / median / mode; median unaffected by outliers)
# · Spread (range / IQR; IQR unaffected by outliers). One template line per letter; every describe answer uses it.
SOCS_LINES=[('S','Shape','#2f6fdf'),('O','Outliers','#c0632b'),('C','Centre','#1f9e74'),('S','Spread','#7b3fbf')]
def _blank(cls,val,ph): return f'<span class="blank {cls}"><span class="ph">{ph}</span><span class="fill">{val}</span></span>'
def socs(pre,shape='',outliers='',centre=('',''),spread=('',''),most='',fs=19,var='the distribution'):
    """SOCS answer template, one row per letter, blanks filled by data-fill="<pre>1" … "<pre>4".
    shape: 'positively skewed' · outliers: 'are no outliers' / 'is an outlier at 21' / 'are possible outliers below 34 weeks'
    centre: (value, measure) e.g. ('38 weeks','median') · spread: (measure, value) e.g. ('IQR','2 weeks') · most: optional 'a and b' for 'Most values lie between …'"""
    sent=[
      ['The distribution is ',_blank(pre+'1',shape,'symmetric / positively skewed / negatively skewed'),'.'],
      ['There ',_blank(pre+'2',outliers,'are no outliers / is an outlier at … / are outliers at …'),'.'],
      ['The distribution is centred at ',_blank(pre+'3',centre[0],'value'),', the ',_blank(pre+'3',centre[1],'median / mean / mode'),'.'],
      ['The ',_blank(pre+'4',spread[0],'range / IQR'),' is ',_blank(pre+'4',spread[1],'value'),'.']+([' Most values lie between ',_blank(pre+'4',most,'a and b'),'.'] if most else [])]
    rows=''.join(f'<div class="socsr"><span class="socsl" style="background:{c}">{l}</span><span class="socsn" style="color:{c}">{n}</span><span class="socst">{"".join(s)}</span></div>' for (l,n,c),s in zip(SOCS_LINES,sent))
    return f'<div class="socs report" style="font-size:{fs}px">{rows}</div>'

# ======================================================================================================
# Interactive features (16 Nov; ideas from the 10MA deck, 12MAG look). JS: tpl/ia.js · CSS: tpl/ia.css (injected by assemble).
# Each widget is driven by data attributes on reveal steps, so click-reveal, back() and the PDF final frame all work.
# Put the attributes on a qslide step (3rd item), on an istep(...), or on an invisible frag: ifr(attrs).
# Several specs of the SAME attribute on one step: join them with ';' (e.g. data-tsort="#a;#b").
# Labels may hold html but no '|' or ';'.
# ======================================================================================================
import html as _html, builtins as _bi
def _q(s): return _html.escape(str(s),quote=True)
def _g(v): return f'{v:g}' if isinstance(v,(int,float)) else str(v)
def ifr(*attrs):
    """invisible reveal steps, one per attribute string (e.g. ifr(tsort('t1'), tmed('t1',label='M = 6')))"""
    return ''.join(f'<span class="frag" {a}></span>' for a in attrs)
def isteps(items,start=1):
    """numbered step cards revealed one per click: [(html, attrs), ...]; attrs drive the widget(s) on the slide"""
    return '<ol class="i-steps">'+''.join(f'<li class="frag" {a}><span class="wn">{k}</span>{t}</li>' for k,(t,a) in enumerate(items,start))+'</ol>'
def islide(pill,head,body,src,frags='',kind='learn',cfu='disc'):
    """a free-layout slide for the interactive widgets (same header/title/source zones as every template).
    kind: learn | we | yt | apk | ex | dn (pill colour)."""
    return _frame(kind+' islide',pill,head,f'<div class="ibody">{body}</div>{frags}',src,cfu=cfu)

# ---------- 1. data tiles: sort → cross off pairs → middle = median · quartiles = medians of halves ----------
def tiles(rid,vals,fs=26):
    """vals in the order given (unordered). Positions a, b below count in the ORDERED list, from 0. Decimals fine."""
    sp=''.join(f'<span class="i-t" data-v="{float(v)}">{_g(v)}</span>' for v in vals)
    return f'<div class="i-tiles" id="{rid}" style="--n:{len(vals)};font-size:{fs}px">{sp}</div>'
def tsort(rid): return f'data-tsort="#{rid}"'
def tcross(rid,a='',b=''): return f'data-tcross="#{rid}|{a}|{b}"'
def tmid(rid,a='',b='',label='',cls='mid'): return f'data-tmid="{_q(f"#{rid}|{a}|{b}|{cls}|{label}")}"'
def tmed(rid,a='',b='',label='',cls='mid'):
    """one click: cross off smallest + largest pairs inward over positions a..b (blank = all), then light the middle 1 or 2 tiles + label"""
    return tcross(rid,a,b)+' '+tmid(rid,a,b,label,cls)
def thalves(rid): return f'data-thalves="#{rid}"'
def tquart(rid,n,q1='',q3=''):
    """three clicks for quartiles = medians of the halves (n odd: the median is left out):
    [split into halves, Q1 (cross + middle of the lower half), Q3 (upper half)]"""
    h=n//2
    return [thalves(rid),tmed(rid,0,h-1,q1,'q'),tmed(rid,n-h,n-1,q3,'q')]

# ---------- 2. sliders (teacher drags; data-fset moves it on a click, so the PDF can show a chosen value) ----------
def _sl(kind,rid,cfg): return f'<div class="i-slider ia{" i-log" if kind=="log" else ""}" id="{rid}" data-kind="{kind}" data-cfg=\'{J(cfg)}\'></div>'
def fence_slider(rid,data,max,min=0,k=None,step=1,lo=None,hi=None,tick=None,lab=None,xl='',dec=2,W=1000,box=False):
    """dot plot of data with Q1, Q3, LF, UF and red outlier zones; data[k] (default: the largest) is dragged between lo and hi.
    Read-out: Q1, Q3, IQR, LF, UF and 'x > UF → x is an outlier' (red) or 'not an outlier' (green).
    box=True: the same as a box plot (whiskers move to the last non-outlier, outliers become dots) = box_slider."""
    if k is None: k=data.index(_bi.max(data))
    cfg=dict(data=list(data),k=k,min=min,max=max,step=step,xl=xl,dec=dec,W=W,mode='box' if box else 'fences')
    for a,v in (('lo',lo),('hi',hi),('tick',tick),('lab',lab)):
        if v is not None: cfg[a]=v
    return _sl('box' if box else 'fences',rid,cfg)
def box_slider(rid,data,max,**kw): return fence_slider(rid,data,max,box=True,**kw)
def z_slider(rid,m,s,x0=None,step=None,xl='',dec=2,W=1000):
    """normal curve, mean m, SD s: drag x (snaps every s/2 by default); shades below x, shows z = (x − x̄)/s and,
    at whole-number z, the % below/above from the 68–95–99.7% rule"""
    cfg=dict(m=m,s=s,xl=xl,dec=dec,W=W)
    if x0 is not None: cfg['x0']=x0
    if step: cfg['step']=step
    return _sl('z',rid,cfg)
def log_slider(rid,lo=0,hi=6,x0=1000,xl='x',W=1000):
    """two aligned scales: log10(x) (even) and x (1, 10, 100, …): drag to see x ⟷ log10(x)"""
    return _sl('log',rid,dict(lo=lo,hi=hi,x0=x0,xl=xl,W=W))
def shape_slider(rid,v0=0,W=1000):
    """drag to skew a histogram (−1 … 1): shape name, tail arrow, mean (red dashed) vs median (green)"""
    return _sl('shape',rid,dict(v0=v0,W=W))
def fset(rid,v): return f'data-fset="#{rid}|{v}"'
def shset(rid,v): return f'data-shset="#{rid}|{v}"'

# ---------- 3. card sort: click a card then a bucket (or drag it); reveal steps move every card to the right bucket ----------
CAT_C,NUM_C='#c0632b','#2f6fdf'
def card_sort(rid,items,buckets=(('Categorical',('Nominal','Ordinal'),CAT_C),('Numerical',('Discrete','Continuous'),NUM_C))):
    """items: [(text, 'Categorical/Nominal'), ...] (answer path; one level 'Categorical' for a one-step sort).
    buckets: [(name, (sub-bucket names) or (), colour)]. Sub-buckets open on data-slevel / the step-2 reveal.
    Steps: sort_steps(rid) (or sort_steps(rid,1) for one level)."""
    cs=''.join(f'<div class="i-cs" data-a="{_q(a)}">{t}</div>' for t,a in items)
    bk=''
    for name,subs,*c in buckets:
        col=f' style="--c:{c[0]}"' if c else ''
        sb=''.join(f'<div class="i-bk sub" data-b="{_q(name+"/"+x)}"><h4>{x}</h4><div class="i-tray"></div></div>' for x in subs)
        bk+=f'<div class="i-bk" data-b="{_q(name)}"{col}><h4>{name}</h4><div class="i-tray"></div>'+(f'<div class="i-subs">{sb}</div>' if subs else '')+'</div>'
    return f'<div class="i-sort ia" id="{rid}"><div class="i-pool">{cs}</div><div class="i-bks">{bk}</div><div class="i-score"></div></div>'
def sort_steps(rid,levels=2):
    """invisible steps: reveal level 1 → (open sub-buckets → reveal level 2). Cards the class placed wrongly keep a red ✗."""
    a=[f'data-sreveal="#{rid}|1"']
    if levels>1: a+=[f'data-slevel="#{rid}|2"',f'data-sreveal="#{rid}|2"']
    return ifr(*a)

# ---------- 4. stem plot built leaf by leaf (leaves fly from the data list) · tally into a frequency table ----------
def stem_fly(rid,vals,unit=1,key='',fs=26,split=False,data=True):
    """vals in the order given; unit = the leaf unit (1: 47 → 4 | 7; 0.1: 4.7 → 4 | 7). split=True: split stems (leaves 0–4, 5–9).
    Rows include empty stems. Steps: leaf(rid,'0-5') · leaf(rid) (all) · lsort(rid) (order each row)."""
    q=[int(round(float(v)/unit)) for v in vals]; st=[x//10 for x in q]; lf=[x%10 for x in q]
    keys=[]
    for s_ in range(min(st),max(st)+1): keys+=[(s_,0),(s_,1)] if split else [(s_,0)]
    row=lambda k:(st[k],(1 if lf[k]>=5 else 0) if split else 0)
    tr=''
    for kk in keys:
        sp=''.join(f'<span class="i-lf" data-k="{k}" data-l="{lf[k]}">{lf[k]}</span>' for k in range(len(vals)) if row(k)==kk)
        tr+=f'<tr><td class="st">{kk[0]}</td><td class="lv"><div class="i-lvw">{sp}</div></td></tr>'
    chips=''.join(f'<span class="i-sch" data-k="{k}">{_g(v)}</span>' for k,v in enumerate(vals))
    return (f'<div class="i-stem" id="{rid}">'+(f'<div class="i-sdata">{chips}</div>' if data else '')+
            f'<div><div class="stemcap">{key}</div><table class="stem3" style="font-size:{fs}px">{tr}</table></div></div>')
def leaf(rid,ks='all'):
    """ks: 'all' · '0-5' · '0,3,7' (positions in the data list)"""
    return f'data-leaf="#{rid}|{ks}"'
def lsort(rid): return f'data-lsort="#{rid}"'
def tally_set(cid,tid,vals,edges,labels=None,head=('Interval','Frequency'),total=True,fs=22):
    """returns (data chips html, frequency table html). edges [a0, a1, …]: class i is a_i ≤ x < a_(i+1).
    Steps: ftally(cid,tid,i[,hist]) per class (lights its values, counts them into row i, grows bar i of a stepped hist) · ftot(tid)."""
    nb=len(edges)-1; b=[next((i for i in range(nb) if edges[i]<=float(v)<edges[i+1]),-1) for v in vals]
    labels=labels or [f'{_g(edges[i])}–&lt;{_g(edges[i+1])}' for i in range(nb)]
    chips=f'<div class="i-dchips" id="{cid}">'+''.join(f'<span class="i-dch" data-b="{x}">{_g(v)}</span>' for v,x in zip(vals,b))+'</div>'
    rows=''.join(f'<tr><td>{labels[i]}</td><td class="i-fq" data-i="{i}" data-n="{b.count(i)}"></td></tr>' for i in range(nb))
    if total: rows+=f'<tr><th>Total</th><td class="i-ftot"></td></tr>'
    return chips,f'<table class="i-ftab" id="{tid}" style="font-size:{fs}px"><tr><th>{head[0]}</th><th>{head[1]}</th></tr>{rows}</table>'
def ftally(cid,tid,i,hist=None):
    """hist: id of a hist(...) chart drawn with extra='data-stepped="1"' (bars start at 0)"""
    return f'data-ftally="#{cid}|#{tid}|{i}"'+(f' data-fgrow="#{hist}|{i}"' if hist else '')
def ftot(tid): return f'data-ftot="#{tid}"'
