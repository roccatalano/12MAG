# 12MAG handover — 14 Nov 2026 (late night)

Read `CLAUDE.md` first (rules, item index, **slide template rules**), then this file.
Repo: `roccatalano/12MAG` (GitHub Pages: roccatalano.github.io/12mag/ → `planner/`). Rocco's dashboard repo `roccatalano/teaching-dashboard-2027` is read-only unless he asks.
Push: `git -c push.negotiate=true push origin HEAD`. G: drive is reached through the desktop-app bridge (stage files to read; commit files to write; can't move/rename/delete).

## NEXT JOB: guided lesson worksheet for Lesson 4 (1G)
Rocco wants to make the **guided worksheet** from the finished 1G slides (`lessons/S4-slides.html`, built by `tools/deck/s4/build.py`).
What CLAUDE.md already says about it:
- Every lesson gets guided slides, a **guided worksheet**, and a bound reference entry (rule 2).
- Planner card wording: "Student companion to the slides, in the same order, with space to answer. **Max 2 double-sided pages.**"
- Rule 12: check every page visually; finished files go in `lessons/` and flat into `01 Lesson materials` on G: (name: `1G worksheet.html`, like `1A-1B worksheet.html`).
Starting points:
- An older worksheet exists: `lessons/S1-worksheet.html/.pdf` (1A–1B, pre-template style; Rocco hasn't reviewed it against the new slide design). Look at it, but expect Rocco to want it to mirror the NEW slide templates.
- **Reuse the slide content, don't retype it:** `tools/deck/s4/build.py` holds every question (verbatim), its figure config (boxplot/dot plot/stem plot data) and the solution steps. Best approach: build the worksheet from the same data (e.g. a `tools/deck/s4/worksheet.py` or a worksheet template next to `tools/deck/tpl/`), so slides and worksheet never drift.
- Likely mirror of the slide layout on paper: question on the left (verbatim, command word highlighted), working space on the right, success-criteria tick boxes, key definitions/formulas box. **Ask Rocco** about: which slides go on the worksheet (all Do Now/APK/WE/You try/exits? WE as worked/filled-in vs blank?), answer space style (lines, grid, blank boxplot axes), and print format (A4, black and white?).
- PDFs: Rocco said (14 Nov) **don't make PDFs of the slides yet** (static versions later). Ask whether the worksheet should have a PDF (it is for printing; S1-worksheet had one, made with paged.js: `lessons/paged.polyfill.min.js`, `a4view.js`).
- Rocco's account skills may help: `11mag-chapter-workbook` (A4 photocopiable HTML workbook) and `maths-model-notes`. Check them before designing from scratch.

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

## Open / later
- **Lessons 1–3 (S1–S3)** still use the old layout → rebuild on the templates (also fixes 'Homework' → 'Coursework', S2 Do Now count, S3 extra exit, S2 '?%' → 71%).
- **1H–1I (L5)** slides not made. Ch 1 coursework check + test (L6).
- Bound reference entry for 1G not made.
- Embedded YouTube cards (CAS slide) show "Error 153" when the file is opened from disk; check they play on GitHub Pages.
- Heptathlon exit (slide 26): fits, but the 15-row table text is small.
- Command-word tagging of the item index; download VCAA glossary definitions.
- Planner cards vs slides for S1/S2 (APK differences); 2027 term dates → `planner/years/2027.json`; point Rocco's dashboard at the planner files (needs his go-ahead).

## Working notes
- Screenshots: `python3 tools/deck/s4/shoot.py "<slide list>" "<slide:steps,…>"` (writes to /home/claude/w/shots; adjust paths in a new session). Needs playwright + /usr/bin/google-chrome.
- Sources staged from G: `02 Sources\Textbooks\...` (Cambridge U3&4 1G = pdf pp. 73–88; Edrolo U3&4 1E = pdf pp. 54–68, 1F WE5 = p. 78; Edrolo U1&2 1F Q16 = p. 63).
- 2024 E1/E2 and 2025 NHT papers are scans (OCR). 2023 NHT is old design.
