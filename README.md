

# App Flask - Gerenciador de Catálogo e Registros

Aplicação web desenvolvida em Python com Flask para o gerenciamento de um catálogo pessoal e registros diários. O sistema oferece operações CRUD completas integradas a um banco de dados para gerenciar livros, além de manter listas em memória para anotações rápidas e registros de notas de alunos. Também inclui uma integração para listagem dinâmica de filmes.

### 1. Visão Geral

A aplicação expõe uma interface web focada na simplicidade de uso para gerenciar diferentes tipos de informações. Inclui:
* **Módulo de Livros (CRUD):** Permite cadastrar, listar (com paginação), atualizar e excluir livros do acervo, com persistência em banco de dados via SQLAlchemy.
* **Módulo de Diário/Notas:** Formulário para registrar alunos e suas respectivas notas.
* **Módulo de Filmes:** Rota dinâmica que lista filmes baseados em propriedades específicas.
* **Anotações Rápidas:** Sistema simples na página inicial para adicionar conteúdos em uma lista temporária.

**Autor:** Thalys dos Santos
**Versão:** 1.0.0

### 2. Arquitetura (Camadas)

* **Interface (App):** Templates HTML (Jinja2) renderizados pelo Flask (`templates/`), responsáveis pela exibição dos dados e formulários de entrada.
* **Controllers/Rotas:** O arquivo `routes.py` gerencia as requisições HTTP (GET/POST), processa dados de formulários e orquestra a lógica de navegação.
* **Application/Service:** Lógica de listagem de filmes encapsulada em `lista_filmes.py`.
* **Infrastructure (Banco de Dados):** Uso do `Flask-SQLAlchemy` para mapeamento objeto-relacional (ORM) e persistência da entidade Livro no banco de dados SQLite.

**Pipeline de Dados**
1. Usuário acessa as rotas e interage com os formulários HTML.
2. Dados enviados via POST são capturados pelo `request.form` no Flask.
3. Para registros temporários (Diário/Conteúdos), os dados são anexados em listas na memória do servidor.
4. Para o catálogo de livros, os dados são instanciados na classe `livro` e persistidos via `db.session`.
5. O servidor processa as alterações e redireciona o usuário atualizando a visualização (View).

### 3. Estrutura do Repositório e Arquitetura

O projeto adota o padrão MVC (Model-View-Controller) adaptado para o ecossistema do microframework Flask:

```text
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACE LAYER (Views)                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │          Templates HTML (Jinja2)                         │   │
│  │  • index.html (Anotações/Home)                           │   │
│  │  • livros.html / novo_livro.html (Catálogo)              │   │
│  │  • sobre.html (Diário de Notas)                          │   │
│  │  • filmes.html (Listagem)                                │   │
│  └────────────────────┬─────────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER (Controllers)            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │       Roteamento Flask (routes.py)                       │   │
│  │  • Gerenciamento de Requisições (GET/POST)               │   │
│  │  • Lógica de Paginação de Livros                         │   │
│  │  • Integração com lista_filmes.py                        │   │
│  └────────────────────┬─────────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                      DOMAIN & INFRA (Models/DB)                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │       Persistência de Dados                              │   │
│  │  • livro.py (Modelo SQLAlchemy)                          │   │
│  │  • instance/livros.sqlite3 (Banco SQLite)                │   │
│  │  • Listas em Memória (conteudos, registros)              │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘

```

**Estrutura de Diretórios Detalhada**

Plaintext

```
app_flask/
│
├── projeto/
│   ├── __init__.py           # Inicialização do app e do SQLAlchemy
│   ├── routes.py             # Controladores e Endpoints da API/Web
│   ├── livro.py              # Modelo de banco de dados (Livro)
│   ├── lista_filmes.py       # Lógica e dados do catálogo de filmes
│   └── templates/            # Arquivos HTML de interface
│       ├── index.html
│       ├── sobre.html
│       ├── filmes.html
│       ├── livros.html
│       ├── novo_livro.html
│       └── atualiza_livro.html
│
├── instance/                 
│   └── livros.sqlite3        # Banco de dados persistente
│
├── requirements.txt          # Dependências do projeto
└── .gitignore                # Regras de exclusão

```

### 4. Instalação

Pré-requisitos: Python 3.10+ instalado.

Bash

```
# Clone o repositório e acesse a pasta do projeto
# (Opcional) Crie e ative um ambiente virtual: python -m venv venv

# Instale as dependências
pip install -r requirements.txt

```

### 5. Configuração

As configurações de inicialização e do banco de dados (URI do SQLAlchemy) estão definidas em `projeto/__init__.py`. Ao executar pela primeira vez, certifique-se de que o contexto da aplicação gere as tabelas do banco de dados caso não existam.

