from fastapi import APIRouter
from classe.agente_cadastro import Agente_Cadastro
from sqlalchemy import create_engine, text
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
apikey = os.getenv("GEMINI_API_KEY")

router = APIRouter(prefix="/cadastro", tags=["Agente_Cadastro"])

@router.put('/atualizar_cadastro')
def atualizar_cadastro(cadastro: Agente_Cadastro):

    engine = create_engine(DATABASE_URL)
    
    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.clientes (nome_cliente, email, cidade, cpf, numero_contato, bairro, estado, cep, logradouro, complemento)
                VALUES ( :nome_cliente, :email, :cidade, :cpf, :numero_contato, :bairro, :estado, :cep, :logradouro, :complemento)
                  """
                        
            dados = {
                "nome_cliente" : menu.nome_cliente,
                "email": menu.email,
                "cidade": menu.cidade,
                "cpf": menu.cpf,
                "numero_contato": menu.numero_contato,
                "bairro": menu.bairro,
                "estado": menu.estado,
                "cep": menu.cep,
                "logradouro": menu.logradouro,
                "complemento": menu.complemento
            }

            con.execute(text(sql), dados)

            engine.dispose()

            return {"Cliente cadastrado com sucesso."}

    except Exception as e:
        return e
