import sqlite3

def criar_tabela_usuarios():
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabela_usuarios()
