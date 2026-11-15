# 12MAG handover — 15 Nov 2026 (updated 13:25)

Read `CLAUDE.md` first (rules, item index, **slide template rules**), then this file. The full to-do list is `docs/TODO.md`.
Repo: `roccatalano/12MAG` (GitHub Pages: roccatalano.github.io/12mag/ → `planner/`). Rocco's dashboard repo `roccatalano/teaching-dashboard-2027` is read-only unless he asks.
Push: `git -c push.negotiate=true push origin HEAD`. G: drive is reached through the desktop-app bridge (stage files to read; commit files to write; can't move/rename/delete).

## Done 15 Nov (13:10): bound reference cards 1C (full), 1D (half), 1E (half)
- `lessons/1C|1D|1E bound reference.html` + combined `1C-1E bound reference.html`; also on G: `01 Lesson materials`. Planner S2 card updated.
- New helpers in `tools/bref/cards.py`: `hist()` (any histogram, axes optional), `mini()` (shape thumbnails), `dots()`, `stem()` (stem plot table, styles in bref.css). Neck-size dot plot image: `tools/bref/vcaa2020e2_q2a.png`.
- VCAA boxes: 1D = 2020 E2 Q2a (93%), 2016 E1 Q3 (87%, from the exam-practice index; S2 slide still says ?%); 1E = 2019 E1 Q3 (71%). 1C has no VCAA question from the lesson, so it carries Examples 6–9 + a description checklist.

## Done 15 Nov (13:30): bound reference card 1F (full A4)
- `lessons/1F bound reference.html` (+ G:), planner S3 card updated. VCAA boxes: 2017 E2 Q1ai (87%, the S3 APK) and 2026 NHT E2 Q1b, d (the S3 exit; NHT = answers only). Exit 1 (Edrolo 1G Q11, adapted from VCAA 2020 E2 Q4aii) left off: the original VCAA wording wasn't to hand.

## Done 15 Nov (13:50): bound reference card 1G (full A4)
- `lessons/1G bound reference.html` (+ G:), planner S4 card updated. New helper `box()` (boxplot SVG with fences, 25% bands, outlier dots; `axis=False` for sketches). VCAA box: 2020 E2 Q2c (55%), answer boxplot drawn. Left off for space: 2021 E2 Q1e (heptathlon, needs the 15-row table) and the APK firefighter question (Edrolo-adapted from VCAA 2017 E1 Q2).

## Done 15 Nov (14:10): bound reference cards 1H (full) + 1I (half)
- `lessons/1H|1I bound reference.html` + combined `1H-1I bound reference.html` (+ G:), planner S5 card updated. New helper `ncurve()` (normal curve with section %, x and z rows, optional shading).
- 1H VCAA boxes: 2019 E2 Q2b (58%), 2021 E2 Q1c (78%). 1I = own-words definitions only (Interactive Textbook; no Study Design dot point, no examples): half card has spare room. Ask Rocco whether to keep 1I separate or merge into 1H.
- All Chapter 1 bound reference cards (1A–1I) are now done.

## Done 15 Nov (13:00–13:25): planner + CAS guide + videos
- Planner: materials with nested copies show no top-level Open/PDF; lesson shapes cleared ('To be filled in last'); bound reference always nested with Open + PDF per card; PDFs + 'Download PDF' button on every bound reference.
- `docs/TODO.md` = full creation + review list.
- Self-study videos `planner/videos.json` (Ch 1 = MaffsGuru 1A–1I + TI z-scores, all approved). CAS guide `planner/cas-skills.json` (one master list; planner: CAS guide → skill → ClassPad / TI-Nspire with steps + one main video + More videos). Ch 1 steps complete; ClassPad dot plot to confirm.

## Done 15 Nov (afternoon): everything Draft + guided worksheets for S2, S3, S5
- **Rocco: every made resource is now 'Draft' on the planner** (materials 'ready' → 'draft'; CFAT cards 'Ready…/Written' → 'Draft'). Nothing goes back to Ready until it passes the fine-tooth-comb review.
- New worksheets (student + solutions, html + pdf; G: names `1C-1E worksheet(.pdf)`, `… worksheet solutions(.pdf)`): `tools/deck/s2|s3|s5/worksheet.py`, shared helpers in `tools/deck/wslib.py` (copied from s4/worksheet.py, plus hist, ncurve, stemfill, table/fillrow, build → html + PDF). Planner cards have Student copy / Solutions copies (S1 has no solutions copy).
- Page counts (target 4 = 2 double-sided sheets): S2 6, S3 4, S5 5. S4 is 4 (solutions 5).
- Worksheets follow the S4 shape (no Do Now section; APK → Example/You try pairs → CAS → exits with "guess the %" → skills checklist → coursework).
- `ws.css` (shared with S4) gained: stem leaves left-aligned, `stemfill` frames, taller answer cells in tables.

- **Lesson shapes cleared (Rocco, 15 Nov):** the planner's right-hand 'Lesson shape' pane now says 'To be filled in last' for every lesson (`SHAPES_ON=false` in `planner/index.html`). Fill them in at the very end.

## Done 15 Nov (afternoon): Lesson 1 slides rebuilt on the templates (deep review, resource 1 of 4)
- `lessons/S1-slides.html` (28 slides), build `tools/deck/s1/build.py`, screenshots `tools/deck/s1/shoot.py`. G: `01 Lesson materials\1A-1B slides.html`. **No PDF** (as S4); `1A-1B slides.pdf` on G: is stale — Rocco to delete.
- **No Do Now in Lesson 1** (Rocco: first lesson of the year, nothing to retrieve).
- Fixed vs old deck: 1A You try was Edrolo 1A **Q11** (an exercise) → now Edrolo 1A WE1–3; old 1B Learn used invented data (40 students' travel) → removed; APK '?%' → 70% (2021 E1 Q1), 57% (2020 E1 Q10) with distractor %s from the reports; exit 3 '?%' → 76%; exit 1 81% (Edrolo) → **83%** (2019 E2 report: 83% scored 1); 'Homework' → Coursework; check-in, Key definitions/formulas and Videos slides added; CAS slide (stats-list set-up, Cambridge 1A survey data).
- Dropped: the old think-pair-share survey slide; APK Cambridge U1&2 2B #5 (needs the 2A #2 table) removed from the planner card.
- Ledger: 'Lesson handout' and 'Exam Q (1A)' rows freed (Rocco agreed; `build_ledger.py` now skips them); S1 rows re-logged.
- Note: `y12_edrolo_exam_practice.csv` 1A Q14 says 90 (avg 0.9); the report shows 83% scored the mark.

## NEXT JOB: deep review of Lesson 1 (1A–1B), continued: worksheet → bound reference → planner card
### Original brief: deep review of Lesson 1 (1A–1B) — Rocco, 15 Nov: "make sure they are up to standard and not AI slop"
Everything is **Draft** on the planner. Review one resource at a time, show Rocco what you found (with screenshots), fix what he agrees to, then mark it Ready only when he says so.

**Lesson 1 resources** (planner card `gm12-u3-s1`, subchapters 1A Types of data, 1B Displaying and describing categorical data):
1. **Slides** `lessons/S1-slides.html/.pdf` (G: `1A-1B slides`). OLD layout, and there is **no build script** in `tools/deck/` for S1 (s2–s5 only): fixing it properly means rebuilding on the templates (`tools/deck/tpl/tpl.py`, model `tools/deck/s4/build.py`; see CLAUDE.md "Slide templates"). Known: says 'Homework' (→ Coursework), Do Now count and lesson order to check against rules 3–4.
2. **Guided worksheet** `lessons/S1-worksheet.html/.pdf` (G: `1A-1B worksheet`). Student copy only, **no solutions copy**, no build script. Max 4 pages (it is 6). New worksheets are built with `tools/deck/wslib.py` (see `tools/deck/s3/worksheet.py`); rebuilding S1 that way gives a solutions copy too.
3. **Bound reference** `lessons/1A|1B|1A-1B bound reference.html/.pdf` (build: `tools/bref/build.py`, content `tools/bref/cards.py`).
4. **Planner card** for the lesson: learning objectives, success criteria, Study Design, key vocab, CAS guide (`stats-list`), self-study videos (MaffsGuru 1A, 1B), Do Now, APK, worked examples / you trys, exits, coursework (planner card vs slides had APK differences: check).
(CFAT 1.1.1 covers 1A–1E: review it with lesson 3, not here.)

**Check every item for:**
1. Wording copied word for word from the source PDF (stage it from G: `02 Sources`), or labelled "adapted".
2. Citation right (book, example/question number, page).
3. % correct = examiner report (past-design reports sit with the past papers in `02 Sources\VCAA past 2016-2022`; current in `VCAA current 2023-26`). Missing report → say which and ask.
4. Maths and answers right; figures match the data.
5. Rules: lesson shape (rule 3), Do Now = 2 × Exam 1 + 2 × Exam 2 current-design VCAA (rule 4), APK sources (rule 5), You try = mapped Edrolo WE (rule 6), exits = Edrolo U3&4 VCAA reprints (rule 7).
6. Burnt items: `tools/ledger.csv`. **Already spotted:** VCAA 2019 E2 Q1a is logged twice (S1 exit via Edrolo U3&4 1A Q14 AND an older 'Exam Q (1A)' row); VCAA 2020 E1 Q10 twice (S1 APK via Edrolo U1&2 1A Q14 AND 'Exam Q (1A)'). Work out which rows are stale (old handout/label era) vs real double use.
7. Writing: own-words notes short and plain, no filler, nothing made up, no "AI voice".
8. Layout: A4 print, page limits, nothing cut off; every slide step checked visually (`tools/deck/s4/shoot.py`, Playwright + /usr/bin/google-chrome).
9. Consistency: slides ↔ worksheet ↔ bound reference ↔ planner card say the same thing.

**Suggested way of working:** read the slides first and list every item (Do Now, APK, examples, you trys, exits) with its source; stage the source pages; compare; give Rocco one findings table per resource (item · problem · proposed fix) before changing anything. Then do the same for the worksheet and bound reference.

## Done 15 Nov: Lesson 5 slides (1H–1I)
- `lessons/S5-slides.html` (34 slides), also `01 Lesson materials\1H-1I slides.html` on G:. Build: `tools/deck/s5/build.py` (screenshots: `tools/deck/s5/shoot.py`).
- Order: title → Today's lesson → **CFAT 1.1.2 slide (20-min timer)** → Key definitions/formulas → Do Now ×4 → APK ×2 → Learn/WE/You try (+ CAS after WE29) → Learn 1I → exits ×2 → check-in → coursework → videos.
- Do Now: VCAA 2025 E1 Q1 (75%), 2024 E1 Q4 (68%), 2025 E2 Q1ci (69%), Q1cii (47%). APK: Cambridge U1&2 2G #13; Edrolo U1&2 1G Q14 (VCAA 2020 E2 Q2bi, 40%). Exits: Edrolo U3&4 1H Q12 (VCAA 2019 E2 Q2b, 58%), 1I Q13 (VCAA 2021 E2 Q1c, 78%). WE 28–34; You trys Edrolo 1H WE1, WE2, WE3, 1I WE1, WE2, WE3 (WE33: none). All logged in the ledger; planner card updated.
- Dropped from the card's APK (already burnt): Cambridge U1&2 2F #12 (S3) and Edrolo U1&2 1G Q13 (= VCAA 2017 E2 Q1bi, burnt by CFAT 1.1.3 via Edrolo U3&4 1H Q13).
- **1I is Interactive-Textbook only**: its Learn slide is in own words (population, sample, random sample) and no 1I examples exist in print. Rocco to check it against Cambridge GO. A 1I success criterion was added ("I can explain the difference between a population and a sample.").
- Template changes (reusable): `norm()` normal-curve chart (tpl.js `drawNorm`: x/z axis rows, section %, frag shading/marks), `cfat()` CFAT slide, histogram `clab` centred labels; **bug fix in `assemble`** (template CSS was inserted at the wrong place when the deck title differed from the engine's).
- Normal-probability CAS videos (ClassPad Help 80/470/81) are on the planner card but not on the slides: GM uses the 68–95–99.7% rule, not normCdf.
- Next: 1H–1I guided worksheet, bound reference entries (1G, 1H–1I), Ch 1 test (L6).

## Planner conventions (15 Nov)
- Material with several versions → `copies: [{label, file, pdf}]` renders side-by-side cards (Student copy / Solutions). A copy with no file shows "To make".
- Card text minimal: one-line description, no subtext on copies (also in CLAUDE.md).
- Material links get `?v=<time>` so browsers always open the newest file. Always overwrite the same file names when iterating; never make new copies.
- A4 HTML must open as A4 pages: inline `a4view.js` + `paged.polyfill.min.js` (see `tools/revision/ch1/build.py`, which also shows a grey "Loading A4 pages…" screen while it lays out).

## Done this session (14 Nov evening)
1. **Insight is never burnt** (Rocco). 10 Insight rows removed from `tools/ledger.csv`; `build_ledger.py` skips Insight.
2. **Lesson 4 (1G) slides** — `lessons/S4-slides.html` (29 slides), also `01 Lesson materials\1G slides.html` on G:.
   - Do Now: VCAA 2023 E1 Q1, Q6; 2025 E2 Q1a, Q1b. APK: Cambridge U1&2 2H #14, #15; Edrolo U1&2 1F Q16 (VCAA 2017 E1 Q2). Exits: Edrolo U3&4 1E Q19 (VCAA 2020 E2 Q2c), Q20 (VCAA 2021 E2 Q1e). WE 22–27 with You trys Edrolo 1E WE4, WE5 (CAS), WE6, 1F WE5. All logged in the ledger; planner card updated (Do Now, success criteria, coursework, slide link).
   - No PDF (Rocco). `01 Lesson materials\1G slides.pdf` on G: is stale — Rocco to delete it.
3. **Slide templates** — `tools/deck/tpl/tpl.py` (+ `tpl.css`, `tpl.js`); engine `tools/deck/engine.html` (made by `tools/deck/make_engine.py` from the old S4 build `s4/build_v1.py` + `s4/extra.js` boxplot drawer). All rules are in CLAUDE.md ("Slide templates"). Key functions: `title, today, keys, qslide (fx/F/V/FR formulas, plist + parts, afig + build, mc/dis), learn (kcard), cas (yt videos), checkin, coursework, videos, assemble`.
4. **Command words** — highlighted yellow in the question + a tile top right ("FIND · the value, with working"). The Study Design has no command-word list; VCAA's separate Glossary of command terms does (vcaa.vic.edu.au; the page needs a browser approval; definitions not yet captured). Not yet done: tag every item in `vcaa_current_index.csv` with its command word.

## Done 15 Nov: Chapter 1 revision booklet
- `lessons/Ch1-revision-booklet.html/.pdf` + `-solutions` (also `01 Lesson materials\Ch1 revision booklet*.html/.pdf` on G:). Linked on the Ch 1 coursework check + test card.
- Insight GM1 Q1–36 + GM2 Q1–12 "Investigating data distributions", CFAT style, one section per subchapter 1A–1H (gradual homework). Multi-part questions go in the latest subchapter they need; shared Insight stems repeated in each box.
- Build: `tools/revision/ch1/build.py` (questions in `qdata.py`, figures pre-rendered TikZ SVGs in `figs.json`). Template for later chapters.
- Notes: GM2 Q6a keeps Insight's answer (3); GM2 Q2a Insight median 35 vs stem plot 36 (noted in solutions).
- Rocco to delete on G: `Ch1 revision booklet PRINT.pdf`, `... solutions PRINT.pdf`, `... LaTeX.zip`, `... build files.zip` (superseded).
- CFAT 1.1.1–1.1.3 cards now use Student copy / Solutions (solutions not made yet). CFAT 1.1.3 added to the Ch 1 check card.

## Open / later
- **Lessons 1–3 (S1–S3)** still use the old layout → rebuild on the templates (also fixes 'Homework' → 'Coursework', S2 Do Now count, S3 extra exit, S2 '?%' → 71%).
- Ch 1 test (L6) not made.
- Embedded YouTube cards (CAS slide) show "Error 153" when the file is opened from disk; check they play on GitHub Pages.
- Heptathlon exit (slide 26): fits, but the 15-row table text is small.
- Command-word tagging of the item index; download VCAA glossary definitions.
- Planner cards vs slides for S1/S2 (APK differences); 2027 term dates → `planner/years/2027.json`; point Rocco's dashboard at the planner files (needs his go-ahead).

## Working notes
- Screenshots: `python3 tools/deck/s4/shoot.py "<slide list>" "<slide:steps,…>"` (writes to /home/claude/w/shots; adjust paths in a new session). Needs playwright + /usr/bin/google-chrome.
- Sources staged from G: `02 Sources\Textbooks\...` (Cambridge U3&4 1G = pdf pp. 73–88; Edrolo U3&4 1E = pdf pp. 54–68, 1F WE5 = p. 78; Edrolo U1&2 1F Q16 = p. 63).
- 2024 E1/E2 and 2025 NHT papers are scans (OCR). 2023 NHT is old design.
