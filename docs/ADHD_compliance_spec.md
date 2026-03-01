# ADHD Compliance Specification
## AI-Academia – ADHD-Compliant Study Material Generator

---

## 1. Purpose

This document defines the measurable ADHD compliance standards that generated study materials must satisfy.

These rules are grounded in research on:

- ADHD-related working memory limitations
- Sustained attention constraints
- Cognitive Load Theory
- Evidence-based study strategies (active recall)
- Cognitive accessibility principles

All rules defined below are:

- Concrete
- Programmatically testable
- Automatically verifiable
- Quantitatively measurable

Manual review is not required for compliance validation.

---

## 2. Compliance Rules

### Rule 1 – Maximum Sentence Length

**Requirement:**  
Each sentence must contain ≤ 20 words.

**Rationale:**  
Working memory limitations associated with ADHD increase vulnerability to overload from long, syntactically dense sentences.

**Programmatic Test:**  
- Split text by sentence delimiters (. ! ?)
- Count words per sentence
- Fail if any sentence > 20 words

---

### Rule 2 – Maximum Paragraph Length

**Requirement:**  
Each paragraph must contain ≤ 80 words.

**Rationale:**  
Large text blocks increase extraneous cognitive load and reduce reading persistence.

**Programmatic Test:**  
- Split text by blank lines
- Count words per paragraph
- Fail if any paragraph > 80 words

---

### Rule 3 – Required Structural Headers

**Requirement:**  
The output must include:

- ## Learning Objectives  
- ## Key Concepts  
- ## Recall Questions  

**Rationale:**  
Explicit structural scaffolding improves information organization and reduces cognitive search effort.

**Programmatic Test:**  
- Check for exact header strings
- Fail if any required header is missing

---

### Rule 4 – Bullet Formatting in Key Concepts

**Requirement:**  
The “Key Concepts” section must contain ≥ 1 Markdown bullet.

**Rationale:**  
Segmented lists reduce cognitive burden by chunking information into discrete units.

**Programmatic Test:**  
- Detect "-" or "*" list markers under Key Concepts
- Fail if none detected

---

### Rule 5 – Active Recall Requirement

**Requirement:**  
The “Recall Questions” section must contain ≥ 2 questions.

**Rationale:**  
Retrieval practice improves long-term retention and strengthens memory consolidation.

**Programmatic Test:**  
- Count lines ending with "?"
- Fail if fewer than 2

---

### Rule 6 – Reading Level Constraint

**Requirement:**  
Flesch-Kincaid Grade Level ≤ 8.

**Rationale:**  
Reducing linguistic complexity improves accessibility for learners with attention regulation challenges.

**Programmatic Test:**  
- Compute Flesch-Kincaid using textstat
- Fail if grade level > 8

---

### Rule 7 – Formula Separation Rule

**Requirement:**  
Mathematical expressions must appear on their own line.

**Rationale:**  
Avoids split-attention effects caused by embedding equations within paragraphs.

**Programmatic Test:**  
- Detect formula patterns (=, +, -, /, ^)
- Verify the line contains only formula content
- Fail if embedded in paragraph text

---

### Rule 8 – Section Spacing Rule

**Requirement:**  
At least one blank line must precede each major section header (except the first).

**Rationale:**  
Visual separation reduces perceptual overload and improves readability.

**Programmatic Test:**  
- Validate blank line before Markdown headers
- Fail if spacing not present

---

## 3. Compliance Score Threshold

To be labeled **“ADHD-Compliant”**, output must pass ≥ 80% of rules.

Compliance Score =  
(Passed Rules / Total Rules) × 100

---

## 4. Compliance Output Format

Example structured output:

{
  "sentence_length": "pass",
  "paragraph_length": "pass",
  "required_sections": "pass",
  "bullet_format": "pass",
  "recall_questions": "pass",
  "reading_level": "pass",
  "formula_separation": "pass",
  "section_spacing": "pass",
  "overall_score": 100,
  "adhd_compliant": true
}

---

## 5. Regeneration Policy

If compliance score < 80%:

- Automatically regenerate with stricter prompt constraints  
OR  
- Display failed rules and compliance score to the user