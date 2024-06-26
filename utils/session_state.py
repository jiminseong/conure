import streamlit as st


def initialize_session_state():
    # if 'inputs' not in st.session_state:
    #     st.session_state.inputs = {"text": "", "type": ""}
    
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0
        
    