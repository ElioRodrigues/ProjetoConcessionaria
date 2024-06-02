import sqlite3

def inserir_dados_do_carro(tipo, n_portas, potencia, ano):
    conexao = sqlite3.connect('main.sqlite')
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO carros (tipo, n_portas, potencia, ano)
        VALUES (?, ?, ?, ?)
    """, (tipo, n_portas, potencia, ano))
    conexao.commit()

if __name__ == "__main__":
    tipo = input('Digite o tipo do carro: ')
    n_portas = int(input("Informe a quantidade de portas: "))
    potencia = float(input("Informe a potência do carro em cavalos: "))
    ano = int(input("Informe o ano do carro: "))
    inserir_dados_do_carro(tipo, n_portas, potencia, ano)