from http import HTTPStatus
from flask import jsonify, request
from app.controllers import verifica_chaves
from app.models.stock_model import Anime


def adcionar_anime():
    data = request.get_json()
    chaves_verificadas = verifica_chaves(data)
    if chaves_verificadas:
        return chaves_verificadas

    anime = Anime(data)
    try:
        result = anime.adcionar_anime()
    except:
        return {"error": "anime is already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY
    return result, HTTPStatus.CREATED


def obter_todos_animes():
    result = Anime.obter_todos_animes()

    return jsonify({"data": result}), HTTPStatus.OK


def obter_anime_por_id(anime_id):
    result = Anime.obter_anime_por_id(anime_id)

    if not result:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    return jsonify({"data": [result]}), HTTPStatus.OK


def atualizar_anime(anime_id):
    data = request.get_json()
    chaves_verificadas = verifica_chaves(data)
    if chaves_verificadas:
        return chaves_verificadas
    result = Anime.atualizar_anime_por_id(data, anime_id)
    if not result:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    print(result, "5" * 50)
    return result, HTTPStatus.OK


def deletar_anime(anime_id):
    result = Anime.deletar_anime_por_id(anime_id)
    if not result:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    return {}, HTTPStatus.NO_CONTENT
