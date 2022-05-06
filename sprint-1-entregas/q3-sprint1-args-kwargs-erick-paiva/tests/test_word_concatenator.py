from main import word_concatenator


def test_word_concatenator():
    words = ["Tá", "pegando", "fogo", "bicho!!!"]

    result = word_concatenator(*words)
    expected = "Tá pegando fogo bicho!!!"

    assert (
        result == expected
    ), "Verifique se as palavras estão sendo corretamente concatenadas"
