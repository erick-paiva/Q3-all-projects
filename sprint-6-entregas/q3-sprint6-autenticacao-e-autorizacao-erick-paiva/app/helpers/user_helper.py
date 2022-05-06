
from http import HTTPStatus


def checkKeys(data):
    valid_keys = ['name', 'last_name', 'email', 'password']
    if not data:
        return {"error": "you need to send the keys"}, HTTPStatus.BAD_REQUEST
    for key in list(data):
        if not key in valid_keys:
            return {"error":"you need to send the correct keys"}, HTTPStatus.BAD_REQUEST
    return False
