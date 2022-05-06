from main import standardize_title


def test_standardize_title():
    title = "cinco quartos de laranja"

    result = standardize_title(title)
    expected = "Cinco Quartos De Laranja"

    assert (
        result == expected
    ), "Verifique a string está sendo formatada em Title corretamente"
