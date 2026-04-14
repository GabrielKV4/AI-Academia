import re
from collections import Counter


COMMON_ENGLISH_WORDS = {
    "the", "and", "is", "are", "was", "were", "to", "of", "in", "for", "on",
    "with", "as", "by", "an", "be", "this", "that", "from", "it", "or", "at",
    "which", "you", "can", "has", "have", "not", "used", "using", "into",
    "their", "more", "also", "than", "such", "these", "between", "data",
    "system", "software", "text", "study", "learning", "summary", "concept",
    "question", "material", "information"
}


def extract_words(text):
    if not isinstance(text, str):
        return []
    return re.findall(r"[A-Za-z']+", text.lower())


def repeated_char_ratio(text):
    if not text:
        return 0.0
    repeated = re.findall(r"(.)\1{3,}", text.lower())
    return len(repeated) / max(len(text), 1)


def consonant_run_count(words):
    count = 0
    for word in words:
        if re.search(r"[bcdfghjklmnpqrstvwxyz]{6,}", word):
            count += 1
    return count


def vowel_ratio(words):
    joined = "".join(words)
    if not joined:
        return 0.0
    vowels = sum(1 for ch in joined if ch in "aeiou")
    return vowels / len(joined)


def english_word_hit_ratio(words):
    if not words:
        return 0.0
    hits = sum(1 for w in words if w in COMMON_ENGLISH_WORDS)
    return hits / len(words)


def alpha_character_ratio(text):
    if not text:
        return 0.0
    alpha = sum(1 for ch in text if ch.isalpha())
    visible = sum(1 for ch in text if not ch.isspace())
    return alpha / max(visible, 1)


def unique_word_ratio(words):
    if not words:
        return 0.0
    return len(set(words)) / len(words)


def is_probably_gibberish(text):
    words = extract_words(text)

    if len(words) < 8:
        return True, "Please enter more readable English study material."

    avg_word_len = sum(len(w) for w in words) / len(words)
    vowel_pct = vowel_ratio(words)
    common_word_pct = english_word_hit_ratio(words)
    consonant_runs = consonant_run_count(words)
    alpha_ratio = alpha_character_ratio(text)
    repeat_ratio = repeated_char_ratio(text)
    unique_ratio = unique_word_ratio(words)

    # Can check for keyboard mashing and gibberish
    gibberish_flags = 0

    if avg_word_len > 12:
        gibberish_flags += 1
    if vowel_pct < 0.20:
        gibberish_flags += 1
    if common_word_pct < 0.05:
        gibberish_flags += 1
    if consonant_runs >= 3:
        gibberish_flags += 1
    if alpha_ratio < 0.55:
        gibberish_flags += 1
    if repeat_ratio > 0.01:
        gibberish_flags += 1
    if unique_ratio > 0.95 and len(words) > 20:
        gibberish_flags += 1

    if gibberish_flags >= 3:
        return True, "The input looks unreadable or gibberish. Please enter clear English study material."

    return False, None


def is_probably_english(text):
    words = extract_words(text)

    if len(words) < 8:
        return False, "Please enter more English text so the system can evaluate it reliably."

    common_word_pct = english_word_hit_ratio(words)
    vowel_pct = vowel_ratio(words)


    if common_word_pct >= 0.08 and vowel_pct >= 0.22:
        return True, None

    return False, "Only English study material is supported right now. Please paste English text."


def validate_input_text(text):
    if not isinstance(text, str) or not text.strip():
        return False, "Input cannot be empty."

    gibberish, gibberish_msg = is_probably_gibberish(text)
    if gibberish:
        return False, gibberish_msg

    english, english_msg = is_probably_english(text)
    if not english:
        return False, english_msg

    return True, None