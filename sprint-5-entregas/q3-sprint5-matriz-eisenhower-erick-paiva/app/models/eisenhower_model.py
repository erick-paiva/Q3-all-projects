from email.policy import default
from app.configs.database import db


class Eisenhower(db.Model):
    id: int
    type: str
    
    __tablename__ = 'eisenhower'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
