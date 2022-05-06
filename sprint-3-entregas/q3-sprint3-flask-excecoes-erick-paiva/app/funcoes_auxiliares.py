import json
import os
from app.error_class import Chaves_invalidas, Email_ja_existe, Tipo_do_valor_na_requisicao

FILEPATH = os.getenv("FILEPATH")


def ler_db_json():
    try:
        with open(FILEPATH, "r") as db:
            data = json.load(db)
            return data
    except:
        criar_db_json_e_pastas()
        return {"data": []}


def criar_db_json_e_pastas():
    try:
        os.makedirs("app/database")
    except:
        pass
    with open(FILEPATH, "w") as db:
        db.write('{"data": []}')


def adcionar_no_json(item: dict):
    
    item["id"] = 1 if len(
        arquivo["data"]) == 0 else arquivo["data"][-1]["id"] + 1
    with open(FILEPATH, "w") as db:
        arquivo = ler_db_json()
        arquivo["data"].append(item)
        json.dump(arquivo, db, indent=4)

        return arquivo


def verifica_chave(chaves: dict):
    chaves_obrigatoria = ['email', 'nome']
    if not sorted(chaves.keys()) == sorted(chaves_obrigatoria):
        raise Chaves_invalidas


def verifica_se_email_ja_existe(obj: dict):
    data = ler_db_json()["data"]

    for i in data:
        if obj["email"] == i["email"]:
            raise Email_ja_existe


def verifica_se_valores_estao_corretos(data: dict):

    for i in data.values():
        if type(i) != str:
            raise Tipo_do_valor_na_requisicao(data=data)
