import sqlite3

def deletar_carro(id):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM carros WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    print(f"Carro com ID {id} deletado com sucesso.")
