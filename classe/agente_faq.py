from pydantic import BaseModel, EmailStr

class Agente_FAQ(BaseModel):
    pergunta: str