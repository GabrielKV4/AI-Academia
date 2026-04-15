# Sprint 2 Grade — Venture 2: AI Academia (ClearPath AI)

**Graded:** April 15, 2026
**Sprint Window:** April 8 – April 14, 2026
**Commits in Window (team only):** 13 (excluding 1 "Zechun Cao" instructor commit)

---

## Overall Grade: 93/100

---

## Summary

ClearPath AI had a very productive Sprint 2. All four P0 critical setup items are fixed, the regeneration logic upgrade (P1) is in, and several P3 feature enhancements (file upload, session history, export) landed alongside the required fixes. Liliana took on real implementation work (new `input_validator.py` module plus full expansion of evaluation evidence to 10 cases), which directly addresses the Milestone 2 concern about her contributions. The main gaps are a small legacy `generate_summaries` function still sitting in `generator.py`, no written failure case analysis for compliance < 80% runs, and the compliance edge case test cases in `tests/edgeCases.md` are specified on paper but not yet translated into runnable pytest cases.

---

## Category Breakdown

### 1. Task Completion (38/40)

**P0 — Critical Setup Fixes (all 4 complete):**
- `requirements.txt` now lists `openai`, `python-dotenv`, `textstat`, `streamlit`, `pandas`, `altair`. Clean install will work. (Commit `2bd4ee1`, Francisco.)
- README section 5 "Run the Application" now documents `streamlit run app.py` as the run command with a full step-by-step setup guide (clone, venv, install, API key, run). (Commit `f55a50a`, Gabriel.)
- `app.py:306` sets `demo_mode = st.checkbox("Use Demo Mode (no API calls)", value=False)`. Real Mode is now the default experience. (Commit `2bd4ee1`, Francisco.)
- Dead nested `generate_adhd_summary` function inside `generate_baseline_summary`'s except block has been removed. `generator.py` is now 111 lines, down from 162. (Commit `2bd4ee1`, Francisco.)

