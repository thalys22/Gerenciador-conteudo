import os
from dotenv import load_dotenv
from app import app
from extensions import db
import livro  # Importa os modelos para o SQLAlchemy reconhecê-los

# Carrega as variáveis do .env 

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
load_dotenv(os.path.join(basedir, '.env'))

# Atualiza a configuração da app para ler o DATABASE_URL do .env em vez do SQLite
database_url = os.environ.get('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

if __name__ == '__main__':
    with app.app_context():
        print(f"Conectando ao banco: {app.config['SQLALCHEMY_DATABASE_URI']}")
        db.create_all()
        print("Tabelas criadas com sucesso no banco de dados!")