### 6. Execução Local

Iniciar a aplicação localmente:

Bash

```
flask --app projeto run
# ou
python -m flask run

```

Acesso via navegador: `http://127.0.0.1:5000/`

### 7. Processamento Principal (CRUD de Livros)

Executado via `routes.py` utilizando o modelo `livro.py`.

-   **Create:** `adiciona_livro()` captura os dados do form e usa `db.session.add()`.
    
-   **Read:** `lista_livros()` consulta o banco usando `livro.query.paginate()` para organizar a exibição em páginas (2 itens por página).
    
-   **Update:** `atualiza_livro(id)` filtra pelo ID e atualiza os campos via `.update({})`.
    
-   **Delete:** `remove_livro(id)` exclui o registro permanentemente do banco com `db.session.delete()`.
    

### 8. Modelo de Dados

A entidade principal do banco de dados é gerida pelo SQLAlchemy em `livro.py`:

-   `id`: Chave Primária (Integer).
    
-   `nome`: Título do livro (String, max 50).
    
-   `descricao`: Resumo da obra (String, max 100).
    
-   `valor`: Preço ou avaliação numérica (Integer).
    

### 9. Endpoints Principais

**Endpoint**

**Método**

**Descrição**

`/`

GET / POST

Renderiza a Home e permite adicionar notas rápidas na lista `conteudos`.

`/diario`

GET / POST

Formulário de notas. Adiciona aluno e nota na lista `registros`.

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

### 10. Validação de Dados e Formulários

A captação de dados é feita diretamente pelo objeto `request.form` do Flask. Condicionais lógicas (ex: `if request.form.get("aluno")`) garantem que strings vazias ou nulas não sejam processadas inadvertidamente nas listas temporárias.

### 11. Exemplos de Uso (Interface)

1.  **Anotações:** Acesse a rota `/` (Home), digite um texto no campo e clique em enviar. O conteúdo aparecerá imediatamente listado abaixo.
    
2.  **Gerir Livros:** Acesse `/livros` para ver o acervo. Clique no botão de adicionar para inserir "O Senhor dos Anéis", descrição "Fantasia Épica" e valor "50". Salve e veja a lista atualizada.
    
3.  **Páginas dinâmicas:** Acesse `/filmes/acao` para que o servidor processe a propriedade "acao" e retorne a lista de filmes correspondente (via `lista_filmes.py`).
    

### 12. Gestão de Dados Temporários vs Persistentes

O aplicativo trabalha com dois tipos de retenção de dados:

-   **Memória (Volátil):** As variáveis globais `conteudos = []` e `registros = []` armazenam as anotações e o diário de notas. Estes dados são perdidos se o servidor for reiniciado.
    
-   **Banco de Dados (Persistente):** O catálogo de livros utiliza o SQLite. Os dados sobrevivem à reinicialização da aplicação.
    

### 13. Feedback e Navegação (Observabilidade UI)

A interface orquestra a navegação do usuário através de redirecionamentos diretos após ações de escrita no banco de dados. Ao adicionar, editar ou remover um livro, o sistema processa o `.commit()` e utiliza `redirect(url_for('lista_livros'))` para garantir que o usuário veja a base de dados sempre atualizada sem reenvio acidental de formulários.

### 14. Tecnologias

-   **Flask:** Microframework Web e roteamento HTTP.
    
-   **Flask-SQLAlchemy:** ORM para manipulação do banco de dados relacional.
    
-   **SQLite3:** Banco de dados integrado, leve e ideal para ambientes de desenvolvimento.
    
-   **Jinja2:** Motor de templates para renderização dinâmica e interpolação de variáveis em HTML.
    
-   **HTML5/CSS3:** Estruturação visual das páginas.
    

### 15. Scripts Úteis

**Módulo**

**Função**

`routes.py`

Coração lógico da aplicação. Roteia URLs e conecta a interface ao banco de dados e listas.

`livro.py`

Define o schema da tabela de livros para o SQLAlchemy criar e gerir as colunas.

`lista_filmes.py`

Lógica extraída para processar e retornar dicionários/listas de filmes para a view principal.

### 16. Deploy e Infraestrutura

Para implantação em plataformas na nuvem (como Render, Heroku ou Azure), recomenda-se a substituição do servidor de desenvolvimento nativo do Flask por um WSGI Server robusto de produção, como o **Gunicorn** (`gunicorn projeto:app`), e a parametrização da porta de rede através de variáveis de ambiente (`PORT`).


### 17. Créditos

Projeto desenvolvido no curso trilha Pyhton
