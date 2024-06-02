import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(255),
            n_portas INT,
            potencia REAL,
            ano INT
        );
    """)
    conexao.commit()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            telefone VARCHAR(255) NOT NULL
        );
    """)
    conexao.commit()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            vendas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            data_venda DATE NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        );
    """)
    conexao.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carro_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venda INTEGER NOT NULL,
            id_carro INTEGER NOT NULL,
            preco_venda REAL NOT NULL,
            FOREIGN KEY (id_venda) REFERENCES vendas(vendas_id),
            FOREIGN KEY (id_carro) REFERENCES carros(id)
        );
    ''')
    conexao.commit()

if __name__ == "__main__":
    criar_tabela()