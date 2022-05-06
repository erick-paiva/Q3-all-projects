from flask import Blueprint
from app.controllers import create_dono

bp_dono = Blueprint("bp_dono", __name__, url_prefix="/donos")

bp_dono.post("")(create_dono)
