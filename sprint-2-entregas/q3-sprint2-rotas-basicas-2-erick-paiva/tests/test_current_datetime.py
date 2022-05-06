import pytest
from werkzeug.exceptions import NotFound

from rotas_basicas.app import app
from .helper import unprocessed_data


def test_verify_if_route_current_datetime_was_defined():
    try:
        app.url_map.bind("").match("/current_datetime")
    except NotFound:
        pytest.fail(
            "Verifique se voce definiu a rota `/current_datetime`", pytrace=False
        )


def test_current_datetime_return_type_is_dict():
    with app.test_client() as client:
        response_data = client.get("/current_datetime").json

        assert (
            type(response_data) is dict
        ), "Verifique se o tipo do retorno de `/current_datetime` é dict"


def test_current_datetime_return_status_code_is_200():
    with app.test_client() as client:
        status_code = client.get("/current_datetime").status_code
        expected = 200

        assert (
            status_code == expected
        ), "Verifique se o status code retornado de `/` é 200"


def test_current_datetime_return_correct_data():
    with app.test_client() as client:
        response = client.get("/current_datetime")
        date, time, msg = unprocessed_data()

        expected = {"current_datetime": date + " " + time, "message": msg}

        assert response.json == expected, "Verifique o retorno de `/current_datetime`"
