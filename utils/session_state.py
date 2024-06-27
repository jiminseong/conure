import streamlit as st

def initialize_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 7

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0  

    if 'selected_tooth' not in st.session_state:
        st.session_state.selected_tooth = ""
  
    if 'selected_bone' not in st.session_state:
        st.session_state.selected_bone = ""

    if 'cpr_step' not in st.session_state:
        st.session_state.cpr_step = 0