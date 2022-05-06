from main import remove_more_than_two_repetitions


def test_remove_more_than_two_repetitions():
    entry_value = "aaaabbbbaacaaaxxxxii"

    result = remove_more_than_two_repetitions(entry_value)
    expected = "aabbaacaaxxii"

    assert result == expected, "Verifique se sua lógica está correta"
