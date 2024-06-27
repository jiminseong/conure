import streamlit as st

def initialize_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0  

    if 'selected_tooth' not in st.session_state:
        st.session_state.selected_tooth = ""

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0
        
    if 'second' not in st.session_state:
        st.session_state.second = 0
        
    if 'colic_result' not in st.session_state:
        st.session_state.colic_result = ""