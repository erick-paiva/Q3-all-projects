from email.policy import default
from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey

class HeroModel (db.Model):
    __tablename__ = 'heroes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), default=0)
    race = Column(String(50), default=0)
