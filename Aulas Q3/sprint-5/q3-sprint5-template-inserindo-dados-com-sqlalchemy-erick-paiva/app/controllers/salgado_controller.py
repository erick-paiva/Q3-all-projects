from flask import current_app, request
from app.models.salgado_model import SalgadoModel

def criar_salgado():
    data = request.get_json()
    
    saldado = SalgadoModel(**data)
    
    current_app.db.session.add(saldado)
    current_app.db.session.commit()
    
    
    return {
        "id": saldado.id,
        "nome": saldado.nome,
        "preco": saldado.preco,
    }
    
def criar_multiplos_salgados():
    data = request.get_json()

    salgados = [SalgadoModel(**salgado) for salgado in data["salgados"]]

    current_app.db.session.add_all(salgados)
    current_app.db.session.commit()

    return {
        "salgados": [
            {
                "id": salgado.id,
                "nome": salgado.nome,
                "preco": salgado.preco
            } for salgado in salgados
        ]
    }
    
def pegar_salgados():
    return {
        "salgados": [
            {
                "id": salgado.id,
                "nome": salgado.nome,
                "preco": salgado.preco
            } for salgado in SalgadoModel.query.all()
        ]
    }

def salgados_por_id (id):
    salgado = SalgadoModel.query.get(id)

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }

def primeiro_salgado():
    salgado = SalgadoModel.query.first()
    
    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }

def filtro_salgados(nome):
    salgados = SalgadoModel.query.filter(SalgadoModel.nome.like("%" + nome + "%"))
    
    return {
        "salgados": [
            {
                "id": salgado.id,
                "nome": salgado.nome,
                "preco": salgado.preco
            } for salgado in salgados
        ]
    }

def filtra_apenas_um_salgado(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter(SalgadoModel.nome==salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }

def filtro(salgado_nome):
    salgado = (
      SalgadoModel
      .query
      .filter_by(nome=salgado_nome)
      .first()
    )

    return {
      "id": salgado.id,
      "nome": salgado.nome,
      "preco": salgado.preco
    }
    
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
# Importando as exceções que o método `.one()` pode estourar
...

def um_salgado(salgado_preco):
    try:
        salgado = SalgadoModel.query.filter_by(preco=salgado_preco).one()
        ...
    except (NoResultFound, MultipleResultsFound):
        ...
        
from sqlalchemy.orm.exc import MultipleResultsFound
# Importando a exceção que o método `.one_or_none()` pode estourar
...

def um_salgado_ou_nenhum(salgado_preco):
    try:
        salgado = (
            SalgadoModel
            .query
            .filter_by(preco=salgado_preco)
            .one_or_none()
        )
        ...
    except MultipleResultsFound:
        ...
        
from werkzeug.exceptions import NotFound
# Importando a exceção que o método `.first_or_404()` pode estourar
...

def primeiro_ou_404(salgado_nome):
    try:
        salgado = (
          SalgadoModel
          .query
          .filter_by(nome=salgado_nome)
          .first_or_404(description="Salgado não encontrado")
        )
        ...
    except NotFound as e:
        ...


from werkzeug.exceptions import NotFound
# Importando a exceção que o método `.get_or_404()` pode estourar
...

def pegar_ou_404(salgado_id):
    try:
      salgado = (
          SalgadoModel
          .query
          .get_or_404(salgado_id, description="Salgado não encontrado")
      )
      ...

    except NotFound as e:
        ...