**P1 — Code Quality (3.5 of 4 complete):**
- Regeneration logic: `generate_adhd_summary` now uses `max_attempts=3` (was 2) with per-attempt console logging of compliance scores. (Commit `3718786`, Francisco.)
- Edge case handling: a brand new `src/input_validator.py` module (131 lines) was added with gibberish detection, English detection, empty input handling, consonant-run and vowel-ratio heuristics, and a top-level `validate_input_text` that is wired into `app.py:471` before generation runs. Solid work and goes beyond what the sprint plan asked for. (Commit `db2f3c2`, Liliana.)
- Input type variety: 10 evaluation input cases in `docs/sprint2_evaluation_evidence.md` cover textbooks (Microbiology, Python), biographies (Napoleon, Musk), popular science books (Black Holes, Thinking Fast and Slow), articles (ML, Mongolian history), and research papers (Parkinson's, Virtual Cells). Meets "diverse academic content types." (Commits `ee4617d`, `2ee40d6`, `e4ec4d2`, Liliana.)
- **Gap:** Legacy cleanup is incomplete. `src/generator.py:90` still defines a standalone `generate_summaries(text)` function that is not called from anywhere in the codebase (verified via grep). This is the same "duplicate standalone functions" issue flagged in Milestone 2 and should be removed before the final demo.

**P2 — Evaluation Expansion (2 of 3 complete):**
- 10 test cases delivered in `sprint2_evaluation_evidence.md` (up from 5 in `milestone2_evaluation.md`). Each case has inputs and notes, which meets the "expand to 10" goal.
- Compliance edge case scenarios are documented in `tests/edgeCases.md` (135 lines, 6 scenarios including oversimplified content, detailed but long sentences, paragraph overflow, weak sections). Good design work, but these are not yet runnable pytest cases in `test_compliance.py` (still 10 test methods, unchanged from Milestone 2).
- **Gap:** No written failure case analysis. `sprint2_evaluation_evidence.md` does not call out any case where compliance fell below 80% after all 3 regeneration attempts, nor does it analyze why. The Sprint 2 plan explicitly asked for this.

**P3 — Feature Enhancements (3 of 4 complete, impressive given they were lowest priority):**
- PDF / .txt / .docx file upload: `app.py:358` `st.file_uploader(type=["pdf", "txt", "docx"])` with parsing branches starting at line 365. (Commit `6f14195`, Gabriel.)
- History / comparison view: `st.session_state.history` initialized at line 25, history entries appended at line 703, reverse-iterated display at line 439. (Commit `6f14195`, Gabriel.)
- Export functionality: `build_export_content` function and two `st.download_button` calls for `.txt` and `.md` formats (app.py lines 224, 729, 737).
- **Gap:** Batch processing was not implemented. Low priority, fine to defer.

### 2. Code Quality (19/20)

- `generator.py` is substantially cleaner. Dead nested function gone, regeneration loop is readable, attempt logging is useful for debugging.
- `input_validator.py` is a well-factored module: pure helper functions, a composite `validate_input_text` entry point, reasonable heuristics.
- `app.py` grew from ~300 lines to 750+ lines to absorb file upload, history, export, and validation. It is doing a lot, but the structure holds up.
- **Minor issue:** The orphan `generate_summaries` function in `generator.py:90` should go. It is the last piece of the "legacy duplicate" concern from Milestone 2.

### 3. Documentation (14/15)

- README is now honest about the actual run command. Setup instructions are complete.
- `sprint2_evaluation_evidence.md` is a substantial new doc (424 lines, 10 cases).
- `tests/edgeCases.md` is a clear design doc for compliance edge cases.
- **Minor gap:** No changelog or sprint-closeout note summarizing what changed this sprint, which would help the final grader.

### 4. Testing / Evaluation (12/15)

- `tests/test_compliance.py` is unchanged from Milestone 2 (10 test methods, all pytest). No new tests were added despite `edgeCases.md` defining 6 new scenarios.
- `tests/edgeCases.md` is paper-only, no assertions.
- 10 evaluation cases documented, but the evidence is descriptive and does not always include the numeric compliance scores / reading levels / sentence-length comparisons the Milestone 2 eval doc had. Final-demo grading will want those numbers.
- **Gap:** No failure case analysis (where compliance < 80% after max attempts).

### 5. Team Contribution (10/10)

All 4 team members committed this sprint. The distribution is much healthier than Milestone 2:

| Team Member | Commits | Contribution Area |
|---|---|---|
| Liliana Martinez | 8 | New `input_validator.py` module, 10-case evaluation evidence doc, edge case test design, legacy function cleanup. Major step up from M2. |
| Francisco Morales (Fmora1) | 3 | P0 setup fixes (requirements.txt, generator cleanup, demo mode default), regeneration logging upgrade. |
| Gabriel Garcia | 2 | README rewrite, file upload + history + export implementation in app.py (209-line single commit). |
| Daniel (danielv464) | 0 | No commits this sprint. |

Note: commit counts are a red flag indicator only, not an actual grade. Daniel having zero commits in the Sprint 2 window is worth flagging to the team, but it is possible he contributed through pair programming, review, or work on a branch that was not merged. All four members still receive the venture-level grade of 93 by default.

---

## Per-Task Completion Status

| Task | Priority | Owner | Status |
|---|---|---|---|
| Fix requirements.txt | P0 | Francisco | DONE |
| Update README with `streamlit run app.py` | P0 | Gabriel | DONE |
| Default to Real Mode | P0 | Francisco | DONE |
| Remove dead code in generator.py | P0 | Francisco | DONE |
| Clean up legacy duplicate functions | P1 | Daniel | PARTIAL (orphan `generate_summaries` remains in generator.py) |
| Improve regeneration logic (3 attempts + logging) | P1 | Francisco | DONE |
| Edge case handling (gibberish, non-English, empty, long) | P1 | Daniel | DONE (Liliana delivered via `input_validator.py`) |
| Add input type variety | P1 | Liliana | DONE (10 cases span textbooks / biographies / articles / papers) |
| Expand M2 evaluation to 10 cases | P2 | Liliana | DONE |
| Failure case analysis (compliance < 80%) | P2 | Liliana | NOT DONE |
| Compliance edge case tests (hard rule pairs) | P2 | Jacob | PARTIAL (designed in `edgeCases.md`, not coded into pytest) |
| PDF / .txt / .docx file upload | P3 | Gabriel | DONE |
| History / comparison view | P3 | Gabriel | DONE |
| Export (Download Summary .md / .txt) | P3 | Jacob | DONE (Gabriel delivered) |
| Batch processing | P3 | Daniel | NOT DONE |

---

## Definition of Done Checklist

- [x] `pip install -r requirements.txt && streamlit run app.py` works from a clean environment
- [x] README accurately documents the setup and run process
- [x] App starts in Real Mode by default
- [x] Dead code removed from generator.py
- [x] At least 10 evaluation test cases documented
- [ ] Each team member has code commits this sprint (3 of 4: Daniel has 0)

---

## Notes on What Is Missing (Carried into Sprint 3)

1. Remove the orphan `generate_summaries(text)` function in `src/generator.py:90`. It is unused and is the last piece of the Milestone 2 "legacy duplicate functions" concern.
2. Translate the 6 scenarios in `tests/edgeCases.md` into actual pytest test cases in `tests/test_compliance.py` (or a new `test_edgecases.py`).
3. Write the failure case analysis: run the 10 Sprint 2 evaluation inputs through the app and document any case where compliance stays below 80% after 3 regeneration attempts. Explain which rules failed and why.
4. Re-run the 10 evaluation cases with numeric metrics (compliance score before/after, reading level, avg sentence length, avg paragraph length). The current evidence doc is descriptive, not quantitative.
5. Ensure Daniel has real commits in Sprint 3.
6. Batch processing feature (P3) is still open.

---

## Individual Grades (Red Flag Indicator Only)

Per the April 9 clarification, every team member receives the venture-level grade (**93**) by default. The table below is a contribution red-flag indicator, not an actual grade.

| Team Member | Commits (Sprint 2) | Notes |
|---|---|---|
| Francisco Morales | 3 | Continues to carry core engineering. Healthy. |
| Gabriel Garcia | 2 | Large, high-value commits (file upload, history, export, README). Healthy. |
| Liliana Martinez | 8 | Major step up from Milestone 2. Took on a real code module plus evaluation expansion. |
| Daniel (danielv464) | 0 | Flag: no visible commits this sprint. Raise with the team and make sure Daniel owns real Sprint 3 work. |

---

## Recommendations for Sprint 3

1. Finish the legacy cleanup (remove `generate_summaries`). 5 minute task.
2. Get Daniel assigned to concrete P0 work in Sprint 3 and confirm he commits.
3. Convert `edgeCases.md` scenarios into real pytest cases so the test suite grows with the spec.
4. Produce the failure case analysis so the final demo has a strong "we know where we still fail" story.
5. Demo rehearsal should explicitly show: empty input refusal, gibberish input refusal, file upload path, history view, export button, AND an expanded baseline summary (the baseline-never-expanded issue was called out in the Milestone 2 video review).
