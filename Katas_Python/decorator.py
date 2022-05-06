
from functools import wraps


def wrapper(funcao, *args, **kwargs):

        try:
            # data = request.get_json()
            # data = {"usernameeeeee": "Gol D. Roger","password": "kaizoku123@"}
            # if data.keys() != trusted_keys: raise NameError("erro")
            print(*args)
            # print(data, "dataaaaaaaa")

        except KeyError:
            # return {"error": "chaves a mais"}
            print("errrrrrrrrro")
            print(KeyError)

        return funcao(*args, **kwargs)
    

def decorator(funcao):
    @wraps(funcao)
        return wrapper(funcao,*args, **kwargs)
        
    return decorator

