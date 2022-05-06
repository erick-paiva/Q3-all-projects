from app.configs.database import db
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import backref, relationship
from app.models.alunos_aulas_table import alunos_aulas


class AulaModel(db.Model):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True)

    titulo = Column(String(50), nullable=False)
    descricao = Column(String(50))

    alunos_list = relationship(
        "AlunoModel", backref=backref("aulas_list"), secondary=alunos_aulas
    )
