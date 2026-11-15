# 12MAG build queue (read by the "12MAG queue runner" scheduled task)

Rocco starts ONE chapter at a time. The runner does the first `todo` task of the ACTIVE chapter, marks it, and starts the next run.
When the chapter has no `todo` tasks left, the runner turns itself off and waits for Rocco to set up the next chapter.

**ACTIVE: Chapter 2**

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
7. `in progress 2026-11-15 18:58` **Lesson l07 (2G, 2H)**: slides + worksheet.
8. `todo` **Lesson l08 (2I)**: slides + worksheet.
9. `todo` **Chapter 2 revision booklet** + solutions (Insight GM1 + GM2 Data Analysis, sections per subchapter; template `tools/revision/ch1/build.py`). Insight is never burnt.
10. `todo` **Chapter 2 test** from the Mathspace Chapter 2 topic assessment (`02 Sources\Textbooks\Mathspace\Chapter 2 - Investigate associations`). If it can't be built from what's there, mark `needs Rocco`.

## Questions for Rocco
(The runner adds questions here, numbered Q1, Q2 …, with the date and time asked, and sends Rocco a phone notification. Rocco answers in the setup chat (Claude writes them under "Answers") or edits this file.
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
| 15 Nov 17:58 | — | l03 videos slide: MaffsGuru 2B video kept (YouTube title checked); 2A MaffsGuru video is locked (paid), so its card stays blank; videos.json status left `draft` | only free, checked links on slides | Ch2 #3 |

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
