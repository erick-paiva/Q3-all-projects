from .answers_snippet import ex1, ex2, ex3, ex4, ex5, ex7, ex8, ex9
from main import (
    spanish_and_brazilian_fruits,
    spanish_and_japan_fruits,
    brazilian_and_japan_fruits,
    popular_spanish_or_brazilian_fruits,
    popular_only_spanish_fruits,
    only_yahoo_emails,
    only_hotmail_emails,
    only_br_emails,
)

from .util import (
    brazilian_fruits,
    spanish_fruits,
    japonese_fruits,
    popular_fruits,
    emails,
)


def test_spanish_and_brazilian_fruits():
    result = spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits)
    expected = ex1
    assert (
        result.sort() == expected.sort()
    ), "A função não está retornando o conjunto das frutas brasileiras e espanholas"


def test_spanish_and_japan_fruits():
    result = spanish_and_japan_fruits(spanish_fruits, japonese_fruits)
    expected = ex2
    assert (
        result.sort() == expected.sort()
    ), "A função não está retornando o conjunto das frutas japonesas e espanholas"


def test_brazilian_and_japan_fruits():
    result = brazilian_and_japan_fruits(brazilian_fruits, japonese_fruits)
    expected = ex3
    assert (
        result.sort() == expected.sort()
    ), "A função não está retornando o conjunto das frutas japonesas e brasileiras"


def test_popular_spanish_or_brazilian_fruits():
    result = popular_spanish_or_brazilian_fruits(
        popular_fruits, spanish_fruits, brazilian_fruits
    )
    expected = ex4
    assert (
        result.sort() == expected.sort()
    ), "A função não está retornando as frutas espanholas ou brasileiras mais populares"


def test_popular_only_spanish_fruits():
    result = popular_only_spanish_fruits(
        popular_fruits, spanish_fruits, japonese_fruits, brazilian_fruits
    )
    expected = ex5
    assert (
        result.sort() == expected.sort()
    ), "A função não está retornando as frutas apenas espanholas que são populares"


def test_only_yahoo_emails():
    result = only_yahoo_emails(emails)
    expected = ex7
    assert isinstance(result, set) == True, "A função deve retornar um conjunto (set)"
    assert (
        result == expected
    ), "A função não está retornando os emails que são do endereço yahoo"


def test_only_hotmail_emails():
    result = only_hotmail_emails(emails)
    expected = ex8
    assert isinstance(result, set) == True, "A função deve retornar um conjunto (set)"
    assert (
        result == expected
    ), "A função não está retornando os emails que são do endereço hotmail"


def test_only_br_emails():
    result = only_br_emails(emails)
    expected = ex9
    assert isinstance(result, set) == True, "A função deve retornar um conjunto (set)"
    assert (
        result == expected
    ), "A função não está retornando os emails que terminam com .br"
