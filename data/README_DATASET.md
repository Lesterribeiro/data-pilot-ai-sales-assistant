Dataset de Vendas
Este projeto utiliza um arquivo chamado sales.csv.

O dataset deve conter, no mínimo, as seguintes colunas:

Coluna	Tipo	Descrição
order_id	inteiro	Identificador do pedido
customer_id	inteiro	Identificador do cliente
date	data	Data da venda
city	texto	Cidade da venda
category	texto	Categoria do produto
product	texto	Nome do produto
quantity	inteiro	Quantidade vendida
price	decimal	Preço unitário
status	texto	Status do pedido
Exemplo
order_id,customer_id,date,city,category,product,quantity,price,status
1,101,2024-01-05,São Paulo,Eletrônicos,Fone Bluetooth,2,120.00,completed
2,102,2024-01-07,Rio de Janeiro,Informática,Mouse Gamer,1,80.00,canceled
Arquivos Esperados
data/
├── sales.csv
└── sales_clean.csv
Observações
O arquivo sales.csv deverá ser inserido futuramente para execução da aplicação e geração das métricas.
