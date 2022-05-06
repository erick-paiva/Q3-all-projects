from http import HTTPStatus
from flask import request, current_app, jsonify
from app.models.capital_model import CapitalModel
from app.models.estado_model import EstadoModel

def create_capital():
    
    session = current_app.db.session
    
    data = request.get_json()
    
    nome_estado = data.pop("estado")
    
    estado = EstadoModel.query.filter_br(nome=nome_estado).first()
    
    data["estados_id"] = estado.id
    
    capital = CapitalModel(**data)
    
    session.add(capital)
    session.commit()
    
    return jsonify({
        "id": capital.id,
        "nome": capital.nome,
        "bairros": capital.bairros,
        "populacao": capital.populacao,
        "estado_nome": capital.estado.nome
    }), HTTPStatus.OK
    

