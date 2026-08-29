-- =========================
-- AGENTES
-- =========================

INSERT INTO public.agente (nome, prompt, url, chave_api)
VALUES
(
    'Agente de Atendimento',
    'Você é um assistente virtual responsável por responder dúvidas dos clientes de forma clara e objetiva.',
    'https://api.exemplo.com/agente/atendimento',
    'chave-api-exemplo-001'
),
(
    'Agente Comercial',
    'Você é um assistente especializado em atendimento comercial, produtos e serviços.',
    'https://api.exemplo.com/agente/comercial',
    'chave-api-exemplo-002'
);


-- =========================
-- CLIENTES
-- =========================

INSERT INTO public.cliente
(nome, email, telefone, cpf, cep, cidade, bairro, logradouro, complemento, isparceiro)
VALUES
(
    'João Silva',
    'joao@email.com',
    '51999999999',
    '12345678901',
    '92010000',
    'Canoas',
    'Centro',
    'Rua Principal',
    'Apto 101',
    false
),
(
    'Maria Santos',
    'maria@email.com',
    '51988888888',
    '98765432100',
    '90010000',
    'Porto Alegre',
    'Centro Histórico',
    'Rua dos Andradas',
    'Sala 202',
    true
),
(
    'Pedro Oliveira',
    'pedro@email.com',
    '51977777777',
    '45678912300',
    '92020000',
    'Canoas',
    'Niterói',
    'Avenida Brasil',
    NULL,
    false
);


-- =========================
-- CHATS
-- =========================

INSERT INTO public.chat
(agente_id, cliente_id, data_inicio)
VALUES
(
    1,
    1,
    '2026-08-26 09:30:00'
),
(
    2,
    2,
    '2026-08-26 10:15:00'
),
(
    1,
    3,
    '2026-08-26 14:00:00'
);


-- =========================
-- MENSAGENS
-- =========================

INSERT INTO public.mensagem
(chat_id, texto, horario, ispergunta)
VALUES
(
    1,
    'Olá, gostaria de saber mais informações sobre o serviço.',
    '2026-08-26 09:30:10',
    true
),
(
    1,
    'Olá! Claro. Posso ajudá-lo com informações sobre nossos serviços.',
    '2026-08-26 09:30:15',
    false
),
(
    1,
    'Qual é o prazo para realizar a contratação?',
    '2026-08-26 09:31:00',
    true
),
(
    1,
    'O prazo para contratação é de até 2 dias úteis.',
    '2026-08-26 09:31:08',
    false
),
(
    2,
    'Quais produtos vocês oferecem?',
    '2026-08-26 10:15:20',
    true
),
(
    2,
    'Trabalhamos com diversos produtos e podemos apresentar as opções disponíveis.',
    '2026-08-26 10:15:30',
    false
),
(
    3,
    'Gostaria de entrar em contato com o suporte.',
    '2026-08-26 14:00:10',
    true
),
(
    3,
    'Claro! Vou encaminhar seu atendimento para o suporte.',
    '2026-08-26 14:00:18',
    false
);