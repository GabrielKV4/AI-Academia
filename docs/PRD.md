# Product Requirements Document (PRD)

---

# Product Name

ClearPath AI  
ADHD-Constrained Study Summary Generator

---

# 1. Problem Statement

Students with ADHD often struggle with:

- Dense academic text
- Long paragraphs
- Complex sentence structures
- Lack of structured review format
- Poor retention from passive reading

Traditional AI summaries optimize for brevity, not cognitive accessibility.

There is no structured validation layer ensuring summaries are cognitively optimized for ADHD learners.

---

# 2. Product Objective

Develop a system that:

- Generates study summaries from academic text
- Enforces measurable ADHD-friendly formatting constraints
- Automatically validates structural compliance
- Quantitatively compares constrained vs unconstrained outputs

The system must combine:

- Generative AI (LLM)
- Deterministic rule enforcement
- Measurable compliance scoring

---

# 3. Target Users

Primary Users:

- High school students with ADHD
- College students with ADHD
- Neurodivergent learners needing structured content

Secondary Users:

- Educators testing structured summarization
- Researchers evaluating constrained generation systems

---

# 4. Core Features

## 4.1 Baseline Summary Generator

- Input: Raw academic text
- Output: Standard LLM summary
- No structural enforcement
- Used for comparison purposes

---

## 4.2 ADHD-Constrained Summary Generator

- Input: Raw academic text
- Output: Structured summary with enforced formatting rules
- Regeneration loop (up to N attempts)
- Validated by Compliance Engine

---

## 4.3 Compliance Engine

The Compliance Engine evaluates summaries using 10 deterministic rules:

1. Sentence length constraint  
2. Paragraph length constraint  
3. Required section headers  
4. Bullet formatting requirement  
5. Minimum recall questions  
6. Reading level constraint  
7. Formula separation rule  
8. Section spacing rule  
9. Minimum key concept bullets  
10. Maximum key concept bullets  

Each rule is programmatically validated.

---

## 4.4 Compliance Scoring

Compliance Score:

Compliance Score = (Passed Rules ÷ 10) × 100

A summary is considered ADHD-compliant if:

Score ≥ 80%

---

## 4.5 Evaluation & Comparison Module

The system computes:

- Flesch–Kincaid reading level
- Average sentence length
- Average paragraph length
- Compliance score

It compares:

- Baseline summary
- ADHD-constrained summary

And outputs quantitative improvement metrics.

---

# 5. System Architecture

## 5.1 Components

1. `generator.py`
   - Handles baseline and constrained generation
   - Implements regeneration loop

2. `compliance_checker.py`
   - Deterministic rule validation
   - Compliance scoring

3. `evaluator.py`
   - Metric computation
   - Output comparison

4. `llm_integration.py`
   - External LLM API calls

---

## 5.2 Processing Flow

User Input  
→ Baseline Generation  
→ ADHD-Constrained Generation  
→ Compliance Validation  
→ Metric Evaluation  
→ Comparison Output  

---

# 6. Functional Requirements

FR1: System must accept raw academic text as input.

FR2: System must generate a baseline summary.

FR3: System must generate an ADHD-constrained summary.

FR4: System must automatically validate the constrained summary against all 10 rules.

FR5: System must compute a compliance score.

FR6: System must regenerate summary if compliance score < 80%.

FR7: System must output measurable comparison metrics.

---

# 7. Non-Functional Requirements

NFR1: Deterministic validation must produce consistent results for identical input.

NFR2: Compliance evaluation must be programmatic and reproducible.

NFR3: Rule thresholds must be explicitly defined and documented.

NFR4: System must be modular and extensible.

---

# 8. Success Metrics

The system is successful if:

- ADHD summaries consistently score ≥ 80% compliance
- ADHD summaries show reduced:
  - Reading level
  - Sentence length
  - Paragraph length
- ADHD summaries include structured retrieval questions
- Improvements are measurable across diverse subject domains

---

# 9. Constraints

- Dependent on external LLM API
- Reading level metric based on Flesch–Kincaid formula
- Rule validation limited to structural (not semantic) correctness

---

# 10. Risks

Risk 1: LLM may not consistently satisfy all constraints  
Mitigation: Regeneration loop

Risk 2: Reading level metric may not fully represent comprehension difficulty  
Mitigation: Use as heuristic, not sole indicator

Risk 3: Over-constraining output may reduce summary richness  
Mitigation: Threshold tuning and rule balance

---

# 11. Future Enhancements

- Adaptive rule tuning based on learner profile
- GUI interface
- Real-time compliance feedback
- Semantic simplification scoring
- Personalized difficulty calibration

---

# 12. Project Classification

This project demonstrates:

- Constrained generative AI
- Deterministic validation architecture
- Human-centered NLP design
- Research-backed rule enforcement
- Quantitative evaluation framework

It is not simply prompt engineering.  
It is a structured generation + validation system.

---

## Deviations from Original Plan

Several enhancements were added beyond the original PRD to improve usability, robustness, and desmstration quality.

### Additions

- A full Streamlit-based user interface was implemented to provide an interactive experienc, including tabs for summaries, compliance results, and charts.
- File upload support was added for `.txt`, `.pdf`, and `.docx` formats, allowing users to input real-world study materials.
- An input validation system was introduced to detect invalid, non-english, or gibberish text before processing.
- A history tracking feature was implemented, storing past runs with timestamps, input previews, and results.
- A compliance trend chart was added to visualize score progression across runs.
- Export functionality was added, allowing users to download results as `.txt` or `.md` files.

---
