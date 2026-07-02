from pydantic import BaseModel

class Agente_Menu(BaseModel):
    nome_cliente: str
    cpf: str