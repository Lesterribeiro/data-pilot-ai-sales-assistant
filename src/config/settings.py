"""
Configurações globais do projeto Data Pilot
"""

APP_NAME = "Data Pilot AI Sales Assistant"

DEFAULT_MODEL = "openrouter/free"

DATA_FILE = "data/sales.csv"

CLEAN_DATA_FILE = "data/sales_clean.csv"

SUPPORTED_STATUS = [
    "completed",
    "canceled",
    "pending"
]
