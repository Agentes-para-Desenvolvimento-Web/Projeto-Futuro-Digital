CREATE TABLE public.agente (
	id serial NOT NULL,
	nome varchar(100) NULL,
	prompt text NOT NULL,
	CONSTRAINT agente_pk PRIMARY KEY (id)
);

CREATE TABLE public.cliente (
	id serial NOT NULL,
	nome varchar(40) NOT NULL,
	email varchar(30) NOT NULL,
	telefone char(11) NOT NULL,
	cpf char(11) NOT NULL,
	cep char(8) NOT NULL,
	cidade varchar(20) NOT NULL,
	bairro varchar(20) NOT NULL,
	logradouro varchar(30) NOT NULL,
	complemento varchar(30) NULL,
	isparceiro bool NOT NULL,
	CONSTRAINT usuario_pk PRIMARY KEY (id),
	CONSTRAINT usuario_unique UNIQUE (email),
	CONSTRAINT usuario_unique_1 UNIQUE (telefone),
	CONSTRAINT usuario_unique_2 UNIQUE (cpf)
);

CREATE TABLE public.chat (
	id serial NOT NULL,
	data_inicio timestamp NULL,
	CONSTRAINT chat_pk PRIMARY KEY (id),
	CONSTRAINT agente_id FOREIGN KEY (id) REFERENCES public.agente(id) ON UPDATE CASCADE,
	CONSTRAINT cliente_id FOREIGN KEY (id) REFERENCES public.cliente(id) ON UPDATE CASCADE
);

CREATE TABLE public.mensagem (
	id serial NOT NULL,
	texto text NOT NULL,
	horario timestamp NOT NULL,
	ispergunta bool NOT NULL,
	CONSTRAINT conversa_pk PRIMARY KEY (id),
	CONSTRAINT chat_id FOREIGN KEY (id) REFERENCES public.chat(id) ON DELETE CASCADE ON UPDATE CASCADE
);
