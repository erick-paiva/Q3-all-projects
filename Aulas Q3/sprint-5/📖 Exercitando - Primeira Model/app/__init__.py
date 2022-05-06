from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://erick:8844@localhost:5432/ExercitandoPrimeiraModel"

    # from models import Music
    from app.model import Music

    db.init_app(app)
    db.create_all(app=app)

    return app