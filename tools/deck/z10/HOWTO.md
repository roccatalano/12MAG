# 12MAG slides: THE slide standard (z10 library)

Agreed with Rocco, 17 Nov 2026. **Every new or converted 12MAG deck is built this way.** This file replaces every older
slide rule (CLAUDE.md "Slide templates", `tools/deck/tpl/`, `tools/deck/<s#>/build.py`, `tools/deck/pdf.py`).
Finished examples: Chapter 1, `s1_build.py` … `s5_build.py` → `lessons/S1-slides.html` … `S5-slides.html`.
The 12MAG content rules in `CLAUDE.md` still apply (never write questions, verbatim + cited, % only from examiner reports,
planner card is the basis, burnt items ledger).

## Files
| File | What it is |
|---|---|
| `template_build.py` | **Clean starter.** Copy it to `s<n>_build.py` for a new lesson. |
| `lib/deck.py` | The library: `S` (slide list), `lesson()`, `qslide()`, `nl_slide()`, `st()`, figures (`stem`, `dotplot`, `hist`, `tiles`, `sumtiles`, `table_hl`, `five`), `casbox()` (CAS steps from `planner/cas-skills.json`), `SOCS`, standard slides (`title_slide`, `overview`, `checkin`, `coursework`) and `build()`. |
| `lib/core.css`, `lib/core.js` | Shared CSS/JS added to every deck: question layout, tiles, stem plot standard + `zstemfit`, dot plots, histograms, count badges, key-as-step, check-in ticks, coursework page, `zfit`. |
| `lib/num.py` (+ `.css/.js`) | Numerical build-ups: `hist_build` (one bar per click), dot/leaf build-ups, `socs_tpl` (SOCS template), `ftab` (filling frequency table), `dlist`, `stemmap`, `bigdot`. |
| `lib/cat.py` (+ `.css/.js`) | Categorical: `bchart`, `schart` (segmented), `schart_big`, `freq_table`, `chips`, `report`, `morph_svg` (bar chart → stacked → 100%). |
| `lib/boxplot.py` (+ `.css/.js`) | `bplot` (boxplot with fences, marks, bands, outliers), `fmt`, `rowtab`. |
| `lib/normal.py` (+ `.css/.js`) | `ncurve` (normal curve), `sh()` shading, `mk()` marks; `window.ZN` exposes the curve maths to lesson interactives. |
| `shell/` | The 10MA deck shell (navigation, help, toolbar, tile engine), CFU icons, coursework example page. Don't edit by hand. |
| `check.py` | Click-through test: every slide, one click at a time; reports overflow/clipping and JS errors; saves a screenshot of every slide fully revealed. |
| `pdf.py` | Slide PDF. |
| `chapter.py` | Chapter file: one HTML with a tab per lesson deck + one PDF. |

Importing a module (`from lib.num import *`) is all it takes to add its CSS and JS to the deck.

## Workflow (new lesson or converting an old deck)
1. `cp tools/deck/z10/template_build.py tools/deck/z10/s<n>_build.py`. Put the real sources in the docstring.
2. Fill it in from the **planner card**, in this order:
   title → learning intentions | success criteria | lesson sequence → CFAT (if any) → APK → Key ideas →
   New learning + Example / You try pairs (+ exam practice) → CAS → exit tasks → check-in → coursework.
   Lesson-only CSS/JS (an interactive, a one-off layout) go in `LESSON_CSS` / `LESSON_JS` at the bottom. If something
   would be useful in another lesson, put it in `lib/` instead.
3. Build: `python3 tools/deck/z10/s<n>_build.py` → `lessons/S<n>-slides.html`.
4. Check (slow: give it 5–10 minutes or run it in the background):
   `pip install playwright pypdf pillow && python3 -m playwright install chromium` (once), then
   `python3 tools/deck/z10/check.py lessons/S<n>-slides.html /tmp/shots`. Fix every reported issue, then LOOK at the
   screenshots (every slide fully revealed) and at some mid-reveal states.
5. PDF: `python3 tools/deck/z10/pdf.py lessons/S<n>-slides.html lessons/S<n>-slides.pdf` (question slides = 2 pages:
   question only, then all steps; others = 1 page, all steps). Pages are 1.5× screenshots.
