from src.llm_integration import call_llm
from src.compliance_checker import ComplianceChecker


def generate_baseline_summary(text):
    prompt = f"""
    Summarize the following study material clearly and concisely.

    {text}
    """

    summary = call_llm(prompt)

    if summary.startswith("ERROR"):
        raise RuntimeError(summary)

    return summary


def generate_adhd_summary(text, max_attempts=2):

    for attempt in range(max_attempts):

        prompt = f"""
        Generate an ADHD-friendly study summary following these STRICT rules:

        STRUCTURE:
        - Must include the exact section headers:
          ## Learning Objectives
          ## Key Concepts
          ## Recall Questions

        RULES:
        - Maximum 20 words per sentence
        - Maximum 80 words per paragraph
        - Reading level at or below Grade 8
        - Use bullet points in Key Concepts
        - At least 3 and no more than 6 bullet points in Key Concepts
        - At least 2 recall questions at the end
        - Leave a blank line between sections
        - Any formula must be on its own line

        Only output the formatted summary.

        Study Material:
        {text}
        """

        summary = call_llm(prompt)

        if summary.startswith("ERROR:"):
            raise RuntimeError(summary)

        checker = ComplianceChecker(summary)
        results = checker.run_all_checks()

        if results["adhd_compliant"]:
            return summary

    return summary  # return last attempt even if not compliant


def generate_summaries(text):

    baseline_prompt = f"""
    Summarize the following educational text:

    {text}
    """

    adhd_prompt = f"""
    Create an ADHD-friendly summary of the following text.
    Use sections:
    - Learning Objectives
    - Key Concepts
    - Recall Questions

    Text:
    {text}
    """

    baseline_summary = call_llm(baseline_prompt)
    adhd_summary = call_llm(adhd_prompt)

    return baseline_summary, adhd_summary