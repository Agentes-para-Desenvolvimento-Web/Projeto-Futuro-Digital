from fastapi import APIRouter
from classe.agente_menu import Agente_Menu
from sqlalchemy import create_engine, text
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
apikey = os.getenv("GEMINI_API_KEY")

router = APIRouter(prefix="/menu", tags=["Agente_Menu"])

@router.post("/novo_usuário")
def novo_usuário(menu: Agente_Menu):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.clientes (nome_cliente, cpf, email)
                  """ 
                       
            dados = {
                "nome_cliente" : menu.nome_cliente,
                "cpf" : menu.cpf,
                "email" : menu.email
            }

            con.execute(text(sql), dados)

            engine.dispose()

    except Exception as e:
        return e

@router.get("/confirmar_usuário")
def confirmar_usuário(menu: Agente_Menu):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:

            sql = """
                SELECT * FROM public.clientes
                WHERE cpf = :cpf AND nome_cliente = :nome_cliente
                  """   
                     
            dados = {
                "cpf" : menu.cpf,
                "nome_cliente" : menu.nome_cliente
            }

            result = con.execute(text(sql), dados)

            cliente = result.fetchone()

            engine.dispose()

            if cliente:
                return {"Usuário encontrado. Como posso te ajudar hoje?"}
            
            else:
                return {"Usuário não encontrado. Deseja se cadastrar?"}

    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")

@router.post("/mensagem_usuario")
def mensagem_usuario(menu: Agente_Menu):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.mensagens (mensagem_usuario)
                VALUES ( :mensagem_usuario)
                WHERE id = :cliente_id
                  """ 
                       
            dados = {
                "mensagem_usuario" : menu.mensagem
            }

            con.execute(text(sql), dados)

            engine.dispose()

    except Exception as e:
        return e

@router.post("/resposta_agente_menu")
def resposta(menu: Agente_Menu):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.mensagens (resposta)
                VALUES ( :resposta)
                WHERE id = :cliente_id
                  """ 
                       
            dados = {
                "resposta" : menu.mensagem
            }

            con.execute(text(sql), dados)

            engine.dispose()

    except Exception as e:
        return e

    url = 'https://generativelanguage.googleapis.com/v1beta/interactions'

    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey
    }

    data = {
        "model": "gemini-3.1-flash-lite",
        "input": '''Você é o Agente Menu de um Ecossistema de Agentes de IA. Sua função é identificar o usuário, verificar se ele já possui cadastro e direcioná-lo para o fluxo correto. Você não responde perguntas técnicas nem executa tarefas dos demais agentes.
                    Objetivos: Receber as informações do usuário. Verificar se ele está cadastrado utilizando a ferramenta/API disponibilizada pelo sistema. Direcionar o usuário conforme o resultado da verificação.
                    Regras: Nunca assuma que um usuário está cadastrado. Sempre utilize a ferramenta de verificação de cadastro antes de decidir o fluxo. Nunca invente informações sobre usuários. Caso ocorra erro na consulta, informe que não foi possível verificar o cadastro no momento. Seja educado, objetivo e profissional.
                    Fluxo de decisão:
                        Caso 1 - Usuário cadastrado. Se a consulta indicar que o usuário existe: Cumprimente o usuário utilizando seu nome. Informe que o cadastro foi localizado. Encaminhe-o para o menu principal ou para o agente solicitado. Exemplo: “Olá, Vinicius! Seu cadastro foi localizado com sucesso. Como posso ajudar você hoje?”
                        Caso 2 - Usuário não cadastrado. Se a consulta indicar que o usuário não existe: Informe que nenhum cadastro foi encontrado. Convide o usuário a realizar o cadastro. Exemplo: “Não encontrei um cadastro vinculado aos dados informados. Posso iniciar seu cadastro agora.”
                        Caso 3 - Erro na consulta. Se houver falha na API ou indisponibilidade do sistema: “Não foi possível verificar seu cadastro neste momento. Tente novamente em alguns instantes.”

                    Ferramenta: Utilize a ferramenta de verificação de usuários.
                    Entrada esperada: e-mail, CPF ou outro identificador informado pelo usuário.
                    Saída esperada:
                        existe = true
                        existe = false
                        erro
                    Nunca responda sem consultar a ferramenta.

                    Restrições: Não criar usuários. Não editar usuários. Não excluir usuários. Não responder perguntas fora do fluxo de identificação. Não gerar informações fictícias.
                    Sua única responsabilidade é validar a existência do usuário e encaminhá-lo para o fluxo apropriado.'''
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )

    resultado = response.json()

    texto = resultado['steps'][1]['content'][0]['text']

    return json.loads(texto)