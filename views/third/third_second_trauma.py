import streamlit as st
from openai import OpenAI
import os


os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)




def summary_prompting():
    # 실제 OpenAI API를 사용 시 아래 주석을 해제
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages = [
            {
                "role": "user",
                "content": 
                    [
                    {"type": "text", 
                        "text": 
                        f"""
                        입력된 데이터는 사용자의 현재 외상을 입은 상태를 보여주는 사진이야.
                        사용자는 지금 다급하게 이 외상을 치료해야해.
                        어떤 외상을 입은 것인지, 어떻게 치료해야 하는지 알려줘야해.
                        사용자는 아파서 당황하고 긴급할테니, 사용자가 한눈에 알아보게 깔끔하게 대답해줘
                        ...
                        """
                        }
                    ] + 
                    [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}} for base64_image in st.session_state.trauma_input]
            }
        ]
    )
    # result = ""
    result = chat_completion.choices[0].message.content
    return result

def display_page3_2():

    # 로고 표시
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
        
    st.markdown(
        f'<div style="display: flex; justify-content: center; margin-bottom: 5%;" align="center">{svg_content}</div>', 
        unsafe_allow_html=True
    )
    
    
    with st.spinner("빠르게 치료 방법 찾는중..."):
        result = summary_prompting()
        st.write(result)
        st.session_state.doctor_consulted = True
    

    # 버튼이 클릭된 경우 지도 표시
    if st.button('주변 가까운 약국 보기'):
        st.session_state.step = 3.3
        st.rerun()
    

