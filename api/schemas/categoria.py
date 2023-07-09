from pydantic import BaseModel


class CategoriaSchema(BaseModel):
    """ Define como uma categoria de ser representada
    """
    id_categoria: int = 1
    categoria: str = "Melhoria contínua"