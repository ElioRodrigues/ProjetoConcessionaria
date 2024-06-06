import sqlite3
import bcrypt

def inserir_usuario(username, senha):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    
    hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute('''
        INSERT INTO usuarios (username, senha) VALUES (?, ?)
    ''', (username, hashed))
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    inserir_usuario('admin', 'admin')
    print("Usuário admin inserido.")
