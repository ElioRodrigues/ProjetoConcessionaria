import sqlite3

def tabelasurpresa():
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabelasurpresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    tabelasurpresa()
