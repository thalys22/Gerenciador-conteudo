# Gerenciador de Conteúdo - App Flask

Aplicação web desenvolvida em Python com Flask para o gerenciamento de um catálogo pessoal e registros diários. O sistema oferece operações CRUD completas integradas a um banco de dados em nuvem para gerenciar livros, além de manter listas em memória para anotações rápidas e registros de notas de alunos. Também inclui uma integração para listagem dinâmica de filmes e suporte a deploy Serverless (na Vercel).

## 1. Visão Geral

A aplicação expõe uma interface web focada na simplicidade de uso para gerenciar diferentes tipos de informações. Inclui:

- **Módulo de Livros (CRUD):** Permite cadastrar, listar (com paginação), atualizar e excluir livros do acervo, com persistência em banco de dados hospedado via SQLAlchemy.
- **Módulo de Diário/Notas:** Formulário para registrar alunos e suas respectivas notas.
- **Módulo de Filmes:** Rota dinâmica que lista filmes baseados em propriedades específicas.
- **Anotações Rápidas:** Sistema simples na página inicial para adicionar conteúdos em uma lista temporária.

**Autor:** Thalys dos Santos

## 2. Tecnologias Utilizadas

- **Flask:** Microframework Web e roteamento HTTP (v3.1+).
- **Flask-SQLAlchemy:** ORM para manipulação do banco de dados relacional.
- **PostgreSQL / Supabase:** Banco de dados relacional oficial hospedado na nuvem (Connection Pooling).
- **Python-dotenv:** Ferramenta para gerenciar credenciais e chaves criptografadas (arquivos `.env`).
- **Jinja2:** Motor de templates para renderização de páginas HTML.
- **Vercel:** Configurações (em `vercel.json`) nativas para provisionamento através do Serverless.

## 3. Estrutura de Diretórios

O projeto segue a estrutura padrão de uma aplicação Flask adaptada para plataformas Serverless.

```plaintext
Flask2/
│   
├── api/                        # Diretório principal da aplicação raiz (para compatibilidade Vercel)
│   ├── app.py                  # Instância aplicação Flask e mapeamento de rotas principais
│   ├── livro.py                # Modelo SQLAlchemy para tabela de "Livros"
│   ├── lista_filmes.py         # Arquivo com listas de filmes (ação, comédia, etc) e respectivo gerenciador
│   ├── extensions.py           # Módulo extra contendo instâncias isoladas, como `db`
│   ├── setup_db.py             # Script manual e isolado para criação programática das tabelas
│   └── templates/              # Páginas e estruturas visuais HTML baseadas em Jinja2
│
├── .env                        # [Arquivo secreto local] Armazena as variáveis de configuração como DATABASE_URL
├── scripts/                    # Scripts adicionais de manutenção do projeto
├── requirements.txt            # Definição de pacotes Python dependentes
├── vercel.json                 # Arquivo de configuração de roteamento/build Vercel
└── README.md                   # Documentação do projeto

## 4. Como Executar (Ambiente Local)

Pré-requisitos: Python 3.9+ instalado em seu ambiente.

1.  **Clone do repositório/pasta do projeto**.
2.  **Crie um arquivo na raiz chamado  `.env`**  contendo a conexão de banco de dados e suas chaves:
    
    env
    
    DATABASE_URL="postgresql://SEU_USUARIO:SUA_SENHA@aws-1-us-east-1.pooler.supabase.com:6543/postgres"
    
3.  **Ativação e Criação de Ambiente Virtual:**
    
    powershell
    
    python -m venv .venv
    
    .\.venv\Scripts\activate
    
4.  **Instalação das Bibliotecas Necessárias:**
    
    powershell
    
    pip install -r requirements.txt
    
5.  **Rodar Aplicação Flask:**  Dado que a aplicação está alocada na pasta  `api`, inicie o servidor com o seguinte comando (estando no diretório principal do projeto):
    
    powershell
    
    flask --app api.app run --debug
    
6.  Acesse no navegador:  `http://127.0.0.1:5000/`

## 5. Endpoints Principais

Endpoint

Método

Descrição

`/`

GET / POST

Renderiza a Home e permite adicionar notas rápidas na lista  `conteudos`.

`/diario`

GET / POST

Formulário de notas. Adiciona aluno e nota na lista em memória.

`/filmes/<prop>`

GET

Lista filmes baseado em uma propriedade dinâmica passada na URL.

`/livros`

GET

Lista todos os livros cadastrados no banco, organizados por paginação.

`/add_livro`

GET / POST

Exibe formulário e cadastra um novo livro no banco.

`/<id>/atualiza_livro`

GET / POST

Exibe formulário preenchido e atualiza os dados do livro correspondente.

`/<id>/remove_livro`

GET

Exclui imediatamente o livro do banco e redireciona para a listagem.

## 6. Persistência de Dados e Deploy

As arquiteturas "Serverless" como a da Vercel "congelam" os repositórios, portanto requerem estratégias exclusivas de salvamento:

-   **Persistentes (Banco Supabase):**  Os campos da rota  `/livros`  (CRUD) são salvos de forma descentralizada na nuvem dentro de um PostgreSQL (Supabase) via Pooler de Conexões. Esses dados jamais se perdem a atualização do server.
-   **Memória (Volátil):**  O "Diário de Notas" ou as "Anotações" da home baseiam-se em listas python instanciadas em fluxo. Durante o  _Cold Start_  do Vercel Web Server (inatividade ou reinicialização), as variáveis voltarão a ser listas vazias.