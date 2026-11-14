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
def dot(rid,cfg): return f'<div class="chart" id="{rid}" data-chart="dot3" data-cfg=\'{J(cfg)}\'></div>'
def stem(rid,rows,key,fs=24):
    i=0; tr=''
    for st,lv in rows:
        sp=''
        for l in lv: sp+=f'<span class="lf2" data-i="{i}">{l}</span>'; i+=1
        tr+=f'<tr><td class="st">{st}</td><td class="lv">{sp}</td></tr>'
    return f'<div><div class="stemcap">{key}</div><table class="stem3" id="{rid}" style="font-size:{fs}px">{tr}</table></div>'

# ---------- formulas: write once, substitute values, solve (animated) ----------
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

def qslide(kind,pill,head,given,steps,answer,src,stat=None,mc=None,key=None,dist=None,dis=None,made='',cfu=None,video=None,cmd=None,afig='',build=()):
    """kind: dn | apk | we | yt | ex.
    given: question html, or (text before, figure, text after) so the figure sits in a fixed middle zone. mc: list of option texts (A, B, …).
    steps: list of (label, html) or (label, html, attrs) — one reveal each, numbered.
    made: a figure shown on the right under the steps (not the answer).
    afig + build: when the figure IS the answer (e.g. a boxplot), it sits in the green answer card; build = [(text, attrs)] lines
         revealed one per click inside the card (e.g. 'Box from Q1 to Q3', 'data-bx="#id|box"'). Hide the axis in the figure ('axis' in hide).
    answer: final answer html (bottom right, revealed last with the % badge).
    key/dist/dis: MC correct letter, % choosing each option, (letter, explanation) distractor — leave dis out when there is no real distractor.
    cmd: (command word, marks, what it needs) e.g. ('Explain',1,'a reason that refers to the data'). Highlighted yellow in the question;
         a tile beside the % badge (top right) says what it needs. MC: no command word.
    steps may include fx(...) steps: formula → substitute → solve. The answer is a concluding statement."""
    if isinstance(given,tuple):  # (text before, figure, text after): text blocks stay whole, figure fills the middle
        pre,fig,post=given; given=f'<div>{pre}</div><div class="fig">{fig}</div>'+(f'<div>{post}</div>' if post else '')
    else: given=f'<div>{given}</div>'
    if cmd and cmd[0]!='Multiple choice':  # highlight the command word where it appears in the question (last occurrence = the actual question line)
        rx=re.compile(r'(?<![\w-])('+re.escape(cmd[0])+r')(?![\w-])(?![^<]*>)',re.I)
        ms=list(rx.finditer(given))
        if ms:
            m=ms[-1]; given=given[:m.start()]+f'<mark class="cw">{m.group(1)}</mark>'+given[m.end():]
    L='<div class="L"><div class="q">'+given
    if mc:
        d=f' data-dist="{",".join(map(str,dist))}"' if dist else ''
        L+=f'<div class="mc"{d}>'+''.join(f'<div data-o="{chr(65+i)}"><b>{chr(65+i)}.</b>{o}</div>' for i,o in enumerate(mc))+'</div>'
    L+='</div></div>'
    R='<div class="R"><ol class="wk">'
    for n,st in enumerate(steps,1):
        lab,txt,att=(st+('',))[:3]
        R+=f'<li class="frag" {att}><span class="wn">{n}</span><span class="sl">{lab}</span>{txt}</li>'
    R+='</ol>'+(f'<div class="made">{made}</div>' if made else '')+'<ol class="wk">'
    sa=f' data-stat="{stat[1]}"' if stat and len(stat)>1 else ''
    if mc:
        R+=f'<li class="frag ans" data-key="{key}"{sa}><span class="wn">✓</span><span class="sl">Answer · {key}</span>{answer}</li>'
        # click 1: answer · click 2: the distractor question · click 3: which option and why (option highlighted)
        if dis: R+=f'<li class="frag dis"><div class="dlab">What’s the distractor?</div><div class="frag" data-dis="{dis[0]}"><span class="dl">{dis[0]}</span> {dis[1]}</div></li>'
        if dist: R+='<span class="frag" data-pct="1"></span>'
    else:
        bl=''.join(f'<div class="frag bl" {a}>{t}</div>' for t,a in build)
        fig=f'<div class="afig">{afig}</div>' if afig else ''
        R+=f'<li class="frag ans"{sa}><span class="wn">✓</span><span class="sl">Answer</span>{answer}{bl}{fig}</li>'
    R+='</ol></div>'
    cls=kind+(' mcslide' if mc else '')
    v=f'<button class="vid" data-src="" data-label="{video}">▶ Video</button>' if video else ''
    return _frame(cls,pill,head,f'<div class="qg">{L}{R}</div>',src,stat,cfu or ('mc' if mc else 'cold' if kind=='we' else 'qw'),v,cmd if cmd and cmd[0]!='Multiple choice' else None)

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
    R=(f'<div class="R"><div class="cas2"><div class="key frag"><h4>TI-Nspire</h4>{ol(ti)}</div>'
       f'<div class="key frag"><h4>ClassPad</h4>{ol(cp)}</div></div>{vc}<ol class="wk" style="margin-top:12px"><li class="frag ans"><span class="wn">✓</span><span class="sl">Read off</span>{answer}</li></ol></div>')
    return _frame('kcas',pill,head,f'<div class="qg"><div class="L"><div class="q">{task}</div></div>{R}</div>',src,cfu='disc')

