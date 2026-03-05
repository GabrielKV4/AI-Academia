# Spike Results Document
## ClearPath AI – Milestone 1 Technical Exploration

---

# 1. Objective of Spike

The purpose of this spike was to determine whether a Large Language Model (LLM) could:

1. Generate structured ADHD-friendly summaries
2. Follow strict formatting constraints
3. Be programmatically validated using deterministic rules
4. Support automated regeneration when constraints fail
5. Produce measurable improvement over baseline summaries

The spike focused on validating technical feasibility before full system refinement.

---

# 2. Experiments Conducted

## 2.1 Baseline Summary Generation

Tested:
- Simple summarization prompt
- Low temperature (0.3) for consistency
- Academic input samples across domains

Result:
- Baseline summaries were coherent
- Structure was inconsistent
- No guarantee of readability level
- No structural scaffolding

Conclusion:
Baseline summaries are insufficient for ADHD learners without structural constraints.

---

## 2.2 Constrained Prompt Engineering

Tested:
- Strict header requirements
- Explicit bullet formatting instructions
- Sentence length limits
- Paragraph length limits
- Reading level constraints
- Mandatory recall questions

Observed Issues:
- LLM occasionally violated sentence limits
- Bullet counts were inconsistent
- Reading level sometimes exceeded Grade 8
- Section spacing was sometimes incorrect

Conclusion:
Prompt engineering alone is not sufficient to guarantee compliance.

---

## 2.3 Deterministic Compliance Layer

Implemented:
- Regex-based sentence segmentation
- Word count validation
- Paragraph segmentation via double newline
- Exact header detection
- Bullet count enforcement
- Recall question count
- Flesch-Kincaid readability scoring
- Formula detection logic
- Section spacing validation

Result:
- Deterministic validation reliably detects violations
- Identical input produces identical compliance output
- Fully programmatic, no manual review required

Conclusion:
A validation layer is necessary to enforce constraints.

---

## 2.4 Regeneration Loop

Implemented:
- Automatic re-generation if compliance < 80%
- Maximum attempt cap (default = 2)

Result:
- Most summaries achieve compliance within 1–2 attempts
- Occasionally still fails strict reading level rule

Conclusion:
Regeneration improves reliability but does not guarantee perfection.
Threshold-based acceptance (≥ 80%) is a practical compromise.

---

# 3. Quantitative Findings

Across 20 evaluation cases:

Observed Trends:
- ADHD summaries consistently reduce:
  - Reading level
  - Average sentence length
  - Paragraph length
- ADHD summaries score significantly higher on structural compliance
- Baseline summaries rarely pass more than 40–60% of rules

Key Insight:
Constrained generation + deterministic validation produces measurable structural improvement.

---

# 4. Architectural Decisions

## Decision 1: Separate Generation and Validation

Reason:
LLMs are probabilistic.
Compliance must be deterministic.

Result:
Modular architecture:
- generator.py
- compliance_checker.py
- evaluator.py
- llm_integration.py

---

## Decision 2: Equal Rule Weighting

Reason:
Simplifies scoring logic.
Avoids subjective weighting debates during Milestone 1.

Future improvement:
Weighted scoring based on empirical impact.

---

## Decision 3: Structural, Not Semantic Validation

Reason:
Semantic simplification detection is complex.
Milestone 1 scope focused on structural compliance.

Future improvement:
Add semantic simplification scoring or lexical complexity analysis.

---

# 5. Risks Identified

Risk 1:
LLM occasionally ignores strict constraints.

Mitigation:
Regeneration loop + threshold-based compliance.

Risk 2:
Reading level formula is imperfect proxy for comprehension.

Mitigation:
Treat readability as heuristic, not sole metric.

Risk 3:
Over-constraining output may reduce richness.

Mitigation:
Balance minimum and maximum bullet constraints.

---

# 6. Scope Adjustments

Originally considered:
- Semantic simplification scoring
- GUI interface
- Adaptive difficulty

Deferred to future milestones to ensure:
- Stable backend architecture
- Deterministic compliance layer
- Quantitative evaluation framework

---

# 7. Final Spike Conclusion

The spike validates that:

- LLMs can generate structured summaries.
- Prompt constraints alone are insufficient.
- Deterministic compliance enforcement is required.
- Regeneration improves structural reliability.
- Quantitative improvement over baseline is measurable.

This confirms technical feasibility for Milestone 1.

The system qualifies as a constrained generative AI architecture, not merely prompt engineering.