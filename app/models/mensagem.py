from pydantic import BaseModel

class Mensagem(BaseModel):
    chat_id : int
    texto : str
    isPergunta : bool # True: Resposta da IA  |  False: Pergunta do usuário