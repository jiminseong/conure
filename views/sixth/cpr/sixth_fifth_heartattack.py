import streamlit as st

def display_page6_5():
    with open("././assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="padding: 1em; margin-left: 10%; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    # 안내 메시지 표시
    st.container()
    st.write("의식을 확인해주세요 - 말을 걸어보고, 손을 대보고, 어깨를 흔들어 의식을 확인해주세요.")

