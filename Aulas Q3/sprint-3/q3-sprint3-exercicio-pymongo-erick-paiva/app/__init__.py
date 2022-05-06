from flask import Flask, request, jsonify
import pymongo
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
# Faça a conexã com o MongoDB.

# Métodos auxiliares

class Product:
    # Crie um atributo de classe que pegue a variável de ambiente DATABASE e crie/acesse o banco de dados.
    # Utilize essa variável em seus métodos.
    
    def __init__(self, name, price, in_stock) -> None:
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def register_product(self):
        # Desenvolva aqui a lógica para inserir um dado no banco.
        pass

    @classmethod
    def all_products(cls):
        # Desenvolva aqui a lógica para capturar todos os dados do banco.
        # Observem o erro você pode ter a necessidade de deletar um dado onde retorne um valor inválido para o flask.
        pass

    @classmethod
    def product_by_name(cls, name):
        # Desenvolva aqui a lógica para capturar um dado específico pelo "name".
        # Observem o erro você pode ter a necessidade de deletar um dado onde retorne um valor inválido para o flask.
        pass

    @classmethod
    def updated_product(cls, name, data_updated):
        # Desenvolva aqui a lógica para fazer a atualização dos dados, identificando qual dado deve ser utilizado e assim atualiza-lo.
        pass

    @classmethod
    def delete_product(cls, name):
        # Por fim desenvolva aqui a lógica para fazer a deleção do dado a partir do "name".
        pass

# Rotas

@app.post('/products')
def register():
    req = request.get_json()

    # Utilize sua classe Product para criar e registrar o produto.

    return {'msg': 'created'}, 201

@app.get('/products')
def get_all():
    # Utilize sua classe para retornar todos os dados do seu banco de dados.
    pass

@app.get('/products/<product_name>')
def get_by_name(product_name):
    # Utilize sua classe para retornar um dado específico do seu banco de dados pelo "name".
    pass

@app.patch('/products/<product_name>')
def update(product_name):
    req = request.get_json()

    # Utilize o método da sua classe para fazer a operação de atualizar os dados, passando seus respectivos parâmetros.

    return {}, 204

@app.delete('/products/<product_name>')
def delete(product_name):
    # Utilize o método da sua classe para fazer a operação de deletar os dados, passando seu respectivo parâmetro.

    return {}, 204