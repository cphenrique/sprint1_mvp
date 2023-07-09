from pydantic import BaseModel


class StatusSchema(BaseModel):
    """ Define como um novo status deve ser representado
    """
    id_status: int = 1
    status: str = "Em andamento"