from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app: Flask):
    
    db.init_app(app)
    app.db = db
    
    from app.models.estado_model import EstadoModel
    from app.models.capital_model import CapitalModel
    
    from app.models.regiao_model import RegiaoModel
    from app.models.bacia_hidro_model import BaciaHidroModel
    from app.models.bacia_estado_table import bacias_estados