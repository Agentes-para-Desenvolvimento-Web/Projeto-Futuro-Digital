from fastapi import APIRouter
from classe.agente_faq import Agente_FAQ
from sqlalchemy import create_engine, text
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
apikey = os.getenv("GEMINI_API_KEY")

router = APIRouter(prefix="/faq", tags=["Agente_FAQ"])

@router.get("/")
def duvidas_usuario(faq: Agente_FAQ):

pergunta = faq.pergunta

    url = 'https://generativelanguage.googleapis.com/v1beta/interactions'

    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey
    }

    data = {
        "model": "gemini-3.1-flash-lite",
        "input":'''
        Responda a pergunta do usuário de forma clara e objetiva, fornecendo informações relevantes e úteis. Evite respostas vagas ou genéricas. Utilize somente esses parâmetros a seguir para responder as perguntas:
        Qual o serviço oferecido pela NETZ?
        A NETZ oferece a possibilidade de o cliente contratar energia elétrica renovável e mais barata para sua casa ou seu comércio, sem a necessidade de investimento inicial ou obras no seu ponto de consumo. Nossa energia é advinda cem porcento de fontes renováveis do mercado de geração distribuída. Uma vez contratados os serviços NETZ, você participará do sistema de compensação de créditos de energia, no qual nossas usinas injetam mensalmente créditos de energia que serão compensados na sua conta de energia. Não se preocupe, a NETZ cuidará de todas as etapas necessárias para entregar os créditos de energia que proporcionarão economia para você e sustentabilidade para o nosso planeta!
        Quem pode contratar o serviço da NETZ?
        Atendemos empresas, pequenos comércios e também a sua casa! Seja em área urbana ou rural, imóvel próprio ou alugado! A NETZ está empenhada em levar o benefício da energia renovável e mais barata a todos os clientes!
        Moro em um imóvel alugado, posso contratar energia limpa, renovável e mais barata da NETZ?
        Sim! Basta que a conta de energia esteja em seu nome!
        O que preciso fazer para ser cliente NETZ?
        Para ser um cliente NETZ, você apenas precisa fazer o cadastro em nosso site! Com base nas informações coletadas, faremos uma análise do seu cadastro e, após aprovado, enviaremos o contrato com os termos e condições para se tornar um cliente NETZ. Após a assinatura do contrato, informaremos a concessionária de energia que, após o prazo regulatório, passará a injetar os créditos da nossa energia limpa e mais barata na sua conta de energia.
        Preciso pagar algo para aderir a NETZ?
        Não cobramos nenhuma taxa de adesão. Apenas após o recebimento dos primeiros créditos na sua conta de energia, você passará a receber uma fatura mensal da NETZ, já aplicando o desconto contratado. Garantimos que todos os meses você pagará menos pela energia que consome, além de usufruir de uma energia limpa e sustentável.
        Preciso pagar algo para a Concessionária Local de Energia?
        Sim, você ainda continuará recebendo sua conta de energia da concessionária local que lhe atende. Porém, essa conta terá o seu valor bem reduzido, uma vez que passará a descontar os créditos de energia injetados pela NETZ.
        Assim como a fatura mensal da NETZ, sua conta de energia precisa ser paga em dia para garantir que a energia elétrica continue sendo entregue no seu comércio ou na sua residência.
        Existe alguma instalação ou adequação necessária para contratar?
        Não. Para ser cliente NETZ, não será necessária nenhuma instalação ou adequação no seu ponto de consumo. A única alteração para participar do nosso movimento será o seu cadastro na concessionária de energia para receber seus créditos de energia, mas não se preocupe, a NETZ cuida de tudo!
        Existe um valor mínimo de conta de energia para se cadastrar?
        Não, a NETZ, ao receber seu cadastro, fará a análise de aceitação baseada em critérios internos e, uma vez aceito, você passará a receber seu benefício mensalmente.
        Tem fidelidade na contratação?
        Você decide se o seu plano é com ou sem fidelidade! Caso opte por não ter fidelidade no momento do seu cadastro, o cancelamento será realizado com um período mínimo de aviso prévio para fazermos as tratativas com a concessionária de energia, a depender da sua região. Este prazo é o tempo que as concessionárias de energia possuem para desconectar você da nossa plataforma. Faremos o aviso assim que nos contatar e, no máximo, em 90 dias você estará desconectado do nosso sistema! Eventuais créditos de energia alocados em sua unidade consumidora até a data em que a concessionária de energia retirar você do sistema de compensação deverão ser pagos para a NETZ dentro das condições contratadas.
        O que eu preciso mudar na minha conta de energia?
        Nada! A NETZ cuida de todo o processo, e a conta da concessionária local de energia permanece em sua titularidade.
        Como funciona a entrega de energia NETZ?
        Mensalmente, nossas usinas produzem energia renovável, gerando créditos de energia perante a concessionária local. Esses créditos são gerenciados pela NETZ e alocados para atender ao seu consumo de energia. Devido às características de produção de energia, pode haver variação na quantidade de energia entregue ao seu ponto de consumo, mas não se preocupe, a energia NETZ sempre será acompanhada do seu desconto contratado e dos benefícios que você já conhece!
        Por quanto tempo o crédito de energia fica na minha conta?
        Conforme a regulação vigente, os créditos de energia podem ser utilizados por um período de até 60 meses.
        O que acontece se eu encerrar meu contrato com a NETZ com um saldo de créditos de energia acumulado na minha conta de energia?
        No momento do encerramento do seu contrato com a NETZ, o saldo de energia será calculado, e o valor, com o seu desconto, será cobrado em uma única parcela. Você poderá usufruir desses créditos durante o seu período de validade.
        Se mudar de endereço perco os créditos de energia?
        Não! Desde que você se mude para uma região atendida pela mesma concessionária de energia, basta que nos comunique antes de fazer a solicitação de alteração de endereço na concessionária local, e que o novo endereço esteja na titularidade, ou seja, no mesmo CPF ou CNPJ da antiga instalação.
        Como o meu benefício é calculado?
        O seu benefício é calculado de acordo com o seu perfil de consumo e a modalidade de contratação de energia com a concessionária local, bem como a energia entregue pela NETZ no mês de análise. Por exemplo, mesmo sendo um cliente NETZ, você precisa manter seu contrato com a concessionária local, e ela cobrará o custo de disponibilidade. Digamos que, no seu caso, o custo de disponibilidade seja de 50 kWh, esse consumo será cobrado integralmente pela concessionária local no valor da tarifa vigente. E se, em um determinado mês, você consumir 300 kWh e a NETZ injetar na rede 200 kWh, o desconto será aplicado sobre os 200 kWh que injetamos. Os outros 100 kWh serão cobrados com seu valor integral, pois foram enviados pela concessionária de energia, sendo 50 kWh o seu custo de disponibilidade (que sempre será cobrado na sua conta) e 50 kWh por você ter utilizado a energia entregue pela concessionária. Vale lembrar que não aplicamos desconto em alguns encargos, como taxa de iluminação pública, doações, multas e juros, entre outros. A sua economia é calculada sempre sobre a energia entregue pela NETZ!
        ''' + pergunta
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )

    resultado = response.json()

    texto = resultado['steps'][1]['content'][0]['text']

    return json.loads(texto)