import sqlite3

def deletar_cliente(id):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    print(f"Cliente com ID {id} deletado com sucesso.")