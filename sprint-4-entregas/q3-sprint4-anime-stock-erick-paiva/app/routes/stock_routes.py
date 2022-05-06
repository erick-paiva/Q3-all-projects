from flask import Blueprint
from app.controllers.stock_control import adcionar_anime, atualizar_anime, deletar_anime, obter_anime_por_id, obter_todos_animes

bp_stock = Blueprint('stock', __name__, url_prefix='/animes')

bp_stock.post('')(adcionar_anime)
bp_stock.get('')(obter_todos_animes)
bp_stock.get('/<int:anime_id>')(obter_anime_por_id)
bp_stock.patch('/<int:anime_id>')(atualizar_anime)
bp_stock.delete('/<int:anime_id>')(deletar_anime)
