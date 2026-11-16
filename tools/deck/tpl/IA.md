# Interactive slide helpers (tools/deck/tpl/tpl.py, ia.js, ia.css) — 16 Nov 2026

Modelled on the 10MA 10MAG Univariate Statistics deck (/home/claude/roccatalano/10ma, read only; Rocco prefers its versions).
Demo (every widget): `python3 tools/deck/demo/build.py` → /tmp/demo.html. PDF: `python3 tools/deck/pdf.py /tmp/demo.html /tmp/demo.pdf`
(replays every step at once, so each widget prints in its final state: sliders at the last preset, sorts answered, plinko = full bell pile).

Attributes go on any reveal step: the 3rd item of a qslide step, an isteps item, or an invisible step `ifr(...)`.
- `ifr(*attrs)` invisible steps · `isteps([(html, attrs), …])` numbered step cards · `islide(pill, head, body, src, frags='', kind='learn')` free-layout slide.
Clicks on widgets (class `ia`) never advance the slide.

## 1 Data tiles (positions in the ORDERED list, 0-based; blank = all)
`tiles(rid, vals, fs=26)` · `tsort(rid)` · `tmed(rid, a='', b='', label='', cls='mid', line=False)` (cross off pairs + light the middle;
`line=True`: solid line between the two middle tiles when the count is even) · `tcross` / `tmid` separately · `thalves(rid)` ·
`tquart(rid, n, q1lab, q3lab, line=False)` → 3 attrs (split, Q1, Q3).
At the split the median tile(s), M label and median line stay; tiles crossed off for the median keep a grey strike.
```python
h, q1, q3 = tquart('e8', 8, 'Q₁ = 10', 'Q₃ = 18', line=True)
isteps([('Order', tsort('e8')), ('M = 13', tmed('e8', label='M = 13', line=True)), ('Halves', h), ('Q₁', q1), ('Q₃', q3)])
```

## 2 Sliders: every one has a visible range control under the figure (10MA style); the figure handle drags too
Presets on a click (and for the PDF): `fset(rid, v)` (fences, box, z, log) · `shset(rid, skew)` (shape).
- `fence_slider(rid, data, max, min=0, k=None, step=1, lo, hi, tick, lab, xl, dec=2, name='', lt='', rt='', pre='', post='', mm=False, vals=None)`:
  10MA house-prices layout. Value list (moving value ringed, outliers red) · dot plot with the fence zone and dashed LF/UF · control
  `[name] lt ──●── rt [value]` · summary on the right: Q1, Q3, IQR, LF = Q1 − 1.5 × IQR, UF = Q3 + 1.5 × IQR, the rules
  'x < LF → outlier' / 'x > UF → outlier' (the one that applies turns red) and 'Outlier: …'. `mm=True` adds median and mean lines.
  ```python
  fence_slider('fs', [620,680,700,720,750,780,820,800], max=3000, k=7, step=10, lo=100, tick=100, lab=500,
               xl='sale price ($ thousands)', name='Price', lt='Knocked down', rt='Mansion', pre='$', post='k', mm=True)
  ```
- `box_slider(rid, data, max, **same kwargs)`: 10MA walking-times layout. Data dots on top (the dragged value is a ring, red when it is
  an outlier) · a boxplot below whose whisker stops at the last non-outlier, with outliers as red dots and dashed fences · summary =
  five-figure summary + IQR + fences + rules + outlier.
  ```python
  box_slider('bs', [12,14,15,15,16,17,18,18,19,20,21,22,24], max=45, k=12, lab=5, xl='walking time (minutes)',
             name='Time', lt='Next door', rt='Very far', post=' min')
  ```
- `z_slider(rid, m, s, x0, step, xl, dec, name='', lt='', rt='')`: normal curve shaded below x, z working, and the 68–95–99.7% % at whole z.
- `log_slider(rid, lo=0, hi=6, x0, xl)`: log10 scale vs x scale (control in log units, shows x).
- `shape_slider(rid, v0)`: control 'Tail to the left ── Tail to the right'; shape name, tail arrow, mean vs median.

