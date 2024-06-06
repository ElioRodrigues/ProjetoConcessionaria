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
        cursor.execute('''SELECT vendas_id, id_cliente, data_venda FROM vendas''')
        vendas = cursor.fetchall()
        for venda in vendas:
            print(f"ID da venda: {venda[0]}")
            print(f"ID do cliente: {venda[1]}")
            print(f"Data da venda: {venda[2]} \n") 
        cursor.execute('''SELECT id_carro, preco_venda FROM carro_venda''')
        carro_vendas = cursor.fetchall()
        for carro_venda in carro_vendas:
            print(f"ID do carro: {carro_venda[0]}")
            print(f"Preço da venda: {carro_venda[1]}")
            
        