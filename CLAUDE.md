# 12MAG course planner — instructions for Claude

Owner: Rocco (teacher). He is new to Claude Code and git: explain in plain words, ask before anything destructive, and never use jargon without a one-line explanation.

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
3. **Lesson shape:** CFAT (if any) → Do Now → APK → Learn + Example/You try pairs → CAS → exit tasks → check-in → homework.
4. **Do Now = retrieval** ("last lesson, last week, last term"): always 2 × Exam 1 + 2 × Exam 2 from CURRENT-design VCAA (2023–26). Covers the current AoS and earlier AoS; the earlier-AoS share grows through the year.
5. **APK = priming, not retrieval:** prerequisite content students should already know. Sources: Cambridge U1&2 skills checklist + the VCAA exam questions at the back of Edrolo U1&2 subchapters. If an APK item is also a candidate exit question, use it as the APK.
6. **Learn notes:** own words, condensed, cite Cambridge. **Examples** = Cambridge Examples. **You try** = mapped Edrolo worked example only (no match → no You try).
7. **Exit tasks:** the VCAA reprint exam questions at the back of Edrolo U3&4 subchapters (past-design VCAA).
8. **CFATs:** Edrolo U3&4 exercise questions ONLY, never the VCAA reprints. **CFAT follow-ups:** Jacaranda textbook exercises.
9. **Chapter tests:** Mathspace topic assessments. **SACs:** custom built. **Revision booklets (per chapter):** Insight GM1/GM2. **Coursework** (Rocco, 14 Nov: call it coursework, not homework, so students know it counts towards their S): students' own Cambridge textbook exercises. Existing decks S1–S3 still say 'Homework'; fix later.
10. **Burnt items:** one use per question across everything (Do Now, APK, exit, CFAT, booklet, test). Match VCAA reprints by their ORIGINAL VCAA source (e.g. an Edrolo exit = VCAA 2019 E1 Q3). Check `tools/ledger.csv` (rows with burnt = yes). After making or using items, add them: re-run `tools/build_ledger.py "<HANDOFF.md path>"` (it re-reads lessons/*.html) or add rows to `tools/ledger_manual.csv`. Example/You try/homework rows are logged but not burnt.
11. **% correct** only from examiner reports (past-design reports sit with the past papers); if a report is missing, say which one and ask Rocco.
12. **Check every slide visually** (all steps shown + mid-reveal) before handing over. Finished resources go in `lessons/` here and flat into `01 Lesson materials` on G:.

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
