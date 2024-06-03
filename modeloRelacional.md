Modelo Relacional
Tabela clientes
Campo	Tipo	Restrição
id	INTEGER	PRIMARY KEY
nome	VARCHAR(255)	NOT NULL
email	VARCHAR(255)	NOT NULL
telefone	VARCHAR(255)	NOT NULL
Tabela carros
Campo	Tipo	Restrição
id	INTEGER	PRIMARY KEY
tipo	VARCHAR(255)	
n_portas	INT	
potencia	REAL	
ano	INT	
Tabela vendas
Campo	Tipo	Restrição
vendas_id	INTEGER	PRIMARY KEY
id_cliente	INTEGER	NOT NULL, FOREIGN KEY
data_venda	DATE	NOT NULL
Tabela carro_venda
Campo	Tipo	Restrição
id	INTEGER	PRIMARY KEY
id_venda	INTEGER	NOT NULL, FOREIGN KEY
id_carro	INTEGER	NOT NULL, FOREIGN KEY
preco_venda	REAL	NOT NULL
Descrição
Clientes: Armazena informações sobre os clientes.
Carros: Armazena informações sobre os carros disponíveis na concessionária.
Vendas: Armazena informações sobre as vendas realizadas, ligando o cliente à venda.
Carro_Venda: Armazena informações sobre quais carros foram vendidos em cada venda, junto com o preço de venda de cada carro.
Relações
Cada cliente pode fazer várias compras (vendas), mas cada venda é associada a um único cliente.
Cada venda pode incluir vários carros, mas cada carro vendido está relacionado a uma venda específica.
A tabela carro_venda é uma tabela de relacionamento que conecta vendas e carros, permitindo a venda de múltiplos carros em uma única transação.