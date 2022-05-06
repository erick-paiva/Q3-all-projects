from flask import Flask, request

from app.controllers.controler import adicionar_um_post, editar_um_post, excluir_um_post, obter_todos_posts, obter_um_post


def home_routes(app: Flask):
    @app.post("/posts")
    def create_post():
        data = request.get_json()
        return adicionar_um_post(data)

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return excluir_um_post(id)

    @app.get("/posts")
    def read_posts():
        return obter_todos_posts()

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return obter_um_post(id)

    @app.patch("/posts/<int:id>")
    def update_post(id):
        data = request.get_json()
        return editar_um_post(id, data)
