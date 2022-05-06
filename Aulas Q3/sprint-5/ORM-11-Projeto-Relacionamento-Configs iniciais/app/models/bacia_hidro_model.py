from dataclasses import dataclass
from app.configs.database import db
from app.models.bacia_estado_table import bacias_estados


@dataclass
class BaciaHidroModel(db.Model):
    id: int
    nome: str
    area: float

    __tableaname__ = 'bacias_hidrograficas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    area = db.Column(db.Integer)

    estados = db.relationship(
        "EstadoModel",
        secondary=bacias_estados,
        backref="bacias"
    )
