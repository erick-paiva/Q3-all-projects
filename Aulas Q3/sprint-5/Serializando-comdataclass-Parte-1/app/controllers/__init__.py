from http import HTTPStatus
from flask import request, jsonify, current_app
from app.models.cachorro_model import Cachorro

  


def create_dog():
    data = request.get_json()
    
    new_dog = Cachorro(**data)

    current_app.db.session.add(new_dog)
    current_app.db.session.commit()
    
    return jsonify(new_dog), HTTPStatus.OK
