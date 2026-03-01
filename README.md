# AI-Academia  
## ADHD-Compliant Study Material Generator

AI-Academia is an engineered content generation system that produces ADHD-friendly study summaries and automatically validates them against measurable compliance standards.

---

## Project Objective (Milestone 1)

Transform standard LLM summaries into structured, ADHD-compliant study material using:

- Real LLM backend integration
- Measurable ADHD compliance rules (8–12)
- Automated compliance validation
- Quantitative baseline comparison

This is not a prompt-only solution.  
This system enforces structured, testable constraints.

---

## How It Works

Input → LLM Generation → Compliance Checker → Score → Output

- The LLM generates a structured summary.
- The compliance checker validates measurable ADHD rules.
- A compliance score (≥ 80%) determines acceptability.
- Baseline comparison demonstrates measurable improvement.

---

## Repository Structure

/docs/
PRD.md
ADHD_compliance_spec.md
spike_results.md
evaluation_test_cases.md
architecture.png

/src/
llm_integration.py
compliance_checker.py
generator.py

requirements.txt
.env.example


---

##  Setup Instructions

1. Clone the repository
2. Install dependencies:


pip install -r requirements.txt


3. Create a `.env` file using `.env.example`
4. Add your API key
5. Run:


python src/generator.py


---

## Compliance Standard

The system enforces measurable ADHD rules including:

- Sentence length limits
- Paragraph length limits
- Reading level constraint
- Required section structure
- Bullet formatting
- Active recall questions
- Structural spacing

A minimum 80% rule pass rate is required for ADHD compliance.

---

## Evaluation

The system compares:

- Baseline GPT summary
- ADHD-constrained summary

Metrics include:

- Reading level difference
- Sentence length difference
- Paragraph length difference
- Rule compliance percentage
