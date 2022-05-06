# Desenvolva sua classe Album abaixo
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.configs.database import db
from sqlalchemy.orm import relationship


class Album(db.Model):
    __tablename__ = "albums"

    album_id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(DateTime)

    band_id = Column(Integer, ForeignKey("bands.band_id"))
    #o relationship é um relacionamento entre as tabelas
    #band_id é uma chave estrageira da coluna da tabela albums
    #bands é o nome da tabela
    #band_id é a chave primaria da tabela bands
    band = relationship("Band", back_populates="albums")
    #back_populates é um atributo da classe Band
    
    musics = relationship("Music", backref="album")
