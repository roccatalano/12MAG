# 12MAG handover — 14 Nov 2026 (evening)

Read `CLAUDE.md` first (rules + item index), then this file. Repo: `roccatalano/12MAG` (GitHub Pages: roccatalano.github.io/12mag/ → redirects to `planner/`).
Rocco's dashboard repo `roccatalano/teaching-dashboard-2027` was used **read-only** (copied its CSS + section code). Don't change it unless asked.

## Done this session
1. **Item index steps 1–3** (details in CLAUDE.md):
   - `tools/y12_edrolo_exam_practice.csv`, `tools/y11_edrolo_exam_practice.csv`: + pdf/printed page, answer, % correct (examiner reports). 6 pre-2016 items flagged "no assessor report info available".
   - `tools/vcaa_current_index.csv`: Do Now pool, 652 current-design items (2023–26), hand-tagged to Cambridge subchapters.
   - `tools/y12_edrolo_exercise_questions.csv`: CFAT pool, 696 Edrolo U3&4 exercise questions, mapped to Cambridge subchapters (`tools/edrolo_exercise_index.py`).
2. **Burnt ledger** `tools/ledger.csv` (122 burnt rows), built by `tools/build_ledger.py "<path to 04 Archive\Planning\Topics\1. Data Analysis\HANDOFF.md>"`. Reads the HANDOFF burnt table + every `src` citation in `lessons/*.html`; role = the slide's class (dn/apk/we/yt/ex/cfat). VCAA reprints keyed by original paper. Manual rows: `tools/ledger_manual.csv` (create if needed).
3. **Course planner** `planner/index.html`:
   - Looks and works like the dashboard (same CSS, nested sections). Tabs: **Course plan** + **Year plan <year>**. Groups labelled **AoS 1–4** (never "Unit").
   - Data: `planner/unit-plan.json` = the content master (AoS → chapters → lessons; each lesson = Cambridge subchapters + card). 68 lessons. Ch 1–5, 7–8 cards came from the dashboard data (`tools/make_unit_plan.py`, one-off); Unit 4 (Ch 10–11, 13–14) = outlines from the Cambridge sample planner.
   - Lesson card sections: materials, CFAT, LOs, SC, Study Design, vocab, CAS, Do Now, APK, worked examples & You trys, exit tasks, **Coursework** (`tools/add_homework.py`: exact breakdown from the deck's last slide, else "Cambridge · Exercise XY, all questions"). Long coursework rows shrink to fit one line.
   - **Lesson shape** panel = live outline of the lesson's slide deck (read from `lessons/<S#>-slides.html`); "Slides not made yet" if no deck.
   - Year tabs: flow lessons into dated slots (teaching days, blocked dates, anchors with `"unit"`, buffers, overflow warning). `planner/years/2027.json` is **blank** until Rocco sends 2027 term dates; `years/index.json` lists years.

## Rocco's decisions (14 Nov)
- Keep the **Cambridge suggested sequence**. No drag-and-drop, no auto-built slides.
- Planner must match the dashboard's nested-card look.
- Say **Coursework**, not homework (students need it for their S).
- Leave CFATs 1.1.1–1.1.3 as they are (13 of their items are Edrolo VCAA reprints, against rule 8).
- Leave the made slides (S1–S3) for now; fix later.
- **Focus now: Chapter 1.**

## Open / next
- **Slides S1–S3 (later):** rename "Homework" → "Coursework" (pill, heading, title-slide flow; re-make PDFs; check every slide, rule 12). S2 Do Now has 3 items (needs 2 × E1 + 2 × E2). S3 has an extra exit from a current-design paper (VCAA 2026 NHT E2 Q1b, Q1d; rule 7 says Edrolo reprints only). S2 exit 3 shows "?%" — report value is 71% (VCAA 2019 E1 Q3).
- **Planner cards vs slides (Ch 1):** S1 card lists APK 2B #5 not on the slides; S2 card APK differs from the slides (slides: 2C #6, 2D #7, 2D #9, 9D #6–7; card also has Edrolo U1&2 1C Q15, Q17). Decide whether cards should be synced to the slides.
- **1G (L4) slides made 14 Nov (evening):** `lessons/S4-slides.html/.pdf` (27 slides; also `1G slides.*` on G:). Build: `tools/deck/s4/build.py` (template = S3 + `extra.js` boxplot drawer: `data-chart="box"`, stepped parts via `data-bx="#id|box,med"`, `=` prefix shows one % band at a time), `shoot.py` (screenshots), `pdf.py` (PDF: question page + answer page for Do Now/APK/exit). Do Now: VCAA 2023 E1 Q1, Q6; 2025 E2 Q1a, Q1b. APK: U1&2 2H #14–15, Edrolo U1&2 1F Q16. Exits: Edrolo 1E Q19, Q20. You trys: Edrolo 1E WE4, WE5 (CAS), WE6, 1F WE5. Card + ledger updated. Worksheet + bound reference for 1G NOT made yet (Rocco: slides only for now). Note: Cambridge Ex 24's boxplot draws its top outlier at ~81 but the question says 86; drawn as in the book.
- Chapter 1 lessons still without decks: **1H–1I (L5)**, Ch 1 coursework check + test (L6; `lessons/Ch1-coursework-check.html` exists).
- ~~Insight un-burn~~ Done 14 Nov: Rocco — nothing from Insight is burnt. The 10 rows are removed from `tools/ledger.csv` and `build_ledger.py` skips Insight.
- 2027 term dates → fill `planner/years/2027.json` (format in its `_help`).
- Last PLANNER.md step: point Rocco's personal dashboard at the planner files (needs his go-ahead; other repo).
- Item index step 4 (extract items fully on first use into `03 Item bank\`) happens lesson by lesson.

## Working notes
- G: drive is reached through the desktop app bridge (stage files to read; can't move/rename/delete there). Sources: `...\12MAG Course Planner\02 Sources\`. HANDOFF + old planning: `04 Archive\Planning\`.
- 2024 E1/E2 and 2025 NHT E1/E2 PDFs are scans (OCR needed). 2023 NHT is old design (in `VCAA past\2022`).
- Push: `git -c push.negotiate=true push origin HEAD` (remote is `https://github.com/roccatalano/12MAG.git`).
- Check planner changes visually (headless Chrome + playwright: serve the repo with `python3 -m http.server`, open `/planner/`).
