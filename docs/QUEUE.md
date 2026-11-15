# 12MAG build queue (read by the "12MAG queue runner" scheduled task)

Rocco starts ONE chapter at a time. The runner does the first `todo` task of the ACTIVE chapter, marks it, and starts the next run.
When the chapter has no `todo` tasks left, the runner turns itself off and waits for Rocco to set up the next chapter.

**ACTIVE: Chapter 2**

Status words: `todo` · `in progress <date time>` · `done <date> — what was made` · `needs Rocco — why` (skipped; ask him).
A task `in progress` for more than 3 hours is treated as crashed: set it back to `todo` and note it.
Everything made is **Draft** on the planner. Nothing is marked Ready by the runner.

## Chapter 2: Investigating associations between two variables (lessons gm12-u3-l03 … l08, check gm12-u3-ch2-test)
1. `in progress 2026-11-15 16:52` **Prefill the lesson cards** (l03–l08) in `planner/unit-plan.json` from the indexes, following the rules in CLAUDE.md: Do Now ×4 per lesson (current-design VCAA from `tools/vcaa_current_index.csv`, not burnt), APK (Cambridge U1&2 skills checklist + Edrolo U1&2 exam questions), Examples (Cambridge) with mapped Edrolo You trys, exits (Edrolo U3&4 exam practice), CAS skill ids (add new skills to `planner/cas-skills.json`, steps checked against `02 Sources\CAS guides`), coursework (Cambridge exercises), self-study videos (`planner/videos.json`, MaffsGuru first; status `draft` until Rocco checks). Reserve every chosen exam item in the ledger (`tools/ledger_manual.csv`, role as planned) so later tasks don't reuse it.
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

## Later chapters (Rocco adds each when he's ready)
- Chapter 1 leftovers: rebuild S3–S5 slides on the templates; worksheets S2–S5 on ws2.py; CFAT 1.1.1–1.1.3 solutions; Ch 1 test.
- Chapters 3, 4, 5, 7, 8: same task pattern as Chapter 2.
