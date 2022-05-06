from flask import Blueprint
from app.controllers.capital_controller import create_capital

bp = Blueprint("bp_capitais", __name__)

bp.post("/capitais")(create_capital)

