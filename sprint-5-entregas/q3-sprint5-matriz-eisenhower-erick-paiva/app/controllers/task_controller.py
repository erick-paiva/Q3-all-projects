from http import HTTPStatus
import psycopg2
from app.configs.database import db
from app.controllers.eisenhower_controller import criar_lista_eisenhower
from app.controllers.services.buscar_por_id import (buscar_categorias_por_id,
                                                    invalid_options)
from app.controllers.services.criar_categoria_senao_existe import \
    criar_categoria_senao_existe
from app.controllers.services.eisenhower_calculate import calcular_prioridade
from app.exc.exceptions import InvalidOption, InvalidValueTask
from app.models.categorie_model import Categories
from app.models.eisenhower_model import Eisenhower
from app.models.tasks_categories_model import Tasks_categories
from app.models.tasks_model import Tasks
from flask import current_app, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session


def adcionar_task_categoria(data: list[str], task_id: int):
    session: Session = db.session

    for i in data:
        categorie = session.query(Categories).filter_by(name=i).first()
        if categorie:
            tasks_categories = Tasks_categories(
                task_id=task_id, category_id=categorie.id)
            session.add(tasks_categories)
            session.commit()


def adcionar_task():
    criar_lista_eisenhower()
    data = request.get_json()
    options = invalid_options(data)
    if options:
        return options, HTTPStatus.BAD_REQUEST
    try:
        criar_categoria_senao_existe(data["categories"], data["description"])
    except KeyError as error:
        print(error, "x" * 50)
        return {"erro": f"you need to send the key {error}"}, HTTPStatus.BAD_REQUEST
    
    session: Session = db.session
    categories = data.pop("categories")

    id_eisenhower = calcular_prioridade(data["importance"], data["urgency"])
    data.update({"eisenhower_id": id_eisenhower})

    eisenhower = session.query(Eisenhower).get(id_eisenhower).type

    try:
        task = Tasks(**data)
        session.add(task)
        session.commit()
    except InvalidOption as error:
        return error.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            return {"msg": "task already exists!"}, HTTPStatus.CONFLICT
    except InvalidValueTask as error:
        return error.message, HTTPStatus.BAD_REQUEST
    except KeyError as error:
        return error.message, HTTPStatus.BAD_REQUEST
    adcionar_task_categoria(categories, task.id)

    return {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "classification": eisenhower,
        "categories": categories,
    }, HTTPStatus.CREATED


def alterar_task(id: int):
    data = request.get_json()

    session: Session = db.session
    task = session.query(Tasks).get(id)

    if not task:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    if data.get("importance") and data.get("urgency"):
        id_eisenhower = calcular_prioridade(
            data["importance"], data["urgency"])
    elif data.get("importance"):
        id_eisenhower = calcular_prioridade(data["importance"], task.urgency)
    elif data.get("urgency"):
        id_eisenhower = calcular_prioridade(task.importance, data["urgency"])

    if id_eisenhower:
        data["eisenhower_id"] = id_eisenhower
        eisenhower = session.query(Eisenhower).get(id_eisenhower).type
    else:
        eisenhower = session.query(Eisenhower).get(task.eisenhower_id).type

    categories = buscar_categorias_por_id(id)

    try:
        a = Tasks(**data)
        for key, value in data.items():
            setattr(task, key, value)
        session.commit()
    except InvalidValueTask as error:
        return error.message, HTTPStatus.BAD_REQUEST
    except InvalidOption as error:
        return error.message, HTTPStatus.BAD_REQUEST

    return {
        "id": task.id,
        "name": task.name,
        "description": task.description,
        "duration": task.duration,
        "classification": eisenhower,
        "categories": categories,
    }, HTTPStatus.OK


def deletar_task(id: int):
    session = current_app.db.session
    task = session.query(Tasks).get(id)
    if not task:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND
    session.delete(task)
    session.commit()
    return "", HTTPStatus.NO_CONTENT
