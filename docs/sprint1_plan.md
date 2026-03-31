## Venture 2 — Sprint 1 Plan

### 🎯 Goal
Deliver a **stable, demo-ready MVP** with a simple UI on top of the existing pipeline.

---

## ✅ Must Complete This Week

### 1. Stabilize Core Pipeline
- Ensure full flow works reliably:
  - input → baseline → ADHD → compliance → comparison
- Clearly report failed rules (no silent failures)

---

### 2. Add a Minimal UI
- Use **Streamlit (preferred)** or simple CLI
- UI should:
  - Accept pasted text input
  - Have a “Generate” button
  - Display:
    - baseline vs ADHD summary
    - compliance score
    - rule-by-rule results

---

### 3. Clean Demo Flow
- One command to run (e.g., `streamlit run app.py`)
- No manual setup during demo

---

### 4. Run Real Evaluation Cases
- Test 3–5 real inputs
- Show:
  - outputs
  - compliance scores
  - clear improvement

---

### 5. Basic Robustness
- Handle:
  - empty input
  - API failures
- Improve output formatting

---

### 6. Team Contribution
- Each member owns a component
- Each member makes at least one meaningful commit

---

## 🧪 Definition of Done
- Open UI → paste text → click once → see full results clearly
- Demo runs smoothly without errors

---
