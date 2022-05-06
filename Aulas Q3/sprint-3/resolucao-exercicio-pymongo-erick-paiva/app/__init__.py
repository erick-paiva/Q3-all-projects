from flask import Flask, request, jsonify
from dotenv import load_dotenv
from os import getenv
import pymongo

load_dotenv()

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Métodos auxiliares


class Product:
    DATABASE = client[getenv('DATABASE')]

    def __init__(self, name, price, in_stock) -> None:
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def register_product(self):
        db = self.DATABASE

        db.product.insert_one(self.__dict__)

    @classmethod
    def all_products(cls):
        db = cls.DATABASE

        all_posts = []
        for p in db.product.find():
            del p['_id']
            all_posts.append(p)

        return all_posts

    @classmethod
    def product_by_name(cls, name):
        db = cls.DATABASE

        product = db.product.find_one({'name': name})
        del product['_id']

        return product

    @classmethod
    def updated_product(cls, name, data_updated):
        db = cls.DATABASE

        current_product = cls.product_by_name(name)

        update = {"$set": {**data_updated}}

        db.product.update_one(current_product, update)

    @classmethod
    def delete_product(cls, name):
        db = cls.DATABASE

        current_product = cls.product_by_name(name)

        db.product.delete_one(current_product)


# Rotas

@app.post('/products')
def register():
    req = request.get_json()

    product = Product(**req)
    product.register_product()

    return {'msg': 'created'}, 201


@app.get('/products')
def get_all():
    return jsonify(Product.all_products()), 200


@app.get('/products/<product_name>')
def get_by_name(product_name):
    return jsonify(Product.product_by_name(product_name)), 200


@app.patch('/products/<product_name>')
def update(product_name):
    req = request.get_json()

    Product.updated_product(product_name, req)

    return {}, 204


@app.delete('/products/<product_name>')
def delete(product_name):
    Product.delete_product(product_name)

    return {}, 204
