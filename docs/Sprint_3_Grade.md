# Sprint 3 Grade, Venture 2: AI Academia (ClearPath AI)

**Graded:** April 28, 2026
**Sprint Window:** April 15 – April 24, 2026 (extended from April 21)
**Final Demo:** April 29, 2026
**Final Deliverables Due:** May 3, 2026

---

## Overall Grade: 94/100

**Note on individual grades:** This is the venture-level grade. Members who severely under-contributed during Sprint 3 may receive a reduced individual grade applied separately.

**Note on grading scope:** Final-presentation prep items (demo script as a written deliverable, rehearsal logs, slide deck drafts, pitch deck refreshes, backup recordings) are not counted against the Sprint 3 grade. They appear in the "Items to Complete by May 3" section instead.

---

## Summary

Sprint 3 closed the Sprint 2 cleanup tail and produced the deepest evaluation evidence the team has shipped so far. The orphan `generate_summaries` function is gone. The 10-case quantitative evaluation in `docs/sprint3_quantitative_eval.md` is a substantial 72KB document with baseline vs. ADHD compliance scores, reading-level deltas, and per-rule breakdowns. A dedicated `docs/failure_analysis.md` walks through cases where ADHD compliance stayed below threshold. Six new pytest cases in `tests/test_edge_cases.py` cover the rule-conflict scenarios that were prose-only in `tests/edgeCases.md`. `requirements.txt` now installs cleanly with `python-docx` and `pypdf` after a Sprint 2 oversight; the PRD has been updated; the architecture diagram was refreshed.

Contribution is the most balanced this team has had. Liliana led the quantitative evaluation work (8 in-window commits). Francisco landed input validation finalization plus the requirements fix (6 commits). Daniel turned around from zero Sprint 2 commits to five: the orphan-function verification, the new pytest module, the architecture diagram refresh, and a few merges. Gabriel cleaned up history view, PRD, and uploaded supporting artifacts (4 commits). All four members contributed real code or documentation.

The grade sits at 94 because the architecture diagram filename has a typo (`docs/architectire.png`) and the references / citations pass is not visible in the diff. Both should be cleaned up by May 3.

---

## Category Breakdown

### 1. Task Completion (39/40)

**P0 (4 of 4 complete):**
- Orphan `generate_summaries` removed from `src/generator.py`. Verified by grep, function no longer exists.
- Quantitative eval rerun on 10 cases: shipped as `docs/sprint3_quantitative_eval.md`. Comprehensive.
- Failure case analysis: shipped as `docs/failure_analysis.md`.
- Edge case design converted to pytest: shipped as `tests/test_edge_cases.py` with 6 test functions.

**P1 (4 of 4 graded; demo script markdown deferred to final-prep):**
- Baseline summary visible by default in UI: addressed in Gabriel's history-view cleanup and project upload.
- Input validator demo path: Francisco finalized `input_validator.py` and added the input-validation evaluation document.
- File upload demo path: covered by Gabriel's Apr 21 file uploads under `docs/`.
- History view polish: shipped (`Cleaned up history view`, Gabriel Apr 21).
- Final demo script (markdown): deferred to final-prep (May 3 deliverables). The team has `demo/Final_Demo_Script.mp4` as a video.

**P2 (3 of 4 complete):**
- PRD reconciliation: shipped (Gabriel multiple commits).
- README feature list: covered by the project upload, though a more formal "Features" section is worth checking.
- Architecture diagram refresh: shipped, but the file is `docs/architectire.png` (filename typo). Carries to May 3.
- References / citations pass: not visible in the diff. Carries to May 3.

**P3:** Not required for the grade. Optional flourishes.

### 2. Code Quality (18/20)

- `tests/test_edge_cases.py` is well-structured with one test per rule-conflict scenario.
- `requirements.txt` is now complete and reproducible.
- `input_validator.py` is consolidated and used as the validation entry point.
- Compliance engine remains the strongest module. No regressions observed.

### 3. Documentation (14/15)

- `sprint3_quantitative_eval.md` is the most thorough evaluation doc the team has produced.
- `failure_analysis.md` is concise and reads like real engineering notes, not boilerplate.
- PRD reflects implemented system after Sprint 3 updates.
- Missing: final demo script as a markdown document.

### 4. Testing / Evaluation (13/15)

