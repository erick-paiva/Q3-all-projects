from main import standardize_text


def test_standardize_text_upper_first_letter_a():
    text = "a famosa atriz Constance"

    result = standardize_text(text)
    expected = "A famosa atriz Constance"

    assert result == expected, "Verifique se a primeira letra do texto é maiuscula"
