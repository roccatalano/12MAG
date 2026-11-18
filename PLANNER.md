# 12MAG course planner — spec (updated 18 Nov 2026)

A standalone Year 12 General Maths (VCE General Maths 3&4) course planner, reused each year by adding a year file. Separate from Physics and from Rocco's personal dashboard.
Live site: https://roccatalano.github.io/12MAG/planner/ (capital MAG). "↻ Get latest" reloads past a cached copy.

## Tabs
### Course plan (no dates, the same every year)
- One vertical list grouped by AoS (label them AoS 1–4, never "Unit"):
  - AoS 1 Data analysis: Ch 1–5 (Ch 6 = revision, practice only)
  - AoS 2 Recursion and financial modelling: Ch 7–8 (Ch 9 = revision)
  - AoS 3 Matrices: Ch 10–11 (Ch 12 = revision)
  - AoS 4 Networks and decision mathematics: Ch 13–14 (Ch 15 = revision)
- Each AoS starts with a **Unit details** card: SAC details (`aos[].sac`), SAC materials, Unit resources (e.g. Ch 1 slides, Ch 1 workbook), CFATs nested by chapter, and the subchapters no CFAT covers.
- Chapter cards show progress badges (Slides, Worksheets, Bound ref, CFATs, Test, Booklet). Click a chapter to see its suggested lessons and its formative assessments (CFATs, chapter tests) underneath.
- A lesson card shows its resources nested (Slides · Worksheet Student/Solutions · Bound reference per subchapter) and a "Lesson details" button for the full card.
- A chapter = its teaching lessons + a "catch-up + coursework check" lesson. Some chapters share one: Ch 1 + 2 (on the Ch 2 card), Ch 3 + 4 (on the Ch 4 card). Chapter tests are formative and sit with the CFATs.
- Course = 65 lessons.

### <year> overview (e.g. 2027 overview)
- A week-by-week calendar: the Course plan lessons flow in order into the year's lesson slots. Lessons are never pinned to days.
- Lessons per week by number of student days (`lessonRule`): 5 days = 3, 3–4 days = 2, 1–2 days = 1. (Real timetables come later.)
- Anchors (fixed dates): `afterSchool` (takes no lesson), `inClass` (takes one), `window` (marks the end of an AoS's teaching time), `redemption`, `exam`, plus the "Semester 2 starts" anchor that holds AoS 3 back until then.
- Spare slots before a SAC become "SAC revision"; later ones "Exam revision". After-school SACs and redemptions share the week's card. A week with no lessons gets one wide card (e.g. "Unit 3 trial exam week").
- The header shows lessons and buffers per term and the teaching time (planned + spare) up to each SAC.

### <year> classes (e.g. 2027 classes)
- Teacher picker and day grid, 4 sessions a day (3 on Wed). Data `years/<year>-timetable.json`; `slots` empty until the 2027 timetables arrive.

## Data files (plain JSON, portable)
- `planner/unit-plan.json` — AoS → chapters → lessons (subchapters + card). **The single source of truth for content: edit it directly.**
- `planner/years/index.json` — list of years. `planner/years/<year>.json` — terms, `lessonRule`, blocked dates, anchors. `planner/years/<year>-timetable.json` — classes and sessions.
- `planner/cas-skills.json` (CAS guide master list), `planner/videos.json` (self-study videos), `planner/tests.json` (chapter test details), `planner/written-youtrys.json`.
- `planner/index.html` — the page; reads the files above. Staff-facing, no personal ticks.
- `tools/build_plan.py` is the old dashboard builder, kept for reference only (the planner files replaced it).

## Rules for changes
- Keep the Cambridge suggested teaching sequence as the lesson order. No drag-and-drop or auto-built slides.
- Plan one chapter at a time: split, merge or reorder lessons inside a chapter; other chapters are untouched.
- New year = add `years/<year>.json` (+ timetable file) and list it in `years/index.json`; the Course plan re-flows unchanged.
- Card text minimal: one-line descriptions; copies get a label and buttons only.

## On hold
- Pointing Rocco's personal dashboard (`roccatalano/teaching-dashboard-2027`) at these files: only when Rocco asks.
