from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import datetime
from model.projeto import Projeto
#from schemas import CategoriaSchema
import re


class ProjetoSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    nome: str = "Expansão da planta Campinas"
    descricao: str = "Projeto de expansão da capacidade de produção da fábrica localizada em Campinas-SP"
    inicio: str = "01/01/2023"
    fim: str = "31/12/2023"
    id_categoria: int = 1
    id_gerente: int = 1
    id_status: int = 1

    @validator('inicio')
    def valida_inicio(cls, v):
        if re.search("^(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$", v):
            return v
        
        raise ValueError('A data deve ser no formato DD/MM/YYYY')

    @validator('fim')
    def valida_fim(cls, v):
        if re.search("^(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$", v):
            return v
        
        raise ValueError('A data deve ser no formato DD/MM/YYYY')


class ProjetoViewSchema(BaseModel):
    """ Define como um novo projeto a ser inserido deve ser representado.
    """
    nome: str = "Expansão da planta Campinas"
    descricao: str = "Projeto de expansão da capacidade de produção da fábrica localizada em Campinas-SP"
    inicio: str = "01/01/2023"
    fim: str = "31/12/2023"
    id_categoria: int = 1
    id_gerente: int = 1
    id_status: int = 1


class ListagemProjetosSchema(BaseModel):
    """ Define como uma listagem de projetos será retornada.
    """
    projetos:List[ProjetoSchema]


class ProjetoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do projeto.
    """
    nome: str = "Nome do Projeto"


class ProjetoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str


def apresenta_projetos(projetos: List[Projeto]):
    """ Retorna uma representação dos projetos seguindo o schema definido em
        ProjetoViewSchema
    """
    result = []
    for projeto in projetos:
        result.append(
            {
                "nome": projeto.nome,
                "descricao": projeto.descricao,
                "inicio": datetime.strftime(projeto.inicio, '%d/%m/%Y'), 
                "fim": datetime.strftime(projeto.fim, '%d/%m/%Y'),
                "categoria": projeto.categoria.categoria,
                "gerente": projeto.gerente.gerente,
                "status": projeto.status.status
            }
        )
    return {"projetos": result}


def apresenta_projeto(projeto: Projeto):
    """ Retorna uma representação do projeto seguindo o schema definido em
        ProjetoViewSchema.
    """
    return {
        "id": projeto.id,
        "nome": projeto.nome,
        "descricao": projeto.descricao,
        "inicio": projeto.inicio,
        "fim": projeto.fim,
        "categoria": projeto.categoria.categoria,
        "gerente": projeto.gerente.gerente,
        "status": projeto.status.status
    }