from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.aluno_model import AlunoModel
    from app.models.aula_model import AulaModel
    from app.models.alunos_aulas_table import alunos_aulas
