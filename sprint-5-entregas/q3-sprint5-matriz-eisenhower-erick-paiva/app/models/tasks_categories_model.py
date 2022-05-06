from sqlalchemy import Column, ForeignKey, Integer
from app.configs.database import db
from dataclasses import dataclass

@dataclass
class Tasks_categories(db.Model):
    
    id: int
    task_id: int
    category_id: int
    
    __tablename__ = 'tasks_categories'
    
    id = Column(Integer, primary_key=True)
    
    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    

