"""
Registro das funções disponíveis
"""

from src.services.metrics_service import (
    total_revenue,
    total_orders,
    average_ticket,
    unique_customers,
    cancellation_rate,
    revenue_per_customer,
    get_revenue_by_period
)

AVAILABLE_FUNCTIONS = {

    "total_revenue": total_revenue,

    "total_orders": total_orders,

    "average_ticket": average_ticket,

    "unique_customers": unique_customers,

    "cancellation_rate": cancellation_rate,

    "revenue_per_customer": revenue_per_customer,

    "get_revenue_by_period":
        get_revenue_by_period

}
