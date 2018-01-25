from reverse_sentence import reverse_sentence


# Basic Tests
def test_reverse_sentence_with_two_words():
    test_string = "hello, world"

    assert reverse_sentence(test_string) == "world hello,"


def test_reverse_sentence_with_three_words():
    test_string = "Yoda is awesome!"

    assert reverse_sentence(test_string) == "awesome! is Yoda"


def test_reverse_sentence_with_multiple_words():
    test_string = "I'm a better engineer today than I was yesterday."

    expected = "yesterday. was I than today engineer better a I'm"
    assert reverse_sentence(test_string) == expected


def test_reverse_sentence_returns_unmodified_with_one_word():
    test_string = "world"

    assert reverse_sentence(test_string) == "world"


# Edge Cases
def test_reverse_sentence_returns_unmodified_with_empty_string_input():
    test_string = ""

    assert reverse_sentence(test_string) == ""


def test_reverse_sentence_returns_unmodified_with_None_input():
    test_string = None

    assert reverse_sentence(test_string) is None


def test_reverse_sentence_with_multiple_spaces_between_words():
    test_string = "How  do  you   like     them      apples?"

    expected = "apples?      them     like   you  do  How"
    assert reverse_sentence(test_string) == expected


def test_reverse_sentence_maintains_leading_and_trailing_whitespace():
    test_string = "  I can do this!     "

    assert reverse_sentence(test_string) == "     this! do can I  "
