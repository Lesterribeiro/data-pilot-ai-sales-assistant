"""
Tela do Assistente
"""

import streamlit as st


def render_chat():

    st.title(
        "🤖 Assistente de Vendas"
    )

    question = st.text_input(
        "Faça sua pergunta"
    )

    if question:

        st.info(
            """
            Integração com
            OpenRouter
            será executada
            após configuração
            do ambiente.
            """
        )
