from flask import Blueprint
from app.controllers.regiao_controller import create_regiao


bp = Blueprint("bp_regioes", __name__)

bp.post("/regioes")(create_regiao)