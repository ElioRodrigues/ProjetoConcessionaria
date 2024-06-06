import sqlite3
from criar_tabela import criar_tabela
from inserir_dados_carros import inserir_dados_do_carro
from listar_carros import listar_carros
from deletar import deletar_carro
from alterar import alterar_dados
from listar_clientes import listar_clientes
from vendas import inserir_venda, inserir_carro_venda, listar_vendas
from inserir_cliente import inserir_cliente
from deletar_cliente import deletar_cliente
from criar_tabela_usuarios import criar_tabela_usuarios
from inserir_usuario import inserir_usuario
from verificar_login import verificar_login
from listar_tabelasurpresa import listar_tabelasurpresa
from tabelasurpresa import tabelasurpresa

conexao = sqlite3.connect('main.sqlite')
cursor = conexao.cursor()

# Criar tabelas
criar_tabela()
criar_tabela_usuarios()
tabelasurpresa()

# Função para registrar novos usuários
def registrar_usuario():
    username = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    inserir_usuario(username, senha)
    print("Usuário registrado com sucesso!")

# Função de login
def login():
    print("Bem-vindo! Faça login para continuar.")
    username = input("Usuário: ")
    senha = input("Senha: ")
    if verificar_login(username, senha):
        print("Login bem-sucedido!")
        return True
    else:
        print("Usuário ou senha incorretos!")
        return False

# Função principal
def main():
    while True:
        print("\n ******MENU******")
        print("\n 1- Cadastrar Carros")
        print("\n 2- Listar Carros")
        print("\n 3- Deletar Carros")
        print("\n 4- Alterar Dados de Carros")
        print("\n 5- Cadastrar Clientes")
        print("\n 6- Listar Clientes")
        print("\n 7- Deletar Clientes")
        print("\n 8- Realizar Venda")
        print("\n 9- Listar Vendas")
        print("\n 10- Tabela Surpresa")
        print("\n 11- Sair\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input('Digite o tipo do carro: ')
            n_portas = int(input("Informe a quantidade de portas: "))
            potencia = float(input("Informe a potência do carro em cavalos: "))
            ano = int(input("Informe o ano do carro: "))
            inserir_dados_do_carro(tipo, n_portas, potencia, ano)

        elif escolha == "2":
            listar_carros()

        elif escolha == "3":
            listar_carros()
            id_carro = int(input("Digite o ID do carro que deseja deletar: "))
            deletar_carro(id_carro)
            print("Lista atualizada de carros: ")
            listar_carros()

        elif escolha == "4":
            listar_carros()
            id = int(input("Digite o id do carro que deseja alterar os dados: "))
            tipo = input("Digite o tipo do carro atualizado: ")
            n_portas = int(input("Digite o número de portas atualizado: "))
            potencia = float(input("Digite a potência do carro atualizado: "))
            ano = int(input("Digite o ano do carro atualizado: "))
            alterar_dados(tipo, n_portas, potencia, ano, id)

        elif escolha == "5":
            nome = input('Digite o nome do cliente: ')
            email = input("Informe o email do cliente: ")
            telefone = input("Informe o telefone do cliente: ")
            inserir_cliente(nome, email, telefone)

        elif escolha == "6":
            listar_clientes()

        elif escolha == "7":
            listar_clientes()
            id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))
            deletar_cliente(id_cliente)
            print("Lista atualizada de clientes: ")
            listar_clientes()

        elif escolha == "8":
            listar_clientes()
            id_cliente = int(input("Digite o ID do cliente: "))
            data_venda = input("Digite a data da venda (YYYY-MM-DD): ")
            id_venda = inserir_venda(id_cliente, data_venda)
            listar_carros()
            id_carro = int(input("Digite o ID do carro vendido: "))
            preco_venda = float(input("Digite o preço da venda: "))
            inserir_carro_venda(id_venda, id_carro, preco_venda)

        elif escolha == "9":
            listar_vendas()
            
        elif escolha == "10":
            listar_tabelasurpresa()

        elif escolha == "11":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção Inválida!")

# Função inicial para login ou registro
def iniciar():
    while True:
        print("\n ******MENU INICIAL******")
        print("\n 1- Login")
        print("\n 2- Registrar Usuário")
        print("\n 3- Sair\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if login():
                main()
                break

        elif escolha == "2":
            registrar_usuario()

        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    iniciar()
