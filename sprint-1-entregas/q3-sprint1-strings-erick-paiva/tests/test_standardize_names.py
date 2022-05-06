from main import standardize_names


def test_standardize_names_blank_spaces():
    name_blank_spaces = "  Batman     "

    result = standardize_names(name_blank_spaces)
    expected = "Batman"

    assert result == expected, "Encontrado espaços em branco no inicio ou fim da string"


def test_standardize_hyphen():
    name = "Super Homem"
    result = standardize_names(name)
    expected = "Super-Homem"

    assert result == expected, "Possivel hifen no lugar errado"
