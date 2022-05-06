import os
from flask import Flask, request, send_from_directory
import werkzeug

UPLOAD_FOLDER = '../files'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1000
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# O método é POST, pois vamos criar o arquivo que está sendo enviado.
# "<filename>" é o nome do arquivo, neste exemplo, deve ser passado
# através da URL.

@app.post("/upload/<filename>")
def post_file(filename):
    arquivos = request.files
    print(arquivos,'aaaaaaaaaaa')
    with open(f"./{filename}", "wb") as f:
        f.write(request.data)

        # primeiro_arquivo = request.files["skate"]
        # primeiro_arquivo.save(f"/home/user/Imagens/skate.png")
    return {"message": "Upload realizado com sucesso!"}, 201

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post("/upload/")
def post_file2():

    primeiro_arquivo = request.files["image"]
    
    print(primeiro_arquivo.filename)
    
    if allowed_file(primeiro_arquivo.filename) == False: return {"erro": "arquivo nao suportado"}, 415
    primeiro_arquivo.save(f"./files/{primeiro_arquivo.filename}")
    return {"message": "Upload realizado com sucesso!"}, 201
