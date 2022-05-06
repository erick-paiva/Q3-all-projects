from datetime import datetime
from http import HTTPStatus
import re
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from app.models import Leads
from app.configs.database import db
from sqlalchemy.orm.session import Session

chaves_aceitas = ["name", "email", "phone"]

def verificar_numero_telefone(numero_telefone: str):
    padrao = "^\([0-9]{2}\)\s?[1-9]?[\d]{4}-[\d]{4}$"
    passou = re.fullmatch(padrao, numero_telefone)
    if not passou:
        return {"error": "O número de telefone não é válido"}, HTTPStatus.BAD_REQUEST


def verificar_chaves_e_valor(data: dict, chaves: list[str] = chaves_aceitas):
    if len(data.values()) == 0:
        return {"error": "Nenhum dado foi enviado"}, HTTPStatus.BAD_REQUEST
    for chave, value in data.items():
        if not chave in chaves:
            return {'error': f'a chave |{chave}| é inválida'}, HTTPStatus.BAD_REQUEST
        if type(value) != str:
            return {"error": "todos os valores devem ser strigs!"}, HTTPStatus.BAD_REQUEST


def salvar_e_commitar(lead: Leads):
    session: Session = db.session()
    session.add(lead)
    session.commit()


def criar_lead():
    data = request.get_json()
    data["phone"] = data["phone"].replace(" ", "")
    chaves_e_valores_verificados = verificar_chaves_e_valor(data)

    if chaves_e_valores_verificados:
        return chaves_e_valores_verificados

    numero_verificado = verificar_numero_telefone(data["phone"])

    if numero_verificado:
        return numero_verificado

    try:
        lead = Leads(**data)

        salvar_e_commitar(lead)
    except IntegrityError as err:
        if re.search("phone", str(err.orig)):
            return {"error": "Celular ja esta em uso!"}, HTTPStatus.CONFLICT
        if re.search("email", str(err.orig)):
            return {"error": "Email ja esta em uso!"}, HTTPStatus.CONFLICT

    return jsonify(lead), HTTPStatus.OK


def obter_lead():
    session = db.session()
    leads = session.query(Leads).order_by(Leads.visits.desc()).all()
    
    if not leads:
        return {"error": "Nenhum lead encontrado"}, HTTPStatus.NOT_FOUND

    return jsonify(leads), HTTPStatus.OK


def atualizar_lead():
    data = request.get_json()
    chaves_e_valores_verificados = verificar_chaves_e_valor(data, ["email"])


    if chaves_e_valores_verificados:
        return chaves_e_valores_verificados

    session: Session = db.session

    record = session.query(Leads).filter(Leads.email == data["email"]).first()

    if not record:
        return {"error": "email não encontrado"}, HTTPStatus.NOT_FOUND

    setattr(record, "visits", record.visits + 1)
    setattr(record, "last_visit", datetime.utcnow())
    session.commit()

    return jsonify(record), HTTPStatus.OK


def delete_lead():
    data = request.get_json()

    email_verificado = verificar_chaves_e_valor(data, ["email"])
    
    if email_verificado:
        return email_verificado

    session: Session = db.session

    record = session.query(Leads).filter(Leads.email == data["email"]).first()

    if not record:
        return {"error": "email não encontrado"}, HTTPStatus.NOT_FOUND

    session.delete(record)
    session.commit()

    return jsonify(record), HTTPStatus.OK

