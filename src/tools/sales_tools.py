"""
Ferramentas usadas pelo Function Calling
"""


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "total_revenue",
            "description": "Retorna a receita total dos pedidos concluídos."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "total_orders",
            "description": "Retorna o total de pedidos concluídos."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "average_ticket",
            "description": "Retorna o ticket médio dos pedidos concluídos."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "unique_customers",
            "description": "Retorna a quantidade de clientes únicos."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "cancellation_rate",
            "description": "Retorna a taxa de cancelamento."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "revenue_per_customer",
            "description": "Retorna a receita média por cliente."
        }
    }
]
{
    "type": "function",
    "function": {
        "name": "get_revenue_by_period",
        "description": "Retorna a receita de um período específico.",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string"
                },
                "end_date": {
                    "type": "string"
                }
            }
        }
    }
}
