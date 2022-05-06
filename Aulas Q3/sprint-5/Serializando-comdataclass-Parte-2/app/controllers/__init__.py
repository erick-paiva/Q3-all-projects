from http import HTTPStatus
from flask import request, jsonify, current_app
from app.models.cachorro_model import Cachorro
from app.models.dono_model import DonoModel
  


def create_dog():
    data = request.get_json()
    
    new_dog = Cachorro(**data)

    current_app.db.session.add(new_dog)
    current_app.db.session.commit()
    
    return jsonify(new_dog), HTTPStatus.OK

def create_dono():
    data = request.get_json()
    
    novo_dono = DonoModel(**data)
    
    current_app.db.session.add(novo_dono)
    current_app.db.session.commit()
    
    return jsonify(novo_dono), HTTPStatus.OK
    