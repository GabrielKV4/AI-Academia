import streamlit as st
import pandas as pd
import altair as alt
from src.compliance_checker import ComplianceChecker
from src.evaluator import evaluate_input

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="ClearPath AI",
    page_icon="📘",
    layout="wide"
)

st.title("ClearPath AI")
st.caption("AI-powered summarization designed for ADHD-friendly learning.")
st.subheader("ADHD-Constrained Study Summary Generator")

st.write(
"""
Paste academic text below. The system generates:

• A **baseline AI summary**

• An **ADHD-optimized summary**

• A **compliance score based on 10 accessibility rules**
"""
)

# -----------------------------
# Text Input
# -----------------------------

user_input = st.text_area(
    "Input Text",
    height=200,
    placeholder="Paste textbook content, lecture notes, or academic paragraphs here..."
)

# -----------------------------
# Fix Suggestions for Rules
# -----------------------------

def get_fix_suggestion(rule):

    suggestions = {
        "sentence_length": "Shorten sentences so they contain 20 words or fewer.",
        "paragraph_length": "Break large paragraphs into smaller chunks under 80 words.",
        "required_sections": "Include the sections: Learning Objectives, Key Concepts, and Recall Questions.",
        "bullet_format": "Use '-' bullet points inside the Key Concepts section.",
        "recall_questions": "Add at least two questions ending with a question mark.",
        "reading_level": "Simplify vocabulary and shorten sentences to reach grade 8 or lower.",
        "formula_separation": "Place formulas on their own line without surrounding text.",
        "section_spacing": "Add a blank line between section headers.",
        "min_key_bullets": "Include at least three bullet points in the Key Concepts section.",
        "max_key_bullets": "Limit the Key Concepts section to six bullets or fewer."
    }

    return suggestions.get(rule, "Review formatting for this rule.")


# -----------------------------
# Generate Button
# -----------------------------

if st.button("Generate Summaries"):
    # Error handling for empty inputs or inputs without enough detail
    if not user_input.strip():
        st.warning("Please enter some text.")
    elif len(user_input.split()) < 15:
        st.warning("Input is too short. Please provide more detailed academic text.")
    elif len(user_input) > 12000:
        st.warning("Input is too long. Please shorten the text amd try again.")
        st.stop()

    else:

        # Small UI upgrade (makes app feel polished)
        with st.spinner("Generating summaries and evaluating compliance..."):

            try:

                results, baseline, adhd = evaluate_input(user_input)

                if baseline.startswith("ERROR") or adhd.startswith("ERROR"):
                    st.error("Failed to generate summaries due to an API issue. Please try again.")
                    st.stop()

                st.divider()

                # -----------------------------
                # Summary Comparison
                # -----------------------------

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Baseline Summary")
                    st.info(baseline)

                with col2:
                    st.subheader("ADHD Optimized Summary")
                    st.success(adhd)

                st.divider()

                # -----------------------------
                # Compliance Evaluation
                # -----------------------------

                checker = ComplianceChecker(adhd)
                compliance = checker.run_all_checks()

                score = compliance["overall_score"]

                st.subheader("ADHD Compliance Results")

                st.metric(
                    label="Compliance Score",
                    value=f"{score}%"
                )

                st.progress(score / 100)

                # Clear status message for demo
                if score >= 80:
                    st.success("This summary meets ADHD accessibility standards.")
                else:
                    st.warning("This summary needs improvements to meet ADHD accessibility standards.")

                st.divider()

                # -----------------------------
                # Rule Breakdown
                # -----------------------------

                st.subheader("Rule Breakdown")

                for rule, data in compliance.items():

                    if isinstance(data, dict):

                        pretty = rule.replace("_", " ").title()
                        status = data["status"]

                        if status == "pass":
                            st.success(f"{pretty} — PASS")

                        else:
                            suggestion = get_fix_suggestion(rule)

                            st.error(f"{pretty} — FAIL")
                            st.caption(f"Suggested Fix: {suggestion}")

                st.divider()

                # -----------------------------
                # Evaluation Comparison Charts
                # -----------------------------

                st.subheader("Evaluation Comparison")
                def safe_number(value):
                    return value if isinstance(value, (int, float)) else 0
                readability_data = {
                    "Metric": [
                        "Reading Level",
                        "Avg Sentence Length",
                        "Avg Paragraph Length"
                    ],
                    "Baseline": [
                        safe_number(results["baseline"]["reading_level"]),
                        safe_number(results["baseline"]["avg_sentence_length"]),
                        safe_number(results["baseline"]["avg_paragraph_length"])
                    ],
                    "ADHD Version": [
                        safe_number(results["adhd"]["reading_level"]),
                        safe_number(results["adhd"]["avg_sentence_length"]),
                        safe_number(results["adhd"]["avg_paragraph_length"])
                    ]
                }

                readability_df = pd.DataFrame(readability_data)

                st.write("### Readability Metrics")

                chart_data = readability_df.melt(
                    id_vars="Metric",
                    var_name="Version",
                    value_name="Value"
                )

                chart = alt.Chart(chart_data).mark_bar().encode(
                    x=alt.X("Metric:N", title="Metric"),
                    y=alt.Y("Value:Q", title="Value"),
                    color="Version:N",
                    xOffset="Version:N"
                )

                st.altair_chart(chart, use_container_width=True)

                # Compliance score comparison

                score_df = pd.DataFrame({
                    "Version": ["Baseline", "ADHD"],
                    "Compliance Score": [
                        safe_number(results["baseline"]["compliance_score"]),
                        safe_number(results["adhd"]["compliance_score"])
                    ]
                })

                st.write("### ADHD Compliance Score")

                st.bar_chart(score_df.set_index("Version"))

                st.caption(
                    "Comparison of readability and structural accessibility between standard AI summaries and ADHD-constrained summaries."
                )

            except RuntimeError as e:
                st.error(f"API Error: {e}")
            except Exception:
                st.error("Unexpected Error has occured. Please try again.")
