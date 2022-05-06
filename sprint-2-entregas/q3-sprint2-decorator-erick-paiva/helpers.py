# Desenvolva sua funções auxiliares para processamento de arquivo txt aqui
from os import getenv

FILENAME = getenv("DATABASE_FILENAME")

def abrir_arquivo():
    with open(FILENAME, "r") as f:
        arquivo = f.readlines()
        
        
print(abrir_arquivo())