# 12MAG slides in the 10MA house style ("z10" builder)

Built 17 Nov 2026 with Rocco. Worked example: **S3, 1F Measures of centre and spread**
→ `s3_build.py` builds `lessons/S3-slides-v2.html` (36 slides). Copy it for every new lesson.

These rules replace the older 12MAG slide-template rules in `CLAUDE.md` for any deck built with this builder.

## Files
| File | What it is |
|---|---|
| `s3_build.py` | The whole builder + the S3 content. Helpers and `qslide()` at the top, slides in the middle, CSS + JS at the bottom. |
| `shell/head.html`, `shell/tail.html` | The 10MA deck shell (CSS, navigation, help panel, toolbar, 10MA tile engine), copied from `10MA/lessons/10MAG Univariate Statistics - Slides.html`. Don't edit by hand. |
| `shell/cfu.json` | Check-for-understanding icons (cold call, quick write, multiple choice, think-pair-share, class discussion), from the old 12MAG decks. |
| `shell/cwr.html`, `shell/cwl.html` | The example A4 coursework page and margin rules from the 10MA coursework slide. |
| `check.py` | Click-through test: steps through every slide one click at a time, reports overflow/clipping and JS errors, saves screenshots. |

## Make a new lesson (e.g. S4)
1. `cp s3_build.py s4_build.py`; change `OUT` (e.g. `S4-slides-v2.html`), `SUB` (subchapter line in the title bars) and the title slide.
2. Replace the slides between `# ---------------- slides ----------------` and `CSS = r'''`. Keep the order from the planner card:
   title → learning intentions | success criteria | lesson sequence → CFAT (if any) → APK → Key ideas → New learning + Example / You try pairs (+ exam practice) → CAS → exit task → check-in → coursework.
3. Content rules (12MAG `CLAUDE.md` still applies): **never write questions**, copy verbatim and cite in the footer; "adapted" in the source pill and footer if a question had to change; % correct only from examiner reports.
4. Build: `python3 tools/deck/z10/s4_build.py`
5. Check: `pip install playwright && python3 -m playwright install chromium` (once), then
   `python3 tools/deck/z10/check.py lessons/S4-slides-v2.html /tmp/shots` — fix every reported issue, then look at the screenshots (every slide fully revealed).

## The one question template: `qslide(...)`
Every question slide uses it, so questions and answers always look the same.
```
qslide(kind, num, title, pill, q, kib, steps, answer, src,
       fig='', figw='1fr', marks=None, vcaa=None, opts=None, key=None,
       watch=None, ans_do='', cls='', stack=False, parts=None)
```
- `kind`: `'ex'` Example · `'yt'` You try (grey bar) · `'apk'` · `'exam'` Exam practice (MC) · `'exit'` · `'cas'` CAS example.
- `pill`: source in the top-right box: `'Cambridge · Example 16'`, `'Edrolo 1F WE3a'`, `'VCAA 2024 Exam 1 Q3'`.
- `q`: the question context (verbatim). **Lettered parts never go in `q`**: use `parts=` (or end `q` with `'<br><b>a.</b> …'` for a single part; it is moved into the working box automatically).
- `kib`: Key idea box text (every question slide has one).
- `fig`: the data / figure column (stem plot, dot plot, histogram, tiles, table). Data is shown once, here.
- `steps`: working, **one idea per click**. Plain string, or `(text, actions)` to animate the figure.
- `answer`: shown in the **green ✓ Answer box** (bold, with units).
- `parts=[(label, part question, steps, answer, actions), …]`: each part is asked, worked and answered in the working box, separated by dotted lines.
- `stack=True`: figure across the top, working in two columns underneath (for side-by-side parts such as Example 14 a | b).
- `vcaa=87`: exam layout (question + data + options left; VCAA % badge, Key idea and working right). The % badge fills on the answer click.
- `opts=[('A','2'),…]`, `key='D'` and `OPTDIST[title] = [18,5,7,71]`: multiple choice. Clicks: answer (correct option ✓) → % bars for every option.
- `watch='…'`: orange **Watch out** box after the answer. Use only on **short-answer exam questions**.
- `cls='tight'`: smaller working text for a crowded slide. `cls='eng'`: the slide uses tiles.

