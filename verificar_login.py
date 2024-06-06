import sqlite3

def verificar_login(username, senha):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios WHERE username = ? AND senha = ?
    ''', (username, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario is not None

if __name__ == "__main__":
    # Teste da função verificar_login
    print(verificar_login('admin', 'admin'))  # Substitua pelos dados reais para teste
