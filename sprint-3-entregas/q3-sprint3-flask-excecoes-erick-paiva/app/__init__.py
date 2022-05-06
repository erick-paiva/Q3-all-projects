from flask import Flask, jsonify, request
from app.error_class import Chaves_invalidas, Email_ja_existe, Tipo_do_valor_na_requisicao

from app.funcoes_auxiliares import adcionar_no_json, ler_db_json, verifica_chave, verifica_se_email_ja_existe, verifica_se_valores_estao_corretos


app = Flask(__name__)


@app.get("/user")
def get_user():
    return jsonify(ler_db_json())

@app.post("/user")
def add_user():
    data = request.get_json()
    
    try:
        verifica_chave(data)
        verifica_se_email_ja_existe(data)
        verifica_se_valores_estao_corretos(data)
    except Chaves_invalidas:
        return jsonify({"erro": "chave nome e email devem ser passadas!"}), 400

    except Email_ja_existe:
        return jsonify({"error": "User already exists."}), 409
        
    except Tipo_do_valor_na_requisicao as error:
        return jsonify(error.message), 400
    
    return jsonify(adcionar_no_json(data)), 201
