from main import dictionary_separator


def test_dictionary_separator():
    user = {"name": "Naruto", "age": 16, "favorite word": "Ichiraku Ramen"}

    result = dictionary_separator(**user)
    expected = (["name", "age", "favorite word"], ["Naruto", 16, "Ichiraku Ramen"])

    assert type(result) is tuple, "Verifique se está retornando uma tupla"
    assert (
        result == expected
    ), "Verifique se está retornando corretamente as chaves e valores"
