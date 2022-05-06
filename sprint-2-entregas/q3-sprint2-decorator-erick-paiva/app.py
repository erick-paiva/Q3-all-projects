from flask import Flask, request

from decorators import verify_keys


app = Flask(__name__)

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# data = request.get_json()
# Desenvolva suas rotas abaixo
@app.post("/login")
@verify_keys(["username","password"])
def logar():
    # print(request.get_json())
    return "",200