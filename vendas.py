import sqlite3

def inserir_venda(id_cliente, data_venda):
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
        INSERT INTO vendas (id_cliente, data_venda)
        VALUES (?, ?)
        ''', (id_cliente, data_venda))
        conexao.commit()
        return cursor.lastrowid

def inserir_carro_venda(id_venda, id_carro, preco_venda):
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
        INSERT INTO carro_venda (id_venda, id_carro, preco_venda)
        VALUES (?, ?, ?)
        ''', (id_venda, id_carro, preco_venda))
        conexao.commit()


def listar_vendas():
    with sqlite3.connect('main.sqlite') as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM vendas')
        vendas = cursor.fetchall()
        for vendas in vendas:
          print(vendas)