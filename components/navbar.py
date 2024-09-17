import streamlit as st

def sidebar():

    with st.sidebar:
        st.page_link("app.py", label="Cost Calculator", icon="🧮")
        st.page_link("pages/ta_advantages.py", label="TechAhead Advantage", icon="🚀")