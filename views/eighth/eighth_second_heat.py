import streamlit as st 
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def extract_strings(string_array):
    if isinstance(string_array, list):
        return [str(item) for item in string_array]
    else:
        raise ValueError("Input must be a list of strings")



# OpenAI와 대화 요청 함수
def request_chat_completion(str):
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 간호사입니다. 온열질환에 대한 진료를 진행해서 친절하고 깔끔한 형식으로 알려주세요"},
            {"role": "user", "content": f'{str}와 같이 증상이 나타나고 있어 해당 증상에 대해 깔끔하게 설명해줘'},
        ],
    )
    result = chat_completion.choices[0].message.content
    st.session_state.heat_result = result
    return result


def display_page8_2():
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
    st.markdown(
            f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>', unsafe_allow_html=True
    ) 
    
    extracted_strings = extract_strings(st.session_state.heat)
    request_chat_completion(extracted_strings)   
    # heat_result가 있는지 확인하고, 있으면 출력
    if st.session_state.heat_result:
        st.write(st.session_state.heat_result)
        
        # 결과가 출력된 후에만 버튼 표시
        if st.button('홈으로 돌아가기'):
            st.session_state.step = 1
            st.experimental_rerun()
    
    
    