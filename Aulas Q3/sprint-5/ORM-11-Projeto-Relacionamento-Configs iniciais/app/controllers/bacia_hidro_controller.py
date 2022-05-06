from http import HTTPStatus
from flask import request, current_app, jsonify
from app.models.bacia_hidro_model import BaciaHidroModel

def create_bacia_hidro():
    
    session = current_app.db.session
    
    data = request.get_json()
    
    bacia = BaciaHidroModel(**data)
    
    session.add(bacia)
    session.commit()
    
    return jsonify({
        "id": bacia.id,
        "nome": bacia.nome,
        "area": bacia.area
    }), HTTPStatus.OK