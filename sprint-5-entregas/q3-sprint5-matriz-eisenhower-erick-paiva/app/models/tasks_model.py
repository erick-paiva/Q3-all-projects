from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey, TEXT
from sqlalchemy.orm import validates
from app.exc.exceptions import InvalidOption, InvalidValueTask


@dataclass
class Tasks(db.Model):

    id: int
    name: str
    description: str
    duration: int
    importance: int
    urgency: int

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(TEXT, nullable=False)
    duration = Column(Integer, nullable=False)
    importance = Column(Integer, nullable=False)
    urgency = Column(Integer, nullable=False)
    eisenhower_id = Column(Integer, ForeignKey(
        'eisenhower.id'), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        if type(name) != str:
            raise InvalidValueTask(msg={"error": "name must be a string"})
        return name.lower()

    @validates('description')
    def validate_description(self, key, description):
        if type(description) != str:
            raise InvalidValueTask(msg={"error": "description must be a string"})
        return description
    
    @validates('duration')
    def validate_duration(self, key, duration):
        if type(duration) != int:
            raise InvalidValueTask(msg={"error": "duration must be a integer"})
        return duration

    @validates('importance')
    def validar_importancia(self, key, importance):
        if type(importance) != int:
            raise InvalidValueTask(
                msg={"error": "Importance must be an integer"})

        if importance < 0 or importance > 2:
            raise InvalidOption(
                msg={"error": "importance must be between 0 and 2"})

        return importance

    @validates('urgency')
    def validar_urgencia(self, key, urgency):
        if type(urgency) != int:
            raise InvalidValueTask(msg={"error": "urgency must be an integer"})

        if urgency < 0 or urgency > 2:
            raise InvalidOption(
                msg={'error': 'urgency must be between 0 and 2'})

        return urgency
