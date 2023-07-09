from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Projeto, Categoria, Gerente, Status
from logger import logger
from schemas import *
from flask_cors import CORS

from datetime import datetime

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
projeto_tag = Tag(name='Projeto', description='Adição, visualização e remoção de projetos')


@app.get('/', tags=[home_tag])
def home():
    """ Redireciona para /openapi, tela que permite a escolha o estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/projeto', tags=[projeto_tag],
          responses={"200": ProjetoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_projeto(form: ProjetoSchema):
    """ Adiciona um novo projeto a base de dados.

    Retorna para uma representação dos projetos e atividades relacionadas.
    """
    projeto = Projeto(
        nome=form.nome,
        descricao=form.descricao,
        inicio=datetime.strptime(form.inicio, '%d/%m/%Y'),
        fim=datetime.strptime(form.fim, '%d/%m/%Y'),
        id_categoria=int(form.id_categoria),
        id_gerente=int(form.id_gerente),
        id_status=int(form.id_status))
    logger.debug(f"Adicionando o projeto '{projeto.nome} na base de dados")
    try:
        # criando conexão com a base de dados
        session = Session()
        # adicionando projeto
        session.add(projeto)
        # efetivando o comando de add novo item na tabela
        session.commit()
        logger.debug(f"{projeto.nome} adicionado com sucesso.")
        return apresenta_projeto(projeto), 200
    
    except Exception as e:
        # tratamento de erros
        error_msg = "Não foi possível adicionar o projeto"
        logger.warning(f"Erro ao adicionar o projeto '{projeto.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/projetos', tags=[projeto_tag],
         responses={"200": ListagemProjetosSchema, "404": ErrorSchema})
def get_projetos():
    """ Faz a busca por todos os Projetos cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Projetos")
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    projetos = session.query(Projeto).all()

    if not projetos:
        # se não há projetos cadastrados
        return {"projetos": []}, 200
    else:
        logger.debug(f"%d Projetos encontrados" % len(projetos))
        # retorna a representação do projeto
        print(projetos)
        return apresenta_projetos(projetos), 200
    

@app.delete('/projeto', tags=[projeto_tag],
            responses={"200": ProjetoDelSchema, "404": ErrorSchema})
def del_projeto(query: ProjetoBuscaSchema):
    """Deleta um Projeto a partir do nome do projeto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    projeto_nome = unquote(unquote(query.nome))
    print(projeto_nome)
    logger.debug(f"Deletando dados sobre projeto #{projeto_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Projeto).filter(Projeto.nome == projeto_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado projeto #{projeto_nome}")
        return {"mesage": "Projeto removido", "nome": projeto_nome}
    else:
        # se o projeto não foi encontrado
        error_msg = "Projeto não encontrado na base"
        logger.warning(f"Erro ao deletar projeto #'{projeto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    

@app.get('/categorias')
def get_categorias():
    """ Faz a busca por todos as Categorias cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Categorias")
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    categorias = session.query(Categoria).all()

    if not categorias:
        # se não há categorias cadastrados
        return {"categorias": []}, 200
    else:
        logger.debug(f"%d Categorias encontradas" % len(categorias))
        # retorna a representação do categoria
        result = []
        for categoria in categorias:
            result.append(
                {
                    "id_categoria": categoria.id,
                    "categoria": categoria.categoria
                }
            )
        return {"categorias": result}
    

@app.get('/gerentes')
def get_gerentes():
    """ Faz a busca por todos os Gerentes cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Gerentes")
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    gerentes = session.query(Gerente).all()

    if not gerentes:
        # se não há gerentes cadastrados
        return {"gerentes": []}, 200
    else:
        logger.debug(f"%d Gerentes encontrados" % len(gerentes))
        # retorna a representação do categoria
        result = []
        for gerente in gerentes:
            result.append(
                {
                    "id_gerente": gerente.id,
                    "gerente": gerente.gerente
                }
            )
        return {"gerentes": result}
    

@app.get('/statuses')
def get_statuses():
    """ Faz a busca por todos os Status cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Statuses")
    # criando conexão com a base de dados
    session = Session()
    # realizando a busca
    statuses = session.query(Status).all()

    if not statuses:
        # se não há gerentes cadastrados
        return {"statuses": []}, 200
    else:
        logger.debug(f"%d Status encontrados" % len(statuses))
        # retorna a representação do categoria
        result = []
        for status in statuses:
            result.append(
                {
                    "id_status": status.id,
                    "status": status.status
                }
            )
        return {"statuses": result}