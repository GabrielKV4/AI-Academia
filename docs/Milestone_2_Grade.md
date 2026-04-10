# Milestone 2 Grade — Venture 2: AI Academia (ClearPath AI)

**Graded:** April 8, 2026
**Deadline:** April 5, 2026 (end of day)
**Late Commits:** None — all 43 commits are on or before 4/5/2026.

---

## Overall Grade: 88/100

---

## Summary

ClearPath AI delivers a Streamlit-based application that generates baseline and ADHD-friendly summaries of academic text, with a 10-rule compliance engine, comparison metrics (reading level, sentence/paragraph length), and visualization charts. The compliance checker is fully implemented and well-tested with unit tests. The evaluation includes 5 real test cases with all required metrics. However, the app **defaults to Demo Mode** (hardcoded fake data), `requirements.txt` is missing critical dependencies (streamlit, pandas, altair), the README doesn't mention the actual run command, and there is dead/duplicate code in the generator module.

### Video Review Notes
The demo video is ~84 seconds (slightly under the 90-180 second requirement). The app runs via `streamlit run app.py` (confirmed in terminal). **Strengths:** Demo Mode is OFF (real API calls used), ADHD summary displays well with Learning Objectives / Key Concepts / Recall Questions sections, compliance scoring shows 80% with 10-rule pass/fail breakdown including suggested fixes for failures, and comparison charts (reading level, sentence/paragraph length, compliance scores) are clean with tooltips. **Gaps:** The baseline summary section is **never expanded** — the viewer cannot see the baseline text for comparison. No edge cases demonstrated (empty input, API failure). Video is 6 seconds short of the 90-second minimum. Only one input case shown (polynomials). Minor deductions for missing demo elements.

---

## Category Breakdown

### 1. End-to-End Demo Path (22/25)
- Streamlit UI accepts pasted text, generates summaries, shows compliance and charts — the core workflow works.
- Three-tab layout (Summaries, Compliance, Charts) is well-organized.
- ADHD summary parsing into expandable sections (Learning Objectives, Key Concepts, Recall Questions) is a nice UX touch.
- Compliance score with progress bar and rule-by-rule pass/fail breakdown. ✓
- Altair bar charts for metric comparison. ✓
- **Issue:** App defaults to "Demo Mode" (checkbox ON), which uses hardcoded fake data. Milestone 2 states that "the app only works in fake demo mode" counts as INCOMPLETE. The real mode does exist and calls the API, but the default experience is fake.
- **Issue:** `requirements.txt` lists only `openai`, `python-dotenv`, `textstat` — missing `streamlit`, `pandas`, `altair`. A clean install would fail.

### 2. Code Quality & Architecture (18/20)
- Clean modular structure: `llm_integration.py`, `generator.py`, `compliance_checker.py`, `evaluator.py`.
- `ComplianceChecker` class implements all 10 ADHD rules with deterministic checking — this is the strongest part of the project.
- Unit tests (`test_compliance.py`) with 11 test methods covering pass/fail cases. ✓
- OpenAI GPT-4o-mini integration with temperature 0.3 and error handling. ✓
- Regeneration loop (max 2 attempts) if compliance < 80%. ✓
- **Issue:** Dead nested function `generate_adhd_summary` inside `generate_baseline_summary`'s except block (lines 26-75 in generator.py). This is dead code that can never execute.
- **Issue:** Legacy duplicate standalone functions in both `compliance_checker.py` and `evaluator.py` — code needs cleanup.

### 3. Documentation & Deliverables (22/25)
- PRD.md — comprehensive with problem statement, user stories, functional/non-functional requirements, risks. ✓
- ADHD_compliance_spec.md — all 10 rules with thresholds clearly specified. ✓
- research_justification.md — research backing for ADHD rules. ✓
- spike_results.md — technical spike findings. ✓
- milestone2_evaluation.md — 5 test cases with all required metrics (compliance scores, reading levels, sentence/paragraph lengths, improvement notes). ✓
- sprint2_ownership.md — all 4 team members with assigned responsibilities. ✓
- Demo videos for both M1 and M2 present in `demo/`. ✓
- architecture.png present. ✓
- `.env.example` present. ✓
- **Issue:** README says to run `python src/evaluator.py` — does NOT mention `streamlit run app.py`, which is the actual MVP command. This violates the M2 requirement that "README instructions match the actual project state."

### 4. Evaluation Evidence (14/15)
- 5 real input test cases in `milestone2_evaluation.md` — meets the M2 requirement.
- Each case shows baseline summary, ADHD summary, both compliance scores, reading level comparison, sentence/paragraph length comparison, and improvement notes. ✓
- M1 evaluation cases (`evaluation_test_cases.md`) only has 6 cases (requirement was 20), and Test Case 1 has garbled/repeated headers in output — but this is an M1 issue, not M2.

### 5. Repository Hygiene (14/15)
- `.gitignore`, `.env.example` present. ✓
- `.streamlit/config.toml` for theme. ✓
- **Critical:** `requirements.txt` is incomplete — missing streamlit, pandas, altair. This would block any grader from running the app from scratch.
- README doesn't document the actual run command.

---

## Individual Grades

| Team Member | Commits | Contribution Area | Grade |
|---|---|---|---|
| Francisco Morales (Fmora1) | 22 | Core engineering — compliance engine, generator, evaluator, app.py, Sprint 1 MVP | 95/100 |
| Gabriel Garcia | 9 | UI/Streamlit work, chart updates, initial PRD, HTML structure | 90/100 |
| danielv464 (Daniel) | 7 | Error handling, debugging, spike plan | 85/100 |
| Liliana | 5 | Evaluation docs, sprint2 ownership, PR merges | 82/100 |

**Note:** Francisco carried the bulk of the engineering. For the final sprint, Liliana should take on implementation tasks.

---

## Key Recommendations for Sprint 2
1. **Fix `requirements.txt`** — add streamlit, pandas, altair. This is the #1 priority.
2. **Update README** to document `streamlit run app.py` as the run command.
3. **Change Demo Mode default to OFF** — the real pipeline should be the default experience.
4. Remove dead code in `generator.py` (nested function in except block).
5. Clean up legacy duplicate functions in compliance_checker.py and evaluator.py.
6. Liliana needs to take on coding tasks for the final sprint.
7. Consider adding more evaluation test cases with diverse academic content.
