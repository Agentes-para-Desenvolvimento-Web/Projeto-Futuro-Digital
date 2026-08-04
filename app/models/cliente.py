from pydantic import BaseModel, EmailStr, Field, field_validator

class Cliente(BaseModel):
    nome : str
    email : EmailStr
    telefone : str = Field(min_length=11, max_length=11)
    cpf : str = Field(min_length=11, max_length=11)
    cep : str = Field(min_length=8, max_length=8)
    cidade : str
    bairro : str
    logradouro : str
    complemento : str
    isparceiro : bool

    @field_validator('telefone')
    def validaTelefone(cls, value : str) -> str:
        if not value.isdigit():
            raise ValueError('O número de telefone deve conter apenas números')
        return value
    
    @field_validator('cpf')
    def validaCPF(cls, value : str) -> str:
        if not value.isdigit():
            raise ValueError('O CPF deve conter apenas números')
        return value

    @field_validator('cep')
    def validaCEP(cls, value : str) -> str:
        if not value.isdigit():
            raise ValueError('O CEP deve conter apenas números')
        return value

    @field_validator('cidade')
    def formataCidade(cls, value : str) -> str:
        return value.title
    
    @field_validator('bairro')
    def formataBairro(cls, value : str) -> str:
        return value.title

    @field_validator('logradouro')
    def formataLogradouro(cls, value : str) -> str:
        return value.title