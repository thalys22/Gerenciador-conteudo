
# Gerenciador de Conteúdo

Aplicação web robusta desenvolvida em Python com Flask para a gestão centralizada de catálogos de livros, registros de notas e exploração de listas de filmes. O projeto utiliza uma arquitetura modular preparada para escalabilidade e deploy serverless (Vercel), com persistência de dados via SQLAlchemy.

### 1. Visão Geral

A aplicação funciona como um hub de gerenciamento pessoal, integrando diferentes módulos de dados em uma interface unificada. Inclui:
* **Gestão de Livros:** CRUD completo (Criação, Leitura, Atualização e Deleção) com persistência em banco SQLite.
* **Sistema de Paginação:** Listagem eficiente de itens com navegação entre páginas.
* **Diário de Registros:** Módulo para cadastro de notas e alunos (armazenamento em memória).
* **Catálogo de Filmes:** Filtros dinâmicos de títulos baseados em categorias.
* **Pronto para Nuvem:** Configuração otimizada para execução em infraestruturas serverless como Vercel.

**Autor:** Thalys dos Santos
**Versão:** 1.0.0

### 2. Arquitetura (Camadas)

* **Interface (App):** Templates dinâmicos em Jinja2 localizados em `api/templates/`, utilizando um layout base (`base.html`) para herança de componentes visuais.
* **Controladores (Routes):** Camada de roteamento em `api/routes.py` que separa a lógica de navegação das definições de dados.
* **Domínio (Models):** Definição da entidade `Livro` em `api/livro.py` utilizando o padrão declarativo do SQLAlchemy.
* **Infrastructure/Extensions:** Configurações de banco de dados e extensões do Flask centralizadas em `api/extensions.py` e `api/__init__.py`.

**Pipeline de Dados**
1. O usuário submete dados via formulários na interface Web.
2. O Flask recebe a requisição e valida a presença de campos obrigatórios.
3. Para **Livros**: Os dados são convertidos em objetos de modelo e persistidos no arquivo `livros.sqlite3`.
4. Para **Filmes/Diário**: O processamento ocorre via lógica de dicionários e listas (voláteis ou estruturadas).
5. A aplicação renderiza a resposta utilizando o motor Jinja2, injetando os dados processados nos templates.

### 3. Estrutura do Repositório e Arquitetura

O projeto adota a separação de responsabilidades para facilitar a manutenção e o deploy independente:

```text
┌─────────────────────────────────────────────────────────────────┐
│                        INTERFACE LAYER                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │          Templates HTML (api/templates/)                 │   │
│  │  • base.html (Estrutura Global)                          │   │
│  │  • livros.html (Galeria com Paginação)                   │   │
│  │  • novo_livro.html (Cadastro)                            │   │
│  └────────────────────┬─────────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │       Roteamento e Lógica (api/routes.py)                │   │
│  │  • Controle de CRUD                                      │   │
│  │  • Filtros de Filmes (api/lista_filmes.py)               │   │
│  └────────────────────┬─────────────────────────────────────┘   │
└───────────────────────┼─────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DOMAIN & STORAGE                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │    Persistência (api/livro.py & SQLite)                  │   │
│  │  • ORM SQLAlchemy                                         │   │
│  │  • Instância de Banco local/produção                     │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘

```

**Estrutura de Diretórios Detalhada**

Plaintext

```
gerenciador-conteudo/
│
├── api/                      # Diretório principal da aplicação
│   ├── templates/            # Views (HTML/Jinja2)
│   ├── __init__.py           # Factory da aplicação
│   ├── routes.py             # Controladores de rotas
│   ├── livro.py              # Modelo da Entidade Livro
│   ├── extensions.py         # Configuração do SQLAlchemy
│   ├── lista_filmes.py       # Lógica de negócio para filmes
│   └── instance/             # Localização do banco de dados SQLite
│
├── requirements.txt          # Dependências do ecossistema Python
├── vercel.json               # Configurações de deploy Serverless
└── README.md                 # Documentação do projeto

```

### 4. Instalação

Pré-requisitos: Python 3.10+ e pip instalados.

Bash

```
# Clone o repositório
git clone [https://github.com/seu-usuario/gerenciador-conteudo.git](https://github.com/seu-usuario/gerenciador-conteudo.git)

# Acesse a pasta
cd gerenciador-conteudo

# Instale as dependências
pip install -r requirements.txt

```

### 5. Configuração do Banco de Dados

A aplicação está configurada para criar o banco de dados automaticamente se ele não existir. Caso precise resetar ou criar manualmente via script:

1.  Verifique o arquivo `api/setup_db.py`.
    
2.  Execute para inicializar a estrutura:
    

Bash

```
python api/setup_db.py

```

### 6. Execução Local

Para rodar o servidor de desenvolvimento:

Bash

```
# No diretório raiz
flask --app api/app.py run

```

Acesse: `http://127.0.0.1:5000/`

### 7. Endpoints Principais

**Recurso**

**Método**

**Descrição**

`/`

GET/POST

Home: Adiciona conteúdos rápidos em memória.

`/livros`

GET

Listagem de livros com suporte a paginação.

`/add_livro`

POST

Cadastro de novo título no banco de dados.

`/edit/<id>`

POST

Atualização de informações de um livro existente.

`/delete/<id>`

GET

Remoção de registro do banco de dados.

`/filmes/<prop>`

GET

Listagem dinâmica de filmes por categoria.

`/diario`

POST

Registro de notas e alunos no módulo diário.

### 8. Gestão de Dados e Paginação

Diferente de sistemas simples, este gerenciador utiliza o método `.paginate()` do SQLAlchemy. Isso garante que, mesmo com centenas de livros, a aplicação carregue apenas uma fração por vez (padrão de 2 itens por página no código atual), otimizando o consumo de memória do navegador.

### 9. Tecnologias Utilizadas

-   **Framework:** Flask (Python)
    
-   **ORM:** Flask-SQLAlchemy
    
-   **Banco de Dados:** SQLite (Relacional)
    
-   **Templates:** Jinja2
    
-   **Configuração Cloud:** Vercel Runtime para Python
    

### 10. Deploy (Vercel)

Este projeto foi estruturado para ser implantado no Vercel com zero configuração adicional, utilizando o arquivo `vercel.json` que aponta para o entrypoint `api/app.py`. Para publicar:

1.  Conecte o repositório ao dashboard do Vercel.
    
2.  O Vercel detectará automaticamente as configurações e fará o build.
    

### 11. Créditos

Projeto desenvolvido por Thalys dos Santos para fins de gerenciamento de portfólio e organização de conteúdos, para demonstração.