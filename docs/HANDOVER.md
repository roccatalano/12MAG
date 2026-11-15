# 12MAG handover — 15 Nov 2026

Read `CLAUDE.md` first (rules, item index, **slide template rules**), then this file.
Repo: `roccatalano/12MAG` (GitHub Pages: roccatalano.github.io/12mag/ → `planner/`). Rocco's dashboard repo `roccatalano/teaching-dashboard-2027` is read-only unless he asks.
Push: `git -c push.negotiate=true push origin HEAD`. G: drive is reached through the desktop-app bridge (stage files to read; commit files to write; can't move/rename/delete).

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
- 1H–1I worksheet not made. Ch 1 coursework check + test (L6).
- Bound reference entry for 1G not made.
- Embedded YouTube cards (CAS slide) show "Error 153" when the file is opened from disk; check they play on GitHub Pages.
- Heptathlon exit (slide 26): fits, but the 15-row table text is small.
- Command-word tagging of the item index; download VCAA glossary definitions.
- Planner cards vs slides for S1/S2 (APK differences); 2027 term dates → `planner/years/2027.json`; point Rocco's dashboard at the planner files (needs his go-ahead).

## Working notes
- Screenshots: `python3 tools/deck/s4/shoot.py "<slide list>" "<slide:steps,…>"` (writes to /home/claude/w/shots; adjust paths in a new session). Needs playwright + /usr/bin/google-chrome.
- Sources staged from G: `02 Sources\Textbooks\...` (Cambridge U3&4 1G = pdf pp. 73–88; Edrolo U3&4 1E = pdf pp. 54–68, 1F WE5 = p. 78; Edrolo U1&2 1F Q16 = p. 63).
- 2024 E1/E2 and 2025 NHT papers are scans (OCR). 2023 NHT is old design.
