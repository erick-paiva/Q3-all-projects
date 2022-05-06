# Desenvolva seus decorators aqui
from curses import wrapper
from distutils.log import error
from functools import wraps

from flask import request

esperado =  ["username","password"]

def verify_keys(trusted_keys: list[str]):

    def decorator(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json() 
                # data = {"usernameeeeee": "Gol D. Roger","password": "kaizoku123@"}
                # if data.keys() != trusted_keys: raise NameError("erro")
                print(*args)
                print(data, "dataaaaaaaa")
                
            except KeyError:
                # return {"error": "chaves a mais"}
                print("errrrrrrrrro")
                print(KeyError)
                
            return funcao(*args, **kwargs)
        return wrapper
    return decorator
    

    

# @verify_keys(esperado)
# def test(a):
#     print(a)
    
    
# test({"usernameeeeee": "Gol D. Roger","password": "kaizoku123@"})