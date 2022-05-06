from copy import deepcopy
import os


ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

def e_permitido(filename):
    return filename.split(".")[-1] in ALLOWED_EXTENSIONS

def verificar_extencao(filename, extension="png"):
    return filename.split(".")[-1] == extension

def obter_arquivos():
    todos_arquivos = []
    for i in ALLOWED_EXTENSIONS:
        if len(os.listdir(f'{UPLOAD_FOLDER}/{i}')) > 0:
            todos_arquivos = [*todos_arquivos, *os.listdir(f'{UPLOAD_FOLDER}/{i}')]
    
    return deepcopy(todos_arquivos)

def verifica_se_ja_existe(file):
    todos_arquivos = obter_arquivos()
    
    return file in todos_arquivos

