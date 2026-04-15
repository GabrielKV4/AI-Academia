# Sprint 3 Plan — Venture 2: AI Academia (ClearPath AI)

**Sprint Duration:** April 15 – April 21, 2026
**Sprint Goal:** Finish cleanup, harden testing and evaluation evidence, and get the app demo-ready for April 29.
**Final Demo:** April 29, 2026

---

## Context

Sprint 2 was strong. All four P0 setup items are fixed, Real Mode is the default, `requirements.txt` installs cleanly, the README documents `streamlit run app.py`, and file upload, history view, export, and input validation all landed as bonus P3 features. Liliana stepped up significantly and now owns the new `input_validator.py` module plus a 10-case evaluation evidence document. Sprint 2 Grade: 93/100.

Sprint 3 is the last full sprint before final polish. The focus is: (1) carry forward the few Sprint 2 gaps, (2) turn the evaluation evidence into hard numbers, (3) convert the edge case design doc into real automated tests, and (4) make sure the final demo story is rehearsed. All team members (especially Daniel, who had zero commits in Sprint 2) need concrete code contributions this sprint.

---

## Sprint 3 Tasks

### P0 — Carry-Forward from Sprint 2 and Demo Blockers (Days 1–2)

| Task | Owner | Description |
|---|---|---|
| Remove orphan `generate_summaries` function | Daniel | Delete the unused `generate_summaries(text)` function at `src/generator.py:90`. Verify nothing imports it (`grep -rn generate_summaries .` should return only the definition). This is the last piece of the Milestone 2 "legacy duplicate functions" concern. |
| Quantitative eval rerun (10 cases) | Liliana | For each of the 10 inputs in `sprint2_evaluation_evidence.md`, rerun the app and record: baseline compliance score, ADHD compliance score, baseline reading level (Flesch-Kincaid), ADHD reading level, avg sentence length (both), avg paragraph length (both), which rules failed for the ADHD version (if any). Save as `docs/sprint3_quantitative_eval.md`. |
| Failure case analysis | Liliana | Identify any case from the 10 where ADHD compliance stayed below 80% after all 3 regeneration attempts. For each such case, document which rules failed, hypothesize why, and propose a prompt or threshold tweak. If every case passes, document that explicitly. Save in the same quantitative eval doc. |
| Convert edge case design into pytest | Daniel | Turn the 6 scenarios in `tests/edgeCases.md` into real pytest cases in a new `tests/test_edge_cases.py`. Each test should construct a sample summary string that triggers the specific rule conflict (e.g., short sentences but weak content, long sentences with strong content) and assert on `ComplianceChecker` output. Target: 6 new passing tests. |

### P1 — Demo Readiness (Days 2–5)

| Task | Owner | Description |
|---|---|---|
| Baseline summary UI fix | Gabriel | In the Milestone 2 demo video, the baseline summary section was never expanded by the presenter. Make the baseline summary visible by default (not hidden in a collapsed expander) or at least make it obvious. The side-by-side comparison is the main value prop and needs to be front and center in the April 29 demo. |
| Input validator demo path | Francisco | Wire a short "try invalid input" path into the demo script: empty input rejection, non-English / gibberish rejection. These are new Sprint 2 features and should be shown. Verify messages from `validate_input_text` display cleanly in the UI. |
| File upload demo path | Gabriel | Verify `.pdf`, `.txt`, `.docx` upload all work end-to-end with a prepared sample file of each type. Save the three sample files under `demo/sample_inputs/`. |
| History view polish | Gabriel | Add at least a timestamp and truncated input preview to each history entry. Right now `st.session_state.history` stores entries but display formatting could be clearer. |
| Demo script v1 | Liliana | Draft `docs/final_demo_script.md` outlining the 4 to 5 minute demo flow: intro, problem, paste study text, show baseline + ADHD, show compliance panel, show charts, show file upload, show invalid input refusal, show history, show export. Include rough timings. |

### P2 — Final Deliverable Preparation (Days 4–6)

| Task | Owner | Description |
|---|---|---|
| PRD reconciliation | Gabriel | Re-read `docs/PRD.md` against the actual app. Flag any requirement that is not implemented or any feature that is implemented but not in the PRD. Update PRD (with a "Deviations from Original Plan" section if needed) so PRD matches the delivered system. |
| References / citations pass | Francisco | Walk through `docs/research_justification.md` and `references.md`. Make sure every ADHD rule in `ADHD_compliance_spec.md` still has a citation behind it, and that citations are in a consistent format. This is scored at the final grade. |
| Update README feature list | Gabriel | README's "How to Run" is good. Add a short "Features" section listing: baseline + ADHD summarization, 10-rule compliance engine, regeneration with up to 3 attempts, input validation (empty / gibberish / non-English), file upload (PDF / TXT / DOCX), history view, .md / .txt export. |
| Architecture diagram refresh | Daniel | `docs/architecture.png` was created before Sprint 2. Verify it still matches the code. If `input_validator.py` is not in the diagram, add it. Export fresh PNG. |

