from dataclasses import dataclass

from app.configs.database import db
from app.models.cachorro_model import Cachorro
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class DonoModel(db.Model):
    id: int
    nome: str
    genero: str
    cachorro: Cachorro

    __tablename__ = "donos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    cachorro_id = Column(Integer, ForeignKey(
        "cachorros.id"), nullable=False, unique=True)

    cachorro = relationship("Cachorro", backref=backref("dono", uselist=False))
