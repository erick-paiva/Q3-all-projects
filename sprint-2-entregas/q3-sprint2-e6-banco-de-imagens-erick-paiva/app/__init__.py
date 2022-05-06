import os
from flask import Flask, jsonify, request, send_from_directory

from app.kenzie.image import e_permitido, obter_arquivos, verifica_se_ja_existe, verificar_extencao

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = int(os.getenv("MAX_CONTENT_LENGTH")) * 1000

try:
    os.makedirs("files/png")
    os.makedirs("files/gif")
    os.makedirs("files/jpg")
except:
    ...

@app.errorhandler(413)
def retonar_erro_tamanho(_):
    return {"error": "o tamanho do arquivo passou de 1mb"}, 413

@app.post("/upload")
def enviar_imagens():

    arquivo = request.files["file"]
    if verifica_se_ja_existe(arquivo.filename): return {"error": "arquivo ja existe !"}, 409
    if e_permitido(arquivo.filename) == False: return {"error": "arquivo nao suportado"}, 415
    
    arquivo.save(f"{UPLOAD_FOLDER}/{arquivo.filename.split('.')[-1]}/{arquivo.filename}")
    return {"message": "Upload realizado com sucesso!"}, 201


@app.get("/files")
def obter_lista_de_imagens():

    todos_arquivos = obter_arquivos()

    return jsonify(todos_arquivos), 200


@app.get("/files/<extension>")
def obter_lista_de_imagens_especifica(extension):
    if e_permitido(f".{extension}") == False: return {"error": "arquivo nao suportado"},404
    
    todos_arquivos = [a for a in obter_arquivos() if verificar_extencao(a ,extension)]

    return jsonify(todos_arquivos), 200

@app.get("/download/<name_extension>")
def fazer_download_de_um_arquivo(name_extension):
    
    if not name_extension in obter_arquivos(): return {"error": "arquivo nao encontrado"},404

    return send_from_directory(directory=f"../files/{name_extension.split('.')[-1]}", path=name_extension, as_attachment=True),200

@app.get("/download-zip")
def fazer_download_de_um_arquivo_zipado():
    extension = request.args.get("extension")
    arquivos = [f'"{a}"' for a in obter_arquivos() if verificar_extencao(a ,extension)]
    
    if len(arquivos) == 0: return {"error": "arquivo nao existe"}, 404
    try:
        os.chdir(f"files/{extension}")
    except:
        pass
    os.system(f'zip arquivos-compactados {" ".join(arquivos)} -6')
    os.system("mv arquivos-compactados.zip /tmp")
    os.chdir(f"../../")
    return send_from_directory(directory="/tmp", path="arquivos-compactados.zip", as_attachment=True),200
