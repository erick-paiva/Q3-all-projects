from flask import Flask, request, send_from_directory

app = Flask(__name__)


def escrever(conteudo):
    # Arquivo aberto em modo de inserção(append) para inserir
    # novas informações sem perder as antigas
    with open("./files/example.txt", "a") as f:
        f.write(conteudo)
        f.write("\n")
        # O "\n" vai para próxima linha


@app.post("/lista")
def cadastrar():
    # Pega os dados da requisição
    data = request.get_json()

    # Pegando os valores da requisição
    quantidade = data.get("quantidade")
    item = data.get("item")

    # Conteúdo que vai ser cadastrado no arquivo example.txt
    conteudo = f"Devo comprar {quantidade} de {item}"

    # Chamando a função "escrever" que foi criada anteriormente
    escrever(conteudo)

    return {"message": "Item adicionado a lista!"}

@app.get("/download/lista")
def download():
    return send_from_directory(
      directory="../files", 
      path="example.txt", 
      as_attachment=True
    )
# O as_attachment indica ao navegador que ele
# deve salvar ao invés de exibir.
