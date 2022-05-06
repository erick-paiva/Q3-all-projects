from datetime import datetime
from app.configs.database import db
from sqlalchemy import Column, String, Integer, DateTime
from dataclasses import dataclass


@dataclass
class Leads(db.Model):
    
    id: int
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: int
    visits: int
    
    __tablename__ = "leads_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    last_visit = Column(DateTime, nullable=False, default=datetime.utcnow())
    visits = Column(Integer, nullable=False, default=1)