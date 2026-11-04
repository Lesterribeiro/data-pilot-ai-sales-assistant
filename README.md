Data Pilot AI Sales Assistant
Assistente Inteligente de Vendas desenvolvido com Python, Streamlit e OpenRouter utilizando Function Calling para responder perguntas sobre indicadores de negócio.

Objetivo
O Data Pilot demonstra como combinar análise de dados e Inteligência Artificial para:

Processar dados de vendas;
Calcular métricas de negócio;
Exibir dashboards interativos;
Permitir consultas em linguagem natural;
Garantir que os cálculos sejam realizados pelo Python e não inventados pela IA.
Funcionalidades
Dashboard
Receita Total
Total de Pedidos
Ticket Médio
Clientes Únicos
Receita Mensal
Top 5 Cidades
Filtro por Categoria
Assistente Inteligente
Perguntas suportadas:

Qual a receita total?
Quantos pedidos foram concluídos?
Qual o ticket médio?
Qual a taxa de cancelamento?
Qual a receita média por cliente?
Qual a receita por período?
Tecnologias Utilizadas
Python
Pandas
Streamlit
Plotly
OpenRouter
OpenAI SDK
Function Calling
Estrutura do Projeto
data-pilot-ai-sales-assistant/

├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── CHECKLIST.md
├── ARCHITECTURE.md
├── CHANGELOG.md

├── assets/
├── data/
├── tests/

└── src/
    ├── config/
    ├── data/
    ├── services/
    ├── tools/
    └── ui/
Dataset
O projeto utiliza um arquivo chamado:

sales.csv
Os requisitos do dataset estão documentados em:

data/README_DATASET.md
Ferramentas Disponíveis
total_revenue
total_orders
average_ticket
unique_customers
cancellation_rate
revenue_per_customer
get_revenue_by_period
Melhorias Implementadas
Receita Média por Cliente
Receita por Período
Ranking de Cidades
Estrutura preparada para Function Calling
Configuração
Criar um arquivo .env baseado em:

.env.example
Exemplo:

OPENROUTER_API_KEY=your_api_key_here
MODEL=openrouter/free
Execução
streamlit run app.py
Evidências
As evidências de execução poderão ser armazenadas na pasta:

assets/
Exemplos:

dashboard.png
chat.png
architecture.png
Documentação Complementar
ARCHITECTURE.md
CHANGELOG.md
CHECKLIST.md
data/README_DATASET.md
Autor
Projeto desenvolvido para fins de estudo e prática de análise de dados com Inteligência Artificial.
