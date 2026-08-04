from pydantic import BaseModel
from datetime import date

class Chat(BaseModel):
    agente_id : int
    cliente_id : int