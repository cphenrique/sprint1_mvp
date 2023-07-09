from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base


class Gerente(Base):
    __tablename__ = 'gerente'

    id = Column("id_gerente", Integer, primary_key=True)
    gerente = Column(String(100), unique=True)

    projetos = relationship("Projeto", back_populates="gerente")    

    def __init__(self, gerente:str):
        """
        Cria um gerente de projeto

        Arguments:
            gerente: nome do gerente do projeto.
        """
        self.gerente = gerente