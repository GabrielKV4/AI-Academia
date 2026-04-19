import pytest
from src.compliance_checker import ComplianceChecker



def run_checks(summary: str):
    checker = ComplianceChecker(summary)
    return checker.run_all_checks()



def test_long_sentence_fails_sentence_length():
    summary = (
        "## Learning Objectives\n"
        "- Understand cell respiration in detail.\n\n"
        "## Key Concepts\n"
        "- Cells use glucose to make ATP energy for life.\n"
        "- Oxygen helps release energy from glucose in stages.\n"
        "- Mitochondria support this process in most eukaryotic cells.\n\n"
        "## Recall Questions\n"
        "How do cells make energy when oxygen is available through a long process involving many linked reactions and transport steps?\n"
        "What role do mitochondria play?\n"
    )

    results = run_checks(summary)

    assert results["sentence_length"]["status"] == "fail"



def test_paragraph_overflow_fails_paragraph_length():
    long_paragraph = " ".join(["Energy moves through ecosystems in predictable ways."] * 12)
    summary = (
        "## Learning Objectives\n"
        f"{long_paragraph}\n\n"
        "## Key Concepts\n"
        "- Producers capture sunlight.\n"
        "- Consumers eat producers or other consumers.\n"
        "- Energy decreases at each trophic level.\n\n"
        "## Recall Questions\n"
        "What do producers do?\n"
        "Why does energy decrease?\n"
    )

    results = run_checks(summary)

    assert results["paragraph_length"]["status"] == "fail"



def test_too_few_bullets_fails_min_key_bullets():
    summary = (
        "## Learning Objectives\n"
        "- Describe the water cycle.\n\n"
        "## Key Concepts\n"
        "- Water evaporates and later condenses.\n"
        "- Precipitation returns water to Earth.\n\n"
        "## Recall Questions\n"
        "What is evaporation?\n"
        "What is precipitation?\n"
    )

    results = run_checks(summary)

    assert results["bullet_format"]["status"] == "pass"
    assert results["min_key_bullets"]["status"] == "fail"



def test_too_many_bullets_fails_max_key_bullets():
    summary = (
        "## Learning Objectives\n"
        "- Explain the parts of an atom.\n\n"
        "## Key Concepts\n"
        "- Protons have a positive charge.\n"
        "- Neutrons have no charge.\n"
        "- Electrons have a negative charge.\n"
        "- The nucleus holds protons and neutrons.\n"
        "- Electrons move around the nucleus.\n"
        "- Atomic number counts protons.\n"
        "- Isotopes have different neutron counts.\n\n"
        "## Recall Questions\n"
        "What charge does an electron have?\n"
        "What does atomic number count?\n"
    )

    results = run_checks(summary)

    assert results["bullet_format"]["status"] == "pass"
    assert results["max_key_bullets"]["status"] == "fail"



def test_inline_formula_fails_formula_separation():
    summary = (
        "## Learning Objectives\n"
        "- Use the force equation.\n\n"
        "## Key Concepts\n"
        "- Force depends on mass and acceleration.\n"
        "- Greater mass can increase force.\n"
        "- Greater acceleration can increase force.\n\n"
        "The main equation F = m * a helps explain motion in simple cases.\n\n"
        "## Recall Questions\n"
        "What does F mean?\n"
        "What happens when acceleration increases?\n"
    )

    results = run_checks(summary)

    assert results["formula_separation"]["status"] == "fail"



def test_missing_blank_lines_fails_section_spacing():
    summary = (
        "## Learning Objectives\n"
        "- Describe photosynthesis.\n"
        "## Key Concepts\n"
        "- Plants use sunlight to make food.\n"
        "- Chlorophyll captures light energy.\n"
        "- Oxygen is released as a product.\n"
        "## Recall Questions\n"
        "What captures light energy?\n"
        "What gas is released?\n"
    )

    results = run_checks(summary)

    assert results["section_spacing"]["status"] == "fail"