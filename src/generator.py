from src.llm_integration import call_llm
from src.compliance_checker import ComplianceChecker


def generate_baseline_summary(text):
    try:
        if not text or not isinstance(text, str):
            return "ERROR: Invalid input text."

        prompt = f"""
        Summarize the following study material clearly and concisely.

        {text}
        """

        summary = call_llm(prompt)

        if not summary or summary.startswith("ERROR") or summary.startswith("Error"):
            return summary

        return summary.strip()

    except Exception as e:
        return f"ERROR: Baseline generation failed - {str(e)}"


def generate_adhd_summary(text, max_attempts=3):

    if not text or not isinstance(text, str):
        return "ERROR: Invalid input text."

    last_summary = None

    for attempt in range(max_attempts):
        try:
            print(f"[Attempt {attempt + 1}] Generating ADHD summary...")

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

            if not summary or summary.startswith("ERROR"):
                print(f"[Attempt {attempt + 1}] LLM failed.")
                continue

            checker = ComplianceChecker(summary)
            results = checker.run_all_checks()

            score = results.get("overall_score", 0)

            print(f"[Attempt {attempt + 1}] Compliance Score: {score}%")

            if results.get("adhd_compliant"):
                print(f"[Attempt {attempt + 1}] Passed compliance.\n")
                return summary

            last_summary = summary

        except Exception as e:
            print(f"[Attempt {attempt + 1}] Error: {e}")
            continue

    print("All attempts completed. Returning best available summary.\n")
    return last_summary or "ERROR: Failed to generate ADHD summary."


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