- 6 new pytest cases for edge scenarios.
- 10-case quantitative evaluation with baseline + ADHD reading levels, sentence and paragraph length stats, per-rule failure flags.
- Failure analysis on cases that did not pass first attempt.
- Strong evaluation evidence overall.

### 5. Team Contribution (10/10)

| Member | In-window Commits | Sprint 3 Work | Signal |
|---|---|---|---|
| Liliana | 8 | Quantitative eval (10 cases), failure analysis, demo video | Strong |
| Francisco / Fmora1 | 6 | Input validator finalization, requirements.txt fix, eval evidence | Strong |
| Daniel / danielv464 | 5 | Test_edge_cases.py (6 tests), architecture diagram, orphan-function cleanup | Strong (turnaround from 0 in Sprint 2) |
| Gabriel | 4 | PRD updates, history view cleanup, file uploads | Strong |

All four members shipped meaningful work. Daniel's turnaround from a zero-commit Sprint 2 to five Sprint 3 commits, including the new pytest module, is the highlight.

---

## Per-Task Completion Status

| Priority | Task | Owner | Status |
|---|---|---|---|
| P0 | Remove orphan generate_summaries | Daniel | Done |
| P0 | Quantitative eval rerun (10 cases) | Liliana | Done |
| P0 | Failure case analysis | Liliana | Done |
| P0 | Convert edge cases to pytest | Daniel | Done (6 tests) |
| P1 | Baseline UI fix | Gabriel | Done |
| P1 | Input validator demo path | Francisco | Done |
| P1 | File upload demo path | Gabriel | Done |
| P1 | History view polish | Gabriel | Done |
| P1 | Demo script v1 (markdown) | Liliana | Deferred to final-prep |
| P2 | PRD reconciliation | Gabriel | Done |
| P2 | References / citations pass | Francisco | Not visible in diff |
| P2 | README feature list | Gabriel | Partial |
| P2 | Architecture diagram refresh | Daniel | Done (filename typo) |

---

## Definition of Done (Sprint 3) Check

- [x] `src/generator.py` no longer contains `generate_summaries`
- [x] `docs/sprint3_quantitative_eval.md` exists with metrics for all 10 cases
- [x] At least one failure case analyzed (or all-pass note)
- [x] `tests/test_edge_cases.py` exists with 6 passing tests
- [x] Baseline summary visible by default in UI
- [~] `demo/sample_inputs/` with .pdf, .txt, .docx samples (verify in repo)
- [~] `docs/final_demo_script.md` (markdown) exists with rough flow (deferred to final-prep)
- [x] README reflects actual feature set
- [x] Every team member has at least one code commit

---

## Items to Complete by May 3 (Final Deliverables)

The May 3 package is required to be under `docs/Final_Demo/` in the repo. Save the following items there:

1. **Final demo slides** (PDF or PPTX) under `docs/Final_Demo/`. Cover: problem (ADHD-friendly studying), pipeline (summarize → score → regenerate up to 3 times), 10-rule compliance engine, evaluation numbers from `sprint3_quantitative_eval.md`, live-demo plan.
2. **Runbook** at `docs/Final_Demo/Runbook.md`. Cover: prerequisites (Python 3.10+, OpenAI API key), env setup, `streamlit run app.py`, how to upload PDF/TXT/DOCX, how to read the compliance panel, how to interpret the regeneration output, common errors.
3. **Final demo video** at `docs/Final_Demo/Final_Demo_Video.mp4` (or a `.md` file linking to the video if hosted on Drive). Backup if the live demo fails Apr 29. The existing `demo/Final_Demo_Script.mp4` may serve as a starting point but should be polished and renamed to fit the `docs/Final_Demo/` package.
4. **Final code on `main`**. Confirm `main` reflects the demo state.

Sprint 3 carryovers worth closing in the same window:

5. **Final demo script as markdown** at `docs/Final_Demo/final_demo_script.md`. The video is good but a written script anchors the slides and runbook. Should outline the 4 to 5 minute demo flow with timings.
6. **Fix architecture diagram filename typo**. `docs/architectire.png` should be `docs/architecture.png`. Update any references in the README or PRD that point to the typo.
7. **References / citations pass**. Walk through `docs/research_justification.md` and `references.md`. Confirm every ADHD rule still has a citation behind it and the citation format is consistent.
