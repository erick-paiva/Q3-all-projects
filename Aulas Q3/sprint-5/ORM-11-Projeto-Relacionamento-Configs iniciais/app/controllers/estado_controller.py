from http import HTTPStatus
from flask import request, current_app, jsonify
from app.models.regiao_model import RegiaoModel
from app.models.estado_model import EstadoModel
from app.models.bacia_hidro_model import BaciaHidroModel

def create_estado():

    session = current_app.db.session

    data = request.get_json()

    nome_regiao = data.pop('regiao')

    regiao = RegiaoModel.query.filter_by(nome=nome_regiao).first()

    data['regiao_id'] = regiao.id
    
    nome_bacia = data.pop("bacia")
    bacia = BaciaHidroModel.query.filter_by(nome=nome_bacia).first()
    estado = EstadoModel(**data)
    estado.bacias.append(bacia)

    session.add(estado)
    session.commit()

    return jsonify({
        "id": estado.id,
        "nome": estado.nome,
        "sigla": estado.sigla,
        "populacao": estado.populacaom,
        "area": float(estado.area),
        "regiao": estado.regiao.nome,
        "bacia": estado.bacias
    }), HTTPStatus.OK
