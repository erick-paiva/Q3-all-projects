# Desenvolva sua classe Band abaixo
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.configs.database import db

class Band(db.Model):
    
    __tablename__ = "bands"
    
    band_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    
    albums = relationship("Album", back_populates="band")
    
    
    