## 3 Card sort (10MA 'Sort it')
`card_sort(rid, items, buckets=…, cols=4, fs=18)` with items `[(text, 'Categorical/Nominal'), …]`. Each card has Step 1 buttons; a right
answer turns green and opens Step 2 showing only that group's sub-buckets; a wrong one shakes red (try again). Score n / N + Reset.
Steps: `sort_steps(rid)` (all Step 1 answers, then all Step 2) · `sort_steps(rid, 1)` · `sort_steps(rid, per_card=True, n=8)` (one card per
click) · `sreveal(rid, level, '0,3')` for your own order. Revealed answers glow green; wrong guesses keep their red mark.

## 4 Stem plot + tally → table → histogram
- `stem_fly(rid, vals, unit=1, key='', split=False)`; `leaf(rid, '0-5'|'0,3'|'all')`; `lsort(rid)`.
- `tally_set(cid, tid, vals, edges, labels=None, head=…, total=True)` → (chips_html, table_html); `ftally(cid, tid, i, hist=None)`; `ftot(tid)`; histogram needs `hist(..., extra='data-stepped="1"')`.

## 5 Two tests: which result is relatively better?
`ztwo(rid, A=(name, mean, SD, score[, step]), B=(…), dec=1)`: two normal curves side by side, each with its own score control and
z = (x − x̄)/s; the verdict line compares the z-scores ('2 > 1.5 → relatively better on English'). Step: `ztset(rid, xA, xB)` (None keeps one).
```python
ztwo('zt', ('Maths', 60, 10, 75), ('English', 70, 5, 74)) + isteps([('English 80', ztset('zt', None, 80))])
```

## 6 Plinko / Galton board
`plinko(rid, rows=10, note='')`: balls go left or right at every peg and pile up in the bins. Buttons Drop 1 · Drop 50 · Reset,
a ball count, and the premise text (default: most land near the middle, fewer further out: a bell shape).
Step: `pdrop(rid, n=50)` drops n balls live. Replays and the PDF add the expected binomial pile at once, so the final frame is a full bell.
`pdrop(rid, n, now=True)` fills at once live too. `pdrop(rid, 0)` resets.
```python
islide('Learn', 'Why a bell shape?', plinko('pk'), SRC, frags=ifr(pdrop('pk', 50), pdrop('pk', 150)))
```

## 7 Rounding: decimal places vs significant figures
`rounder(rid, value, mode='dp', n=2)` (give value as a string to keep its digits, e.g. '0.0047386'). Mode buttons, a count control
(dp 0–4, sf 1–4) and −/+ buttons. Kept digits are blue, leading zeros grey, the **deciding digit** yellow and labelled ('5 or more: round up' /
'less than 5: keep'), and the rounded result is green. Rounding works on the digit string, so there are no float errors.
Step: `rset(rid, 'dp'|'sf', n)`.

## 8 Normal curve (`norm(...)`, drawn by tpl.js; ia.js adjusts it)
- The 34% / 13.5% / 2.35% / 0.15% labels sit above the highest point of the curve under them, so they never touch it. On small
  charts with no room above, they go inside the band under the curve.
- `norm(rid, {..., "br": True})`: three hooked brackets under the axis (68% over z = ±1, 95% over ±2, 99.7% over ±3). They stay on to
  the end. `"br": [1, 2]` draws some only; `"brhide": True` hides them until `nbr(rid, '1')`, `nbr(rid, '2')`, … (they then stay).

Labels may hold HTML but not `|` or `;`. Join two specs on one step with `;`.

## Controls (as 10MA)
Click/→ = step, double = next slide; ← = back, double ← = previous slide cleared; Backspace = back, double = clear slide. Widget clicks never advance.
Replays (back, PDF) jump widgets to their final state.
