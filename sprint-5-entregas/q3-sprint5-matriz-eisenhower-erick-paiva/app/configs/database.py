from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app: Flask):
    
    db.init_app(app)
    
    app.db = db
    
    from app.models.tasks_model import Tasks
    from app.models.categorie_model import Categories
    from app.models.eisenhower_model import Eisenhower
    from app.models.tasks_categories_model import Tasks_categories
    