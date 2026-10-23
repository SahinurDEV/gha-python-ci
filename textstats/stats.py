import re
from collections import Counter

_WORD = re.compile(r"[a-z']+")


def words(text):
    return _WORD.findall(text.lower())


def word_count(text):
    return len(words(text))


def top_words(text, n=3):
    return Counter(words(text)).most_common(n)


def average_word_length(text):
    w = words(text)
    if not w:
        return 0.0
    return round(sum(len(x) for x in w) / len(w), 2)
