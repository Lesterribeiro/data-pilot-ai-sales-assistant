import streamlit as st

from src.ui.dashboard import (
    render_dashboard
)

from src.ui.chat_page import (
    render_chat
)


st.set_page_config(
    page_title="Data Pilot",
    layout="wide"
)

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Chat IA"
    ]
)


if menu == "Dashboard":

    render_dashboard()

else:

    render_chat()
