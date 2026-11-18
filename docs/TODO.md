# 12MAG to-do list (rebuilt 18 Nov 2026 from the planner audit)

Tick items off here as they are done. Everything is **Draft** until it has passed review. The old 15 Nov list is in git history.

## A. Quick fixes (found in the 18 Nov audit)
- [ ] CFAT 3.11.1 (on 11C) and 3.11.2 (on Ch 11 test) are on the cards but have no Student/Solutions material links on the planner (files exist in the repo and on G:)
- [ ] CFAT 1.4.2 is listed twice on the 5A card (shows "2 CFATs" on the 2027 overview)
- [ ] Copy the HTML versions to G: 01 Lesson materials (only PDFs there): CFAT 2.7.x, 2.8.x, 3.10.x, 4.14.x; Ch 10, 13, 14 revision booklets; Ch 10 test
- [ ] Burnt twice — pick a replacement for one use of each: VCAA 2020 E2 Q4aii (S3 exit + old l18, now in 5B), VCAA 2017 E1 Q4 (CFAT 1.1.1 + 4B), VCAA 2012 E1 Q2 (1A Do Now row + 7C–7E); check VCAA 2024 NHT E1 Q2 and 2025 E2 Q1b (may only be duplicate ledger rows)
- [ ] Ledger tidy: one style for the `where` column (lesson id), `Exit`/`exit` → one word, remove old "Deck Do Now/Exit" rows, re-point rows that still say l18
- [ ] One status vocabulary: materials use draft/ready/todo, CFATs use Draft/Final
- [ ] Planner descriptions: one line per material type, no page counts (they go stale); coursework-check descriptions still say "homework" and mention a success-criteria back page (dropped)
- [ ] SAC anchor labels: "AoS 1 SAC: Part 1" vs "AoS 1 SAC Part 2" (pick one)
- [ ] Old duplicate files in `lessons/` not linked anywhere: `CFAT-1.1.x`, `Ch1-coursework-check`, `Ch1-revision-booklet(-solutions)` (Claude can't delete on G:; repo copies can go if Rocco agrees)

## B. Review — Chapter 1 (Step-up from 19 Nov), one lesson at a time
| Lesson | Slides | Worksheet | Bound reference | CFAT / other |
|---|---|---|---|---|
| L1 · 1A–1B | [x] | [x] | [ ] | — |
| L2 · 1C–1E | [ ] | [ ] | [ ] | — |
| L3 · 1F | [ ] | [ ] | [ ] | [x] CFAT 1.1.1 (Final) |
| L4 · 1G | [ ] | [ ] | [ ] | — |
| L5 · 1H–1I | [ ] | [ ] | [ ] | [x] CFAT 1.1.2 (Final) |
| Ch 1+2 check | — | — | — | [x] CFAT 1.1.3 (Final) · [ ] Ch 1 test · [ ] coursework check · [ ] Ch 1 workbook |

What every review checks: verbatim wording (changes labelled "adapted") · sources cited · % correct from examiner reports · maths right · lesson shape and burnt rules · plain writing · prints on A4, nothing cut off · slides, worksheet and bound reference agree; planner links open the right files.

## C. Review — Chapters 2–14
All built as Draft (slides, worksheets, CFATs, tests, booklets, coursework checks). Review chapter by chapter in teaching order, same checklist as B.

## D. Gaps against the rules
- [ ] Bound reference entries for Ch 2–14 (rule 2: every lesson)
- [ ] Chapter workbooks for Ch 2–14 (replace separate revision booklets on the planner)
- [ ] Convert old-style decks (Ch 2–14) to the z10 slide standard when each lesson is next worked on
- [ ] No exit task: 2I, 4A, 11E (no VCAA Leslie reprints)
- [ ] No APK: 2I, 14E
- [ ] No CFAT covers 2I, 8D, 8F, 8G
- [ ] Self-study videos: 59 of 69 still draft (Ch 2–14); 8G, 8H, 8I have no URL yet
- [ ] CAS guide: `transformed-lsrl` and `transformation-check` still draft
- [ ] Ch 1 review videos (1A–1I, on G:) are not on the planner — add them, or leave off?
- [ ] SAC tasks for AoS 2–4; Unit resources for AoS 2–4
- [ ] CFATs 1.1.1–1.1.3 use 13 VCAA reprints (against rule 8) — Rocco: leave for now
- [ ] Merged test lessons may be too long (Ch 1+2 test /78)

## E. Planner and tools
- [ ] 2027 timetables → `planner/years/2027-timetable.json` (waiting on Rocco)
- [ ] Idea: `tools/audit.py` one-click check (missing links, duplicate CFATs, burnt twice, G: files missing HTML, stale descriptions) before every push
- [ ] Idea: review status per material (To make → Draft → Reviewed → Final) with a "review progress" filter
- [ ] Idea: "What's next" bar on the year overview (next 3 lessons + whether each is Final)
- [ ] Idea: show each lesson's gaps on its own card (No exit task, No bound ref)
- [ ] Tag every VCAA index item with its command word; capture the VCAA glossary definitions
- [ ] Point the teaching dashboard at the planner files — on hold until Rocco asks
