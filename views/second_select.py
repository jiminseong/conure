import streamlit as st

def display_page2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
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
    with col4:
        if st.button('골절'):
            st.session_state.step=7
            st.rerun()

    st.markdown(
        """
        <style>

        .st-emotion-cache-uwy95n{
            width : 100%;
        }
        </style>
        """,
            unsafe_allow_html=True
        )

