# Milestone 2 Deliverables
## Team: AI-Academia
## Focus: ADHD-Compliant Study Material Generator MVP
## Due: April 5, 2026

---

## Milestone 2 Objective

By Milestone 2, your team must demonstrate a **working MVP**, not just separate components.

The MVP should show a reliable, user-facing workflow:

Input text -> baseline summary -> ADHD summary -> compliance checking -> comparison display

Milestone 2 is the point where the project must be:

- runnable from a clean repository setup
- demo-ready in class
- stable enough to use live
- supported by concise evaluation evidence

---

# 1. MVP Definition

Your Milestone 2 MVP must support this exact scenario:

1. User opens the app.
2. User pastes academic text.
3. User clicks one button.
4. System generates:
   - a baseline summary
   - an ADHD-friendly summary
5. System automatically checks ADHD compliance.
6. System displays:
   - both outputs
   - compliance score
   - rule-by-rule pass/fail results
   - quantitative comparison metrics

If any of these steps fail during the demo, the MVP is incomplete.

---

# 2. Required Deliverables

## A. Working Demo Application

You must provide a working UI in:

`app.py`

The app must:

- accept pasted text input
- have a clear `Generate` action
- show baseline and ADHD summaries side by side or in clearly separated sections
- display ADHD compliance score
- display rule-by-rule results
- display baseline versus ADHD comparison metrics
- handle empty input gracefully
- handle API failure gracefully

Preferred run command:

```bash
streamlit run app.py
```

## B. Clean Setup and Run Instructions

Your repository must allow a grader to run the MVP with minimal setup.

Required:

- complete `requirements.txt`
- `.env.example`
- README setup steps that match the real MVP workflow

The README must clearly answer:

- how to install dependencies
- how to provide the API key
- what command to run
- what a successful run should display

## C. Stable Core Pipeline

The real generation path must work without known blocking bugs.

You must verify:

- baseline generation works
- ADHD generation works
- compliance scoring works
- comparison metrics work
- failed rules are reported clearly

Known broken logic from Sprint 1 must be resolved before Milestone 2.

## D. MVP Evaluation Evidence

Create or update:

`docs/milestone2_evaluation.md`

Include at least **5 real input cases** that were actually run through the MVP.

For each case, include:

- short input description
- baseline summary
- ADHD summary
- baseline compliance score
- ADHD compliance score
- reading level comparison
- average sentence length comparison
- average paragraph length comparison
- short note on what improved

The point here is not quantity. The point is credible MVP evidence.

## E. Sprint 2 Ownership Record

Create:

`docs/sprint2_ownership.md`

Include:

- each team member
- assigned component
- specific Milestone 2 responsibility

Example components:

- UI and demo flow
- LLM integration and prompt quality
- compliance checker and scoring
- evaluation artifacts and documentation

## F. Updated Demo Video

Provide a new demo video in:

`demo/`

The video must show the actual MVP workflow in real mode or clearly labeled fallback mode.

Required content:

1. launching the app
2. entering input
3. clicking generate
4. viewing both summaries
5. viewing compliance score and rule breakdown
6. viewing baseline versus ADHD comparison

Recommended length:

- 90 to 180 seconds

---

# 3. Definition of Done

Milestone 2 is complete only if:

- the app runs from the documented command
- the dependency list is complete
- the core workflow succeeds during a live demo
- the compliance checker produces a real score
- the comparison display is understandable
- README instructions match the actual project state
- evaluation evidence is included

---

# 4. What Counts as Incomplete

Milestone 2 is incomplete if any of the following are true:

- the app only works in fake demo mode
- the real pipeline crashes
- the setup instructions do not match the repo
- required dependencies are missing
- compliance results are hard-coded
- the comparison output is not shown in the UI
- evaluation evidence is missing or purely hypothetical

---

# 5. Suggested Sprint 2 Priority Order

1. Fix runtime bugs in generation, evaluation, and scoring.
2. Make the Streamlit app the official MVP path.
3. Complete dependency and README setup.
4. Validate 5 real MVP runs.
5. Record ownership and update the demo video.

---

# 6. Grading Emphasis for Milestone 2

Milestone 2 will be judged primarily on:

- reliability
- completeness of the MVP flow
- clarity of the user-facing demo
- correctness of compliance reporting
- alignment between code, docs, and demo

Feature expansion is secondary to stability.

