import sqlite3
import bcrypt

def verificar_login(username, senha):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT senha FROM usuarios WHERE username = ?
    ''', (username,))
    registro = cursor.fetchone()
    conexao.close()
    
    if registro:
        hashed = registro[0]
        if bcrypt.checkpw(senha.encode('utf-8'), hashed):
            return True
    
    return False

if __name__ == "__main__":
    print(verificar_login('admin', 'admin'))  # Substitua pelos dados reais para teste
