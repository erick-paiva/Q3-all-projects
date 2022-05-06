from app.configs.database import db
from sqlalchemy import Column, String, Integer
from dataclasses import dataclass


@dataclass
class Cachorro(db.Model):
    
    id: int
    nome: str
    idade: int
    raca: str
    
    __tablename__ = "cachorros"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
    raca = Column(String(50), nullable=False)
    # peso = Column(Integer, nullable=False)