6. Chapter file: `python3 tools/deck/z10/chapter.py <chapter> S<a> S<b> …` → `lessons/Ch<chapter>-slides.html` + `.pdf`.
7. Copy to G: `01 Lesson materials` as `<subs> slides.html/.pdf`; planner links `lessons/S<n>-slides.html/.pdf`.
8. Changing the library: rebuild ALL decks and compare `check.py` screenshots before and after (pixel diff); nothing may
   change unless you meant it.

## The one question template: `qslide(...)`
```
qslide(kind, num, title, pill, q, kib, steps, answer, src,
       fig='', figw='1fr', marks=None, vcaa=None, opts=None, key=None,
       watch=None, ans_do='', cls='', stack=False, parts=None)
```
- `kind`: `'ex'` Example · `'yt'` You try (grey bar) · `'apk'` · `'exam'` Exam practice · `'exit'` · `'cas'` CAS example.
- `pill`: source in the top-right box: `'Cambridge · Example 16'`, `'Edrolo 1F WE3a'`, `'VCAA 2024 Exam 1 Q3'` (exam pills name the VCAA source, never Edrolo; Edrolo goes in the footer).
- `q`: the question context (verbatim). **Lettered parts never go in `q`**: use `parts=` (a single `'<br><b>a.</b> …'` at the end is moved into the working box automatically).
- `kib`: Key idea box (every question slide has one). Shared ones: `KI_MED`, `KI_MEDH`, `KI_RANGE`, `KI_IQR`, `KI_MEAN`, `KI_CAS`.
- `fig`: the data / figure column. Data is shown once, here.
- `steps`: working, **one idea per click**: plain string, or `(text, actions)` to animate the figure. A string starting `<div class="zpart` (e.g. `socs_tpl(...)`) is placed as-is.
- `answer`: the **green ✓ Answer box** (bold, with units).
- `parts=[(label, part question, steps, answer, actions), …]`: each part asked, worked and answered in the working box, dotted lines between.
- `stack=True`: figure across the top, working in two columns underneath (side-by-side parts).
- `vcaa=87`: exam layout (question + data + options left; VCAA % badge, Key idea, working right). The badge fills on the answer click.
- MC: `opts=[('A','2'),…]`, `key='D'`, `OPTDIST[num or title] = [18,5,7,71,…]` (examiner report). Clicks: answer → % bars.
- `watch='…'`: orange **Watch out** box after the answer, **short-answer exam questions only**.
- `cls='tight'`: smaller working text for a crowded slide.

New learning: `nl_slide(title, lead, body, src, cls)`; steps in it are `st('<b>1</b> …', do=…, cls='stp')` (black text, red bold).

Standard slides (one call each): `title_slide(title, [subchapters with pages])`, `overview(code, LI, SC, SEQ, src)`,
`checkin(SC)`, `coursework(code, heading, [(Do, Questions)…], 'Exercise 1F: Using summary statistics', src)`.

## Step actions (space-separated, in `(text, actions)` or `st(..., do=...)`)
Each click re-applies every shown step's actions, so marks build up and stay; ← undoes exactly one step.
- **Tiles** (10MA engine): `sort:T` · `mid:T:a:b:mid|q` · `band:T:a:b:lo|hi` · `clr:T` · count `tn:T:start:K` / `tclr:T`
- **Stem plots**: `ln:id:start:K` number leaves (count badges) · `lm:id:i,j` median (red) · `lq:id:i,j` quartiles (blue) · `lb:id:a:b:lo|hi` halves · `lx:id:i,j` circle extremes · `sk:id` **write the key** (stem built with `build=True`) · `xl:id:a-b` leaves appear (num, `zstem zbuild`)
- **Dot plots**: `dn:id:K` number dots · `dm:id:i,j` median + M line · `xd:id:a-b` dots appear · `xm:id:k` mode dots red (num)
- **Histograms**: `xb:id:i` bar i appears (`hist_build`, num) · `hc:id` running totals · `hm:id:i` median column · `hq:id:i,j` quartile columns
- **Tables**: `tc:id:k,k` highlight cells · `dim:id:row` fade a row · `fill:id:k` fill a cell (`five`, num `ftab`; `fills(id, cells)`) · `xs:id:r` highlight row r (num)
- **SOCS template** (num): `bf:id:0-3` fill lines · `bok:id` turn green
- **Number boxes**: `cnt:id` numbers them · `sum:id` running total · `bal:id:value` "÷ n = value"
- **Categorical charts** (cat): `ax:id` axes · `bg:id:i,j` bars/segments grow · `lg:id` legend · `tf:id:key,key` fill table/report blanks · `hv:id:value:hb|hy|hg` highlight chips · `hr:id:r` highlight table row · `mo:id:1|2|3` morph stage (stack, 100%, legend)
- **Boxplots** (boxplot): `bx:id:part,part` show parts (`axis, box, med, wl, wu, out`, named fences/marks/bands) · `bx1:id:band` only this band · `bxo:id` colour outliers · `bdx:id` mark dot-plot extremes
- **Normal curve** (normal): `nx:id` x row · `nz:id` z row · `np:id` section % · `ns:id:a:b:col:label` shade (`sh()`) · `nm:id:z:col:label` mark (`mk()`) · `ncl:id` clear · `smp` samples
- **Exam**: `stat:87` fill the VCAA badge · `key:D` · `pct` % bars · New learning pairs: `pair:idA:idB`, `pair2:idA:idB`

