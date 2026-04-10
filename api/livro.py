from .extensions import db

class livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Integer)
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
  # No interpretador 
  
  #from app import app
  #from app import db
  #from livro import livro
  #app.app_context().push()
  #db.create_all()