from http import HTTPStatus
from flask import request, current_app, jsonify
from app.models.regiao_model import RegiaoModel


def create_regiao():
    
    session = current_app.db.session
    
    data = request.get_json()
    
    regiao = RegiaoModel(**data)
    
    session.add(regiao)
    session.commit()
    
    
    return jsonify({
            "id": regiao.id,
            "nome": regiao.nome,
            "numero_estados": regiao.numero_estados
        }), HTTPStatus.OK
