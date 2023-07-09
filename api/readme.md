# GERPRO Gerenciador de projetos

GERPRO é uma ferramenta desenvolvida para auxiliar na gestão de projetos.

Features

- Permite criar e deletar projetos;
- Considera os campos de nome do projeto, descrição resumida, datas de início e fim estimado do projeto, Gerente resonsável, status atual e categoria;
- Lista os projetos por ordem de cadastro, para permitir o acompanhamento individualizado;

Tecnologias utilizadas

- Python: Linguagem de programação utilizada no back-end;
- Flask: Framework web para construção da aplicação;
- SQLAlchemy: Biblioteca de Object-Relational Mapping (ORM);
- OpenAPI: Para escrever, produzir, consumir e visualizar serviços da API;
- HTML: Linguagem de markup do front-end;
- Bootstrap: Framework que fornece estruturas de CSS para criação de aplicações front-end;
- Javascript: Linguagem de programação de comportamento que permite a criação de conteúdos dinâmicos;
- SQLite: Banco de dados utilizado para persistência dos dados;

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/project-management-system.git

Navigate to the project directory:

bash

cd project-management-system

Create a virtual environment (optional, but recommended):

bash

python3 -m venv env
source env/bin/activate

Install the required dependencies:

bash

pip install -r requirements.txt

Start the application:

bash

    python app.py

    Access the application in your web browser at http://localhost:5000.

Usage

    Register a new account or log in with your existing credentials.
    Create a project by providing its details such as name, description, start date, and deadline.
    Assign the project to a specific category.
    Update project details as necessary.
    Track project progress and update it accordingly.
    View the list of projects and search for specific projects by name or category.
    Log out when you're done.