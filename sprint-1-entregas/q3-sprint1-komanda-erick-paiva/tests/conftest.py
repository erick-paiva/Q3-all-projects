from pytest import fixture


@fixture
def table_1():
    table_1 = [{"id": 1, "amount": 5}, {"id": 19, "amount": 5}]
    expected = 55.0

    return table_1, expected


@fixture
def table_2():
    table_2 = [
        {"id": 10, "amount": 3},
        {"id": 20, "amount": 2},
        {"id": 21, "amount": 5},
    ]
    expected = 65

    return table_2, expected
