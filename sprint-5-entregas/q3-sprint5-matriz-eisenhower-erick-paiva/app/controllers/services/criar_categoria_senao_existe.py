from app.models.categorie_model import Categories
from sqlalchemy.orm.session import Session
from app.configs.database import db


def criar_categoria_senao_existe(categories: list[str], description: str):
    session: Session = db.session
    for i in categories:
        categorie = session.query(Categories).filter_by(name=i).first()
        if not categorie:
            categorie = Categories(name=i, description=description)
            session.add(categorie)
            session.commit()
