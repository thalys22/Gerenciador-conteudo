import sqlite3

conn = sqlite3.connect('livros.sqlite3')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print('tables:', tables)
conn.close()
