import streamlit as st


def initialize_session_state():
    # if 'inputs' not in st.session_state:
    #     st.session_state.inputs = {"text": "", "type": ""}
    
    if 'step' not in st.session_state:
        st.session_state.step = 1
