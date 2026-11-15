"""Shared building blocks for the guided worksheets (S1/S4 house style: A4, black and white, answers in red on the solutions copy).
Used by tools/deck/<s#>/worksheet.py. Copied from tools/deck/s4/worksheet.py (which still has its own copy)."""
import os, math, asyncio
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
CSS=open(os.path.join(os.path.dirname(__file__),'s4','ws.css')).read()
CAM='Cambridge General Mathematics Units 3&amp;4'; EDR='Edrolo General Mathematics Units 3&amp;4'
CAM12='Cambridge General Mathematics Units 1&amp;2'; EDR12='Edrolo General Mathematics Units 1&amp;2'
RED='#c00'
# ---------------------------------------------------------------- figures (static SVG)
def _fmt(v,dec=0): return f'{v:.{dec}f}' if dec else (str(int(v)) if float(v).is_integer() else str(v))
def axis_svg(mn,mx,step,lab=None,xl='',W=340,dec=0,body='',top=26,extra_h=0):
    lab=lab or step; L,R=14,14; s=lambda v:L+(v-mn)/(mx-mn)*(W-L-R); y=top+30
    o=[f'<line x1="{L}" y1="{y}" x2="{W-R}" y2="{y}" stroke="#000" stroke-width="1"/>']
    n=round((mx-mn)/step)
    for i in range(n+1):
        v=mn+i*step; big=abs(((v-mn)/lab)-round((v-mn)/lab))<1e-6
        o.append(f'<line x1="{s(v):.1f}" y1="{y}" x2="{s(v):.1f}" y2="{y+(5 if big else 3)}" stroke="#000" stroke-width="{0.9 if big else 0.6}"/>')
        if big: o.append(f'<text x="{s(v):.1f}" y="{y+14}" text-anchor="middle" font-size="9">{_fmt(round(v,6),dec)}</text>')
    if xl: o.append(f'<text x="{W/2}" y="{y+26}" text-anchor="middle" font-size="9">{xl}</text>')
    h=y+(30 if xl else 19)+extra_h
    return f'<svg viewBox="0 0 {W} {h}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}{body(s,y) if callable(body) else body}</svg>'
def boxplot(mn,mx,step,lw,q1,m,q3,uw,out=(),lab=None,xl='',dec=0,draw=True,caps=False,fences=(),W=340):
    """draw=True: black boxplot to read from. draw=False: blank axis for students; the boxplot appears in red on the solutions copy."""
    def body(s,y):
        c='#000' if draw else RED; cls='' if draw else ' class="solfig"'; yc=y-14; bh=16
        o=[f'<g{cls} stroke="{c}" fill="none" stroke-width="1.2">',
           f'<rect x="{s(q1):.1f}" y="{yc-bh/2}" width="{s(q3)-s(q1):.1f}" height="{bh}" fill="{"#fff" if draw else "none"}"/>',
           f'<line x1="{s(m):.1f}" y1="{yc-bh/2}" x2="{s(m):.1f}" y2="{yc+bh/2}" stroke-width="1.8"/>',
           f'<line x1="{s(lw):.1f}" y1="{yc}" x2="{s(q1):.1f}" y2="{yc}"/><line x1="{s(q3):.1f}" y1="{yc}" x2="{s(uw):.1f}" y2="{yc}"/>']
        if caps: o+= [f'<line x1="{s(x):.1f}" y1="{yc-5}" x2="{s(x):.1f}" y2="{yc+5}"/>' for x in (lw,uw)]
        o+= [f'<circle cx="{s(x):.1f}" cy="{yc}" r="2.6" fill="{c}"/>' for x in out]
        for fx,t in fences: o.append(f'<line x1="{s(fx):.1f}" y1="{yc-15}" x2="{s(fx):.1f}" y2="{y}" stroke-dasharray="3 2" stroke-width=".9"/><text x="{s(fx):.1f}" y="{yc-17}" font-size="8" fill="{c}" stroke="none" text-anchor="middle">{t}</text>')
        return ''.join(o)+'</g>'
    return axis_svg(mn,mx,step,lab,xl,W,dec,body,top=30 if fences else 22)
