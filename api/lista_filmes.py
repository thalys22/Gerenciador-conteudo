import urllib.request
import json
import os

def resultado_filmes(tipo):
  api_key = os.getenv('TMDB_API_KEY')
  if tipo == 'Populares':
    url = f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key={api_key}'
  elif tipo == "Animação":
    url = f'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key={api_key}'
  elif tipo == "2010":
    url = f'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key={api_key}'
  
  resposta = urllib.request.urlopen(url)
  dados = resposta.read()
  dados_json = json.loads(dados)
  return dados_json['results']