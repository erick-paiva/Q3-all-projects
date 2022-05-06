from app.controllers.categorie_controller import (adicionar_uma_categoria,
                                                  alterar_categoria,
                                                  deletar_categoria,
                                                  listar_categorias)
from flask import Blueprint

bp = Blueprint('bp_categories', __name__)

bp.get('/')(listar_categorias)
bp.post("/categories")(adicionar_uma_categoria)
bp.patch("/categories/<int:id>")(alterar_categoria)
bp.delete("/categories/<int:id>")(deletar_categoria)
