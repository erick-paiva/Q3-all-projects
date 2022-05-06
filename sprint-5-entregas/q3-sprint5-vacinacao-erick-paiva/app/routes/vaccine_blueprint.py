from flask import Blueprint
from app.controllers.vaccine_controller import adcionar_vacina, obter_todas_as_vacinas

bp_vaccine = Blueprint("vaccine", __name__, url_prefix="/vaccinations")


bp_vaccine.post("")(adcionar_vacina)
bp_vaccine.get("")(obter_todas_as_vacinas)
