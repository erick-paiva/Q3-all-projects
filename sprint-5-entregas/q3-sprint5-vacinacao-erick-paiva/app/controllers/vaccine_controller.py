from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.vaccine_model import Vacina
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

chaves = ["cpf", "name", "vaccine_name", "health_unit_name"]


def verificar_chaves(data):

    chaves_nao_encontradas = [key for key in data.keys() if key in chaves]

    if chaves_nao_encontradas != chaves:
        return jsonify({"error": "Você deve passar todas as chaves !"}), HTTPStatus.BAD_REQUEST


def tratar_data(data):
    return {chave: data[chave] for chave in chaves if chave in data}


def vericar_valores(data):

    for value in data.values():
        if type(value) == str and len(value) == 0:
            return jsonify({"error": "todos os campos devem ser preenchidos"}), HTTPStatus.BAD_REQUEST
        elif type(value) != str:
            return jsonify({"error": "todos os valores devem ser string"}), HTTPStatus.BAD_REQUEST

    if len(data["cpf"]) != 11:
        return jsonify({"error": "cpf deve ter 11 digitos"}), HTTPStatus.BAD_REQUEST


def adcionar_vacina():
    data = tratar_data(request.get_json())

    chaves_verificadas = verificar_chaves(data)
    if chaves_verificadas:
        return chaves_verificadas

    dados_verificados = vericar_valores(data)

    if dados_verificados:
        return dados_verificados

    try:
        vacina = Vacina(**data)
        current_app.db.session.add(vacina)
        current_app.db.session.commit()
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return jsonify({"error": "cpf ja foi cadastrado"}), HTTPStatus.CONFLICT
        

    return {
        "cpf": vacina.cpf,
        "name": vacina.name,
        "vaccine_name": vacina.vaccine_name,
        "first_shot_date": vacina.first_shot_date,
        "second_shot_date": vacina.second_shot_date,
        "health_unit_name": vacina.health_unit_name,
    }, HTTPStatus.CREATED


def obter_todas_as_vacinas():
    serializer_vacinas = [
        {
            "cpf": vacina.cpf,
            "name": vacina.name,
            "vaccine_name": vacina.vaccine_name,
            "first_shot_date": vacina.first_shot_date,
            "second_shot_date": vacina.second_shot_date,
            "health_unit_name": vacina.health_unit_name,

        } for vacina in Vacina.query.all()
    ]

    return jsonify(serializer_vacinas), HTTPStatus.OK
