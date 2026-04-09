from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'
db = SQLAlchemy()
db.init_app(app)

from projeto import routes

# comando para inicar o servidor flask --app projeto run --debug
# pip list > requirements.txt