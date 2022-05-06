# Desenvolva sua classe Music abaixo
from sqlalchemy import Column, ForeignKey, Integer, String, Time
from app.configs.database import db
from sqlalchemy.orm import relationship


class Music(db.Model):
    __tablename__ = "musics"

    music_id = Column(Integer, primary_key=True)
    title = Column(String)
    duration = Column(Time)
    
    #album.album_id é uma chave estrangeira da coluna da tabela albums
    album_id = Column(Integer, ForeignKey("albums.album_id"))
