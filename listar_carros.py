import sqlite3

def listar_carros():
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()

    carros = cursor.execute("""
        SELECT id, tipo, n_portas, potencia, ano FROM carros
    """).fetchall()

    for carro in carros:
        print(carro)

if __name__ == "__main__":
    listar_carros()