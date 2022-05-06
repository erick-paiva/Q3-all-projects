from http import HTTPStatus
from flask import jsonify
# from app.exceptions import ChavesFaltantes
from app.model import Post


def verifica_chaves(chaves: dict, todas: bool = True):
    chaves_requeridas = ["tags", "title", "content", "author"]
    chaves_faltantes = []
    chaves = chaves.keys()
    if len(chaves) < 4 and todas:
        return {"voce precisa enviar todas as chaves!": chaves_requeridas}
    for k in chaves:
        if not k in chaves_requeridas:
            chaves_faltantes.append(k)
    if len(chaves_faltantes) > 0:
        return {"error você enviou chaves invalidas": chaves_faltantes}


def adicionar_um_post(data: dict):

    chaves = verifica_chaves(data)
    if chaves:
        return jsonify(chaves), HTTPStatus.BAD_REQUEST
    post = Post(data)
    post.criar_uma_publicacao()
    Post.serialize_post(post)

    return jsonify(post.__dict__), HTTPStatus.OK


def obter_todos_posts():
    todos_posts = Post.obter_todas_publicacoes()

    for i in todos_posts:
        Post.serialize_post(i)
    return jsonify(todos_posts), HTTPStatus.OK


def obter_um_post(id: int):
    post = Post.obter_uma_publicacao(id)
    Post.serialize_post(post)
    if not post:
        return {"error": f"nao foi possivel encotrar um post com o id {id}"}, HTTPStatus.NOT_FOUND
    Post.serialize_post(post)

    return jsonify(post), HTTPStatus.OK

def excluir_um_post(id: int):
    post = Post.delete_post(id)
    if not post:
        return {"error": f"não foi possivel encontrar o post com o id {id}"}, HTTPStatus.NOT_FOUND
    Post.serialize_post(post)
    return jsonify(post), HTTPStatus.NO_CONTENT

def editar_um_post(id:int, data: dict):
    chaves = verifica_chaves(data, False)
    if chaves:
        return chaves
    post = Post.editar_um_post(id, data)
    Post.serialize_post(post)
    if not post:
        return {"error": f"não foi possivel editar o post com o id {id}"}, HTTPStatus.NOT_FOUND
    return jsonify(post), HTTPStatus.OK
    