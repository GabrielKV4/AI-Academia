import re
import textstat
from src.generator import generate_baseline_summary, generate_adhd_summary
from src.compliance_checker import ComplianceChecker


# -----------------------------
# Helper Metric Functions
# -----------------------------

def average_sentence_length(text):
    sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
    if not sentences:
        return 0
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences)


def average_paragraph_length(text):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not paragraphs:
        return 0
    total_words = sum(len(p.split()) for p in paragraphs)
    return total_words / len(paragraphs)


def reading_level(text):
    return textstat.flesch_kincaid_grade(text)


# -----------------------------
# Core Evaluation Logic
# -----------------------------

def evaluate_input(input_text):
    # Validate input early
    if not input_text or not isinstance(input_text, str):
        raise ValueError("Invalid input provided. Expected non-empty string.")

    try:
        print("Generating baseline summary...")
        baseline = generate_baseline_summary(input_text)

        if not baseline or baseline.startswith("ERROR") or baseline.startswith("Error"):
            raise RuntimeError(baseline or "Baseline generation failed.")

        print("Generating ADHD-constrained summary...")
        adhd = generate_adhd_summary(input_text)

        if not adhd or adhd.startswith("ERROR") or adhd.startswith("Error"):
            raise RuntimeError(adhd or "ADHD summary generation failed.")

        # Run compliance checks safely
        try:
            baseline_checker = ComplianceChecker(baseline)
            baseline_results = baseline_checker.run_all_checks()
        except Exception:
            baseline_results = {"overall_score": 0}

        try:
            adhd_checker = ComplianceChecker(adhd)
            adhd_results = adhd_checker.run_all_checks()
        except Exception:
            adhd_results = {"overall_score": 0}

        try:
            baseline_reading = reading_level(baseline)
        except Exception:
            baseline_reading = 0

        try:
            adhd_reading = reading_level(adhd)
        except Exception:
            adhd_reading = 0

        results = {
            "baseline": {
                "reading_level": baseline_reading,
                "average_sentence_length": average_sentence_length(baseline),
                "average_paragraph_length": average_paragraph_length(baseline),
                "compliance_score": baseline_results.get("overall_score", 0)
            },
            "adhd": {
                "reading_level": adhd_reading,
                "average_sentence_length": average_sentence_length(adhd),
                "average_paragraph_length": average_paragraph_length(adhd),
                "compliance_score": adhd_results.get("overall_score", 0)
            }
        }

        return results, baseline, adhd

    except Exception as e:
        raise RuntimeError(f"Summary generation failed: {str(e)}")


# -----------------------------
# Comparison Printer
# -----------------------------

def print_comparison(results):

    print("\n--- Evaluation Results ---\n")

    print("Baseline:")
    for key, value in results["baseline"].items():
        print(f"{key}: {round(value, 2)}")

    print("\nADHD Version:")
    for key, value in results["adhd"].items():
        print(f"{key}: {round(value, 2)}")

    print("\nImprovements:")
    print("Reading Level ↓",
          round(results["baseline"]["reading_level"] - results["adhd"]["reading_level"], 2))

    print("Sentence Length ↓",
          round(results["baseline"]["average_sentence_length"] - results["adhd"]["average_sentence_length"], 2))

    print("Paragraph Length ↓",
          round(results["baseline"]["average_paragraph_length"] - results["adhd"]["average_paragraph_length"], 2))

    print("Compliance ↑",
          round(results["adhd"]["compliance_score"] - results["baseline"]["compliance_score"], 2))


# -----------------------------
# CLI Runner
# -----------------------------

if __name__ == "__main__":

    sample_input = """
Web scraping and social media data collection are two approaches used to gather data from the internet. Web scraping involves pulling information and data from websites using a web data extraction tool, often known as a web scraper. One example would be a travel company looking to gather information about hotel prices and availability from different booking websites. Web scraping can be used to automatically gather this data from the various websites and create a comprehensive list for the company to use in its business strategy without the need for manual work. 

Social media data collection involves gathering information from various platforms like Twitter and Instagram using application programming interface or monitoring tools. An application programming interface (API) is a set of protocols, tools, and definitions for building software applications allowing different software systems to communicate and interact with each other and enabling developers to access data and services from other applications, operating systems, or platforms. Both web scraping and social media data collection require determining the data to be collected and analyzing it for accuracy and relevance. 

Web Scraping 

There are several techniques and approaches for scraping data from websites. See Table 2.2 for some of the common techniques used. (Note: The techniques used for web scraping will vary depending on the website and the type of data being collected. It may require a combination of different techniques to effectively scrape data from a website.) 
"""

    results, baseline, adhd = evaluate_input(sample_input)

    print_comparison(results)

    print("\n--- Baseline Summary ---\n")
    print(baseline)

    print("\n--- ADHD Summary ---\n")
    print(adhd)

