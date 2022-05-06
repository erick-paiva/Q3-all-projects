from app.configs.database import db
from sqlalchemy import Integer, Column, ForeignKey


# class AlunoAulaModel(db.Model):
#     __tablename__ = "alunos"

#     id = Column(Integer, primary_key=True)

#     aluno_id = Column(Integer, ForeignKey("alunos.id"))
#     aula_id = Column(Integer, ForeignKey("aulas.id"))


alunos_aulas = db.Table('alunos_aulas',
    Column('id', Integer, primary_key=True),
    Column('aluno_id', Integer, ForeignKey('alunos.id')),
    Column('aula_id', Integer, ForeignKey('aulas.id'))
)