New learning slides use `nl_slide(title, lead, body, src, cls)`. Their steps are black text with red bold (10MA style).

## Figure helpers
`stem(id, [(stem, 'leaves'), …], key)` · `dotplot(id, values, lo, hi, axis_label)` · `hist(id, start, width, freqs, ymax, ystep, xlabel, ylabel)` · `tiles(t, values)` (10MA tiles; `data-s` holds the sorted values) · `tilerow(label, t, values)` · `sumtiles(id, values)` (number boxes with a running total) · `table_hl(id, [(header, [cells]), …])` (cells `data-k = row*100 + col`) · `five(id, values)` (five-number summary table that fills in).

## Step actions (space-separated in `(text, actions)`)
Each click re-applies every shown step's actions, so marks build up and stay; ← undoes exactly one step.
- Tiles (10MA engine): `sort:T` · `mid:T:a:b:mid|q` (middle of a..b; n even → two tiles with a thin line between) · `band:T:a:b:lo|hi` · `clr:T`
- Counting to a position (how medians and quartiles are found: work out the (n+1)/2th position, then count to it): `tn:T:start:K` numbers tiles 1..K · `tclr:T` clears the numbers · `ln:id:start:K` numbers stem-plot leaves
- Stem plots: `lm:id:i,j` median (red) · `lq:id:i,j` quartiles (blue) · `lb:id:a:b:lo|hi` halves · `lx:id:i,j` circle the extremes
- Dot plots: `dn:id:K` number dots 1..K in counting order · `dm:id:i,j` mark the median and draw the M line
- Histograms: `hc:id` running totals (only on non-empty columns) · `hm:id:i` median column · `hq:id:i,j` quartile columns
- Number boxes: `cnt:id` numbers them · `sum:id` running total · `bal:id:value` "÷ n = value"
- Tables: `tc:id:k,k` highlight cells · `dim:id:row` fade a row · `fill:id:k` fill a five-number cell
- Exam: `stat:87` fill the VCAA % badge · `key:D` · `pct` show the % bars
- New learning pairs: `pair:idA:idB`, `pair2:idA:idB`

## House rules agreed with Rocco (17 Nov)
- Question context at the top; parts a, b, c… asked and answered **in the working box**, one after another, dotted lines between.
- Answers: green ✓ Answer box. Short-answer exam questions: orange **Watch out** box after it. **No "What's the distractor?" boxes.** No yellow command-word chips.
- Median = **(n+1)/2th position, then count to it** (never cross off from both ends). n even: a thin line centred between the two middle values. Tile rows never wrap.
- CAS: TI-Nspire **and** ClassPad steps both on the slide (the PDF needs them).
- Interactives must be mathematically right (test the extremes) and have a context (e.g. the house-prices mean-or-median slider: knock down / typical / renovated / mansion, fences drawn, three verdicts).
- Check-in: one tick box per success criterion (click = green tick, for modelling).
- Coursework: like 10MA: short table (Cambridge Exercise Q…, Practice booklet), margin rules, example A4 page on the right. No "minimum for a coursework tick" line.
- **No Do Now slides and no 'Videos that might help' slide** (Rocco attaches those to Google Classroom).
- Check every slide with `check.py` and by eye before handing over.

## Still open
- `check.py` flags two slides in S3 as slightly over-full with every step shown: Example 21's working box, and the question column of the VCAA 2024 Exam 1 Q14 exam-practice slide.
- 2024 Exam 1 Q3: there is no distractor box now, but the note about why 18% chose 2 was a teacher guess. If it comes back, label it as one.
- PDF/print version not built yet.
