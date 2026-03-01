import unittest
from src.compliance_checker import ComplianceChecker


class TestADHDCompliance(unittest.TestCase):

    def setUp(self):
        """Setup common test data."""

        # A "Good" text that should pass all rules
        self.good_text = (
            "## Learning Objectives\n"
            "- Understand the basics of gravity.\n"
            "- Calculate force using mass and acceleration.\n\n"

            "## Key Concepts\n"
            "- Gravity pulls objects together.\n"
            "- It depends on mass.\n\n"

            "The formula for force is simple.\n"
            "F = m * a\n\n"

            "## Recall Questions\n"
            "1. What is gravity?\n"
            "2. How does mass affect force?\n"
        )

        # A "Bad" text that violates multiple rules
        self.bad_text = (
            "This is a massive block of text that goes on and on without any breaks or bullets "
            "which makes it extremely difficult for someone with ADHD to follow because the sentence "
            "structure is convoluted and the vocabulary is unnecessarily complex like obfuscation "
            "and recalcitrant essentially creating a cognitive wall and continuing further to ensure "
            "that we exceed the eighty word paragraph limit that was defined in the compliance "
            "specification for the purposes of testing paragraph density rules and ensuring that "
            "this paragraph clearly surpasses the maximum word count threshold set by the system.\n\n"
            "Another paragraph with F = m * a embedded inside a sentence causing split attention."
        )

        # Bad spacing example (no blank lines before headers)
        self.bad_spacing_text = (
            "## Learning Objectives\n"
            "- Understand gravity.\n"
            "## Key Concepts\n"
            "- Gravity pulls objects.\n"
            "## Recall Questions\n"
            "What is gravity?\n"
        )

    # ----------------------------
    # Core Rule Tests
    # ----------------------------

    def test_sentence_length_compliance(self):
        checker_good = ComplianceChecker(self.good_text)
        checker_bad = ComplianceChecker(self.bad_text)

        checker_good.check_sentence_length()
        self.assertEqual(checker_good.results['sentence_length']['status'], 'pass')

        checker_bad.check_sentence_length()
        self.assertEqual(checker_bad.results['sentence_length']['status'], 'fail')

    def test_paragraph_length_failure(self):
        checker = ComplianceChecker(self.bad_text)
        checker.check_paragraph_length()

        self.assertEqual(
            checker.results["paragraph_length"]["status"],
            "fail"
        )

    def test_reading_level_compliance(self):
        checker_good = ComplianceChecker(self.good_text)
        checker_good.check_reading_level()

        self.assertEqual(
            checker_good.results['reading_level']['status'],
            'pass'
        )

    def test_required_sections(self):
        checker = ComplianceChecker(self.good_text)
        checker.check_required_sections()

        self.assertEqual(
            checker.results["required_sections"]["status"],
            "pass"
        )

    def test_bullet_format(self):
        checker = ComplianceChecker(self.good_text)
        checker.check_bullet_format()

        self.assertEqual(
            checker.results["bullet_format"]["status"],
            "pass"
        )

    def test_recall_questions(self):
        checker = ComplianceChecker(self.good_text)
        checker.check_recall_questions()

        self.assertEqual(
            checker.results["recall_questions"]["status"],
            "pass"
        )



    def test_formula_separation_rule(self):
        checker_good = ComplianceChecker(self.good_text)
        checker_bad = ComplianceChecker(self.bad_text)

        checker_good.check_formula_separation()
        self.assertEqual(
            checker_good.results["formula_separation"]["status"],
            "pass"
        )

        checker_bad.check_formula_separation()
        self.assertEqual(
            checker_bad.results["formula_separation"]["status"],
            "fail"
        )

    def test_section_spacing_rule(self):
        checker_good = ComplianceChecker(self.good_text)
        checker_bad = ComplianceChecker(self.bad_spacing_text)

        checker_good.check_section_spacing()
        self.assertEqual(
            checker_good.results["section_spacing"]["status"],
            "pass"
        )

        checker_bad.check_section_spacing()
        self.assertEqual(
            checker_bad.results["section_spacing"]["status"],
            "fail"
        )


    def test_full_compliance_pass(self):
        checker = ComplianceChecker(self.good_text)
        results = checker.run_all_checks()

        self.assertTrue(results["adhd_compliant"])
        self.assertGreaterEqual(results["overall_score"], 80)

    def test_full_compliance_fail(self):
        checker = ComplianceChecker(self.bad_text)
        results = checker.run_all_checks()

        self.assertFalse(results["adhd_compliant"])


if __name__ == '__main__':
    unittest.main()
