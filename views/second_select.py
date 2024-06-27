import streamlit as st

def display_page2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
       f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col2:
        if st.button('외상'):
            st.session_state.step = 3
            st.rerun()
        if st.button('치아손상'):
            st.session_state.step = 5
            st.rerun()
    with col3:
        if st.button('복통'):
            st.session_state.step = 4
            st.rerun()
        if st.button('심정지'):
            st.session_state.step = 6
            st.rerun()
    

    st.markdown(
    """
    <style>

    .st-emotion-cache-7ym5gk{
        width : 100%;
    }
    </style>
    """,
            unsafe_allow_html=True
        )

