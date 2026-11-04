"""
Dashboard principal
"""

import streamlit as st


def render_dashboard():

    st.title(
        "📊 Data Pilot"
    )

    st.subheader(
        "Painel de Vendas"
    )

    col1, col2, col3, col4 = (
        st.columns(4)
    )

    with col1:
        st.metric(
            "Receita",
            "R$ 0,00"
        )

    with col2:
        st.metric(
            "Pedidos",
            "0"
        )

    with col3:
        st.metric(
            "Ticket Médio",
            "R$ 0,00"
        )

    with col4:
        st.metric(
            "Clientes",
            "0"
        )

    st.info(
        """
        Dashboard preparado
        para integração com
        sales.csv.
        """
    )
