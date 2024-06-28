import os
import streamlit as st
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# OpenAI와 대화 요청 함수
def request_chat_completion():
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 간호사입니다."},
            {"role": "user", "content": st.session_state.colic_input},
        ],
    )
    result = chat_completion.choices[0].message.content
    st.session_state.colic_result = result
    return result


def display_page4_2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )
    
    
    request_chat_completion()
    st.write(st.session_state.colic_result)