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
