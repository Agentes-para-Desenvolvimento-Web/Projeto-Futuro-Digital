from pydantic import BaseModel

class Agente(BaseModel):
    nome : str
    prompt : str
    url : str
    chave_api : str