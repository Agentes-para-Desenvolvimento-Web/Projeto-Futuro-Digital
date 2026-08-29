import os
from fastapi import APIRouter
from models.agente import Agente
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

router = APIRouter(prefix='/agente', tags=['Agente', 'IA'])

@router.get('')
def listarAgentes():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = 'SELECT * FROM agente'
            response = con.execute(text(sql))
            result = response.mappings().all()
    except Exception as e:
        return e
    engine.dispose()
    return result

# Create
@router.post('')
def inserirAgente(agente: Agente):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """INSERT INTO public.agente
                                (nome, prompt, url, chave_api)
                        VALUES (:nome, :prompt, :url, :chave_api)"""
            dados = {
                "nome": agente.nome,
                "prompt": agente.prompt,
                "url": agente.url,
                "chave_api": agente.chave_api
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Agente cadastrado com sucesso!'

# Read (buscar agente por id)
@router.get('/{id}')
def buscarAgente(id: int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """SELECT * FROM public.agente
                    WHERE id = :id"""
            response = con.execute(text(sql), {"id": id})
            result = response.fetchone()
    except Exception as erro:
        return erro
    engine.dispose()
    return result._mapping

# Update
@router.put('/{id}')
def atualizarAgente(id: int, agente: Agente):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """UPDATE public.agente
                    SET nome = :nome,
                        prompt = :prompt,
                        url = :url,
                        chave_api = :chave_api
                    WHERE id = :id"""
            dados = {
                "id": id,
                "nome": agente.nome,
                "prompt": agente.prompt,
                "url": agente.url,
                "chave_api": agente.chave_api
            }
            con.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'Agente atualizado com sucesso!'

# Delete
@router.delete('/{id}')
def deletarAgente(id: int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as con:
            sql = """DELETE FROM public.agente
                    WHERE id = :id"""
            con.execute(text(sql), {"id": id})
            return 'Agente deletado com sucesso!'
    except Exception as erro:
        return erro
