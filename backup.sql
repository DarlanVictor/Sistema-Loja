--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: clientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clientes (
    id integer NOT NULL,
    cpf text,
    nome text,
    endereco text,
    numero text,
    complemento text,
    bairro text,
    municipio text,
    uf text,
    cep text,
    telefone text,
    email text
);


ALTER TABLE public.clientes OWNER TO postgres;

--
-- Name: clientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.clientes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.clientes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: fornecedores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fornecedores (
    cnpj text NOT NULL,
    nome text,
    logradouro text,
    numero text,
    complemento text,
    bairro text,
    municipio text,
    uf text,
    cep text,
    telefone text,
    email text
);


ALTER TABLE public.fornecedores OWNER TO postgres;

--
-- Name: produtos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.produtos (
    codigo integer NOT NULL,
    nome_marca text,
    descricao text,
    quantidade integer,
    preco_custo money,
    preco_venda money,
    categoria text,
    unidade_medida text,
    fornecedor text
);


ALTER TABLE public.produtos OWNER TO postgres;

--
-- Name: produtos_codigo_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.produtos ALTER COLUMN codigo ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.produtos_codigo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name text NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    access text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id, cpf, nome, endereco, numero, complemento, bairro, municipio, uf, cep, telefone, email) FROM stdin;
1	12345678931	João Gomes	Rua Coronel Correia	1255		Centro	Caucaia	CE	61600000	85999999999	joaogomes@gmail.com
\.


--
-- Data for Name: fornecedores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fornecedores (cnpj, nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email) FROM stdin;
15436940000103	AMAZON SERVICOS DE VAREJO DO BRASIL LTDA.	AV PRESIDENTE JUSCELINO KUBITSCHEK	2041	ANDAR 18 20 21 22 E 23 LADO A TORRE E	VILA NOVA CONCEICAO	SAO PAULO	SP	04.543-011	(11) 4130-2000	amzbr-tax-compliance@amazon.com
45242914000105	C&A MODAS S.A.	AL ARAGUAIA	1222	1022	ALPHAVILLE CENTRO INDUSTRIAL E EMPRESARIAL	BARUERI	SP	06.455-000	(11) 2134-6434	intimacoesfiscais@cea.com.br
24435941000116	TOP SAUDE CLINICA MEDICA LTDA	AVENIDA EDSON DA MOTA CORREIA	714	bloco A	CENTRO	CAUCAIA	CE	61.600-040	(85) 3268-2255	societario@quantcontabil.com
07616162000106	MUNICIPIO DE CAUCAIA	RODOVIA CE 090	1076	KM 1	ITAMBE	CAUCAIA	CE	61.600-970	(85) 3254-7095 / (85) 3254-7095	carvalhohelvecio@hotmail.com
\.


--
-- Data for Name: produtos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.produtos (codigo, nome_marca, descricao, quantidade, preco_custo, preco_venda, categoria, unidade_medida, fornecedor) FROM stdin;
1	Pelicula de celular morola g32	pelicula de vidro 3D	5	R$ 4,00	R$ 20,00	Acessórios	UNIDADE	ShopeeCell
2	fone de ouvido bluetooth	cor azul	10	R$ 5,49	R$ 12,00	Acessórios	UNIDADE	ShopeeCell
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, username, password, access) FROM stdin;
1	admin	admin	admin123	Administrador
2	admin	admin	admin123	Administrador
3	admin	admin	admin123	Administrador
4	teste	teste	123	Usuário
5	darlan	darlan	12345	Administrador
\.


--
-- Name: clientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clientes_id_seq', 2, true);


--
-- Name: produtos_codigo_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.produtos_codigo_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: clientes clientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (id);


--
-- Name: fornecedores fornecedores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fornecedores
    ADD CONSTRAINT fornecedores_pkey PRIMARY KEY (cnpj);


--
-- Name: produtos produtos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.produtos
    ADD CONSTRAINT produtos_pkey PRIMARY KEY (codigo);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

