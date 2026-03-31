# Sprint 2 Ownership
---

# Team Members
**Daniel Villafranco - Error Handling & App Stability**
- Responsibilities:
    - Ensure the app never crashes during the demo.
- Tasks:
    - Empty input
    - API failures
    - Invalid responses
    - Unexpected errors
    - Long inputs
    - Ensure error messages display like:
        - `Please paste text before generating`
        - `API error occurred`
- Deliverables:
    - Stable runtime behavior
    - Clear error messages
    - No crashing during demo

**Francisco Morales - Main App Integration & Backend Piplines**
- Responsibilities:
    - Ensure the entire pipline runs correctly in the app.
    - Work that must work:
        - `Input > Baseline summary > ADHD Summary > Compliance Check > Comparison Charts`
- Tasks:
    - Verify `evaluate_input()` works with the real API
    - Confirm `ComplianceChecker.run_all_checks()` returns correct results
    - Ensure results are passed correctly to the UI
    - Run 5 real test inputs through the system
    - Help finalize the demo workflow
- Deliverables:
    - Stable pipline inside `app.py`
    - Correct evaluation outputs
    - Data for the evaluation document

**Gabriel Garcia - UI Layout & Presentation**
- Responsibilities:
    - Improve how results are displayed in the Streamlit interface
- Tasks:
    - Improve formatting of summary sections
    - Ensure ADHD sections display cleanly
    - Verfiy charts render correctly
    - Improve spacing and readabilty
    Make sure the UI is demo-friendly
- Deliverables:
    - Clean UI layout
    - Clear summary comparison
    - Clear chart presentation

**Liliana Martinez - Evaluation Evidence & Documentation**
- Responsibilities:
    - Produce the evaluation evidence required for Milestone 2
- Tasks:
    - Create `docs/milestone2_evaluation.md`
    - Run 5 real input cases and record:
        - Input description
        - Baseline summary
        - ADHD summary
        - Baseline compliance score
        - ADHD compliance score
        - Reading level comparison
        - Sentence length comparison
        - Paragraph length comparison
        - Short explanation of improvements
    - Create `docs/sprint2_ownership.md`
        - List each team member and their responsibilities
- Deliverables:
    - Evaluation document
    - Ownership record