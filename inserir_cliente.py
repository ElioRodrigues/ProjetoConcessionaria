import sqlite3

def inserir_cliente(nome, email, telefone):
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
        ''', (nome, email, telefone))
        conexao.commit()
