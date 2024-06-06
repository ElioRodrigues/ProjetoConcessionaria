import sqlite3

def listar_tabelasurpresa():
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM tabelasurpresa')
        surpresa = cursor.fetchall()
        for task in surpresa:
            print(task)
