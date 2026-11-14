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

def _stat(stat):
    """stat: None · ('mc', 90) % answered correctly · ('mark', 84) % scored full marks · ('avg', 55) average % of marks · ('nht',) answers only"""
    if not stat: return ''
    k=stat[0]
    txt={'mc':'of students answered correctly','mark':'scored full marks','avg':'average mark'}.get(k)
    if k=='nht': return '<div class="stat">VCAA: NHT report gives answers only</div>'
    if k=='new': return '<div class="stat">VCAA: report not yet released</div>'
    return f'<div class="stat">VCAA: <b>?%</b> {txt}</div>'
def _frame(cls,pill,head,body,src,stat=None,cfu='qw',extra=''):
    return (f'<section class="slide T {cls}" data-cfu="{cfu}"><div class="hd"><div class="pill">{pill}</div>{_stat(stat)}</div>'
            f'<h2 class="tt">{head}</h2>{body}{extra}<div class="src">{src}</div></section>')

def qslide(kind,pill,head,given,steps,answer,src,stat=None,mc=None,key=None,dist=None,dis=None,made='',cfu=None,video=None,cmd=None):
    """kind: dn | apk | we | yt | ex.
    given: question html, or (text before, figure, text after) so the figure sits in a fixed middle zone. mc: list of option texts (A, B, …).
    steps: list of (label, html) or (label, html, attrs) — one reveal each, numbered.
    made: something students construct (e.g. a boxplot) shown on the right under the steps.
    answer: final answer html (bottom right, revealed last with the % badge).
    key/dist/dis: MC correct letter, % choosing each option, (letter, explanation) distractor.
    cmd: (command word, marks, what it needs) e.g. ('Explain',1,'a reason that refers to the data'). Shown as a chip on the
         question (always visible) and as the FIRST reveal on the right, before any working. MC: ('Multiple choice',1,None)."""
    if isinstance(given,tuple):  # (text before, figure, text after): text blocks stay whole, figure fills the middle
        pre,fig,post=given; given=f'<div>{pre}</div><div class="fig">{fig}</div>'+(f'<div>{post}</div>' if post else '')
    else: given=f'<div>{given}</div>'
    chip=''
    if cmd:
        w,m,_=(tuple(cmd)+(None,))[:3]
        chip=f'<div class="cmd"><b>{w.upper()}</b>'+(f'<span>{m} mark{"s" if m!=1 else ""}</span>' if m else '')+'</div>'
    L='<div class="L"><div class="q">'+chip+given
    if mc:
        d=f' data-dist="{",".join(map(str,dist))}"' if dist else ''
        L+=f'<div class="mc"{d}>'+''.join(f'<div data-o="{chr(65+i)}"><b>{chr(65+i)}.</b>{o}</div>' for i,o in enumerate(mc))+'</div>'
    L+='</div></div>'
    R='<div class="R">'
    if cmd and len(cmd)>2 and cmd[2]:
        R+=f'<div class="cmdbox frag"><div class="lab">What “{cmd[0].lower()}” needs</div><p>{cmd[2]}</p></div>'
    R+='<div class="zone">Working</div><ol class="wk">'
    for n,s in enumerate(steps,1):
        lab,txt,att=(s+('',))[:3]
        R+=f'<li class="frag" {att}><span class="wn">{n}</span><span class="sl">{lab}</span>{txt}</li>'
    R+='</ol>'+(f'<div class="made">{made}</div>' if made else '')+'<div class="end">'
    sa=f' data-stat="{stat[1]}"' if stat and len(stat)>1 else ''
    if mc:
        R+=f'<div class="ansbox frag" data-key="{key}"{sa} data-s="sol"><div class="lab">Answer · {key}</div><p>{answer}</p></div>'
        if dis: R+=f'<div class="frag" data-s="sol"><div class="dbox"><div class="lab">What’s the distractor?</div><div class="frag" data-dis="{dis[0]}"><div class="lab2">Distractor · {dis[0]}</div><p>{dis[1]}</p></div></div></div>'
        if dist: R+='<span class="frag" data-pct="1"></span>'
    else:
        R+=f'<div class="ansbox frag"{sa}><div class="lab">Answer</div><p>{answer}</p></div>'
    R+='</div></div>'
    cls=kind+(' mcslide' if mc else '')
    v=f'<button class="vid" data-src="" data-label="{video}">▶ Video</button>' if video else ''
    return _frame(cls,pill,head,f'<div class="qg">{L}{R}</div>',src,stat,cfu or ('mc' if mc else 'cold' if kind=='we' else 'qw'),v)

