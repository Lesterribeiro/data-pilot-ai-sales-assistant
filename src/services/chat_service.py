"""
Serviço de integração
OpenRouter
"""

import os

from openai import OpenAI


def get_client():

    api_key = os.getenv(
        "OPENROUTER_API_KEY"
    )

    return OpenAI(
        api_key=api_key,
        base_url=(
            "https://openrouter.ai/api/v1"
        )
    )
