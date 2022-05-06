from main import sum_numbers


def test_sum_numbers():
    numbers = [1, 2, 3, 4, 5, 6]

    result = sum_numbers(*numbers)
    expected = 21

    assert (
        result == expected
    ), "Verifique se a soma dos args está sendo feita corretamente"


def test_sum_numbers_one_number():
    numbers = [220]

    result = sum_numbers(*numbers)
    expected = 220

    assert (
        result == expected
    ), "Verifique se a soma dos args está sendo feita corretamente"