def learn(pill,head,rule,pic,tip,src,frags=''):
    """rule: html for the rule/definition box (top) · pic: picture/animation (middle) · tip: one watch-out (bottom).
    frags: extra invisible step spans that drive the picture."""
    body=f'<div class="lrn"><div class="key frag">{rule}</div><div class="pic">{pic}</div>{frags}<div class="tip frag">{tip}</div></div>'
    return _frame('learn',pill,head,body,src,cfu='disc')

def cas(pill,head,task,ti,cp,answer,src):
    """task: question + data (left). ti/cp: lists of steps for TI-Nspire and ClassPad (right). answer: what to read off."""
    ol=lambda xs:'<ol>'+''.join(f'<li>{x}</li>' for x in xs)+'</ol>'
    R=(f'<div class="R"><div class="zone">Steps</div><div class="cas2"><div class="key frag"><h4>TI-Nspire</h4>{ol(ti)}</div>'
       f'<div class="key frag"><h4>ClassPad</h4>{ol(cp)}</div></div><div class="end"><div class="ansbox frag"><div class="lab">Read off</div><p>{answer}</p></div></div></div>')
    return _frame('kcas',pill,head,f'<div class="qg"><div class="L"><div class="q">{task}</div></div>{R}</div>',src,cfu='disc')

def title(lesson,h1,sub,code,flow=('Do Now','APK','Learn','Worked examples','You try','Exit tasks')):
    col={'CFAT':'#00838F','Do Now':'#00838F','APK':'var(--apk)','Learn':'var(--learn)','Worked examples':'var(--we)','You try':'var(--yt)','Exit tasks':'var(--exit)'}
    return (f'<section class="slide s-title"><div class="kicker"><i></i>Unit 3<i></i>AOS 1 Data Analysis<i></i>Lesson {lesson}</div><h1>{h1}</h1><div class="sub">{sub}</div>'
            '<div class="flow">'+''.join(f'<div style="border-color:{col.get(f,"var(--ink)")}">{f}</div>' for f in flow)+
            f'</div><div class="foot"><span>12MAG · General Mathematics 3&amp;4</span><span>{code}</span></div></section>')

def today(li,seq):
    """li: learning intentions · seq: list of (text, small, colour or None)"""
    s=''.join(f'<li{' style="--c:'+c+'"' if c else ""}>{t} <small>{m}</small></li>' for t,m,c in seq)
    body=(f'<div class="lisc" style="grid-template-columns:1.15fr 1fr"><div><h3>Learning intentions</h3><ul>'+''.join(f'<li style="font-size:22px;padding:6px 0 6px 32px">{x}</li>' for x in li)+
          f'</ul></div><div><h3>Lesson sequence</h3><ol class="seq">{s}</ol></div></div>')
    return _frame('',"Today’s lesson","Today’s lesson",body,'',cfu='')

def scgrid(sc):
    h=(len(sc)+1)//2
    return '<div class="lisc" style="grid-template-columns:1fr 1fr"><ul>'+''.join(f'<li>{x}</li>' for x in sc[:h])+'</ul><ul>'+''.join(f'<li>{x}</li>' for x in sc[h:])+'</ul></div>'
def success(sc): return _frame('','Success criteria','By the end of this lesson you’ll be able to say…',scgrid(sc),'',cfu='')
def checkin(sc): return _frame('','Check-in','How did you go?',scgrid(sc)+'<p class="muted" style="font-size:24px;margin-top:22px">Thumbs up, sideways or down for each one, then rate it on your worksheet: ✓ got it · ~ nearly · ✗ not yet</p>','',cfu='tf')
def coursework(sets,revision):
    """sets: list of (title, [(skill, questions)])"""
    k=''.join(f'<div class="key hw"><h4>{t}</h4><table>'+''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in rows)+'</table></div>' for t,rows in sets)
    body=f'<div class="row" style="gap:24px">{k}</div><div class="key hw" style="margin-top:18px"><h4>Revision book</h4><p style="font-size:26px">{revision}</p></div>'
    return _frame('','Coursework','Coursework',body,'',cfu='')

def assemble(S,doc_title,out,base=f'{ROOT}/lessons/S4-slides.html'):
    """Wrap slides in the deck engine (CSS, charts, reveal engine) taken from the current base deck."""
    h=open(base,encoding='utf-8').read()
    i=h.find('</style>'); j=h.find('<section'); k=h.rfind('</section>')+len('</section>')
    head=re.sub(r'<title>.*?</title>',f'<title>{doc_title}</title>',h[:i])
    css=open(f'{HERE}/tpl.css',encoding='utf-8').read()
    doc=head+css+h[i:j]+'\n'.join(S)+h[k:]
    open(out,'w',encoding='utf-8').write(doc); return len(S)
