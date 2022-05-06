from main import title_creator


def test_title_creator():
    text = "pense num deserto"

    result = title_creator(text)
    expected = "--------------------Pense Num Deserto--------------------"

    assert (
        result == expected
    ), "Verifique se a quantidade de caracteres especiais é igual a 20 de cada lado"
