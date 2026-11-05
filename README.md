# Data Pilot AI Sales Assistant 

O **Data Pilot AI Sales Assistant** é um painel inteligente de análise de vendas construído em Python com Streamlit. Ele integra técnicas de análise de dados com Inteligência Artificial por meio do OpenRouter utilizando **Function Calling**, permitindo consultas dinâmicas tanto visualmente quanto em linguagem natural.

A regra fundamental do projeto: **O Python calcula os dados com precisão e a IA apenas explica o resultado**, evitando qualquer tipo de alucinação numérica.

---

## Tecnologias Utilizadas

- **Python** (Linguagem base)
- **Pandas** (Tratamento e manipulação dos dados de vendas)
- **Streamlit** (Construção da interface visual e do chat)
- **Plotly** (Renderização de gráficos iterativos)
- **OpenRouter API** (Integração com LLM utilizando chamadas de ferramentas)

---

## Como Instalar e Rodar o Projeto

Siga os passos abaixo no terminal para executar a aplicação localmente:

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com
   cd data-pilot-ai-sales-assistant
   ```

2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as variáveis de ambiente:**
   Copie o arquivo `.env.example` para um novo arquivo chamado `.env`:
   ```bash
   cp .env.example .env
   ```
   Abra o arquivo `.env` e insira sua chave da API do OpenRouter:
   ```env
   OPENROUTER_API_KEY=sua_chave_da_api_aqui
   MODEL=openrouter/free
   ```

4. **Executar a aplicação:**
   ```bash
   streamlit run app.py
   ```

---

## Ferramentas (Functions) Disponíveis para a IA

O modelo de linguagem está instruído para identificar a intenção do usuário e acionar as seguintes funções estruturadas no arquivo `metrics_service.py`:

- `total_revenue`: Retorna o faturamento bruto total de pedidos concluídos.
- `total_orders`: Retorna a contagem total de pedidos finalizados com sucesso.
- `average_ticket`: Calcula o valor médio gasto por pedido.
- `unique_customers`: Apresenta o número de compradores únicos na base de dados.
- `cancellation_rate`: Calcula a taxa percentual de pedidos cancelados.
- **`revenue_per_customer` (Melhoria Implementada):** Retorna o valor médio faturado por cliente único.
- **`get_revenue_by_period` (Melhoria Implementada):** Retorna a receita total calculada de forma dinâmica por intervalo de datas.

---

## Melhorias Implementadas

1. **Métrica de Negócio Nova:** Criação da função `revenue_per_customer` para acompanhar o real valor de ciclo de vida e gasto médio do cliente único na plataforma comercial.
2. **Filtros Temporais por Chat:** Criação da lógica `get_revenue_by_period` garantindo a capacidade do agente de receber comandos analíticos com parâmetros implícitos de datas.

---
Desenvolvido por [Lesterribeiro](https://github.com) para fins de estudo e portfólio em IA Generativa e Análise de Dados.
