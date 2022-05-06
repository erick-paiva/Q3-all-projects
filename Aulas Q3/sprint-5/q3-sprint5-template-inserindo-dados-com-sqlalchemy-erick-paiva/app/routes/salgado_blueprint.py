from flask import Blueprint
from app.controllers.salgado_controller import criar_multiplos_salgados, criar_salgado

bp_salgado = Blueprint("salgado", __name__, url_prefix="/salgados")


bp_salgado.post("")(criar_salgado)
bp_salgado.post("/multiplos")(criar_multiplos_salgados)
