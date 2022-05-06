def calcular_prioridade(importancia: int, urgencia: int):

    if importancia == 1 and urgencia == 1:
        return 1
    elif importancia == 2 and urgencia == 1:
        return 2
    elif importancia == 1 and urgencia == 2:
        return 3
    else:
        return 4