## House rules (Rocco, 17 Nov)
**Title page**
- Formal topic title, unit line, the **textbook on its own row**, the **subchapters as a vertical list** (with pages).
  **No big S#, no "Lesson N".** (`title_slide` does this.)

**Questions and answers**
- Question context at the top; parts a, b, c… asked and answered **in the working box**, one after another, dotted lines between.
- Answers: green ✓ Answer box. Short-answer exam questions: orange **Watch out** box after it. **No "What's the distractor?" boxes. No yellow command-word chips.**
- Median = **(n+1)/2th position, then count to it** (count badges; never cross off from both ends). n even: a thin line centred between the two middle values. Tile rows never wrap.
- **Describe-the-distribution answers: SOCS template first** (blank, one line per letter: Shape, Outliers, Centre, Spread), **then fill it in line by line** (`socs_tpl` + `bf`/`bok`).

**Figures**
- **Stem plots are big**: the stem plot standard (`stem()` + `zstemfit`) sizes them as large as the figure box allows; **fixed columns**, stems and leaves the same font, and **highlights never resize** anything.
  **Writing the key is its own step** whenever a stem plot is built or answered (`stem(..., build=True)` + `sk:id`).
- **Histograms: one bar per click**, with the **matching frequency-table row highlighted** in the same click (`hist_build` + `xb` + row fill/highlight).
- Charts are built, not shown: axes on their own step, then bars/segments one per step.
- **Model transformations visually**: bar chart → stacked bar → 100% bar (`morph_svg` + `mo:id:1..3`).
- **Shape slides show the mean vs median comparison** (where each sits for symmetric / positively / negatively skewed).
- **Use space well**: no cramped plots. Where a question has an **a and b chart, use three columns** (question + data | part a + chart a | part b + chart b). Figures fill their box; don't leave a small plot in a big empty box.
- Data is shown once (in `fig`), never repeated in the working.

**Interactives**
- Must be mathematically right (test the extremes) and **every interactive has a context** (e.g. house prices knock-down / typical / renovated / mansion for mean vs median; party ages for the fences slider; two tests for z-scores).

**CAS, check-in, coursework**
- CAS: TI-Nspire **and** ClassPad steps both on the slide (the PDF needs them), copied from `planner/cas-skills.json` (`casbox`).
- Check-in: one tick box per success criterion (click = green tick, for modelling).
- Coursework: like 10MA: short table (Cambridge Exercise Q…, Practice booklet), margin rules, example A4 page on the right
  whose **heading shows this lesson's own exercise** (`coursework(..., 'Exercise 1F: Using summary statistics', ...)`). No "minimum for a coursework tick" line.
- **No Do Now slides and no 'Videos that might help' slide** (Rocco attaches those to Google Classroom).
- Footer of every slide = the source (book, example/question, page) and "Working by teacher." where it applies; "adapted" in the pill and footer when a question had to change.

**Checking**
- Run `check.py` and look at every slide fully revealed (and some mid-reveal states) before handing over.

## Notes
- `build(..., css_first=True)` puts module + lesson CSS before core.css (only S4 uses it, to stay exactly as approved).
- S2 fits its stem plots before `zfit` (one line in its `LESSON_JS`), also to stay exactly as approved.
- `lib/num.css` and `lib/cat.css` both style `.zft` tables; a deck using both modules should be checked carefully.
- Chapter file: decks load only when their tab is first shown (the fit scripts measure the slides and break in a hidden frame).
