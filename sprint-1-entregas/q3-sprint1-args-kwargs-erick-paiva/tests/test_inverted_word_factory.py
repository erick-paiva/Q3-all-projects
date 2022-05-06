from main import inverted_word_factory


def test_inverted_word_factory():
    words = ["eae", "amigão", "belezinha?"]

    result = inverted_word_factory(*words)
    expected = "?ahnizeleb oãgima eae"

    assert (
        result == expected
    ), "Verifique se tanto as letras como a ordem das palavras foram invertidas"
