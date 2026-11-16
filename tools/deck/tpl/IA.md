# Interactive slide helpers (tools/deck/tpl/tpl.py, ia.js, ia.css) — 16 Nov 2026

Inspired by the 10MA 10MAG Univariate Statistics deck (/home/claude/roccatalano/10ma, read only). Demo: `python3 tools/deck/demo/build.py` → /tmp/demo.html.

Attributes go on any reveal step: the 3rd item of a qslide step, an isteps item, or an invisible step `ifr(...)`.
- `ifr(*attrs)` invisible steps · `isteps([(html, attrs), …])` numbered step cards · `islide(pill, head, body, src, frags='', kind='learn')` free-layout slide.

## Data tiles (positions in the ORDERED list, 0-based; blank = all)
`tiles(rid, vals, fs=26)`; `tsort(rid)`; `tmed(rid, a='', b='', label='', cls='mid')` (cross off pairs + light middle); `tcross`/`tmid` separately; `thalves(rid)`; `tquart(rid, n, q1lab, q3lab)` → 3 attrs (split, Q1, Q3).
```python
pic = tiles('t1', [23,17,31,21,12,40,19,28,21,15,26])
isteps([('Order the data', tsort('t1')), ('Cross off pairs', tmed('t1', label='M = 21'))])
h, q1, q3 = tquart('t1', 11, 'Q₁ = 17', 'Q₃ = 28')
```

## Sliders (teacher drags; `fset(rid, v)` animates to a value on a click / for the PDF)
- `fence_slider(rid, data, max, min=0, k=None, step=1, lo, hi, tick, lab, xl, dec=2)`: dot plot + Q1/Q3/LF/UF + red outlier zones, live "x = 25 > UF = 16 → outlier".
- `box_slider(...)`: same as a boxplot (whisker to last non-outlier, outlier dots).
- `z_slider(rid, m, s, x0, step, xl)`: normal curve shading + z working + 68–95–99.7 % at whole z.
- `log_slider(rid, lo=0, hi=6, x0, xl)`: log10 scale vs x scale.
- `shape_slider(rid, v0)` + `shset(rid, v)`: skew a histogram, shape name, tail arrow, mean vs median.

## Card sort
`card_sort(rid, items, buckets=…)` items `[(text, 'Categorical/Nominal'), …]`; `sort_steps(rid)` (two-level) / `sort_steps(rid, 1)`. Click card then bucket, or drag; reveal step marks ✓/✗ and moves cards.

## Stem plot + tally → table → histogram
- `stem_fly(rid, vals, unit=1, key='', split=False)`; `leaf(rid, '0-5'|'0,3'|'all')`; `lsort(rid)`.
- `tally_set(cid, tid, vals, edges, labels=None, head=…, total=True)` → (chips_html, table_html); `ftally(cid, tid, i, hist=None)`; `ftot(tid)`; histogram needs `hist(..., extra='data-stepped="1"')`.

Labels may hold HTML but not `|` or `;`; join two specs on one step with `;`.

## Controls (as 10MA)
Click/→ = step, double = next slide; ← = back, double ← = previous slide cleared; Backspace = back, double = clear slide. Widget clicks never advance. Replays (back, PDF) jump widgets to their final state.
