import pytest
from werkzeug.exceptions import NotFound

from rotas_basicas.app import app


def test_verify_if_route_home_was_defined():
    try:
        app.url_map.bind("").match("/")
    except NotFound:
        pytest.fail("Verifique se voce definiu a rota `/`", pytrace=False)


def test_home_return_type_is_dict():
    with app.test_client() as client:
        response_data = client.get("/").json

        assert (
            type(response_data) is dict
        ), "Verifique se o tipo do retorno de `/` é dict"


def test_home_return_status_code_is_200():
    with app.test_client() as client:
        status_code = client.get("/").status_code
        expected = 200

        assert (
            status_code == expected
        ), "Verifique se o status code retornado de `/` é 200"


def test_home_return_correct_data():
    with app.test_client() as client:
        response = client.get("/")
        expected = {"data": "Hello Flask!"}

        assert response.json == expected, "Verifique o retorno de `/`"
