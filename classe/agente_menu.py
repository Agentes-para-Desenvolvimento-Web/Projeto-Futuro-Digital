from pydantic import BaseModel, EmailStr

class Agente_Menu(BaseModel):
    mensagem: str
    nome_cliente: str
    cpf: str
    email: EmailStr