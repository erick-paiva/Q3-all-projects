from flask import Blueprint
from app.controllers.estado_controller import create_estado


bp = Blueprint("bp_estados", __name__)

bp.post("/estados")(create_estado)
