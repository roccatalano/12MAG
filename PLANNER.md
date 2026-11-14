# 12MAG unit planner — spec (Rocco, 14 Nov 2026)

A standalone "2027 Year 12 General Maths" planner, separate from Physics and from Rocco's personal dashboard.
Two tabs: **Unit plan** (content, no dates, reusable every year) and **Year plan** (one tab per year, dates).

## Tab 1 — Unit plan (no dates)
- 4 AoS cards → Cambridge chapters inside each → lessons inside each chapter.
  - AoS 1 Data analysis: Ch 1–5 (Ch 6 = revision, practice only)
  - AoS 2 Recursion and financial modelling: Ch 7–8 (Ch 9 = revision)
  - AoS 3 Matrices: Ch 10–11 (Ch 12 = revision)
  - AoS 4 Networks and decision mathematics: Ch 13–14 (Ch 15 = revision)
- **A chapter = its proposed teaching lessons + exactly one "Chapter n coursework check + test" lesson.** Nothing else (no SAC or revision lessons here).
- **A lesson = a list of Cambridge subchapters** (e.g. `1C, 1D, 1E`, or half a subchapter: `5D (part 1)`) + its lesson card:
  learning intentions · success criteria · Cambridge Examples + Edrolo You trys · APK · Do Now · exits · CAS · CFAT (if any) · materials (files in `01 Lesson materials`, named by subchapter range).
- Planning happens one chapter at a time: split, merge or reorder lessons inside a chapter; other chapters are untouched.
- First draft: Ch 1–5 from the current dashboard lessons (S1–S5, L03–L22, chapter tests); Ch 7–8 and Unit 4 chapters as shells with the proposed lesson count from the Cambridge sample planner (`00 Admin\Study Design\Sample-planner-and-timeline.docx`), to be planned later.

## Tab 2 — Year plan (one per year: 2027, 2028, …)
- **Inputs (per year):** term start/end dates; teaching days (3 lessons/week, which weekdays); public holidays, pupil-free days, school events (blocked dates); optional pinned anchors (SAC dates, trial exams) — added later.
- **Flow:** unit-plan lessons are placed in order into the free lesson slots. Lessons are never pinned to days.
- **Buffers:** every slot left over (and any slot before a pinned anchor) shows as a buffer lesson — later filled with SAC, revision, catch-up.
- **Warnings:** shows how many buffers remain per term, and flags when content runs past an anchor or past the end of a unit.
- New year = add a new year tab with new dates; the unit plan re-flows unchanged.

## Data (plain files, portable to the school Google account later)
- `planner/unit-plan.json` — AoS → chapters → lessons (subchapters + card fields). The single source of truth for content.
- `planner/years/2027.json` — terms, teaching weekdays, blocked dates, anchors.
- `planner/index.html` — the planner page (both tabs), reads the JSON files. Staff-facing; no personal ticks.
- Rocco's dashboard (`index.html`) reads the same files and adds his personal layer (ticks, notes, "taught on" dates for re-flowing from where the class actually is).
- `tools/gm12/build_plan.py` is replaced by these files once the planner works; until then nothing on the dashboard changes.

## Build order
1. Write `unit-plan.json` from the current dashboard data (Ch 1–5) + shells (Ch 7–8, 10–11, 13–14).
2. Write `years/2027.json` from the 2027 term dates already in `build_plan.py` (T1 starts 25 Jan, students 28 Jan; T2 starts 12 Apr; Labour Day 8 Mar) — Rocco checks and adds Terms 3–4 and blocked dates.
3. Build `planner/index.html` (Unit plan tab + 2027 tab), check it visually, push.
4. Point the personal dashboard at the new files.
