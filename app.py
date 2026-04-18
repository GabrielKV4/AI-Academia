import streamlit as st
import pandas as pd
import altair as alt
from src.input_validator import validate_input_text
from src.compliance_checker import ComplianceChecker
from src.evaluator import evaluate_input
import streamlit.components.v1 as components
import random
import traceback

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="ClearPath AI",
    page_icon="📘",
    layout="wide"
)

# -----------------------------
# Background Styling
# -----------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 20% 30%, rgba(79, 140, 255, 0.25), transparent 40%),
        radial-gradient(circle at 80% 20%, rgba(120, 100, 255, 0.2), transparent 40%),
        linear-gradient(135deg, #0e1117 0%, #1a1d24 100%);
}

* {
    transition: all 0.2s ease-in-out;
}

.block-container {
    background-color: rgba(20, 24, 35, 0.6);
    padding: 2rem;
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Tab and Button Styling
# -----------------------------

st.markdown("""
<style>
.stTabs [role="tablist"] {
    justify-content: space-between;
}

.stTabs [role="tab"] {
    flex-grow: 1;
    text-align: center;
    font-size: 18px;
    padding: 12px 0;
}

.stTabs [aria-selected="true"] {
    background-color: #404247;
    border-radius: 8px;
    color: #1f77b4 !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    background-color: #1f77b4 !important;  /* your color */
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stButton > button {
    animation: fadeIn 0.6s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Main Heading
# -----------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@400;500&display=swap');
    </style>
    
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='
            font-family: "Playfair Display", serif;
            color: #0859fc; 
            '>ClearPath AI</h1>
        <h5 style='
            color: #89affa;
            '>AI-powered summarization designed for ADHD-friendly learning</h3>
        <h7 style='
            color: #afc8fa;
            '>ADHD-Constrained Study Summary Generator</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Info Box
# -----------------------------

st.markdown(
    """
    <div style="
        border: 1px solid #0e1015;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: #212429;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
    ">
        <p style='text-align: left; color: #ffffff; font-size: 24px;'>
            The system generates:
        </p>
        <ul style='color: #ffffff; font-size: 16px;'>
            <li><strong>🧠 Simple summary</strong></li>
            <li><strong>⚡ ADHD-friendly version</strong></li>
            <li><strong>✅ Clarity score</strong></li>
        </ul>
    </div>
    <br>
    <br>
    <br>
    <br>
    <br>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Text Field Styling
# -----------------------------

st.markdown("""
<style>

textarea {
    font-size: 18px !important;
    line-height: 1.6 !important;
    padding: 12px !important;
    border-radius: 10px !important;
}

[data-testid="stTextArea"] label {
    font-size: 20px !important;
    font-weight: 600 !important;
    margin-bottom: 6px !important;
}

[data-testid="stTextArea"] textarea {
    border: 1px solid #0e1015;
    border-radius: 10px;
    background-color: #212429;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 4px 12px rgba(255, 255, 255, 0.15);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Text Above Text Field
# -----------------------------

st.markdown("""
<div style='text-align: center; margin-bottom: 20px;'>
    <label for='input-text' style='font-size: 24px; font-weight: 600; color: #ffffff;'>✨ Paste Your Study Material Below ✨</label>
</div>
            """, unsafe_allow_html=True)

# -----------------------------
# Text Field Creation
# -----------------------------

user_input = st.text_area(
    "Input",
    height=200,
    placeholder="Paste textbook content, lecture notes, or academic paragraphs here...",
    label_visibility="collapsed"
)

# -----------------------------
# Demo Mode and Generate Button Setup
# -----------------------------

col1, col2 = st.columns([3, 1])  # adjust ratio if needed

with col1:
    demo_mode = st.checkbox("Use Demo Mode (no API calls)", value=False)

# -----------------------------
# Generate Button CSS
# -----------------------------

st.markdown("""
<style>

.stButton > button {
    background: linear-gradient(135deg, #4f8cff, #7a5cff);
    color: white;
    font-size: 18px;
    font-weight: 600;
    padding: 14px 20px;
    border-radius: 12px;
    border: none;
    box-shadow: 0 4px 14px rgba(79, 140, 255, 0.4);
    transition: all 0.2s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 18px rgba(79, 140, 255, 0.6);
}

.stButton > button:active {
    transform: scale(0.97);
}

.stButton > button:disabled {
    background: #555 !important;
    color: #aaa !important;
    box-shadow: none;
    cursor: not-allowed;
}

</style>
""", unsafe_allow_html=True)

with col2:
    generate_clicked = False

    if isinstance(user_input, str):
        word_count = len(user_input.split())

        if not user_input.strip():
            st.warning("Please enter some text.")
        elif word_count <= 15:
            st.warning("Input is too short. Please provide more content.")
        elif word_count >= 12000:
            st.warning("Input is too long. Please reduce the size.")
        else:
            generate_clicked = st.button("Generate Summaries", use_container_width=True)
    else:
        st.error("Invalid input type.")
        
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
# Generate Button Handler
# -----------------------------

if generate_clicked:
    
    with st.spinner("Generating summaries and evaluating compliance..."):

        try:

            # Demo mode with fake outputs to test UI
            if demo_mode:
                # Fake outputs (no API call)
                baseline = "This is a baseline summary of the provided academic text. It is longer and more complex."

                adhd = """Learning Objectives:
            - Understand the main idea
            - Identify key terms

            Key Concepts:
            - Concept 1 explained simply
            - Concept 2 broken down
            - Concept 3 summarized

            Recall Questions:
            - What is the main idea?
            - Why is this concept important?
            """

                results = {
                    "baseline": {
                        "reading_level": 12,
                        "avg_sentence_length": 22,
                        "avg_paragraph_length": 120,
                        "compliance_score": 40
                    },
                    "adhd": {
                        "reading_level": 7,
                        "avg_sentence_length": 12,
                        "avg_paragraph_length": 60,
                        "compliance_score": 85
                    }
                }
            else:   # Real mode with API calls
                results, baseline, adhd = evaluate_input(user_input)

            if baseline.startswith("ERROR") or adhd.startswith("ERROR"):
                st.error("Failed to generate summaries due to an API issue. Please try again.")
                st.stop()

            tab1, tab2, tab3 = st.tabs(["Summaries", "Compliance", "Charts"])

            # -----------------------------
            # Summary Comparison
            # -----------------------------

            with tab1:
                
                
                # Parse ADHD sections
                sections = {
                    "Learning Objectives": "",
                    "Key Concepts": "",
                    "Recall Questions": ""
                }

                current_section = None

                for line in adhd.split("\n"):
                    line = line.strip()

                    if "Learning Objectives" in line:
                        current_section = "Learning Objectives"
                        continue
                    elif "Key Concepts" in line:
                        current_section = "Key Concepts"
                        continue
                    elif "Recall Questions" in line:
                        current_section = "Recall Questions"
                        continue

                    if current_section and line:
                        sections[current_section] += line + "\n"

                # Expandable sections for ADHD summary
                with st.expander("🎯 Learning Objectives", expanded=True):
                    st.write(sections["Learning Objectives"] or "No content found.")

                with st.expander("🧩 Key Concepts"):
                    st.write(sections["Key Concepts"] or "No content found.")

                with st.expander("❓ Recall Questions"):
                    st.write(sections["Recall Questions"] or "No content found.")

                st.markdown("---")

                # Baseline summary expandble field
                with st.expander("📘 Baseline Summary"):
                    st.info(baseline)

            # -----------------------------
            # Compliance Evaluation
            # -----------------------------

            checker = ComplianceChecker(adhd)
            compliance = checker.run_all_checks()

            score = compliance.get("overall_score", 0)

            with tab2:
                st.subheader("ADHD Compliance Results")

                st.metric(
                    label="Compliance Score",
                    value=f"{score}%"
                )

                st.progress(score / 100)

                if score >= 80:
                    st.success("This summary meets ADHD accessibility standards.")
                else:
                    st.warning("This summary needs improvements to meet ADHD accessibility standards.")

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

            # -----------------------------
            # Rule Breakdown
            # -----------------------------

            with tab3:
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

                base = alt.Chart(chart_data).mark_bar().encode(
                    x=alt.X("Metric:N", title=None, axis=alt.Axis(labelAngle=0, labelLimit=200)),
                    y=alt.Y("Value:Q", title="Words / Grade Level"),
                    xOffset="Version:N",
                    color=alt.Color("Version:N", title="Key")
                )
                
                bars = base.mark_bar(width=40)
                
                text = base.mark_text(
                    dy=-10,
                    fontSize=14,
                    fontWeight="bold",
                ).encode(
                    text=alt.Text("Value:Q", format=".0f")
                )
                
                
                chart = (bars + text).properties(
                    width="container",
                    height=400
                )

                st.altair_chart(chart, use_container_width=True)

                score_df = pd.DataFrame({
                    "Version": ["Baseline", "ADHD"],
                    "Compliance Score": [
                        safe_number(results["baseline"]["compliance_score"]),
                        safe_number(results["adhd"]["compliance_score"])
                    ]
                })

                st.write("### ADHD Compliance Score")
                
                score_chart = alt.Chart(score_df).mark_bar().encode(
                    x=alt.X("Version:N",title=None, axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("Compliance Score:Q")
                ).properties(
                    height=400
                )

                st.altair_chart(score_chart, use_container_width=True)

                st.caption(
                    "Comparison of readability and structural accessibility between standard AI summaries and ADHD-constrained summaries."
                )
            
            
            html_code = f"""
            <div id="scroll-to-me" style='background: cyan; height=1px;'>hi</div>
            <script id="{random.randint(1000, 9999)}">
            var e = document.getElementById("scroll-to-me");
            if (e) {{
                e.scrollIntoView({{behavior: "smooth"}});
                e.remove();
            }}
            </script>
            """
            components.html(html_code)

        except RuntimeError as e:
            st.error(f"API Error: {e}")
        except Exception as e:
            st.error(f"Unexpected Error: {e}")
            traceback.print_exc()

