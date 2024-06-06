+----------------+         +-----------------+          +--------------+          +----------------+
|    Clientes    |         |     Vendas      |          |    Carros    |          |  Carro_Venda   |
+----------------+         +-----------------+          +--------------+          +----------------+
| id (PK)        |    1    | vendas_id (PK)  |   N    1 | id (PK)      |    N     | id (PK)        |
| nome           +--------<| id_cliente (FK) +--------<| tipo          +---------<| id_venda (FK)  |
| email          |         | data_venda      |          | n_portas     |          | id_carro (FK)  |
| telefone       |         +-----------------+          | potencia     |          | preco_venda 
   |                                                                              
+----------------+                                      | ano          |          +----------------+
                                                        +--------------+
