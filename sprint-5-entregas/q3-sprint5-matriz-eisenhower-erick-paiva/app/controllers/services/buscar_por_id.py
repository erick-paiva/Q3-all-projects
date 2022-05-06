
from flask import current_app, session
from app.models.tasks_model import Tasks
from app.models.tasks_categories_model import Tasks_categories
from app.models.categorie_model import Categories
from app.models.eisenhower_model import Eisenhower
from sqlalchemy.orm import Session, Query


def buscar_tasks_por_id(id: int):
    session: Session = current_app.db.session

    query: Query = (
        session.query(Tasks.id, Tasks.name, Tasks.description,
                      Tasks.duration, Eisenhower.type)
        .select_from(Categories)
        .join(Tasks_categories)
        .join(Tasks)
        .join(Eisenhower)
        .filter(Categories.id == id)
        .all()
    )

    result = [task._asdict() for task in query]

    return result

def buscar_categorias_por_id(id: int):
    session: Session = current_app.db.session

    query: Query = (
        session.query(Categories.name)
        .select_from(Categories)
        .join(Tasks_categories)
        .join(Tasks)
        .join(Eisenhower)
        .filter(Tasks.id == id)
        .all()
    )

    result = [categorie[0] for categorie in query]

    return result
    

def invalid_options(data: dict):

    importace = data["importance"]
    urgency = data["urgency"]
    invalids = {}


    if importace < 1 or importace > 2:
        invalids["importance"]= importace

    if urgency < 1 or urgency > 2:
        invalids["urgency"] =  urgency
        
    if invalids:
        return {
            "msg": {
                "valid_options": {
                    "importance": [1, 2],
                    "urgency": [1, 2]
                },
                "recieved_options": invalids
            }
        }
