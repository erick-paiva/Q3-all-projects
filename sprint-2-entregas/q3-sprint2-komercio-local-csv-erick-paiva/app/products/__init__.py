import csv
from os import getenv


def obter_todos_produtos_ou_um(index=None):
    with open(getenv("FILEPATH"), "r") as p:
        produtos = [{"id": int(i["id"]), "name": i["name"], "price": float(i["price"])}
                    for i in csv.DictReader(p)]
        if index != None:
            for i in produtos:
                if int(i["id"] == index):
                    return i
            return False
    return produtos


def paginacao(page=0, per_page=3):
    if page > 0:
        page = (page - 1) * per_page
    else:
        page = 0
    if per_page < 1:
        per_page = 1
    produto = obter_todos_produtos_ou_um()

    return {
        "page": page // per_page+1,
        "quantity": len(produto[page:per_page+page]),
        "data": produto[page:per_page+page],
    }


def cadastrar_novo_produto(prod={}):
    if prod.get("name") == None or prod.get("price") == None or len(prod.keys()) > 2:
        return False
    fieldnames = ["id", "name", "price"]
    new_id = obter_todos_produtos_ou_um()[-1]["id"] + 1

    with open(getenv("FILEPATH"), "a") as p:
        data = csv.DictWriter(p, fieldnames=fieldnames)
        new_prod = {
            "id": new_id,
            "name": prod.get("name"),
            "price": prod.get("price")
        }
        data.writerow(new_prod)

    return new_prod


def editar_um_produto(idP, prod=True):
    if obter_todos_produtos_ou_um(idP) == False or prod == True:
        return {"error": f"product id {idP} not found"}, 404

    with open(getenv("FILEPATH"), "r") as p:
        produtos = []
        for i in csv.DictReader(p):
            if int(i["id"]) == idP:
                obj = {
                    "id": idP,
                    "name": prod.get("name") if prod.get("name") else i["name"],
                    "price": prod.get("price") if prod.get("price") else float(i["price"])
                }
                produtos.append(obj)
            else:
                produtos.append({"id": int(i["id"]), "name": i["name"],
                                 "price": float(i["price"])})

    with open(getenv("FILEPATH"), 'w', newline='') as csvfile:
        fieldnames = ["id", "name", "price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

    return obj, 200


def apagar_um_produto(idP):
    if obter_todos_produtos_ou_um(idP) == False:
        return {"error": f"product id {idP} not found"}, 404

    with open(getenv("FILEPATH"), "r") as p:
        produtos = []
        for i in csv.DictReader(p):
            if int(i["id"]) == idP:
                obj = {
                    "id": int(i["id"]), "name": i["name"],
                     "price": float(i["price"])
                }
            else:
                produtos.append({"id": int(i["id"]), "name": i["name"],
                                 "price": float(i["price"])})

    with open(getenv("FILEPATH"), 'w', newline='') as csvfile:
        fieldnames = ["id", "name", "price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

    return obj, 200
