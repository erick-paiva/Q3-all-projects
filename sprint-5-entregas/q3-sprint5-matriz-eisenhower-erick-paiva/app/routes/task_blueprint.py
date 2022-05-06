from app.controllers.task_controller import (adcionar_task, alterar_task,
                                             deletar_task)
from flask import Blueprint

bp = Blueprint('bp_tasks', __name__)

bp.post("/tasks")(adcionar_task)
bp.patch("/tasks/<int:id>")(alterar_task)
bp.delete("/tasks/<int:id>")(deletar_task)
