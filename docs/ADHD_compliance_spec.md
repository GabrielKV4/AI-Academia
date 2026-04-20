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

## 2. Compliance Score Threshold

To be labeled **“ADHD-Compliant”**, output must pass ≥ 80% of rules.

Compliance Score =  
(Passed Rules / Total Rules) × 100

---

## 3. Compliance Output Format

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

## 4. Regeneration Policy

If compliance score < 80%:

- Automatically regenerate with stricter prompt constraints  
OR  
- Display failed rules and compliance score to the user# ADHD Compliance Specification

---

## System Overview

The ADHD Compliance Engine enforces structured, measurable formatting constraints on AI-generated study summaries.

These rules are derived from:

- Cognitive Load Theory  
- Working Memory Research  
- Readability Science  
- Retrieval-Based Learning  

All rules are:

- Quantitative  
- Automatically validated  
- Deterministic  
- Programmatically testable  

A summary is considered **ADHD-compliant** if:

> **Compliance Score ≥ 80%**

---

# Rule Set (Milestone 1)

---

## Rule 1 — Maximum Sentence Length

**Constraint:**  
Each sentence must contain ≤ 20 words.

**Rationale:**  
Long sentences increase working memory demand and reduce comprehension in learners with ADHD.

**Validation Method:**  
- Regex-based sentence segmentation  
- Word count per sentence  
- Fail if any sentence exceeds 20 words  

**References:**  
- Martinussen et al. (2005)  
- Sweller (1988)  

---

## Rule 2 — Maximum Paragraph Length

**Constraint:**  
Each paragraph must contain ≤ 80 words.

**Rationale:**  
Large text blocks increase visual and cognitive load, impairing sustained attention.

**Validation Method:**  
- Paragraphs split using double newline (`\n\n`)  
- Word count per paragraph  
- Fail if any paragraph exceeds 80 words  

**References:**  
- Sweller (1988)  
- Martinussen et al. (2005)  

---

## Rule 3 — Required Section Structure

**Constraint:**  
The summary must include exactly these headers:

- `## Learning Objectives`  
- `## Key Concepts`  
- `## Recall Questions`  

**Rationale:**  
Structured segmentation improves comprehension and retention.

**Validation Method:**  
- Exact string presence check  

**References:**  
- Ausubel (1960)  
- Chandler & Sweller (1991)  

---

## Rule 4 — Bullet Formatting in Key Concepts

**Constraint:**  
The Key Concepts section must use bullet formatting (`-` or `*`).

**Rationale:**  
Segmented bullet presentation reduces split-attention and improves clarity.

**Validation Method:**  
- Regex extraction of Key Concepts section  
- Multiline bullet detection pattern  

**References:**  
- Chandler & Sweller (1991)  
- Mayer (2005)  

---

## Rule 5 — Minimum Recall Questions

**Constraint:**  
At least 2 recall questions must appear in the Recall Questions section.

**Rationale:**  
Retrieval practice significantly improves long-term retention.

**Validation Method:**  
- Regex detection of question marks (`?`)  
- Fail if fewer than 2 detected  

**References:**  
- Roediger & Karpicke (2006)  
- Karpicke & Blunt (2011)  

---

## Rule 6 — Reading Level Constraint

**Constraint:**  
Flesch–Kincaid Grade Level ≤ 8.0

**Rationale:**  
Lower linguistic complexity improves accessibility and reduces processing burden.

**Validation Method:**  
- `textstat.flesch_kincaid_grade()`  
- Fail if grade > 8.0  

**References:**  
- Chall & Dale (1995)  
- Crossley et al. (2008)  

---

## Rule 7 — Formula Separation Rule

**Constraint:**  
Any mathematical formula must appear on its own line.

**Rationale:**  
Inline formulas increase split-attention effects and disrupt reading flow.

**Validation Method:**  
- Regex detection of formula patterns (`a = b`)  
- Ensure formula lines contain only mathematical expressions  

**References:**  
- Sweller, van Merriënboer, & Paas (1998)  
- Mayer (2005)  

---

## Rule 8 — Section Spacing Rule

**Constraint:**  
Each section header must be preceded by a blank line.

**Rationale:**  
Visual separation reduces attentional switching cost.

**Validation Method:**  
- Header index inspection  
- Verify preceding `\n\n`  

**References:**  
- Sweller et al. (1998)  
- Mayer (2005)  

---

## Rule 9 — Minimum Key Concept Bullets

**Constraint:**  
The Key Concepts section must contain ≥ 3 bullet points.

**Rationale:**  
Ensures meaningful segmentation and prevents overly shallow summaries.

**Validation Method:**  
- Regex count of bullet lines within Key Concepts section  
- Fail if bullet count < 3  

**References:**  
- Cowan (2001)  
- Sweller (2011)  

---

## Rule 10 — Maximum Key Concept Bullets

**Constraint:**  
The Key Concepts section must contain ≤ 6 bullet points.

**Rationale:**  
Excessive segmentation increases cognitive load and overwhelms working memory.

**Validation Method:**  
- Regex count of bullet lines  
- Fail if bullet count > 6  

**References:**  
- Miller (1956)  
- Cowan (2001)  

---

# Compliance Scoring

- Total Rules: 10  
- Each rule contributes equally  
- Compliance Score = (Passed Rules ÷ 10) × 100  

A summary is considered:

- **ADHD-Compliant** if score ≥ 80%  
- **Non-Compliant** if score < 80%  

---

# System Architecture Classification

## Deterministic Components

- Sentence counting  
- Paragraph counting  
- Bullet counting  
- Reading level computation  
- Header validation  
- Formula detection  
- Spacing validation  

## Generative Component

- LLM summary generation  

The compliance engine functions as a validation layer that enforces measurable structural constraints on generative output.

---