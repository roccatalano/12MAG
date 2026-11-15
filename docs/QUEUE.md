# 12MAG build queue (read by the "12MAG queue runner" scheduled task)

Rocco starts ONE chapter at a time. The runner does the first `todo` task of the ACTIVE chapter, marks it, and starts the next run.
When the chapter has no `todo` tasks left, the runner turns itself off and waits for Rocco to set up the next chapter.

**ACTIVE: Chapter 2** (runner "12MAG Ch 2 runner")

**ACTIVE (fourth runner): Chapter 5** (runner "12MAG Ch 5 runner", added 15 Nov by Rocco; same rule: only its own section)

**ACTIVE (third runner): Chapter 4** (runner "12MAG Ch 4 runner", added 15 Nov by Rocco; runs alongside Ch 3, same rule: only its own section)

**ACTIVE (second runner): Chapter 3** (runner "12MAG Ch 3 runner", added 15 Nov by Rocco; runs alongside Ch 2: each runner only takes tasks from its own chapter section)

Status words: `todo` · `in progress <date time>` · `done <date> — what was made` · `needs Rocco — why` (skipped; ask him).
A task `in progress` for more than 3 hours is treated as crashed: set it back to `todo` and note it.
Everything made is **Draft** on the planner. Nothing is marked Ready by the runner.

**Timing log (Rocco, 15 Nov):** every run adds one row to the Run log at the bottom when it finishes (or stops early): task, start and finish time (Sydney), minutes taken, result, and anything that slowed it (e.g. new chart type built, usage limit hit, G: unreachable). If the session offers a way to see usage (e.g. the explain-usage skill), add the tokens used too; otherwise leave that cell blank.

