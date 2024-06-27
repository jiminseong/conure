import os
from datetime import date
import streamlit as st
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]
OpenAI.api_key = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    
def request_chat_completion(data):
    # open api 사용 시 주석 풀기
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"{data}",
    #         },
    #         {
    #             "role": "system",
    #             "content": """
    #                 복통 환자를 진료하는 간호사
    #                 """,
    #         }
    #     ],
    #     model="gpt-4o",
    # )
    # result = chat_completion.choices[0].message.content
    result = "예시용 문자 데이터"
    return result

# def request_chat_completion(
#     prompt, system_role="복통 환자를 진료하는 간호사", model="gpt-4o", stream=True
# ):
#     messages = [
#         {"role": "system", "content": system_role},
#         {"role": "user", "content": prompt},
#     ]

#     chat_completion = client.chat.completions.create(
#         model=model, messages=messages, stream=stream
#     )
    
#     # result = chat_completion.choices[0].message.content
#     result = "예시용문자"
#     return result

# def print_streaming_response(response):
#     message = ""
#     for chunk in response:
#         delta = chunk.choices[0]["delta"]
#         if "content" in delta:
#             message += delta["content"]
#         else:
#             break
#     return message

def display_page4_2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()

    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    )

    st.write(st.session_state.colic_result)