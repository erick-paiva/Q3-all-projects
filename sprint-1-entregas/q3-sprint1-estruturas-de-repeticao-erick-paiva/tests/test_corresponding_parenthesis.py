from main import corresponding_parenthesis


def test_corresponding_parenthesis_empty():
    entry_value = [")(", "()", "))((", "(())"]

    for value in entry_value:
        result = corresponding_parenthesis(value)
        expected = ""

        assert (
            result == expected
        ), 'Verifique e se está retornando "" caso todos os parenteses tenham match'


def test_corresponding_parenthesis():
    expected_values = {"())": ")", "(()": "(", "))(": ")", ")((()(((": "(((("}

    for entry, expected in expected_values.items():
        result = corresponding_parenthesis(entry)

        assert (
            result == expected
        ), "Verifique se sua lógica está retornando corretamente"
