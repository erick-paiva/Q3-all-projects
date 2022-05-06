from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, TEXT
from app.configs.database import db
from sqlalchemy.orm import backref


@dataclass
class Categories(db.Model):
    __tablename__ = 'categories'
    
    id: int
    name: str
    description: str
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(TEXT, nullable=False)
    
    tasks = db.relationship("Tasks", secondary="tasks_categories", backref=backref("categories"))
    
   
    
    