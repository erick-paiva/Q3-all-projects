from app.configs.database import db

class RegiaoModel(db.Model):
    
    __tablename__ = "regioes"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    numero_estados = db.Column(db.Integer)
    
    estados = db.relationship("estadoModel", backref="regiao", uselist=True)
    
    
