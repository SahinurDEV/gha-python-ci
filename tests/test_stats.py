from textstats import word_count, top_words, average_word_length


def test_word_count():
    assert word_count("Hello, world! Hello again.") == 4


def test_empty_text():
    assert word_count("") == 0
    assert average_word_length("") == 0.0


def test_top_words():
    assert top_words("a b a c a b", n=2) == [("a", 3), ("b", 2)]


def test_average_word_length():
    assert average_word_length("hi there") == 3.5


def test_case_insensitive():
    assert top_words("Cat cat CAT", n=1) == [("cat", 3)]
