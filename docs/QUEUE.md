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
2. `todo` **CFATs for Chapter 2** + solutions (Edrolo U3&4 exercise questions only: `tools/y12_edrolo_exercise_questions.csv`; Word layout per the 12mag-cfat-word skill if listed, otherwise as CFAT 1.1.x). Add them to the planner.
3. `todo` **Lesson l03 (2A, 2B)**: slides (`tools/deck/<id>/build.py` on tpl.py) + guided worksheet (ws2.py, student + solutions).
4. `todo` **Lesson l04 (2C)**: slides + worksheet.
5. `todo` **Lesson l05 (2D, 2E)**: slides + worksheet.
6. `todo` **Lesson l06 (2F)**: slides + worksheet.
7. `todo` **Lesson l07 (2G, 2H)**: slides + worksheet.
8. `todo` **Lesson l08 (2I)**: slides + worksheet.
9. `todo` **Chapter 2 revision booklet** + solutions (Insight GM1 + GM2 Data Analysis, sections per subchapter; template `tools/revision/ch1/build.py`). Insight is never burnt.
10. `todo` **Chapter 2 test** from the Mathspace Chapter 2 topic assessment (`02 Sources\Textbooks\Mathspace\Chapter 2 - Investigate associations`). If it can't be built from what's there, mark `needs Rocco`.

## Questions for Rocco
(The runner adds one line per question here instead of guessing.)
- (15 Nov, prefill) Draft CFAT 1.2.1 burnt VCAA reprints Edrolo 2B Q11 (VCAA 2016 E1 Q8) and 2B Q12 (VCAA 2019 E2 Q3), which are l04's planned exits (and against rule 8). Plan: task 2 rebuilds the Ch 2 CFATs from exercise questions only, which frees them for the exits. OK?
- (15 Nov) 2I 'Which graph?' (l08) has no Edrolo U3&4 exam-practice questions, so no exits. Use current-design 2I items (VCAA 2024 NHT E1 Q7, 2025 E1 Q8) instead, or leave none?
- (15 Nov) No Edrolo worked example matches Cambridge Examples 1, 13, 14, 17, 18, 20, 21 → no You try (rule 6). 2H has no Cambridge Example; Edrolo 2D WE2 (third variable) could be a 2H You try. Want it?
- (15 Nov) APK duplicates removed: Cambridge U1&2 2H #14 (l04, already used in S4) and 7C #5 (l07, also in l06). l03 has no Edrolo U1&2 exam APK (the U1&2 categorical items are burnt).
- (15 Nov) Ch 2 videos added as `draft`; 2A, 2C, 2E, 2G, 2I still need their YouTube links checked/filled from the MaffsGuru pages.

## Later chapters (Rocco adds each when he's ready)
- Chapter 1 leftovers: rebuild S3–S5 slides on the templates; worksheets S2–S5 on ws2.py; CFAT 1.1.1–1.1.3 solutions; Ch 1 test.
- Chapters 3, 4, 5, 7, 8: same task pattern as Chapter 2.

## Run log
| Task | Start | Finish | Minutes | Tokens | Result / what slowed it |
|---|---|---|---|---|---|
| Ch2 #1 Prefill | 2026-11-15 16:52 | 2026-11-15 17:01 | 9 | | done; logged afterwards from GitHub history |
