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

conexao = sqlite3.connect('main.sqlite')
cursor = conexao.cursor()

criar_tabela()

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
    print("\n 10- Sair\n")

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
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção Inválida!")

