from komanda import calculate_tab


def test_calculate_tab_1(table_1):
    table_1, expected = table_1
    result = calculate_tab(table_1)

    assert (
        result == expected
    ), "Verifique se a soma dos valores está sendo feita corretamente"


def test_calculate_tab_2(table_2):
    table_2, expected = table_2
    result = calculate_tab(table_2)

    assert (
        result == expected
    ), "Verifique se a soma dos valores está sendo feita corretamente"