### P3 — Nice-to-Have (Days 5–7)

| Task | Owner | Description |
|---|---|---|
| Batch processing | Daniel | Allow processing multiple text inputs in sequence with aggregate compliance stats. Carried over from Sprint 2 P3. Only if P0/P1 are fully complete. |
| Compliance score trend in history | Gabriel | In the history view, show a small line chart of compliance scores across past runs. Optional flourish. |
| Dark mode / theme polish | Francisco | Clean up `.streamlit/config.toml` theme. Optional. |
| Record a 1-minute teaser demo | Liliana | Short teaser video (~60 seconds) showing the best scenario, usable as a social post or a slide embed. Optional. |

---

## Definition of Done (Sprint 3)

- [ ] `src/generator.py` no longer contains `generate_summaries` or any other unused function
- [ ] `docs/sprint3_quantitative_eval.md` exists with numeric metrics for all 10 evaluation cases
- [ ] At least one failure case is analyzed (or a note that all 10 pass compliance)
- [ ] `tests/test_edge_cases.py` exists with at least 6 new pytest cases, all passing
- [ ] `pytest tests/` runs and passes (existing + new tests)
- [ ] Baseline summary is visible by default in the Streamlit UI
- [ ] `demo/sample_inputs/` contains one .pdf, one .txt, and one .docx working sample
- [ ] `docs/final_demo_script.md` exists with a rough 4 to 5 minute flow
- [ ] README lists the actual feature set of the app
- [ ] Every team member (all 4) has at least one code commit this sprint

---

## Contribution Expectations

Sprint 2 distribution was: Liliana 8, Francisco 3, Gabriel 2, Daniel 0. Sprint 3 must close the Daniel gap. Daniel is explicitly assigned two P0 tasks (orphan function removal, edge case pytest conversion) and one P2 task (architecture diagram refresh). If Daniel cannot take these on, the team should flag it to Jacob on Day 2 so the work can be redistributed before the end of the sprint. Francisco should continue to lead core engineering but intentionally hand off implementation tasks where possible. Liliana and Gabriel should keep their Sprint 2 momentum.

Remember: individual commit counts are a red flag indicator only, not a grade. What matters is that every team member has a visible, meaningful contribution by final demo.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 2 (completed) | Apr 8–14 | Setup fixes, real mode default, evaluation expansion, bonus P3 features |
| Sprint 3 (this sprint) | Apr 15–21 | Cleanup, quantitative eval, automated edge case tests, demo readiness |
| Sprint 4 | Apr 22–28 | Final polish, demo rehearsal, slide deck, dry run |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |

---

## Final Demo Day Heads-Up (April 29)

Two weeks out. Rehearse toward this format during Sprint 3 and Sprint 4.

**12 minutes per team, hard cap.** I will cut you off at 12:00 to keep all 8 teams on schedule, so rehearse to 10:30 or 11:00 to leave margin. Suggested split:

1. **About 3 min: overall design.** What the product does, the core pipeline, and the architectural decisions that matter (retrieval strategy, validator or grounding approach, refusal policy). No code walkthroughs.
2. **About 4 min: individual contributions.** Every team member speaks briefly about what they personally owned this semester. Plan what you will say, roughly 45 to 60 seconds each.
3. **About 4 min: live demo of the highlights.** Pick 2 or 3 scenarios from your existing demo script. Required: at least one refusal or failure case and at least one end-to-end grounded answer. Do not spend this time on UI polish.
4. **About 1 min: Q&A**, included in the 12 minutes.

**Running order** is Venture 1 through Venture 8 in order, so AI Academia presents second.

**Backup plan:** have a prerecorded screen capture of the working path ready in case the live demo fails. Internet or API hiccups are not an excuse on demo day.

**Slides and runbook:** not due before the presentation, but both are required artifacts in the final deliverables package due May 3. Save them under `docs/Final_Demo/` in your repo.

**Avoid:** narrating code, reading slides verbatim, skipping the refusal case, opening with missing features. Present the version you are proud of.

Rehearse the full 12 minutes end to end at least twice, at least once with a timer.
