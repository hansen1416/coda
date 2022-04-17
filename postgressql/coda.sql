--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6
-- Dumped by pg_dump version 13.6

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
-- Name: board; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.board (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    group_id integer NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.board OWNER TO hlz;

--
-- Name: board_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.board_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.board_id_seq OWNER TO hlz;

--
-- Name: board_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.board_id_seq OWNED BY public.board.id;


--
-- Name: board_permission; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.board_permission (
    id integer NOT NULL,
    board_id integer NOT NULL,
    user_id integer NOT NULL,
    permission integer NOT NULL
);


ALTER TABLE public.board_permission OWNER TO hlz;

--
-- Name: board_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.board_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.board_permission_id_seq OWNER TO hlz;

--
-- Name: board_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.board_permission_id_seq OWNED BY public.board_permission.id;


--
-- Name: invite; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.invite (
    id integer NOT NULL,
    board_id integer NOT NULL,
    sender_user_id integer NOT NULL,
    receiver_user_id integer NOT NULL,
    status smallint NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.invite OWNER TO hlz;

--
-- Name: COLUMN invite.status; Type: COMMENT; Schema: public; Owner: hlz
--

COMMENT ON COLUMN public.invite.status IS 'default:0, accpeted:1, rejected:2';


--
-- Name: invite_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.invite_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.invite_id_seq OWNER TO hlz;

--
-- Name: invite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.invite_id_seq OWNED BY public.invite.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.post (
    id integer NOT NULL,
    board_id integer NOT NULL,
    user_id integer NOT NULL,
    thread_id integer NOT NULL,
    content text NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.post OWNER TO hlz;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO hlz;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: superusers; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.superusers (
    id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.superusers OWNER TO hlz;

--
-- Name: superusers_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.superusers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.superusers_id_seq OWNER TO hlz;

--
-- Name: superusers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.superusers_id_seq OWNED BY public.superusers.id;


--
-- Name: thread; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.thread (
    id integer NOT NULL,
    board_id integer NOT NULL,
    user_id integer NOT NULL,
    title character varying(128) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.thread OWNER TO hlz;

--
-- Name: thread_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.thread_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.thread_id_seq OWNER TO hlz;

--
-- Name: thread_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.thread_id_seq OWNED BY public.thread.id;


--
-- Name: thread_permission; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.thread_permission (
    id integer NOT NULL,
    board_id integer NOT NULL,
    thread_id integer NOT NULL,
    user_id integer NOT NULL,
    permission integer NOT NULL
);


ALTER TABLE public.thread_permission OWNER TO hlz;

--
-- Name: thread_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.thread_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.thread_permission_id_seq OWNER TO hlz;

--
-- Name: thread_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.thread_permission_id_seq OWNED BY public.thread_permission.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: hlz
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(128) NOT NULL,
    email character varying(128) NOT NULL,
    password character varying(192) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO hlz;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: hlz
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO hlz;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hlz
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: board id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.board ALTER COLUMN id SET DEFAULT nextval('public.board_id_seq'::regclass);


--
-- Name: board_permission id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.board_permission ALTER COLUMN id SET DEFAULT nextval('public.board_permission_id_seq'::regclass);


--
-- Name: invite id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.invite ALTER COLUMN id SET DEFAULT nextval('public.invite_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Name: superusers id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.superusers ALTER COLUMN id SET DEFAULT nextval('public.superusers_id_seq'::regclass);


--
-- Name: thread id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.thread ALTER COLUMN id SET DEFAULT nextval('public.thread_id_seq'::regclass);


--
-- Name: thread_permission id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.thread_permission ALTER COLUMN id SET DEFAULT nextval('public.thread_permission_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: board; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.board (id, name, group_id, created_at) FROM stdin;
\.


--
-- Data for Name: board_permission; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.board_permission (id, board_id, user_id, permission) FROM stdin;
\.


--
-- Data for Name: invite; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.invite (id, board_id, sender_user_id, receiver_user_id, status, created_at) FROM stdin;
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.post (id, board_id, user_id, thread_id, content, created_at) FROM stdin;
\.


--
-- Data for Name: superusers; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.superusers (id, user_id) FROM stdin;
1	1
\.


--
-- Data for Name: thread; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.thread (id, board_id, user_id, title, created_at) FROM stdin;
\.


--
-- Data for Name: thread_permission; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.thread_permission (id, board_id, thread_id, user_id, permission) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hlz
--

COPY public.users (id, username, email, password, created_at) FROM stdin;
\.


--
-- Name: board_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.board_id_seq', 1, false);


--
-- Name: board_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.board_permission_id_seq', 1, false);


--
-- Name: invite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.invite_id_seq', 1, false);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.post_id_seq', 1, false);


--
-- Name: superusers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.superusers_id_seq', 1, true);


--
-- Name: thread_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.thread_id_seq', 1, false);


--
-- Name: thread_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.thread_permission_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hlz
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: board_permission board_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.board_permission
    ADD CONSTRAINT board_permission_pkey PRIMARY KEY (id);


--
-- Name: board board_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.board
    ADD CONSTRAINT board_pkey PRIMARY KEY (id);


--
-- Name: invite invite_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.invite
    ADD CONSTRAINT invite_pkey PRIMARY KEY (id);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: superusers superusers_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.superusers
    ADD CONSTRAINT superusers_pkey PRIMARY KEY (id);


--
-- Name: thread_permission thread_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.thread_permission
    ADD CONSTRAINT thread_permission_pkey PRIMARY KEY (id);


--
-- Name: thread thread_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.thread
    ADD CONSTRAINT thread_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: hlz
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

