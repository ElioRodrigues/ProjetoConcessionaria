# Modelo Entidade-Relacionamento (MER)

## Diagrama

## Descrição das Entidades e Relações

### Entidades

#### Cliente
- **ID** (Primary Key)  
  - Tipo: Inteiro
  - Descrição: Identificador único do cliente.
- **Nome**
  - Tipo: Texto
  - Descrição: Nome completo do cliente.
- **Email**
  - Tipo: Texto
  - Descrição: Endereço de email do cliente.
- **Telefone**
  - Tipo: Texto
  - Descrição: Número de telefone do cliente.

#### Pedido
- **ID** (Primary Key)
  - Tipo: Inteiro
  - Descrição: Identificador único do pedido.
- **Data**
  - Tipo: Data
  - Descrição: Data do pedido.
- **Cliente_ID** (Foreign Key)
  - Tipo: Inteiro
  - Descrição: Identificador do cliente que fez o pedido.
- **Total**
  - Tipo: Decimal
  - Descrição: Valor total do pedido.

### Relações

- **Cliente** 1---N **Pedido**
  - Um Cliente pode fazer muitos Pedidos.
  - Cada Pedido pertence a um Cliente específico.
