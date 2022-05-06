from flask import current_app
from app.models.eisenhower_model import Eisenhower


def criar_lista_eisenhower():
    lista = ["Do It First", "Delegate It", "Schedule It", "Delete It"]

    session = current_app.db.session
    categorias = session.query(Eisenhower).all()

    if not categorias:
        for i in lista:
            eisenhower = Eisenhower(type=i)
            session.add(eisenhower)
        session.commit()

    return lista
