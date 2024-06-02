import sqlite3

def listar_clientes():
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
        for cliente in clientes:
          print(cliente)