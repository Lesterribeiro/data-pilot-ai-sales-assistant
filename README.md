Data Pilot AI Sales Assistant
Assistente Inteligente de Vendas construído com Python, Streamlit e OpenRouter utilizando Function Calling para responder perguntas sobre métricas de negócio de forma confiável.

Objetivo
O projeto demonstra a construção de uma aplicação de análise de vendas capaz de:

Processar dados de vendas;
Gerar indicadores de negócio;
Exibir dashboards interativos;
Responder perguntas em linguagem natural;
Utilizar Function Calling para garantir que os cálculos sejam realizados pelo Python e não inventados pela IA.
Arquitetura
sales.csv
    │
    ▼
Data Processor
    │
    ▼
Metrics Service
    │
    ▼
Function Tools
    │
    ▼
OpenRouter
    │
    ▼
Chat IA

    ▲
    │
Dashboard Streamlit
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
Permite consultas em linguagem natural como:

Qual a receita total?
Quantos pedidos foram concluídos?
Qual o ticket médio?
Qual a taxa de cancelamento?
Qual a receita média por cliente?
Qual a receita em determinado período?
Tecnologias
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
A documentação esperada do dataset encontra-se em:

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
Nova métrica para avaliar o potencial de monetização da base de clientes.

Receita por Período
Permite consultas filtradas por intervalo de datas.

Ranking de Cidades
Visualização das cidades com maior volume de receita.

Insights de Negócio
Geração de indicadores para apoio à tomada de decisão.

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
Autor
Projeto desenvolvido para fins de estudo, prática de análise de dados e desenvolvimento de assistentes inteligentes utilizando IA Generativa.
