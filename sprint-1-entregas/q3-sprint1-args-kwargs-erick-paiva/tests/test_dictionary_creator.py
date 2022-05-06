from main import dictionary_creator


def test_dictionary_creator():
    change_keys = ["username", "password", "address"]
    user = {"name": "Williams", "key": "1234"}

    result = dictionary_creator(*change_keys, **user)
    expected = {"username": "Williams", "password": "1234"}

    assert (
        result == expected
    ), "Verififque se o dicionário está sendo atualizado corretamente"


def test_dictionary_creator_none():
    change_keys = ["username"]
    user = {"name": "Williams", "key": "1234"}

    result = dictionary_creator(*change_keys, **user)

    assert (
        result is None
    ), "Verififque se está retornando None caso args seja menor que kwargs"
