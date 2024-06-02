import sqlite3

def alterar_dados(tipo, n_portas, potencia, ano, id):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE carros SET tipo = ?, n_portas = ?, potencia = ?, ano = ?
        WHERE id = ?
    """, (tipo, n_portas, potencia, ano, id))
    conexao.commit()