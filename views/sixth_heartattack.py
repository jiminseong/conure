import streamlit as st


def display_page6():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>',
        unsafe_allow_html=True,
    )

    st.write("여섯번째 페이지")
