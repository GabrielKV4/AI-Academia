# Sprint 2 Plan — Venture 2: AI Academia (ClearPath AI)

**Sprint Duration:** April 8 – April 14, 2026
**Sprint Goal:** Fix critical setup issues, make real mode the default, and expand evaluation coverage.
**Final Demo:** April 29, 2026

---

## Context

After Milestone 2, ClearPath AI has a functional Streamlit app with baseline and ADHD-friendly summary generation, a solid 10-rule compliance engine with unit tests, and comparison metrics with charts. The main issues are: incomplete `requirements.txt`, README doesn't mention the actual run command, Demo Mode is the default, and there's dead/duplicate code. Sprint 2 focuses on making the app reliably runnable from scratch and expanding its robustness.

---

## Sprint 2 Tasks

### P0 — Critical Setup Fixes (Days 1–2)

| Task | Owner | Description |
|---|---|---|
| Fix requirements.txt | Francisco | Add `streamlit`, `pandas`, `altair` to requirements.txt. Verify with `pip install -r requirements.txt` in a clean environment |
| Update README | Gabriel | Document `streamlit run app.py` as the primary run command. Add full setup guide matching actual workflow |
| Default to Real Mode | Francisco | Change Demo Mode checkbox to default OFF. The real pipeline should be the default experience |
| Remove dead code in generator.py | Francisco | Remove the dead nested `generate_adhd_summary` function inside `generate_baseline_summary`'s except block (lines 26-75) |

### P1 — Code Quality (Days 2–4)

| Task | Owner | Description |
|---|---|---|
| Clean up legacy functions | Daniel | Remove duplicate standalone functions in `compliance_checker.py` and `evaluator.py` |
| Improve regeneration logic | Francisco | Increase max regeneration attempts from 2 to 3. Add logging for each attempt's compliance score |
| Edge case handling | Daniel | Test and handle: very short inputs, non-English text, text with heavy math/formulas, extremely long inputs |
| Add input type variety | Liliana | Test with different academic content types: textbook excerpts, research papers, lecture notes |

### P2 — Evaluation Expansion (Days 3–5)

| Task | Owner | Description |
|---|---|---|
| Expand M2 evaluation | Liliana | Add 5 more test cases (total 10) covering diverse academic subjects and content lengths |
| Add failure case analysis | Liliana | Document cases where compliance < 80% after all regeneration attempts. Analyze why |
| Compliance edge cases | Jacob | Write test cases for compliance rules that are hard to satisfy simultaneously (e.g., short sentences + sufficient detail) |

### P3 — Feature Enhancements (Days 5–7)

| Task | Owner | Description |
|---|---|---|
| PDF/file upload support | Gabriel | Add file upload to Streamlit UI (PDF, .txt, .docx) in addition to paste |
| History/comparison view | Gabriel | Allow users to see past summaries and compare across inputs |
| Export functionality | Jacob | Add "Download Summary" button for ADHD-friendly summary (as .md or .txt) |
| Batch processing | Daniel | Allow processing multiple text inputs in sequence with aggregate compliance stats |

---

## Definition of Done (Sprint 2)

- [ ] `pip install -r requirements.txt && streamlit run app.py` works from a clean environment
- [ ] README accurately documents the setup and run process
- [ ] App starts in Real Mode by default (Demo Mode is opt-in)
- [ ] Dead code removed from generator.py
- [ ] At least 10 evaluation test cases documented
- [ ] Each team member has code commits this sprint

---

## Contribution Expectations

Francisco carried the bulk of engineering (22 of 43 commits). **Jacob** has zero code commits (5 documentation-only commits) — Sprint 2 is the time to take on real implementation work. Liliana should expand beyond evaluation docs into testing and validation. All team members are expected to have meaningful code contributions.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 2 (this sprint) | Apr 8–14 | Setup fixes, real mode default, evaluation expansion |
| Sprint 3 | Apr 15–21 | Feature polish, accessibility, presentation prep |
| Sprint 4 | Apr 22–28 | Final integration, demo rehearsal, final deliverables |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |
