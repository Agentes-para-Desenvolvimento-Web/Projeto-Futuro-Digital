from pydantic import BaseModel, EmailStr

class Agente_Menu(BaseModel):
    nome_cliente: str
    cpf: str
    email: EmailStr
    cidade: str
    numero_contato: str
    bairro: str
    estado: str
    cep: str
    logradouro: str
    complemento: str