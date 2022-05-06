from http import HTTPStatus
from flask import Flask, jsonify, request
from app.products import apagar_um_produto, editar_um_produto, obter_todos_produtos_ou_um, paginacao, cadastrar_novo_produto


app = Flask(__name__)

@app.get("/products/query")
@app.get("/products")
def products ():
    page = request.args.get("page") or 0
    per_page = request.args.get("perpage") or 3
    response = jsonify(paginacao(int(page), int(per_page)))
    return response, 200

@app.get("/products/<int:idP>")
def get_one_product (idP=0):
    data = obter_todos_produtos_ou_um(idP)
    if data == False:
        return {"error": f"product id {idP} not found"}, 404
    else:
        return jsonify(data), 200


@app.post("/products")
def registrar_novo_produto():
    data = request.get_json()
    new_prod = cadastrar_novo_produto(data)
    if new_prod == False : return {"error": "error your object has too many keys or keys with incorrect names!"}, HTTPStatus.BAD_REQUEST
    
    return new_prod, HTTPStatus.CREATED

@app.patch("/products/<int:idP>")
def atualizar_um_produto (idP=True):
    data = request.get_json()
    objj = editar_um_produto(idP,data)
    return objj

@app.delete("/products/<int:idP>")
def deletar_um_producto (idP):
    objj = apagar_um_produto(idP)
    return objj