## Chapter 2: Investigating associations between two variables (lessons gm12-u3-l03 … l08, check gm12-u3-ch2-test)
1. `done 2026-11-15 — l03–l08 cards prefilled: Do Now ×4 each (burnt ones replaced), You trys mapped, coursework Q ranges, CAS steps (scatterplot, r, r²), Ch2 videos (draft); 46 items reserved in the ledger` **Prefill the lesson cards** (l03–l08) in `planner/unit-plan.json` from the indexes, following the rules in CLAUDE.md: Do Now ×4 per lesson (current-design VCAA from `tools/vcaa_current_index.csv`, not burnt), APK (Cambridge U1&2 skills checklist + Edrolo U1&2 exam questions), Examples (Cambridge) with mapped Edrolo You trys, exits (Edrolo U3&4 exam practice), CAS skill ids (add new skills to `planner/cas-skills.json`, steps checked against `02 Sources\CAS guides`), coursework (Cambridge exercises), self-study videos (`planner/videos.json`, MaffsGuru first; status `draft` until Rocco checks). Reserve every chosen exam item in the ledger (`tools/ledger_manual.csv`, role as planned) so later tasks don't reuse it.
2. `done 2026-11-15 — CFAT 1.2.1 (2A-2B, /17) + 1.2.2 (2C-2D, /16), HTML + PDF like CFAT 1.1.x (Word version replaced, Rocco 15 Nov), student + solutions, Edrolo exercise Qs only; old 1.2.1 ledger rows freed` **CFATs for Chapter 2** + solutions — Rocco 15 Nov: RECREATE CFAT 1.2.1/1.2.2 from scratch under rule 8 (Edrolo U3&4 exercise questions only: `tools/y12_edrolo_exercise_questions.csv`; HTML + PDF in the CFAT 1.1.x layout (Rocco 15 Nov: NOT Word; model `tools/cfat/ch2/build_html.py`)). Add them to the planner.
2b. `done 2026-11-15 — CFAT 1.2.3 (2E-2H, /15) HTML + PDF + solutions; sits on the l09 (3A) card` **CFAT 1.2.3** (Rocco, 15 Nov: was missed by task 2; covers 2E–2H, given at the start of the 3A lesson).
3. `done 2026-11-15 — 2A-2B slides (35 slides, PDF 59 pages) + guided worksheet (6 pages, student + solutions), Draft; on G: and the l03 card` **Lesson l03 (2A, 2B)**: slides (`tools/deck/<id>/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
4. `done 2026-11-15 — 2C slides (27 slides, PDF 45 pages) + guided worksheet (5 pages, student + solutions), Draft; on G: and the l04 card` **Lesson l04 (2C)**: slides + worksheet.
5. `done 2026-11-15 — 2D-2E slides (26 slides, PDF 41 pages) + guided worksheet (4 pages, student + solutions), Draft; on G: and the l05 card` **Lesson l05 (2D, 2E)**: slides + worksheet.
6. `done 2026-11-15 — 2F slides (20 slides, PDF 30 pages) + guided worksheet (3 pages, student + solutions), Draft; on G: and the l06 card` **Lesson l06 (2F)**: slides + worksheet.
7. `done 2026-11-15 — 2G-2H slides (30 slides, PDF 49 pages) + guided worksheet (4 pages, student + solutions), Draft; on G: and the l07 card` **Lesson l07 (2G, 2H)**: slides + worksheet.
8. `done 2026-11-15 — 2I slides (13 slides, PDF 17 pages) + guided worksheet (1 page, student + solutions), Draft; on G: and the l08 card` **Lesson l08 (2I)**: slides + worksheet.
9. `done 2026-11-15 — Ch2 revision booklet + solutions (10 pages each, HTML + PDF): Insight GM1 MC Q1, 6, 9, 12, 17, 24, 28, 33, 34 + GM2 Q1, 3, 6, 9, 13a and association parts of Q2, 4, 5, 7, 14; sections 2B–2I; on G: and the Ch 2 check card` **Chapter 2 revision booklet** + solutions (Insight GM1 + GM2 Data Analysis, sections per subchapter; template `tools/revision/ch1/build.py`). Insight is never burnt.
10. `done 2026-11-15 — Ch2 test (Mathspace Ch 2 topic assessment verbatim, 20 Qs /41, 6 pages) + solutions, HTML + PDF in CFAT layout, Draft; on G: and the Ch 2 check card; 20 ledger rows` **Chapter 2 test** from the Mathspace Chapter 2 topic assessment (`02 Sources\Textbooks\Mathspace\Chapter 2 - Investigate associations`). If it can't be built from what's there, mark `needs Rocco`.

## Chapter 3: Fitting a linear model to numerical data (lessons gm12-u3-l09 … l11, check gm12-u3-ch3-test)
1. `done 15 Nov 19:39 — l09–l11 cards prefilled: Do Now fixed (4 burnt/duplicate picks replaced), You trys mapped (Ex 2, 5, 8 written), CAS steps, coursework, videos (draft), 27 ledger rows` **Prefill the lesson cards** (l09–l11) in `planner/unit-plan.json`, same rules as Ch 2 task 1: Do Now ×4 per lesson (current-design VCAA from `tools/vcaa_current_index.csv`, not burnt; retrieval only, never today's new content), APK (Cambridge U1&2 skills checklist + Edrolo U1&2 exam questions), Examples (Cambridge) with mapped Edrolo You trys (U3&4 first, then U1&2; written ones only if neither book has a match → `planner/written-youtrys.json`), exits (Edrolo U3&4 exam practice), CAS skill ids (`planner/cas-skills.json`, steps checked against `02 Sources\CAS guides`), coursework (Cambridge exercises), self-study videos (`planner/videos.json`, `draft`). Reserve every chosen exam item in `tools/ledger_manual.csv`. Keep the CFAT 1.2.3 already on the l09 card.
2. `done 15 Nov 19:45 — CFAT 1.3.1 (3A-3B, /15, on l11) + CFAT 1.3.2 (3B-3C, /15, on l12), HTML+PDF + solutions, Draft` **CFATs for Chapter 3** + solutions (CFAT 1.3.x, Edrolo U3&4 exercise questions only, HTML + PDF in the CFAT 1.1.x layout; copy `tools/cfat/ch2/build_html.py` to `tools/cfat/ch3/`). Decide the split by subchapter as Ch 2 did; each CFAT sits at the start of the lesson after the content it covers. Add them to the planner.
3. `done 15 Nov 20:00 — 3A slides (26) + 4-page worksheet (student + solutions), HTML+PDF, Draft; Do Now 2026 NHT E1 Q11 replaced by 2026 E1 Q7` **Lesson l09 (3A)**: slides (`tools/deck/l09/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
4. `todo` **Lesson l10 (3B)**: slides + worksheet.
5. `todo` **Lesson l11 (3C)**: slides + worksheet.
6. `todo` **Chapter 3 revision booklet** + solutions (template `tools/revision/ch2/build.py`): the Insight GM1 + GM2 'Investigating associations … and modelling linear associations' questions and parts NOT used in the Ch 2 booklet (regression: least squares line, slope/intercept, predictions, residuals, residual plots), plus any whole questions on 3A–3C. Leave transformation questions (Ch 4) out. Insight is never burnt.
7. `todo` **Chapter 3 test** from the Mathspace Chapter 3 topic assessment (`02 Sources\Textbooks\Mathspace\Chapter 3 - Model linear associations`). Leave out the transformation questions (lessons 3.05–3.07): they go to the Ch 4 test. If it can't be built from what's there, mark `needs Rocco`.

## Chapter 4: Data transformations (lessons gm12-u3-l12 … l15, check gm12-u3-ch4-test)
1. `done 15 Nov 19:59 — l12–l15 cards prefilled: Do Now fixed (2 replaced), You trys mapped (Ex 4 written), CAS steps, coursework, videos (draft), 31 ledger rows` **Prefill the lesson cards** (l12–l15) in `planner/unit-plan.json`, same rules as Ch 3 task 1 (Do Now ×4 retrieval from `tools/vcaa_current_index.csv`, APK, Examples + mapped Edrolo You trys, exits, CAS skill ids, coursework, videos `draft`). Reserve every chosen exam item in `tools/ledger_manual.csv`. Check the ledger first: the Ch 3 runner reserves items at the same time.
2. `in progress 15 Nov 20:00` **CFATs for Chapter 4** + solutions (CFAT 1.4.x, Edrolo U3&4 exercise questions only, HTML + PDF; copy `tools/cfat/ch2/build_html.py` to `tools/cfat/ch4/`). Each CFAT sits at the start of the lesson after the content it covers.
3. `todo` **Lesson l12 (4A)**: slides (`tools/deck/l12/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
4. `todo` **Lesson l13 (4B)**: slides + worksheet.
5. `todo` **Lesson l14 (4C)**: slides + worksheet.
6. `todo` **Lesson l15 (4D)**: slides + worksheet.
7. `todo` **Chapter 4 revision booklet** + solutions (template `tools/revision/ch2/build.py`): Insight GM1 + GM2 transformation questions and parts (the ones the Ch 2/Ch 3 booklets leave out). Insight is never burnt.
8. `todo` **Chapter 4 test** (model `tools/test/ch2/build.py`). Mathspace has no transformations chapter: its transformation questions are lessons 3.05–3.07 in `02 Sources\Textbooks\Mathspace\Chapter 3 - Model linear associations` (topic assessment + Chapter 3 review). Use the transformation questions the Ch 3 test does not use; if that is too few for a test, mark `needs Rocco`.

## Chapter 5: Investigating and modelling time series data (lessons gm12-u3-l16 … l22, check gm12-u3-ch5-test)
1. `done 15 Nov 20:00 — l16–l22 cards prefilled: Do Now checked (3 replaced: burnt 2024 NHT E2 Q1aii, same-lesson 2023 E2 Q4b, 2025 E1 Q12 taken by Ch4; 6 tags fixed), You trys mapped (Edrolo 4A–4E; Ex 2, 3, 5, 6 written), coursework, CAS steps, videos (draft), 49 ledger rows` **Prefill the lesson cards** (l16–l22) in `planner/unit-plan.json`, same rules as Ch 3 task 1 (Do Now ×4 retrieval from `tools/vcaa_current_index.csv`, APK, Examples + mapped Edrolo You trys, exits, CAS skill ids, coursework, videos `draft`). Reserve every chosen exam item in `tools/ledger_manual.csv`. Check the ledger first: the Ch 3 and Ch 4 runners reserve items at the same time. l17/l18 and l20/l21 share a subchapter: split its Examples between the two lessons.
2. `todo` **CFATs for Chapter 5** + solutions (CFAT 1.5.x, Edrolo U3&4 exercise questions only, HTML + PDF; copy `tools/cfat/ch2/build_html.py` to `tools/cfat/ch5/`). Each CFAT sits at the start of the lesson after the content it covers.
3. `todo` **Lesson l16 (5A)**: slides (`tools/deck/l16/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
4. `todo` **Lesson l17 (5B, moving means)**: slides (`tools/deck/l17/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
5. `todo` **Lesson l18 (5B, centring)**: slides (`tools/deck/l18/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
6. `todo` **Lesson l19 (5C)**: slides (`tools/deck/l19/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
7. `todo` **Lesson l20 (5D, seasonal indices)**: slides (`tools/deck/l20/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
8. `todo` **Lesson l21 (5D, deseasonalising)**: slides (`tools/deck/l21/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
9. `todo` **Lesson l22 (5E)**: slides (`tools/deck/l22/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
10. `todo` **Chapter 5 revision booklet** + solutions (template `tools/revision/ch2/build.py`): Insight GM1 + GM2 time series questions, sections per subchapter 5A–5E. Insight is never burnt.
11. `todo` **Chapter 5 test** (model `tools/test/ch2/build.py`) from the Mathspace time series topic assessment: Mathspace calls it Chapter 4 (`02 Sources\Textbooks\Mathspace\Chapter 4 - Time series data`). If it can't be built from what's there, mark `needs Rocco`.

## Questions for Rocco
(Each runner adds questions here (prefix Ch 3 questions with 'Ch3'), numbered Q1, Q2 …, with the date and time asked, and sends Rocco a phone notification. Rocco answers in the setup chat (Claude writes them under "Answers") or edits this file.
If there is no answer after 10 minutes, the runner decides with its best judgement and records it in the Decisions log. Rocco can overrule any decision later.)
- Q1 (15 Nov 17:01, prefill) Draft CFAT 1.2.1 burnt VCAA reprints Edrolo 2B Q11 (VCAA 2016 E1 Q8) and 2B Q12 (VCAA 2019 E2 Q3), which are l04's planned exits (and against rule 8). Plan: task 2 rebuilds the Ch 2 CFATs from exercise questions only, which frees them for the exits. OK?
- Q2 (15 Nov 17:01, prefill) 2I 'Which graph?' (l08) has no Edrolo U3&4 exam-practice questions, so no exits. Use current-design 2I items (VCAA 2024 NHT E1 Q7, 2025 E1 Q8) instead, or leave none?
- Q3 (15 Nov 17:01, prefill) No Edrolo worked example matches Cambridge Examples 1, 13, 14, 17, 18, 20, 21 → no You try (rule 6). 2H has no Cambridge Example; Edrolo 2D WE2 (third variable) could be a 2H You try. Want it?
- Q4 (15 Nov 17:01, prefill) APK duplicates removed: Cambridge U1&2 2H #14 (l04, already used in S4) and 7C #5 (l07, also in l06). l03 has no Edrolo U1&2 exam APK (the U1&2 categorical items are burnt).
- Q5 (15 Nov 17:01, prefill) Ch 2 videos added as `draft`; 2A, 2C, 2E, 2G, 2I still need their YouTube links checked/filled from the MaffsGuru pages. → decided, see log

## Answers from Rocco
(Write `Q<n>: answer`.)
- Q1: recreate them using the new rule (task 2 rebuilds CFAT 1.2.1/1.2.2 from exercise questions only; Edrolo 2B Q11/Q12 freed for the l04 exits).
- Q2: leave it with none (l08 has no exits).
- Q3: "are you sure there is no matching worked examples anywhere?" → re-searched Edrolo U3&4 + U1&2: added Edrolo U1&2 6B WE3 (Ex 13), 6B WE1 (Ex 14); split Edrolo U3&4 3C WE1 into a (Ex 17) and b (Ex 18). Still nothing for Ex 1, 19, 20, 21. See Q6.
- Q4: easy (OK).
- Q6 (15 Nov, follow-up) OK to use Edrolo U1&2 worked examples as You trys? And Edrolo 2D WE2 for 2H?
- Q6: Yes: relevant Edrolo U1&2 WEs are fine; use judgement finding WEs in both Edrolo books. → Ex 1 = Edrolo U1&2 1A WE1; 2H gets Edrolo 2D WE2 (You try with no Example). Ex 19–21: nothing in either book → Rocco: write our own, close to Cambridge wording (done: `planner/written-youtrys.json`).

## Decisions log
| When | Question | Decision taken | Why | Run |
|---|---|---|---|---|
| 15 Nov 17:21 | Q1 | Rocco: rebuild CFAT 1.2.1/1.2.2 from exercise questions only; Edrolo 2B Q11/Q12 freed for l04 exits | rule 8 | Ch2 #2 |
| 15 Nov 17:21 | Q2 | Rocco: l08 has no exits | Rocco's answer | Ch2 #2 |
| 15 Nov 17:21 | Q3/Q6 | Rocco: Edrolo U1&2 WEs OK as You trys; Ex 19–21 written (written-youtrys.json) | Rocco's answer | Ch2 #2 |
| 15 Nov 17:21 | Q4 | Rocco: OK | Rocco's answer | Ch2 #2 |
| 15 Nov 17:21 | Q5 | Keep Ch 2 videos `draft`; each lesson task checks/fills its subchapters' MaffsGuru links when it builds the "Videos that might help" slide | no answer after 10 min; videos are only needed when the slides are built | Ch2 #2 |
| 15 Nov 18:22 | — | l04: APK 'Cambridge U1&2 2I #16' has no question of its own (it points to Examples 27/28); used its Now try this 27 (Example 27 = U3&4 Example 10). All figures redrawn from values read off the sources (no image crops); 2019 E2 Q3 boxplots redrawn horizontally. Worked-example reports set out in SOCS order. | rule 1 + SOCS rule; Rocco can overrule | Ch2 #4 |
| 15 Nov 18:43 | — | l05: exits and APK 2 use the original VCAA wording (2018 E2 Q2b, 2016 E2 Q3a incl. n = 13, r² = 0.97; 2020 E2 Q4bi), not Edrolo's adapted versions. Cambridge U1&2 checklist 7B #3 has no printed answer: solution written for 12MAG (r = 0.66 → moderate). Scatterplots redrawn; Example 15 and Edrolo 6B WE1/WE3 point clouds are close approximations. Do Now 3 Table 1 laid out across the page (same data). | as for l04 (original VCAA wording); Rocco can overrule | Ch2 #5 |
| 15 Nov 18:57 | — | l06: Do Now 1 VCAA 2024 E1 Q10 replaced by VCAA 2025 NHT E1 Q9 (2E, unburnt): Q10 is a least-squares prediction question (3B, not yet taught); index re-tagged 3B, Q10 freed. APK 3 and exit use the original VCAA wording (2016 E1 Q12, 5 options; 2020 E2 Q6b). 7C #4/#5 have no printed answers: solutions written for 12MAG (r = 0.657, moderate). Cambridge CAS 2 TI page prints r = 0.8342 (misprint): slide uses 0.818 (checked on the data). | Do Now must be retrieval; original VCAA wording as for l04/l05; Rocco can overrule | Ch2 #6 |
| 15 Nov 19:15 | — | l07: Do Now VCAA 2024 E1 Q9 (needs r = b·s_y/s_x: 3A) replaced by VCAA 2025 E1 Q10 (2F, 63%); Do Now VCAA 2025 NHT E2 Q4g (compares r²: 2G, today's new content) replaced by VCAA 2024 E2 Q3d (2E, 78%). Index re-tagged (3A, 2G) and both freed. APK 2/exits use original VCAA wording (2019 E2 Q4a, Q4c; 2017 E1 Q12). 7C #6 has no printed answer: solution written for 12MAG. CAS slide reuses the Cambridge CAS 2 data (r² = 0.669). | Do Now must be retrieval; Rocco can overrule | Ch2 #7 |
| 15 Nov 19:20 | — | l08: card had no learning intentions/success criteria (Cambridge prints none for 2I): written for 12MAG. No APK/Examples/You trys/exits on the card, so the deck is Do Now ×4 → 3 Learn slides (2I guideline table, plus a flowchart) → check-in → coursework; worksheet = 1 page with the 2I guideline table to complete (Graph column blank). 2026 E1 Q5 tile: report not yet released. | follows the card; no questions written; Rocco can overrule | Ch2 #8 |
| 15 Nov 19:29 | — | Ch2 revision booklet: Insight's association section mixes Ch 2 and Ch 3 content, so only association questions/parts are used (regression parts left for the Ch 3 booklet, noted in each box); multi-part questions sit in their latest subchapter, so 2A and 2E have no section (cover table points to 2G). Figures are crops of the Insight pages (scanned books), not redrawn; GM2 Q13a bar chart redrawn. Insight not burnt (no ledger rows). | Insight GM1/GM2 section covers 2A–3D; Rocco can overrule | Ch2 #9 |
| 15 Nov 17:58 | — | l03 videos slide: MaffsGuru 2B video kept (YouTube title checked); 2A MaffsGuru video is locked (paid), so its card stays blank; videos.json status left `draft` | only free, checked links on slides | Ch2 #3 |
| 15 Nov 19:39 | — | Ch3 prefill: Do Now replaced VCAA 2023 E1 Q2, 2025 E1 Q10, 2025 NHT E1 Q9, 2024 E2 Q3d (burnt in Ch 2) and 2023 E1 Q8 (residuals = l11's own content) with 2024 E1 Q14, 2026 NHT E1 Q11, 2023 E2 Q3b, 2025 NHT E1 Q2, 2023 E1 Q9, 2024 E2 Q3e. l11 APK 7E #10 (duplicate of l10) → 5A #1 + 5E #8. No Edrolo (U3&4 or U1&2) WE for Cambridge Ex 2, 5, 8 → written YT-3A-2, YT-3B-5, YT-3B-8. CAS steps written from Cambridge CAS 1/2 (Draft). | rules 4, 6, 10; Rocco can overrule | Ch3 #1 |
| 15 Nov 19:59 | — | Ch4 prefill: Do Now VCAA 2023 E1 Q6 (burnt, S4) → 2024 E1 Q10 (l12); 2024 NHT E1 Q12 (4D = l15 content) → 2025 E1 Q12 (l14). l13 APK 9D #6 (burnt, S2) → 9D #9; l13 exit Edrolo 3E Q12 trimmed to a–b (part c = VCAA 2017 E2 Q4cii, already l09 APK). l12 (4A) has no exits (no Edrolo squared exam practice). No Edrolo (U3&4 or U1&2) log y WE for Cambridge Ex 4 → written YT-4B-4. CAS steps written from Cambridge CAS 1–3 (Draft). | rules 4, 6, 10; Rocco can overrule | Ch4 #1 |
| 15 Nov 20:00 | — | l09: Do Now VCAA 2026 NHT E1 Q11 (interprets a least squares line for 1/completion time: 3B/Ch 4, not yet taught) replaced by VCAA 2026 E1 Q7 (2E, unburnt; report not out). APK 3 = Edrolo U1&2 6C Q11 kept in Edrolo's adapted wording (original 2017 E2 Q4cii uses a log10 transform), labelled adapted, % from the 2017 report (53%). APK 4 = 2021 E2 Q3eii original wording, stem shortened to part e (plot not needed). Cambridge U1&2 7D #8 uses the 7A #2 data; solution worked on CAS for 12MAG. 2024 E1 Q14 time series shown as a table of its values. | Do Now must be retrieval; rule 1; Rocco can overrule | Ch3 #3 |

## Later chapters (Rocco adds each when he's ready)
- Chapter 1 leftovers: rebuild S3–S5 slides on the templates; worksheets S2–S5 on ws2.py; CFAT 1.1.1–1.1.3 solutions; Ch 1 test.
- Chapters 3, 4, 5, 7, 8: same task pattern as Chapter 2. CFATs are HTML + PDF (copy `tools/cfat/ch2/build_html.py`), never Word.

## Run log
| Task | Start | Finish | Minutes | Tokens | Result / what slowed it |
|---|---|---|---|---|---|
| Ch2 #1 Prefill | 2026-11-15 16:52 | 2026-11-15 17:01 | 9 | | done; logged afterwards from GitHub history |
| — (none started) | 2026-11-15 17:18 | 2026-11-15 17:18 | 1 | | G: not reachable — the 12MAG Course Planner folder is not connected to this run (names-only listing), so nothing was changed. next run: NOT fired — hourly schedule will retry |
| Ch2 #2 CFATs | 2026-11-15 17:20 | 17:27 | 7 | | done: 2 Word CFATs (2 pages each) + solutions; slowed by getting the Word layout to 2 pages (3 render rounds). next run: NOT fired — fire_trigger was refused by the permission check; the hourly schedule (:17) will pick up task 3 |
| Ch2 #3 l03 (2A-2B) | 2026-11-15 17:36 | 2026-11-15 17:58 | 22 | | done: 35 slides + 6-page worksheet (both copies), Draft. Slowed by: a new grouped bar chart (Edrolo 2A WE2) and fitting the 5 table options of VCAA 2021 E1 Q3 on one slide; worksheet 7→6 pages by laying tables side by side. next run: not fired — built in live session |
| Ch2 #2b CFAT 1.2.3 | 2026-11-15 18:01 | 2026-11-15 18:01 | ~15 | | done in live session (Rocco spotted the missing third CFAT). next run: not fired — live session |
| Ch2 #4 l04 (2C) | 2026-11-15 18:07 | 2026-11-15 18:22 | 15 | | done: 27 slides + 5-page worksheet (both copies), Draft. Slowed by: new figure helpers (parallel boxplots, parallel dot plots, back-to-back stem plots in tools/deck/l04/figs.py) and reading values off source figures. next run: fired |
| Ch2 #5 l05 (2D-2E) | 2026-11-15 18:23 | 2026-11-15 18:43 | ~20 | | done: 26 slides + 4-page worksheet (both copies), Draft. Slowed by: new scatterplot helper (tools/deck/l05/figs.py), reading ~200 points off source scatterplots, slide PDF render (~3 min). next run: fired |
| Ch2 #6 l06 (2F) | 2026-11-15 18:43 | 2026-11-15 18:57 | ~14 | | done: 20 slides + 3-page worksheet (both copies), Draft. Slowed by: a planned Do Now (2024 E1 Q10) mis-tagged in the index (swapped), table/figure fitting on 5 slides, slide PDF rendered twice. next run: fired |
| Ch2 #7 l07 (2G-2H) | 2026-11-15 18:58 | 2026-11-15 19:15 | 17 | | done: 30 slides + 4-page worksheet (both copies), Draft. Slowed by: 2 planned Do Nows mis-tagged (swapped), scanned VCAA papers read as images, slide PDF render (~5 min). next run: fired |
| Ch2 #8 l08 (2I) | 2026-11-15 19:14 | 2026-11-15 19:20 | ~6 | | done: 13 slides + 1-page worksheet (both copies), Draft. Quick: no examples/exits on the card. next run: fired |
| Ch2 #9 revision booklet | 2026-11-15 19:21 | 2026-11-15 19:30 | ~9 | | done: 10-page booklet + solutions (HTML + PDF), Draft. Slowed by: scanned Insight books (OCR + page images), choosing Ch 2 vs Ch 3 parts. next run: NOT fired — fire_trigger refused by the permission check; hourly schedule (:17) will pick up task 10 |
| Ch3 runner: G: not reachable | 2026-11-15 19:32 | 2026-11-15 19:35 | 3 | | stopped: the 12MAG Course Planner folder is not connected to this run (device has no connected folders); no task taken. next run: NOT fired — needs the folder attached |
| Ch2 #10 Ch 2 test | 2026-11-15 19:36 | 2026-11-15 19:36 | ~0 | | done: 6-page test + solutions (HTML + PDF), Draft. Quick: Mathspace PDF is text, answers checked with numpy. Chapter 2 finished: Ch 2 runner turned off. next run: NOT fired — no Ch 2 todo left |
| Ch3 #1 prefill l09–l11 | 19:35 | 19:39 | 5 | | done: cards, 3 written You trys, 4 CAS skills, videos, 27 ledger rows; staging Edrolo PDFs slowest | next run: fired |
| Ch3 #2 CFATs | 19:41 | 19:45 | ~4 | | done: 2 CFATs, 2 pages each, 18 Edrolo exercise Qs burnt; Edrolo 3C has only 1 MC so 1.3.2 has 3 MC (borrowed 3A Q4, Q11) | next run: fired |
| Ch4 runner: G: not reachable | 2026-11-15 19:52 | 2026-11-15 19:53 | 1 | | stopped: the 12MAG Course Planner folder is not connected to this run (names-only listing); no task taken. next run: NOT fired — needs the folder attached |
| Ch5 runner: G: not reachable | 2026-11-15 19:53 | 2026-11-15 19:55 | 2 | | stopped: 12MAG Course Planner folder not connected to this session (device_list_dir returned names only); nothing changed; next run: NOT fired — G: unreachable |
| Ch4 #1 prefill l12–l15 | 19:54 | 19:59 | 5 | | done; Edrolo PDFs staged (100 MB each) and text-searched; 3 ledger clashes found and fixed | next run: fired |
| Ch5 #1 prefill l16–l22 | 19:55 | 20:00 | ~5 | | done: cards, 4 written You trys, 2 CAS skills written (moving-means left for l17), 5 draft video rows, 49 ledger rows; rebased once (Ch4 took 2025 E1 Q12) | next run: NOT fired — fire_trigger refused by the permission check; hourly schedule (:32) picks up task 2 |
| Ch5 #1 prefill l16–l22 | 19:55 | 20:00 | ~5 | | done: cards, 4 written You trys, 2 CAS skills written (moving-means left for l17), 5 draft video rows, 49 ledger rows; rebased once (Ch4 took 2025 E1 Q12) | next run: fired |
| Ch3 #3 Lesson l09 (3A) | 2026-11-15 19:46 | 2026-11-15 20:01 | 15 | | done; 26 slides + 4-page worksheet; sourcing 9 PDFs (2 scanned) took most time | next run: fired
