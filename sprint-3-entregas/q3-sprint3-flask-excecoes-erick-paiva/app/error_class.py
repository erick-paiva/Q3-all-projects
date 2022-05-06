class Email_ja_existe(Exception):
    pass


class Chaves_invalidas(Exception):
    pass


class Tipo_do_valor_na_requisicao(Exception):
    def __init__(self, status_code=400, data=None):
        self.tipo = {int: "integer", dict: "dictionary",
                     list: "list", float: "float"}
        self.erros = {}
        if type(data["email"]) != str:
            self.erros["email"] = self.tipo[type((data["email"]))]
        if type(data["nome"]) != str:
            self.erros["nome"] = self.tipo[type((data["nome"]))]

        self.message = {
            "wrong fields": [

                self.erros
            ]
        }

        self.status_code = status_code