def title(lesson,topic,sub,code,flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')):
    """topic: the formal topic name (e.g. the Cambridge subchapter title) · sub: subchapter code(s) and textbook."""
    col={'CFAT':'#00838F','Do Now':'#00838F','APK':'var(--apk)','Learn':'var(--learn)','Worked examples':'var(--we)','You try':'var(--yt)','Exit tasks':'var(--exit)'}
    return (f'<section class="slide s-title"><div class="kicker"><i></i>Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson {lesson}</div><h1 style="font-size:84px">{topic}</h1><div class="sub">{sub}</div>'
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
    d=''.join(f'<div class="kd frag"><div><b>{x[0]}</b><span>{x[1]}</span></div>'+(f'<div class="kpic">{x[2]}</div>' if len(x)>2 else '')+'</div>' for x in defs)
    f=''.join(f'<div class="kf frag"><span class="kn">{x[0]}</span><span class="kx">{x[1]}</span>'+(f'<span class="kr">{x[2]}</span>' if len(x)>2 else '')+'</div>' for x in forms)
    body=f'<div class="col2"><div><h3>Key definitions</h3>{d}</div><div><h3>Key formulas</h3>{f}</div></div>'
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
    """one card per subchapter: (subchapter title, questions line, [notes])"""
    k=''.join(f'<div class="card3 cw"><h3>{t}</h3><p class="cwq">{q}</p>'+''.join(f'<p class="cwn">{n}</p>' for n in (x[0] if x else []))+'</div>' for t,q,*x in subs)
    return _frame('','Coursework','Coursework',f'<div class="cwgrid">{k}</div>','',cfu='')
def videos(items=(),blank=8):
    """last slide of every deck: 'Videos that might help'. items: yt(...) cards; the rest are blank cards to fill later."""
    cards=''.join(items)+''.join('<div class="ytc blank"><div class="ytf"></div><div class="ytt">Video to add</div></div>' for _ in range(max(0,blank-len(items))))
    return _frame('','Videos','Videos that might help',f'<div class="ytgrid">{cards}</div>','',cfu='')

def assemble(S,doc_title,out,base=f'{ROOT}/tools/deck/engine.html'):
    """Wrap slides in the slide engine (tools/deck/engine.html: CSS, charts, reveal engine) plus the template CSS/JS."""
    h=open(base,encoding='utf-8').read()
    i=h.find('</style>'); head,tail=h.split('<!--SLIDES-->')
    head=re.sub(r'<title>.*?</title>',f'<title>{doc_title}</title>',head)
    css=open(f'{HERE}/tpl.css',encoding='utf-8').read()
    head=head[:i]+css+head[i:]
    for x,y in [('s4apply(s,f);','s4apply(s,f);tplapply(s,f);'),('s4reset(s);','s4reset(s);tplreset(s);')]:
        assert tail.count(x)==1,x; tail=tail.replace(x,y)
    tail=tail.replace('/* ---------- reveal engine ---------- */',open(f'{HERE}/tpl.js',encoding='utf-8').read()+'\n/* ---------- reveal engine ---------- */',1)
    open(out,'w',encoding='utf-8').write(head+'\n'.join(S)+tail); return len(S)
