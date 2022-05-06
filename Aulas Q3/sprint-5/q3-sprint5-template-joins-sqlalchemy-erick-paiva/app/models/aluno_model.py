from app.configs.database import db
from sqlalchemy import Integer, String, Column


class AlunoModel(db.Model):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True)

    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(50), nullable=False)
