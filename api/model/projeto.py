from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Projeto(Base):
    __tablename__ = 'projeto'

    id = Column("id_projeto", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    descricao = Column(String(4000))
    inicio = Column(DateTime)
    fim = Column(DateTime)
    id_categoria = Column(Integer, ForeignKey("categoria.id_categoria"), nullable=False)
    categoria = relationship('Categoria', back_populates='projetos')
    id_gerente = Column(Integer, ForeignKey("gerente.id_gerente"), nullable=False)
    gerente = relationship('Gerente', back_populates='projetos')
    id_status = Column(Integer, ForeignKey("status.id_status"), nullable=False)
    status = relationship('Status', back_populates='projetos')
    dt_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str, inicio:DateTime, fim:DateTime, id_categoria:Integer, id_gerente:Integer, id_status:Integer, dt_insercao:Union[DateTime, None] = None):
        """
        Cria um Projeto

        Arguments:
            nome: nome do projeto.
            descricao: detalhamento do projeto.
        """
        self.nome = nome
        self.descricao = descricao
        self.inicio = inicio
        self.fim = fim
        self.id_categoria = id_categoria
        self.id_gerente = id_gerente
        self.id_status = id_status
        if dt_insercao:
            self.dt_insercao = dt_insercao