def dotplot(mn,mx,vals,xl='',r=4,W=340,lab=1):
    from collections import Counter
    c=Counter(vals); hmax=max(c.values()); dy=2*r*0.95
    def body(s,y): return ''.join(f'<circle cx="{s(v):.1f}" cy="{y-r-1-k*dy:.1f}" r="{r}" fill="#fff" stroke="#000" stroke-width=".7"/>' for v,f in c.items() for k in range(f))
    return axis_svg(mn,mx,1,lab,xl,W,0,body,top=max(4,hmax*dy-24))
def stem(rows,key):
    return '<table class="stem">'+''.join(f'<tr><td class="st">{a}</td><td>{" ".join(map(str,b))}</td></tr>' for a,b in rows)+f'</table><div class="key">{key}</div>'

# ---------------------------------------------------------------- building blocks (S1 classes)
def ans(t,inline=False): return f'<span class="ans in">{t}</span>' if inline else f'<div class="ans">{t}</div>'
def lines(n,a='',cpl=46):
    if a:
        import re as _re
        n=max(n,sum(1+len(_re.sub('<[^>]+>','',seg))//cpl for seg in a.split('<br>')))
    return f'<div class="lines" style="position:relative">{"<div></div>"*n}'+(f'<div class="ans" style="position:absolute;top:-1.6mm;left:0;right:0;line-height:8mm;font-size:9.5pt">{a}</div>' if a else '')+'</div>'
def blank(a,w=30): return f'<span class="blank" style="min-width:{w}mm"><u>{a}</u></span>'
def five(vals=None,lab=('min','Q<sub>1</sub>','M','Q<sub>3</sub>','max')):
    v=vals or ['']*5
    return '<table class="t fill5"><tr>'+''.join(f'<th>{l}</th>' for l in lab)+'</tr><tr>'+''.join(f'<td><span class="ans in">{x}</span></td>' for x in v)+'</tr></table>'
def parts(items,cols=1):
    return f'<div class="parts" style="grid-template-columns:repeat({cols},minmax(0,1fr))">'+''.join(f'<div class="pt"><b>{k}</b><div>{q}<div class="pl">{ans(a,True)}</div></div></div>' for k,q,a in items)+'</div>'
def mc(opts,cols=1): return f'<div class="mc" style="grid-template-columns:repeat({cols},auto)">'+''.join(f'<div><b>{"ABCDE"[i]}.</b>{o}</div>' for i,o in enumerate(opts))+'</div>'
def guess(a,mcq=True):
    return (f'<div class="guess" data-a="{a}">Guess: <b>%</b> of students who got this right <span></span>'+(' &nbsp; Most common wrong answer <span class="sh"></span>' if mcq else '')+'</div>')
def cite(t): return f'<div class="cite">{t}</div>'
def q(t): return f'<p class="q">{t}</p>'
def box(hd,body,right='',cls=''): return f'<div class="box {cls}"><div class="hd">{hd}<span>{right}</span></div><div class="bd">{body}</div></div>'
def pair(h1,b1,h2,b2): return f'<div class="pair"><div class="hd">{h1}</div><div class="hd">{h2}</div><div class="bd">{b1}</div><div class="bd">{b2}</div></div>'
def item(n,body,fig='',sep=True):
    st=' style="border-top:1px dashed #bbb;padding-top:2mm;margin-top:2mm"' if sep else ''
    return f'<div class="row"{st}><div style="flex:1">{body}</div>'+(f'<div class="fig">{fig}</div>' if fig else '')+'</div>'


def hist(start,w,v,ymax,ystep,xl='',yl='frequency',draw=True,W=300,H=150,dec=None,lab=None,pct=False,clab=None):
    """Histogram on a grid. draw=False: empty grid for students; the bars appear in red on the solutions copy."""
    L,R,T,B=34,8,8,30; n=len(v); bw=(W-L-R)/n; k=(H-T-B)/ymax; y0=H-B
    o=[]
    y=0
    while y<=ymax+1e-9:
        yy=y0-y*k; o.append(f'<line x1="{L}" y1="{yy:.1f}" x2="{W-R}" y2="{yy:.1f}" stroke="#ccc" stroke-width=".5"/><text x="{L-4}" y="{yy+3:.1f}" font-size="8.5" text-anchor="end">{y:g}{"%" if pct else ""}</text>'); y+=ystep
    c='#000' if draw else RED; cls='' if draw else ' class="solfig"'
    o.append(f'<g{cls}>'+''.join(f'<rect x="{L+i*bw:.1f}" y="{y0-f*k:.1f}" width="{bw:.1f}" height="{f*k:.1f}" fill="{"#d9d9d9" if draw else "none"}" stroke="{c}" stroke-width="1"/>' for i,f in enumerate(v) if f)+'</g>')
    lab=lab or 1
    if clab:
        o+= [f'<text x="{L+(i+.5)*bw:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle">{t}</text>' for i,t in enumerate(clab)]
    else:
        for i in range(n+1):
            if i%lab==0:
                t=start+i*w; t=f'{t:.{dec}f}' if dec is not None else f'{t:g}'
                o.append(f'<text x="{L+i*bw:.1f}" y="{y0+11}" font-size="8.5" text-anchor="middle">{t}</text>')
    o.append(f'<line x1="{L}" y1="{y0}" x2="{W-R}" y2="{y0}" stroke="#000"/><line x1="{L}" y1="{y0}" x2="{L}" y2="{T-2}" stroke="#000"/>')
    if xl: o.append(f'<text x="{(L+W-R)/2}" y="{H-3}" font-size="9" text-anchor="middle">{xl}</text>')
    if yl: o.append(f'<text x="9" y="{(T+y0)/2}" font-size="9" text-anchor="middle" transform="rotate(-90 9 {(T+y0)/2})">{yl}</text>')
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}</svg>'

def ncurve(m=None,s=None,xl='',W=320,H=110,dec=0,pct=True,zrow=True,fill_x=False,fill_pct=False):
    """Normal curve. fill_x / fill_pct: blanks for students (answers in red on the solutions copy)."""
    x0,x1=12,W-12; yb=H-(10+(12 if m is not None else 0)+(12 if zrow else 0)+(12 if xl else 0)); top=8
    X=lambda z:x0+(z+3.6)/7.2*(x1-x0); Y=lambda z:yb-(yb-top)*math.exp(-z*z/2)
    o=[f'<polyline points="{" ".join(f"{X(z):.1f},{Y(z):.1f}" for z in [-3.6+i*.05 for i in range(145)])}" fill="none" stroke="#000" stroke-width="1.2"/>',
       f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke="#000"/>']
    o+= [f'<line x1="{X(z):.1f}" y1="{Y(z):.1f}" x2="{X(z):.1f}" y2="{yb+3}" stroke="#777" stroke-width=".6"/>' for z in range(-3,4)]
    if pct:
        cls=' class="solfig" fill="#c00"' if fill_pct else ''
        for z,p in [(-3.3,'0.15'),(-2.5,'2.35'),(-1.5,'13.5'),(-.5,'34'),(.5,'34'),(1.5,'13.5'),(2.5,'2.35'),(3.3,'0.15')]:
            yy=min(Y(z)+13,yb-3) if abs(z)<2 else yb-3
            o.append(f'<text{cls} x="{X(z):.1f}" y="{yy:.1f}" font-size="{7.5 if abs(z)<2 else 6.2}" text-anchor="middle">{p}%</text>')
    yy=yb+10
    if m is not None:
        cls=' class="solfig" fill="#c00"' if fill_x else ''
        o+= [f'<text{cls if z else ""} x="{X(z):.1f}" y="{yy}" font-size="8" text-anchor="middle">{m+z*s:.{dec}f}</text>' for z in range(-3,4)]
        yy+=12
    if zrow:
        o+= [f'<text x="{X(z):.1f}" y="{yy}" font-size="7.5" fill="#555" text-anchor="middle">{"z = " if z==-3 else ""}{z}</text>' for z in range(-3,4)]; yy+=12
    if xl: o.append(f'<text x="{W/2}" y="{yy}" font-size="8.5" text-anchor="middle">{xl}</text>')
    return f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W*0.27:.0f}mm">{"".join(o)}</svg>'

def table(rows,head=True,cls='t',style='font-size:9pt'):
    out=f'<table class="{cls}" style="{style}">'
    for i,r in enumerate(rows):
        tag='th' if head and i==0 else 'td'
        out+='<tr>'+''.join(f'<{tag}>{c}</{tag}>' for c in r)+'</tr>'
    return out+'</table>'

def fillrow(vals):
    """A table row whose cells are answers (red on solutions, blank for students)."""
    return [f'<span class="ans in">{v}</span>' for v in vals]

def build(code,title,P,name):
    JS=''.join(f'<script>{open(f"{ROOT}/lessons/{n}").read()}</script>' for n in ('a4view.js','paged.polyfill.min.js'))
    def page(sol,screen=True):
        return f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{code} guided worksheet{" · solutions" if sol else ""}</title><style>{CSS}</style>{JS if screen else ""}</head><body class="{"sol" if sol else ""}">'+'\n'.join(P)+'</body></html>'
    for sol,fn in ((0,f'{name}-worksheet'),(1,f'{name}-worksheet-solutions')):
        open(f'{ROOT}/lessons/{fn}.html','w').write(page(sol))
        open(f'/tmp/{fn}.html','w').write(page(sol,False))
    from playwright.async_api import async_playwright
    async def pdf():
        async with async_playwright() as p:
            b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); pg=await b.new_page()
            for fn in (f'{name}-worksheet',f'{name}-worksheet-solutions'):
                await pg.goto(f'file:///tmp/{fn}.html'); await pg.wait_for_timeout(600)
                await pg.pdf(path=f'{ROOT}/lessons/{fn}.pdf',format='A4',prefer_css_page_size=True,print_background=True)
            await b.close()
    asyncio.run(pdf()); print('built',name)

