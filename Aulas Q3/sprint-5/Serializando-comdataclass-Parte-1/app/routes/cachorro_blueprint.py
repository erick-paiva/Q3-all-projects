from flask import Blueprint

from app.controllers import create_dog

bp_dogs = Blueprint("dogs", __name__, url_prefix="/dogs")

bp_dogs.post("")(create_dog)

