from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base


class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column("id_categoria", Integer, primary_key=True)
    categoria = Column(String(100), unique=True)

    projetos = relationship("Projeto", back_populates="categoria")
    
    def __init__(self, categoria:str):
        """
        Cria uma categoria de projeto

        Arguments:
            categoria: categoria do projeto.
        """
        self.categoria = categoria