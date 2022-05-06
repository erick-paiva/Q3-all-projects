from flask import Blueprint

from app.controllers import atualizar_lead, criar_lead, delete_lead, obter_lead

bp_leads = Blueprint("leads_api", __name__, url_prefix="/leads")


bp_leads.post("")(criar_lead)
bp_leads.get("")(obter_lead)
bp_leads.patch("")(atualizar_lead)
bp_leads.delete("")(delete_lead)


