from pydantic import BaseModel


class GerenteSchema(BaseModel):
    """ Define como um novo gerente deve ser representado
    """
    id_gerente: int = 1
    gerente: str = "Fulano"