"""Life cycle (Leslie) diagram helper for AoS 3 decks, worksheets and bound reference cards.
lifecycle(births, survs, labels=None) -> inline SVG.
births[i] = birth rate of age group i+1 (arc back to group 1; 0 = no arc unless show0), survs[i] = survival rate group i+1 -> i+2.
Style follows Cambridge U3&4 11E (red birth arcs above, blue survival arrows below the row of circles)."""
def _f(x):
    return ('%g' % x) if isinstance(x, (int, float)) else str(x)

def lifecycle(births, survs, labels=None, w=560, color=('#c62828', '#1565c0'), show0=False, fs=15, cls=''):
    n = len(births); labels = labels or [str(i + 1) for i in range(n)]
    gap = (w - 60) / max(n - 1, 1); R = 18; K = max(1, sum(1 for b in births[1:] if b or show0)); y = R + 18 + 26 * K + 20 + (40 if (births[0] or show0) else 0)
    xs = [30 + i * gap for i in range(n)]; H = y + 50
    o = [f'<svg class="lc {cls}" viewBox="0 0 {w} {H}" width="{w}" style="max-width:100%;display:block;margin:4px auto;font-family:inherit">',
         f'<defs><marker id="ar{id(o) if False else ""}r" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{color[0]}"/></marker>'
         f'<marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{color[1]}"/></marker></defs>']
    # births: arcs from group i back to group 1 (group 1 self-loop if births[0])
    k = 0
    for i, b in enumerate(births):
        if not (b or show0): continue
        if i == 0:
            o.append(f'<path d="M{xs[0]-10},{y-R+3} C{xs[0]-34},{y-70} {xs[0]+34},{y-70} {xs[0]+10},{y-R+3}" fill="none" stroke="{color[0]}" stroke-width="1.8" marker-end="url(#arr)"/>'
                     f'<text x="{xs[0]}" y="{y-58}" text-anchor="middle" font-size="{fs}" fill="{color[0]}">{_f(b)}</text>')
            continue
        k += 1; hgt = 18 + 26 * k
        x1, x0 = xs[i], xs[0]
        o.append(f'<path d="M{x1},{y-R} Q{(x0+x1)/2},{y-R-2*hgt} {x0+6},{y-R+1}" fill="none" stroke="{color[0]}" stroke-width="1.8" marker-end="url(#arr)"/>'
                 f'<text x="{(x0+x1)/2}" y="{y-R-hgt-4}" text-anchor="middle" font-size="{fs}" fill="{color[0]}" paint-order="stroke" stroke="#fff" stroke-width="4">{_f(b)}</text>')
    for i in range(n - 1):
        if survs[i] == 0 and not show0: continue
        o.append(f'<line x1="{xs[i]+R}" y1="{y}" x2="{xs[i+1]-R-1}" y2="{y}" stroke="{color[1]}" stroke-width="1.8" marker-end="url(#arb)"/>'
                 f'<text x="{(xs[i]+xs[i+1])/2}" y="{y+20}" text-anchor="middle" font-size="{fs}" fill="{color[1]}">{_f(survs[i])}</text>')
    for i, x in enumerate(xs):
        o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="#fff" stroke="#222" stroke-width="1.6"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="{fs-1}">{labels[i]}</text>')
    o.append('</svg>')
    return ''.join(o)
