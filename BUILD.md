# 12MAG Study Hub: build guide (for scheduled builds)

Each run builds **exactly one** subtopic page, checks it, pushes it, and ticks it off below. Templates: `data-analysis/1a.html` and `data-analysis/1b.html` — copy their structure, classes and behaviour exactly.

## Queue (build top to bottom; tick when pushed)
- [x] 1A Types of data
- [x] 1B Displaying and describing the distributions of categorical variables
- [ ] 1C Displaying and describing numerical data
- [ ] 1D Dot plots and stem plots
- [ ] 1E Using a logarithmic (base 10) scale
- [ ] 1F Measures of centre and spread
- [ ] 1G The five-number summary and the boxplot
- [ ] 1H The normal distribution and the 68–95–99.7% rule
- [ ] 1I Populations and samples
- [ ] 2A Bivariate data – classifying the variables
- [ ] 2B Associations between categorical variables
- [ ] 2C Association between a numerical and a categorical variable
- [ ] 2D Associations between two numerical variables
- [ ] 2E How to interpret a scatterplot
- [ ] 2F Correlation coefficient
- [ ] 2G Coefficient of determination
- [ ] 2H Correlation and causality
- [ ] 2I Which graph?
- [ ] 3A Fitting a least squares regression line
- [ ] 3B Using the LSRL to model a relationship
- [ ] 3C Conducting a regression analysis
- [ ] 4A Squared transformation
- [ ] 4B Log transformation
- [ ] 4C Reciprocal transformation
- [ ] 4D Choosing and applying the appropriate transformation
- [ ] 5A Time series data
- [ ] 5B Moving means
- [ ] 5C Moving medians
- [ ] 5D Seasonal indices
- [ ] 5E Fitting a trend line and forecasting

(Recursion, Matrices and Networks are added here after Data Analysis is finished and Rocco has reviewed it.)

## Locking
Before starting, check the "In progress" line. If it names a subtopic started less than 50 minutes ago, STOP (another run is working). Otherwise set it to `In progress: <code> <ISO time>` and push before building. Clear it when done.

In progress: none

## Page recipe (every page)
1. **Learn** — own-words notes (never copied from Cambridge), key-ideas box, definition cards, warn boxes quoting VCAA examiner reports verbatim with citation, sentence frames marked "(teacher frame)".
   - **📘 Textbook pointer boxes** (`<div class="tb">`) next to each matching idea: Cambridge example number + exact title + printed page, and Exercise pages at the end. Get them from `Textbook Resources\Cambridge\Textbook\2023-cambridge-units-3-4.pdf` (PDF page = printed + 12 for Ch 1; measure the offset for other chapters).
   - Examples in notes use data/variables from VCAA papers (cited).
2. **Explore** — one interactive built on VCAA data (sorter, builder, slider…). Charts via `assets/charts.js` (`data-chart` JSON or `drawChart`): uniform scales, baseline, axis labels on every chart.
3. **Watch** — one YouTube embed (`youtube-nocookie.com/embed/ID`) + "open on YouTube" fallback link. Maffs Guru first (map in Planning\Topics\1. Data Analysis\README.md); find the YouTube ID by web search. If unverifiable, note it in the run summary.
4. **Exam practice** — 4–6 VCAA questions, **verbatim**, cited (`VCAA 2024 Exam 1, Q3`). **Never write or alter questions.** Priority: current Study Design VCAA 2023–2026 (`Past Exams\Current Study Design\<year>\vcaa\`), then past-design VCAA where it adds report data. MC → `.q[data-answer]` with % bars from the report; typed → `data-accept`; tables → `data-multi`; drawings → `data-reveal`. Exam 2 parts show % per mark + average. Quote examiner comments verbatim. Files: `-report` = external assessment report (statistics); `-guide` = marking scheme. NHT reports give answers only — say so. Figures: crop from the paper at ~220 dpi, trimmed to white, into `assets/img/<code>/`.
5. **Reference sheet** — A4, colour + black & white versions (same markup, `.sheet.colour`/`.sheet.bw`), no notes box, must print on ONE page. Panels: key content, worked mini-example, display/decision box, ⚠ Exam traps with report statistics, sources footer "© VCAA, used for educational purposes".

## Site wiring
- Link the card on `index.html` (change `card soon` div → `<a class="card" href="data-analysis/<code>.html" data-lesson="<code>">` with "Ready").
- Bump `?v=` on CSS/JS links when shared assets change.

## Checks before pushing (all must pass)
- Playwright screenshots of every section at 1280px and 390px (no horizontal scroll at 390px), every interactive clicked, no console errors.
- Both reference-sheet PDFs print as exactly 1 A4 page; look at them.
- Every question checked verbatim against the source paper; every statistic checked against the report.
- Commit (end message with the attribution lines) and push to `main`; tick the queue; clear the lock.

## Run summary
Append one line per run to `BUILD-LOG.md`: date, subtopic, questions used (with sources), anything needing Rocco (missing reports, unverified video, judgement calls).
