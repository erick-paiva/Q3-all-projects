from datetime import datetime
from typing import Union
import pymongo
from pymongo import ReturnDocument
client = pymongo.MongoClient("mongodb://localhost:27017/")

kenzie = client["kenzie"]

posts = kenzie.posts


class Post ():
    def __init__(self, data: dict) -> None:

        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.title = data["title"]
        self.author = data["author"]
        self.tags = data["tags"]
        self.content = data["content"]

    @staticmethod
    def obter_todas_publicacoes():
        all_blogs = posts.find()

        return list(all_blogs)

    @staticmethod
    def obter_uma_publicacao(id: int):
        return posts.find_one({"id": id})

    @staticmethod
    def serialize_post(post: Union["Post", dict]):
        if type(post) is dict:
            post.update({"_id": str(post["_id"])})
        elif type(post) is Post:
            post._id = str(post._id)

        return post

    def criar_uma_publicacao(self):
        todas_pub = self.obter_todas_publicacoes()
        if not todas_pub:
            self.id = 1
            posts.insert_one(self.__dict__)
        else:
            self.id = todas_pub[-1]["id"] + 1
            posts.insert_one(self.__dict__)

    def delete_post(id: int):
        return posts.find_one_and_delete({"id": id})

    @classmethod
    def editar_um_post(cls,id: int, data: dict):
        data["updated_at"] = datetime.now()
        post = posts.find_one_and_update({"id": id}, {"$set": data}, return_document=ReturnDocument.AFTER)
        
        return post
    