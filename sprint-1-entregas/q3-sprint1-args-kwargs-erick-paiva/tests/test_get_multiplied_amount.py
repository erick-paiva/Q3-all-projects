from main import get_multiplied_amount


def test_get_multiplied_amount():
    numbers = [1, 2, 3]
    multiplier = 2

    result = get_multiplied_amount(multiplier, *numbers)
    expected = 12

    assert (
        result == expected
    ), "Verifique se a multiplicação da soma está sendo feita corretamente"


def test_get_multiplied_amount_per_zero():
    numbers = [1, 2, 3]
    multiplier = 0

    result = get_multiplied_amount(multiplier, *numbers)
    expected = 0

    assert (
        result == expected
    ), "Verifique se a multiplicação da soma está sendo feita corretamente"
