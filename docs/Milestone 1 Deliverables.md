# Milestone 1 Deliverables  
## Team: AI-Academia  
### Focus: ADHD-Compliant Study Material Generator

---

## Milestone 1 Objective

By Milestone 1, your team must demonstrate:

- Real LLM backend integration  
- Clearly defined and measurable ADHD compliance standards  
- Automated compliance validation (not manual review)  
- Quantitative evaluation versus a baseline  
- Clean, professional GitHub organization  

Milestone 1 proves that your system is engineered and measurable — not just prompt-based.

---

# 1. Final PRD-Lite (1–2 pages)

Your PRD must clearly reflect the pivot:

**AI-powered ADHD-compliant study material generator**

## The PRD must include:

### A. Product Definition
- Clear description of the system  
- Defined target user persona  
- One-sentence April 5 MVP demo description  

### B. ADHD Compliance Specification (8–12 Rules)

Each rule must be:
- Concrete  
- Measurable  
- Programmatically testable  
- Supported by at least 2 credible ADHD learning references  

Examples of acceptable rules:

- Maximum sentence length ≤ 20 words  
- Maximum paragraph length ≤ 80 words  
- Reading level ≤ Grade 8 (Flesch-Kincaid)  
- Required section headings  
- Bullet formatting required for key concepts  
- Learning objectives section at the top  
- Active recall questions at the end  
- Clear spacing between sections  

If a rule cannot be checked automatically, it does not count.

### C. MVP Scope (April 5 Preview)

Explicitly define:
- Input format (text or PDF)  
- Output format (ADHD-compliant structured summary)  
- Compliance score displayed  
- Baseline comparison included  

### D. Acceptance Criteria (Testable)

Examples:

- No paragraph exceeds defined word threshold  
- Reading level computed and ≤ target threshold  
- ≥ 80% ADHD rules pass automatically  
- Required structural sections always present  

---

# 2. Working Backend LLM Integration

You must demonstrate:

- Live LLM API call (OpenAI, Claude, etc.)  
- Structured prompt enforcing ADHD constraints  
- Environment variable usage (.env)  
- Basic error handling  

Mock responses or static text are not acceptable.

---

# 3. ADHD Compliance Checker (Engineering Requirement)

You must implement a compliance checker in:

/src/compliance_checker.py

The checker must automatically validate:

- Sentence length  
- Paragraph length  
- Bullet density  
- Reading level  
- Required section structure  

Example output format:

{
  "sentence_length": "pass",
  "paragraph_length": "pass",
  "reading_level": "fail",
  "section_structure": "pass"
}

If rules fail:
- Either regenerate output automatically  
- Or display compliance score with failed rules clearly indicated  

Manual inspection does not count.

---

# 4. Evaluation Starter Kit (Minimum 20 Test Cases)

Create the file:

/docs/evaluation_test_cases.md

It must include:

- 20 input samples  
- Baseline GPT summary (no ADHD constraints)  
- ADHD-constrained summary  
- Compliance scores for both  
- Quantitative comparison metrics  

Required comparison metrics:

- Reading level difference  
- Average sentence length difference  
- Paragraph length difference  
- Percentage ADHD rule compliance  
- Structural compliance rate  

You must demonstrate measurable improvement over baseline.

---

# 5. Spike Results Document

Create:

/docs/spike_results.md

Must include:

- What was attempted  
- What worked  
- What failed  
- Architectural decisions made  
- Changes to scope after spike  
- Plan B if LLM output is inconsistent  

---

# 6. Architecture Diagram (1 page)

Create:

/docs/architecture.png

It must clearly show:

Input → Extraction → Segmentation → LLM Generation → Compliance Checker → Output → Evaluation Logging  

Clearly label deterministic components versus generative components.

---

# 7. Demo Video (Required)

Add a short demo video (60–120 seconds) that shows:

1. Input text (or PDF/text paste)
2. Generated ADHD-compliant summary
3. Compliance checker running automatically
4. Compliance score displayed
5. Baseline vs ADHD comparison (at least one example)

### How to include it in this Markdown file

Option A (recommended): commit the video to the repo (keep it small, e.g., < 25MB) and link it here:

- **Demo video:** [docs/demo.mp4](docs/demo.mp4)

Option B: upload the video to a GitHub Release or external host (YouTube/Drive) and paste the link here:

- **Demo video link:** <PASTE_LINK_HERE>

> Note: GitHub does not always inline-play videos in Markdown, but it will render a clickable link. If you want inline playback, you can try the HTML tag below (may depend on GitHub rendering):

```html
<video src="docs/demo.mp4" controls width="800"></video>
```

### Required in the Demo Video for Milestone 1

You must demonstrate:

1. Input text  
2. Generated ADHD-compliant summary  
3. Compliance checker running automatically  
4. Compliance score displayed  
5. Baseline versus ADHD comparison  

If compliance checking is manual, Milestone 1 is incomplete.

---

# 8. GitHub Repository Requirements

Your repository must include:

- /docs/PRD.md  
- /docs/ADHD_compliance_spec.md  
- /docs/spike_results.md  
- /docs/evaluation_test_cases.md  
- /docs/architecture.png  
- /src/llm_integration.py  
- /src/compliance_checker.py  
- /src/generator.py  

Additionally:

- Updated README with:
  - Project description  
  - Run instructions  
  - LLM setup instructions  
  - Architecture overview  
- requirements.txt  
- .env.example  
- At least one meaningful commit per team member  
- Sprint 1 issue board with assigned owners  

---

# Not Acceptable for Milestone 1

- Prompt-only solution without validation layer  
- No measurable ADHD rules  
- No backend integration  
- No baseline comparison  
- No structured repository organization  

---

# Milestone 1 Standard

Your project must evolve from:

“We prompt GPT to summarize nicely.”

To:

“We engineered a constrained content generation system with measurable ADHD compliance and validation.”

That is the expected senior-level outcome for Milestone 1.
