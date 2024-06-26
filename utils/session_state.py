import streamlit as st

def initialize_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 5

    if 'selected_tooth' not in st.session_state:
        st.session_state.selected_tooth = ""
