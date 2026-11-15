# 12MAG course planner — instructions for Claude

Owner: Rocco (teacher). He is new to Claude Code and git: explain in plain words, ask before anything destructive, and never use jargon without a one-line explanation.

**New chat? Read `docs/HANDOVER.md` next** (latest state, decisions, open items).

## What this repo is
The standalone **Year 12 General Maths (12MAG) course planner** (GitHub Pages: roccatalano.github.io/12mag/). Moved here 14 Nov 2026 from `roccatalano/teaching-dashboard-2027` (which still shows 12MAG on Rocco's personal dashboard for now — don't change that repo unless asked).
- `PLANNER.md` — the planner spec. **Built 14 Nov:** `planner/index.html` (Course plan tab + one Year plan tab per year; same card/nested-section design as Rocco's dashboard, whose CSS and section code it copies; label the four groups AoS 1–4, never 'Unit'), data in `planner/unit-plan.json` (the single source of truth for content: edit it directly) and `planner/years/<year>.json` (+ `years/index.json` listing the years). 2027 is a blank tab until Rocco sends the term-dates file. The site root redirects to `planner/`.
- `lessons/` — finished 12MAG materials (html + pdf), same files as `teaching-dashboard-2027/lessons/gm12/`.
- `tools/` — current plan builder (`build_plan.py`, writes the dashboard JSON in the OTHER repo; to be replaced by planner data files), source indexes (`y12_edrolo_exam_practice.csv`, `y11_edrolo_exam_practice.csv`, `y11_cambridge_skills_checklist.csv`, `cambridge_go_videos.csv`, `sd.json`, `vcaa_donow_aos1.json`), and slide-deck build code (`deck/s3/` = current template).
- `docs/CLEANUP.md` — history of the 14 Nov G: drive reorganisation.
- Long-term idea (Rocco): a school-wide system where each teacher's dashboard picks the subjects they teach. Keep subject data self-contained and portable.

## Item index — next steps (agreed 14 Nov: "index now, fill on first use")
1. ~~Add page numbers + % correct to the Edrolo exam-practice indexes.~~ **Done 14 Nov.** Columns: `pdf_page`, `printed_page` (= pdf − 7), `answer` (Exam 1: correct letter; Exam 2: average mark/max), `pct_correct` (Exam 1: % choosing the correct option; Exam 2: average mark as % of max), `note`. 6 items from pre-2016 papers (2007, 2009, 2012, 2014, 2015 Exam 1) are flagged "no assessor report info available" (Rocco, 14 Nov: leave blank).
2. ~~Rebuild the current-design VCAA (2023–26) question index.~~ **Done 14 Nov:** `tools/vcaa_current_index.csv` = the Do Now pool. 652 items (280 Exam 1 Qs + 372 Exam 2 parts) from 7 sittings: 2023, 2024 NHT, 2024, 2025 NHT, 2025, 2026 NHT, 2026 (2023 NHT is still the old Core+Modules design, so it is excluded). Each item is hand-tagged to one Cambridge U3&4 subchapter (`also` = secondary tags), with marks, paper page, answer and % correct (Nov reports only: NHT reports give no % and the 2026 report isn't out yet). `stem_end` is only a locator (OCR text for the scanned 2024 and 2025 NHT papers): extract verbatim from the PDF on first use (step 4). Z-scores are tagged 1H, as in Cambridge. `vcaa_donow_aos1.json` (the per-lesson picks) is kept, but its tags differ from this index on 35 items; this index wins.
3. ~~Index Edrolo U3&4 exercise questions (non-VCAA).~~ **Done 14 Nov:** `tools/y12_edrolo_exercise_questions.csv` = the CFAT pool. 696 questions (551 skill, 137 'Joining it all together', 8 non-VCAA 'Questions from multiple lessons'); Exam practice and every VCAA-cited question are excluded. Columns: Edrolo lesson + Q, section, skill heading, `cambridge_sub` (mapped from the Edrolo lesson, refined by skill heading; blank for multi-lesson questions), pdf/printed page, MC or short answer, number of parts, `used_in` (burnt by CFAT 1.1.1–1.1.3), stem start. Map lives in `tools/edrolo_exercise_index.py`. NB: 13 of the questions CFATs 1.1.1–1.1.3 used are Exam-practice VCAA reprints (against rule 8). Rocco, 14 Nov: leave those CFATs as they are for now; don't fix them unless he asks.
4. Extract an item fully (verbatim text, figure data, answer) the first time a lesson uses it; save to the item bank so it is never re-extracted.

## 12MAG (VCE General Maths 3&4, 2027) — current rules (Rocco, 14 Nov 2026)
These replace all older 12MAG rules (old Planning\CLAUDE.md, project docs).
1. **Never write questions.** Copy verbatim and cite the source. Adapt only when unavoidable and label it "adapted".
2. **Every lesson gets:** guided slides, guided worksheet, bound reference entry. (Lesson handouts and log-book labels are discontinued.)
3. **Lesson shape:** CFAT (if any) → Do Now → APK → Learn + Example/You try pairs → CAS → exit tasks → check-in → coursework.
4. **Do Now = retrieval** ("last lesson, last week, last term"): always 2 × Exam 1 + 2 × Exam 2 from CURRENT-design VCAA (2023–26). Covers the current AoS and earlier AoS; the earlier-AoS share grows through the year.
5. **APK = priming, not retrieval:** prerequisite content students should already know. Sources: Cambridge U1&2 skills checklist + the VCAA exam questions at the back of Edrolo U1&2 subchapters. If an APK item is also a candidate exit question, use it as the APK.
6. **Learn notes:** own words, condensed, cite Cambridge. **Examples** = Cambridge Examples. **You try** = mapped Edrolo worked example only (no match → no You try).
7. **Exit tasks:** the VCAA reprint exam questions at the back of Edrolo U3&4 subchapters (past-design VCAA).
8. **CFATs:** Edrolo U3&4 exercise questions ONLY, never the VCAA reprints. **CFAT follow-ups:** Jacaranda textbook exercises.
9. **Chapter tests:** Mathspace topic assessments. **SACs:** custom built. **Revision booklets (per chapter):** Insight GM1/GM2. **Coursework** (Rocco, 14 Nov: call it coursework, not homework, so students know it counts towards their S): students' own Cambridge textbook exercises. Existing decks S1–S3 still say 'Homework'; fix later.
10. **Burnt items:** one use per question across everything (Do Now, APK, exit, CFAT, booklet, test). Match VCAA reprints by their ORIGINAL VCAA source (e.g. an Edrolo exit = VCAA 2019 E1 Q3). Check `tools/ledger.csv` (rows with burnt = yes). After making or using items, add them: re-run `tools/build_ledger.py "<HANDOFF.md path>"` (it re-reads lessons/*.html) or add rows to `tools/ledger_manual.csv`. Example/You try/homework rows are logged but not burnt.
11. **% correct** only from examiner reports (past-design reports sit with the past papers); if a report is missing, say which one and ask Rocco.
12. **Check every slide visually** (all steps shown + mid-reveal) before handing over. Finished resources go in `lessons/` here and flat into `01 Lesson materials` on G:.

## Slide templates (Rocco, 14 Nov) — every deck is built from `tools/deck/tpl/tpl.py`
Build a lesson with a `tools/deck/<S#>/build.py` that only fills content into the templates (see `tools/deck/s4/build.py`); the engine is `tools/deck/engine.html` (re-make with `make_engine.py`). Rules:
- **Order:** title (formal topic) → Today's lesson (3 white cards: learning intentions · success criteria with tick boxes · lesson sequence) → Key definitions (with small pictures) and Key formulas (fences carry "x < LF → outlier") → Do Now ×4 → APK → Learn / WE / You try / CAS → exits → check-in (one tick-box card) → coursework (one card per subchapter) → **Videos that might help** (always last; blank cards to fill).
- **Question slides:** question on the left (verbatim; command word highlighted yellow), blue line, working on the right as numbered cards revealed one per click, ending in a **green answer card** (a concluding statement). Header tiles top right: command word tile ("FIND · …"), VCAA % tile, video button.
- **Model formulas:** formula → substitute (values flip in) → result, using the Key formulas names. Data sets: use CAS one-variable stats, don't order by hand. Outliers: IQR → fences → "56 > 55 = UF → outlier" statements; draw the fences on the boxplot.
- **Annotate the question** at the step that needs it (e.g. the 20.5th line on a dot plot, highlighted cells, marked leaves). Axes appear only when their step comes.
- **Multi-part questions (a, b, c…):** parts listed down the page on the left (`plist`); ONE big green answer card that reveals one part per click (`parts=`). Never run parts together in a line.
- If the figure is the answer (a boxplot to construct), it is built inside the green answer card.
- **MC:** answer card → next click "What's the distractor?" → next click the option + why. No distractor card unless there is a real one.
- **Exam question pills name the VCAA source** (e.g. 'APK · VCAA 2021 Exam 1 Q1', 'Exit task 1 of 3 · VCAA 2019 Exam 2 Q1a'), never Edrolo; the Edrolo/textbook reference stays in the source line at the bottom. Highlight EVERY occurrence of the command word (not inside quotations).
- **Answer templates (Rocco, 15 Nov):** when the answer is a table, chart or report, show it first as a dark template card (`('TMPL', html)` in qslide steps; blanks `B(cls,val)` filled by `data-fill`, bars/segments by `data-grow="#id|i"`), fill it step by step while annotating the question (`data-hi="#id|rows|hc/hv/hy/hb/hg"`, only the thing being counted), then one more click turns it green. Several answer cards per slide are fine: step, step, answer (`('ANS', html)`), step, step, answer. Steps carry `data-pk` to fade the parts of the question not being worked on (`data-pks` on whole question blocks); the last click restores everything in full (static PDF state).
- **Questions take normal spacing** (`G(text, figure, question)`), not the stretched figure zone, unless filling the card makes sense (multi-part lists: parts fill the card).
- **Learn slides for displays follow the data → frequency table → graph flow** (tally chips into the table, then grow the bars; bars → stacked → % for segmented bar charts; report templates filled part by part with the three highlight colours).
- **Coursework slide mirrors the planner's coursework card** (Cambridge exercises with skills + Q numbers, and the chapter revision booklet sections).
- **Charts are built, not shown:** axes and labels appear on their own step (chart `ax=True` + `data-ax="#id"`), then bars/segments grow one per step (`data-grow`, several with `;`).
- **Flowcharts/trees reveal top-down, one branch at a time** (parent → first branch → its children → next branch → its children); use `data-s` groups and trailing empty frags to fix the order.
- **Coursework items are tick boxes** (same look as the success criteria).
- **Learn:** rule card + the related key formula/definition cards on top, picture, one tip. **CAS slides are static** (Rocco, 15 Nov): TI and ClassPad step cards, small embedded YouTube cards stretched to the width of the step cards, then the read-off card, all shown at once.

- **Slide PDF** (Rocco, 15 Nov): `python3 tools/deck/pdf.py lessons/S#-slides.html lessons/S#-slides.pdf`. Question slides (Do Now, APK, WE, You try, exit) → 2 pages (question only, then the final frame); everything else → the final frame only. Copy to G: as `<subs> slides.pdf`.

## Guided worksheets (Rocco, 15 Nov)
- Build with `tools/deck/<s#>/worksheet.py` on **`tools/deck/ws2.py`** (CFAT / revision-booklet style; model: `tools/deck/s1/worksheet.py`) → student + solutions copies (html + PDF). G: names `<subs> worksheet(.pdf)`, `<subs> worksheet solutions(.pdf)`. (`wslib.py` = the old ruled-line style used by S2–S5; move them to ws2.)
- **Pages: never cram** (Rocco, 15 Nov). Normal 10 pt text and margins, decent chart grids, boxes at their natural height (don't stretch them to fill a page: Rocco found that too much). Aim for about 2 pages per subchapter but go over rather than squeeze. Use the **fewest pages that fit without cramming** (some staff print single-sided; S1 = 5 pages). Each part of a multi-part You try gets its own answer space. Student and solutions copies must have the same page count. (`PAGE` groups in ws2.py force page breaks + stretch: not used now.)
- **Questions only, in slide order:** learning intentions → APK → Example/You try pairs → exits ('guess the %') → skills checklist + coursework. **No CAS steps and no Key ideas / learning notes**: those live in the bound reference (Rocco walks around and checks CAS set-ups).
- **Look:** running header 'VCE General Maths 3&4' (left) and the AoS (right, e.g. 'AoS 1 · Data analysis'); 'Page n of N' at the bottom. Title box = subchapters + title only. Every question in its own box ('Question n' for APK, 'Exit task n'); exam boxes name the VCAA source in the header ('Question 2 · VCAA 2021 Exam 1 Q1'). **Example n and You try n share ONE box split down the middle** (`exyt`). One-word answers get a writing line (`'L'`); longer answers get blank space. **Examples keep the scaffold** (blank table, chart grid, boxed report template); **You trys get none: blank space only** (students do the whole question). Solutions = the same layout with answers in red (You try tables/charts drawn in red in the space; MC: red ✓ + one-line why).
- **References:** none on Examples, You trys or the Cambridge APK. Exam questions show only the VCAA source in the box header, never Edrolo. Keep the real sources in the build script's docstring.

## Bound reference entries (Rocco, 15 Nov)
- **One card per subchapter**, in colour, with dashed cut lines so it can be trimmed and stuck in the top left of a double page in the student's A4 bound reference (the rest of the double page is for their own notes). The lesson card's "Bound reference entry" links that lesson's subchapter cards (single or combined for printing).
- **Half A4 by default; full A4 if it doesn't fit.** One fixed text size for every card (never scale fonts to fill). Fill spare space with useful content, e.g. a VCAA question.
- Content: Study Design dot points covered, definitions, key ideas, formulas, diagrams, Cambridge examples (cited), condensed TI/ClassPad CAS steps where relevant.
- **Reuse the lesson's own exam questions** (Do Now, APK, exits) on the card: this does NOT burn them again. Prefer the original VCAA wording when the lesson used an adapted version. The box title names the VCAA source (e.g. 'VCAA 2019 Exam 2 Q1a' + % tile): no extra source line, no Edrolo reference.
- Build: `tools/bref/build.py` (content in `tools/bref/cards.py`, styles `bref.css`) → `lessons/<sub> bound reference.html/.pdf` + `<lesson subs> bound reference.html/.pdf` (PDFs printed automatically; each html has an on-screen 'Download PDF' button).
- **Planner (Rocco, 15 Nov):** the Bound reference entry always nests, even for a one-subchapter lesson: one copy per subchapter (Open + PDF), plus a 'print both/all' copy when there are several.

## Self-study videos and CAS skills (Rocco, 15 Nov)
- **Self-study videos:** `planner/videos.json`, one or more per Cambridge subchapter. Free YouTube, VCE-focused; main source = MaffsGuru's free *General Maths Units 3 and 4* course (its sections use the same headings as Cambridge). `status: approved` = checked (Rocco, 15 Nov: all Ch 1 videos checked). The planner shows them per lesson ("Self-study videos"); slides' "Videos that might help" and worksheets should read from here.
- **CAS guide** (Rocco, 15 Nov: call it the CAS guide, not CAS skills): on the planner, CAS guide → one nested card per skill to master → nested ClassPad and TI-Nspire cards, each with the step-by-step and its video(s). `planner/cas-skills.json` is the ONE master list: each skill once (`id`, condensed TI-Nspire + ClassPad steps, tip, videos). Lesson cards only list skill ids (`card.cas: ["histogram", …]`). Slides, worksheets and bound reference cards copy their CAS steps from here; fix a step here, not in a deck. Empty steps = write on first use, checked against the official CAS help videos (`02 Sources\CAS guides`).

## Source files (G: drive)
Root: `G:\Shared drives\1. EKC CURRICULUM\1. KLA Folders\MATHEMATICS\VCE Maths\General Maths U3 & 4\12MAG Course Planner\` (the old `12MAG 2027` folder is archived — don't use it).
- `00 Admin\` Study Design, curriculum grid, Cambridge sample planner.
- `01 Lesson materials\` ALL made materials, flat, named `<subchapters> <type>.<ext>` (e.g. `1C-1E slides.pdf`, `CFAT 1.1.1 (1A-1E).pdf`, `Ch1 test.pdf`). No lesson numbers or weeks in names: lessons are merged/split on the planner only.
- `02 Sources\` VCAA current 2023-26 (`2025 E1.pdf`, `2025 NHT E2 report.docx`…), VCAA past 2016-2022 (originals of the Edrolo reprints, for % correct), Textbooks (Cambridge U3&4 + U1&2, Edrolo U3&4 + U1&2, Jacaranda, Mathspace), Insight, Bound references, CAS guides, RESERVED (commercial trials, Cambridge tests, Nelson — not used in class).
- `03 Item bank\` items extracted on first use. `04 Archive\` old material. `Planning\`.
Claude can create/overwrite files on G: but cannot move, rename or delete them.

## Planner decisions (Rocco, 14 Nov)
- Keep the Cambridge suggested teaching sequence as the lesson order. No drag-and-drop or auto-built slides: too complicated.
- The planner must look and work like the teacher dashboard's nested-card system.
- **Keep card text minimal** (Rocco, 15 Nov): a material's description is one line max; side-by-side copies (e.g. Student copy / Solutions) get a label and buttons only, no subtext. A material with nested copies shows no Open/PDF buttons next to its title (they're in the copies).
