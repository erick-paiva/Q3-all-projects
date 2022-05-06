from http import HTTPStatus


def return_world():
    return {"data": "world"}, HTTPStatus.OK
