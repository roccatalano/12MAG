# 12MAG cleanup plan (for Claude Code on Rocco's PC)

Rocco starts a session and says "do phase 1" (later "do phase 2"). Do one step at a time, show what you will do, and wait for "go" before each step that moves files.

ROOT = `G:\Shared drives\1. EKC CURRICULUM\1. KLA Folders\MATHEMATICS\VCE Maths\General Maths U3 & 4\12MAG 2027`

## Safety rules (always)
- Never permanently delete. Anything not wanted goes to `ROOT\_to_check\` with its old path kept as subfolders.
- Write every move to `ROOT\_cleanup_log.csv` (old path, new path, reason) so it can be undone.
- Before each step, do a DRY RUN: print the list of moves and wait for Rocco's "go".
- Google Drive: if a file is "online only", moving it is fine (no download needed). If a move errors, log it and continue.
- Windows paths must stay under 260 characters. Keep names short; no `~`.

## Phase 1 — G: drive folder cleanup

### Step 0 — tools check
Check `python --version` and `git --version`. If missing, tell Rocco exactly what to install (python.org installer, tick "Add to PATH"; git-scm.com defaults) and stop.

### Step 1 — inventory
Make `ROOT\_inventory.csv`: every file with path, size, modified date, and an MD5 hash (hash only files < 200 MB; skip the rest by name+size). Report: file count, total size, exact duplicates (same hash), and files whose names end in ` (n)`.

### Step 2 — create the new structure (empty folders)
```
00 Admin\                     Study Design, curriculum grid, sample planner, trial exam tracker
01 Lessons\Step-up\S1 1A-1B\  … S2 1C-1E\, S3 1F\, S4 1G\, S5 1H-1I\, Holiday\
01 Lessons\Term 1\            one folder per dashboard lesson, named "<id> <section>", e.g. "L03 2A-2B", "Ch1 test"
02 Assessments\CFATs\Chapter 1\ … ; Chapter tests\ ; SACs\
03 Sources\VCAA\Current design\2023 … 2026\
03 Sources\VCAA\Past design\2000 … 2022\
03 Sources\Commercial (RESERVED)\<year>\<publisher>\
03 Sources\Textbooks\Cambridge\ Edrolo\ Jacaranda\ Nelson (RESERVED)\ Mathspace\
03 Sources\Insight (RESERVED)\
03 Sources\Bound references\ ; 03 Sources\CAS guides\ ; 03 Sources\Videos\
04 Archive\
Planning\                     keep: CLAUDE.md, TODO.md, Topics\ (README, HANDOFF). Everything else → 04 Archive\Planning\
```
Get the Term 1 lesson list from `classes/general-maths-12.json` (lesson ids + sections) in this repo.

### Step 3 — VCAA current design (2023–2026): one clean copy each
Sources: `Past Exams\Current Study Design\`, `Past Exams\VCAA Exams\Current Study Design [2023-2026]\`, and the loose files at the top of `Past Exams\` and `Past Exams\Current Study Design\`.
- Rename to: `<year> [NHT ]E1.pdf`, `<year> [NHT ]E2.pdf`, `… E1 report.docx`, `… E1 guide.docx` (assessment guide), `… E1 markguide.pdf`.
- Commercial papers in `Current Study Design\<year>\<publisher>\` → `03 Sources\Commercial (RESERVED)\<year>\<publisher>\` (names unchanged).
- When two files are the same paper: keep one (prefer the exact-hash match; otherwise the newer/larger), others → `_to_check`.
- WARNING: some files called "report" are actually copies of the exam (e.g. 2017 NHT). Open page 1 text to check before naming. Same for "-w" vs plain exam PDFs (keep "-w" = with working space? check and ask Rocco if unsure).
- Pre-2023 VCAA/Further papers (incl. 2023 NHT Further Maths) → `03 Sources\VCAA\Past design\<year>\` (merge `Past Study Design\` and `VCAA Exams\Past Study Design [2018-2022]\`), same naming.

### Step 4 — textbooks and references
- `Textbook Resources\*` → `03 Sources\Textbooks\` (Cambridge subfolders kept). Copy (not move) Edrolo U1&2 from `G:\...\General Maths U1 & 2\Exams\2026\Semester 2 Unit 2\Planning\Resources\Textbooks\2023-edrolo-units-1-2.pdf` into `03 Sources\Textbooks\Edrolo\`.
- `Other Resources\Insight Revision Books` → `03 Sources\Insight (RESERVED)\`; `Other Resources\Bound References` → `03 Sources\Bound references\`; `CAS Videos\*.pdf` → `03 Sources\CAS guides\`.
- `Study Design\*` and `Past Exams\General Maths - Trial Exam Tracker.xlsx` → `00 Admin\`.

### Step 5 — lesson and assessment materials
- `1. Data Analysis (Chapters 1-6)\CFATs\` → `02 Assessments\CFATs\`.
- `Lesson Materials\Lesson n`, `1. Data Analysis…\Slides`, `Lesson Handouts`, `Do Now & Exit Tasks`, `Examples & You Trys`, `Homework Revision Booklets`, `Concept Maps`: sort into the matching `01 Lessons\…` folder by subchapter (1A–1B → S1, 1C–1E → S2, 1F → S3, 1G → S4, 1H–1I → S5). Chapter-wide items (whole-chapter homework booklet, concept map) → `01 Lessons\Step-up\_Chapter 1\`.
- Show Rocco the proposed sort as a table before moving.

### Step 6 — archive
`Claude outputs\`, `Past Exams\To Be Sorted\`, `Planning\Engine*`, `Planning\How-tos`, `Planning\Backups`, `Planning\Examples from 10MAA`, `Planning\A5 Summaries`, `Planning\Templates`, old drawio files, `Planning\QUEUE.md`, `READ ME FIRST.md`, `Skills to adapt.md`, interview prompt → `04 Archive\` (keep subfolder names).

### Step 7 — verify
- Every row of `_inventory.csv` is now either at a new path or in `_to_check` (match by hash). Report anything missing.
- List folders that are now empty (old structure). Tell Rocco he can delete them in Drive; do not delete them yourself.
- Update `Planning\CLAUDE.md` folder map and `Planning\Topics\1. Data Analysis\HANDOFF.md` paths to the new structure. Write `03 Sources\SOURCES.md`: a table of every VCAA paper (year, E1/E2, NHT, report? guide?).

## Hosting decision (Rocco, 14 Nov 2026)
- Keep this repo PUBLIC on GitHub Pages for now, with all 12MAG html/pdf materials embedded under `lessons/gm12/` exactly as before (push = live).
- When the planner is complete, the whole 12MAG planner moves to the school Google account and this repo's 12MAG part is discontinued. So: keep everything portable (plain html + json + pdf, relative links, no GitHub-only features).
- 12MAG must become an INDEPENDENT planner, separate from the Physics tab (see phase 2, step 5).

## Phase 2 — planning data out of build_plan.py (repo)
1. Move the hard-coded dicts in `tools/gm12/build_plan.py` (`W`, `LOS`, `DET`, `WEDO`, `CASV`, `APK`, `EXIT`, `QMAP`, `MAT_FILES`, …) into data files: `tools/gm12/data/lessons.yaml` (one entry per lesson id) + `tools/gm12/data/sources.csv` (registry of every source file in `03 Sources`) + `tools/gm12/ledger.csv` (one row per use of a question: item, source, lesson id, use type, date).
2. `build_plan.py` only reads those files, checks (a) every referenced source exists in `sources.csv`, (b) no item appears twice in `ledger.csv` except allowed reuse, then writes the JSON. Output must be identical to the current JSON (diff it).
3. Make the deck engine shared: `tools/gm12/deck/engine/` (shell, reveal engine, charts, explainers, screenshot→PDF) taken from `deck/s3/`; each lesson is a content file.
5. Standalone planner page `planner/12mag-2027.html`: a staff-facing "2027 Year 12 General Maths" unit planner that reads only `classes/general-maths-12.json` (no Physics, no personal ticks/notes). Same lesson cards and embedded materials as the dashboard. The personal dashboard (`index.html`) keeps the 12MAG tab by reading the same JSON, with ticks/notes stored per lesson id.
4. Optional: item cache `tools/gm12/items/<source>/<id>.md` (verbatim text, figure data, worked answer) filled the first time an item is used.
