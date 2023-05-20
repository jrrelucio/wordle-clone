from wordleclone.app import valid_word


def test_Alice():
    """If the word provided is a valid 5-letter word"""

    assert valid_word("Alice") == "Alice"


def test_empty():
    """If a word is not provided, a generic valid_word is provided"""

    assert valid_word("") == "Not a valid word"

def test_fours():
    """If the name is Brutus, a special valid_word is provided"""

    assert valid_word("four") == "Not a valid word"