def title(code,t,sub):
    return f'<div class="title"><div class="code">{code}</div><h1>{t} <span class="solmark">· SOLUTIONS</span></h1><div class="pg">{CAM}<br>{sub}</div></div>'
def lis(L): return box('Learning intentions','<ul class="ki">'+''.join(f'<li>{x}</li>' for x in L)+'</ul>')
def checklist(SC): return box('Skills checklist','<div class="scg">'+''.join(f'<div class="sc"><div class="tick"></div><div><b>{i}. {s}</b></div></div>' for i,s in enumerate(SC,1))+'</div>','Tick when you can do it')
def coursework(cols,rev):
    return box('Coursework · Cambridge exercises',f'<div class="hwg" style="grid-template-columns:repeat({len(cols)+1},1fr)">'+''.join(f'<div><div class="hwh">{h}</div><div class="hwq">{t}</div><div class="tick"></div></div>' for h,t in cols)
      +f'<div><div class="hwh">Revision book</div><div class="hwq">{rev}</div><div class="tick"></div></div></div>'
      '<div class="sig"><div class="stamp">Teacher stamp</div><div class="lines"><div>Teacher signature <i></i> Date <i class="d"></i></div><div>Parent signature <i></i> Date <i class="d"></i></div></div></div>','Tick when done')

def stemfill(rows,key,cap=''):
    """Stem plot frame: stems printed, a ruled line for each stem's leaves (leaves in red on the solutions copy)."""
    r=''.join(f'<tr><td class="st">{a}</td><td class="lf"><span class="ans in">{" ".join(map(str,b))}</span></td></tr>' for a,b in rows)
    return f'<table class="stem sf">{"<tr><td colspan=2 class=cap>"+cap+"</td></tr>" if cap else ""}{r}</table><div class="key">{key}</div>'
