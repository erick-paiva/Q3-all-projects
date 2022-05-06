from datetime import datetime, timedelta
from email.policy import default
from sqlalchemy import Column, String, DateTime, CHAR, CheckConstraint
from app.configs.database import db


class Vacina(db.Model):

    __tablename__ = "vaccine_cards"

    now = datetime.now()

    cpf = Column(String(11), primary_key=True)
    name = Column(String(60), nullable=False)
    first_shot_date = Column(DateTime, default=now)
    second_shot_date = Column(DateTime, default=now+timedelta(90))
    vaccine_name = Column(String(60))
    health_unit_name = Column(String(60))
    CheckConstraint('length("cpf") = 11', name="cpf_length_11")
