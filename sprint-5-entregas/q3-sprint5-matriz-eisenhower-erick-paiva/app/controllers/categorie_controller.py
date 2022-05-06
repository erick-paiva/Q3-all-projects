import re
from http import HTTPStatus
from flask import current_app, jsonify, request
from app.controllers.services.buscar_por_id import buscar_tasks_por_id
from app.models.categorie_model import Categories
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query
from app.configs.database import db
from app.models.tasks_categories_model import Tasks_categories


def adicionar_uma_categoria():
    session: Session = current_app.db.session
    data = request.get_json()

    categoria = Categories(**data)

    try:
        session.add(categoria)
        session.commit()
    except IntegrityError as e:
        if re.search("categories_name_key", str(e)):
            return {"msg": "category already exists!"}, HTTPStatus.CONFLICT

    return jsonify(categoria), HTTPStatus.CREATED


def alterar_categoria(id: int):
    data = request.get_json()

    session: Session = db.session

    categorie = session.query(Categories).get(id)

    if not categorie:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(categorie, key, value)

    session.commit()

    return jsonify(categorie), HTTPStatus.OK


def deletar_categoria(id: int):
    session = current_app.db.session
    categorie = session.query(Categories).get(id)
    if not categorie:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND
    session.delete(categorie)
    session.commit()
    return "", HTTPStatus.NO_CONTENT


def listar_categorias():
    session = current_app.db.session

    query: Query = (
        session.query(Categories)
        .select_from(Categories)
        .join(Tasks_categories)
        .filter(Categories.id == Tasks_categories.category_id)
        .all()
    )
    result = [{
        "id": c.id,
        "name": c.name,
        "description": c.description,
        "task": buscar_tasks_por_id(c.id)
    } for c in query]

    return jsonify(result), HTTPStatus.OK
