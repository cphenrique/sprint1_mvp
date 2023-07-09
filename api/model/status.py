from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base


class Status(Base):
    __tablename__ = 'status'

    id = Column("id_status", Integer, primary_key=True)
    status = Column(String(100), unique=True)

    projetos = relationship("Projeto", back_populates="status")
    

    def __init__(self, status:str):
        """
        Cria um status de projeto

        Arguments:
            status: status do projeto.
        """
        self.status = status