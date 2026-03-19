import textstat
import re


class ComplianceChecker:
    def __init__(self, text):
        self.text = text
        self.results = {}
        self.total_rules = 0
        self.passed_rules = 0

    def _record_result(self, rule_name, passed, details=None):
        self.total_rules += 1
        if passed:
            self.passed_rules += 1

        self.results[rule_name] = {
            "status": "pass" if passed else "fail",
            "details": details
        }

    # Rule 1: Max 20 words per sentence
    def check_sentence_length(self, max_words=20):
        sentences = [s.strip() for s in re.split(r'[.!?]', self.text) if s.strip()]
        long_sentences = [s for s in sentences if len(s.split()) > max_words]

        passed = len(long_sentences) == 0
        self._record_result(
            "sentence_length",
            passed,
            {"long_sentence_count": len(long_sentences)}
        )

    # Rule 2: Max 80 words per paragraph
    def check_paragraph_length(self, max_words=80):
        paragraphs = [p.strip() for p in self.text.split('\n\n') if p.strip()]
        violations = sum(1 for p in paragraphs if len(p.split()) > max_words)

        passed = violations == 0
        self._record_result(
            "paragraph_length",
            passed,
            {"violating_paragraphs": violations}
        )

    # Rule 3: Required Headers
    def check_required_sections(self):
        required = [
            "## Learning Objectives",
            "## Key Concepts",
            "## Recall Questions"
        ]

        missing = [h for h in required if h not in self.text]
        passed = len(missing) == 0

        self._record_result(
            "required_sections",
            passed,
            {"missing_sections": missing}
        )

    # Rule 4: Bullet formatting in Key Concepts
    def check_bullet_format(self):
        key_section_match = re.search(
            r'## Key Concepts(.*?)(##|\Z)',
            self.text,
            re.DOTALL
        )

        if not key_section_match:
            self._record_result(
                "bullet_format",
                False,
                {"reason": "Key Concepts section missing"}
            )
            return

        section_text = key_section_match.group(1)
        bullets = re.findall(r'^\s*[-*]\s+', section_text, re.MULTILINE)

        passed = len(bullets) > 0
        self._record_result(
            "bullet_format",
            passed,
            {"bullet_count": len(bullets)}
        )

    # Rule 5: At least 2 recall questions
    def check_recall_questions(self, min_questions=2):
        questions = re.findall(r'.*\?', self.text)
        passed = len(questions) >= min_questions

        self._record_result(
            "recall_questions",
            passed,
            {"question_count": len(questions)}
        )

    # Rule 6: Reading level ≤ Grade 8
    def check_reading_level(self, max_grade=8.0):
        grade = textstat.flesch_kincaid_grade(self.text)
        passed = grade <= max_grade

        self._record_result(
            "reading_level",
            passed,
            {"grade_level": grade}
        )

    # Rule 7: Formula Separation Rule
    def check_formula_separation(self):
        lines = self.text.split('\n')
        formula_pattern = re.compile(r'[a-zA-Z0-9]+\s*=\s*[a-zA-Z0-9]+')

        violations = 0

        for line in lines:
            if formula_pattern.search(line):
                stripped = line.strip()
                if not re.fullmatch(r'[a-zA-Z0-9\s=\+\-\*/\^\(\)\.]+', stripped) or len(stripped.split()) > 5:
                    violations += 1

        passed = violations == 0
        self._record_result(
            "formula_separation",
            passed,
            {"violations": violations}
        )

    # Rule 8: Section Spacing Rule
    def check_section_spacing(self):
        headers = re.findall(r'## .*', self.text)
        violations = 0

        for header in headers[1:]:
            index = self.text.find(header)
            if index > 0 and not self.text[index - 2:index] == '\n\n':
                violations += 1

        passed = violations == 0
        self._record_result(
            "section_spacing",
            passed,
            {"spacing_violations": violations}
        )

    # Rule 9: Minimum 3 Key Concept bullets
    def check_min_key_bullets(self, min_bullets=3):
        key_section_match = re.search(
            r'## Key Concepts(.*?)(##|\Z)',
            self.text,
            re.DOTALL
        )

        if not key_section_match:
            self._record_result(
                "min_key_bullets",
                False,
                {"reason": "Key Concepts section missing"}
            )
            return

        section_text = key_section_match.group(1)
        bullets = re.findall(r'^\s*[-*]\s+', section_text, re.MULTILINE)

        passed = len(bullets) >= min_bullets
        self._record_result(
            "min_key_bullets",
            passed,
            {"bullet_count": len(bullets)}
        )

    # Rule 10: Maximum 6 Key Concept bullets
    def check_max_key_bullets(self, max_bullets=6):
        key_section_match = re.search(
            r'## Key Concepts(.*?)(##|\Z)',
            self.text,
            re.DOTALL
        )

        if not key_section_match:
            self._record_result(
                "max_key_bullets",
                False,
                {"reason": "Key Concepts section missing"}
            )
            return

        section_text = key_section_match.group(1)
        bullets = re.findall(r'^\s*[-*]\s+', section_text, re.MULTILINE)

        passed = len(bullets) <= max_bullets
        self._record_result(
            "max_key_bullets",
            passed,
            {"bullet_count": len(bullets)}
        )

    def compute_score(self):
        score = (self.passed_rules / self.total_rules) * 100
        self.results["overall_score"] = round(score, 2)
        self.results["adhd_compliant"] = score >= 80

    def run_all_checks(self):
        self.results = {}
        self.total_rules = 0
        self.passed_rules = 0

        self.check_sentence_length()
        self.check_paragraph_length()
        self.check_required_sections()
        self.check_bullet_format()
        self.check_recall_questions()
        self.check_reading_level()
        self.check_formula_separation()
        self.check_section_spacing()
        self.check_min_key_bullets()
        self.check_max_key_bullets()

        self.compute_score()
        return self.results

def max_sentence_length(text):
    sentences = re.split(r'[.!?]', text)
    max_len = 0

    for s in sentences:
        words = s.strip().split()
        if len(words) > max_len:
            max_len = len(words)

    return max_len


def max_paragraph_length(text):
    paragraphs = text.split("\n")
    max_len = 0

    for p in paragraphs:
        words = p.strip().split()
        if len(words) > max_len:
            max_len = len(words)

    return max_len


def check_compliance(summary):

    results = {}

    text = summary

    results["Max sentence length ≤ 20"] = max_sentence_length(text) <= 20
    results["Max paragraph length ≤ 80"] = max_paragraph_length(text) <= 80
    results["Has Learning Objectives"] = "Learning Objectives" in text
    results["Has Key Concepts"] = "Key Concepts" in text
    results["Has Recall Questions"] = "Recall Questions" in text

    return results