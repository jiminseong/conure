import streamlit as st


def display_page3():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
       f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    st.write("세번째 페이지")