from flask import Flask, render_template, request
from flask import render_template, request, redirect, url_for
from .lista_filmes import resultado_filmes
from .extensions import db
from .livro import livro
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/livros.sqlite3'

db.init_app(app)

# Do not auto-create database tables on import (serverless deployments have
# readonly/ephemeral filesystems). Use the `flask create-db` CLI command locally.

@app.cli.command('create-db')
def create_db_command():
  """Create the database tables."""
  with app.app_context():
    db.create_all()
    click.echo('Database tables created.')

conteudos = []
registros = []
# localhost:5000/
@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("conteudo"):
            conteudos.append(request.form.get("conteudo"))
            
    return render_template(
        "index.html",
        conteudos=conteudos
    )

@app.route('/diario', methods=["GET", "POST"])
def diario():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            aluno = request.form.get("aluno") 
            nota = request.form.get("nota")
            registros.append(
                {
                    "aluno": aluno,
                    "nota": nota
                }
            )
    return render_template(
        "sobre.html",
        registros=registros  
    )
    
@app.route('/filmes/<propriedade>', methods=["GET", "POST"])
def lista_filmes(propriedade):
    return render_template(
        "filmes.html", 
        filmes=resultado_filmes(propriedade)
    )
    
@app.route('/livros', methods=["GET", "POST"])
def lista_livros():
  page = request.args.get('page', 1, type=int)
  per_page = 2
  todos_livros = livro.query.paginate(page=page, per_page=per_page)
  return render_template(
    "livros.html",
    livros=todos_livros
  )
  
@app.route('/add_livro', methods=["GET", "POST"])
def adiciona_livro():
  nome = request.form.get('nome')
  descricao = request.form.get('descricao')
  valor = request.form.get('valor')
  if request.method == 'POST':
    livro_add = livro(
      nome,
      descricao,
      valor
    )
    db.session.add(livro_add)
    db.session.commit()
    return redirect(url_for('lista_livros'))
  return render_template(
    "novo_livro.html"
    
  )
  
@app.route('/<int:id>/atualiza_livro', methods=['GET', 'POST'])
def atualiza_livro(id):
  livro_bd = livro.query.filter_by(id=id).first()
  if request.method == 'POST':
    nome = request.form['nome']
    descricao = request.form['descricao']
    valor = request.form['valor']
    
    livro.query.filter_by(id=id).update({
        "nome": nome,
        "descricao": descricao,
        "valor": valor
      })
    db.session.commit()
    return redirect(url_for('lista_livros'))
  return render_template(
    "atualiza_livro.html",
    livro=livro_bd
  )

@app.route('/<int:id>/remove_livro')
def remove_livro(id):
  livro_bd = livro.query.filter_by(id=id).first()
  db.session.delete(livro_bd)
  db.session.commit()
  return redirect(url_for('lista_livros'))

if __name__ == '__main__':
  app.run(debug=True)
  

# comando para inicar o servidor flask --app projeto run --debug
# pip list > requirements.txt