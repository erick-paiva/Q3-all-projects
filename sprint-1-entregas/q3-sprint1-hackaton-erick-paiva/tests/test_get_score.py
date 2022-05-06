from .hackatons import hackatons
from hackaton import get_score


def test_get_score_1():
    expected = "A Team Kenzie ficou classificada em 1"
    result = get_score("Team Kenzie", hackatons["hackaton_1"])

    assert type(result) is str, "Verifique se o tipo retornado é uma string"
    assert (
        result == expected
    ), "Verifique se sua função está retornando exatamente a string pedida"


def test_get_score_2():
    expected = "A Team VHSYS ficou classificada em 3"
    result = get_score("Team VHSYS", hackatons["hackaton_2"])

    assert type(result) is str, "Verifique se o tipo retornado é uma string"
    assert (
        result == expected
    ), "Verifique se sua função está retornando exatamente a string pedida"


def test_get_score_3():
    expected = "A Team Mirum ficou classificada em 1"
    result = get_score("Team Mirum", hackatons["hackaton_3"])

    assert type(result) is str, "Verifique se o tipo retornado é uma string"
    assert (
        result == expected
    ), "Verifique se sua função está retornando exatamente a string pedida"


def test_get_score_4():
    expected = "A Team Ateliware ficou classificada em 1"
    result = get_score("Team Ateliware", hackatons["hackaton_2"])

    assert type(result) is str, "Verifique se o tipo retornado é uma string"
    assert (
        result == expected
    ), "Verifique se sua função está retornando exatamente a string pedida"
