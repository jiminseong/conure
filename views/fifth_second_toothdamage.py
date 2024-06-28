import streamlit as st
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def tooth_prompting():
    # open api 사용 시 주석 풀기
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""
                    이 사용자는 일반인이며 어려운 설명은 이해하기 어려울 수 있습니다. 
                    현재 FirstAID라는 인공지능 api 사용 웹에서 치아 손상진단을 위해 접근하였습니다. 
                    구체적으로 행동요령과 구급처치법을 설명해 주세요. 
                    그리고 이 환자의 문제가 발생한 부분은 {st.session_state.selected_tooth[0]}이며 증상은
                    {st.session_state.selected_tooth[1]}입니다. 구체적인 증상은{st.session_state.selected_tooth[4]}입니다. 
                    """,
            }
        ],
        model="gpt-4o",
    )
    result = chat_completion.choices[0].message.content
    st.session_state.tooth_result = result
    return result

def display_page5_2():
    st.title("치아 손상 진단")

    
    # 증상 선택 옵션 제공
    st.markdown("증상에 대해 선택해주세요.")
    symptom_options = [
        "통증",
        "시림",
        "출혈",
        "부기",
        "이가 흔들림",
        "기타"
    ]
    selected_symptom = st.selectbox("증상", symptom_options)
    st.session_state.selected_tooth.append(selected_symptom)
    additional_info = st.text_area("자세한 증상에 대해 설명해주세요.")
    st.session_state.selected_tooth.append(additional_info)
    
    # 폼 생성
    with st.form(key='diagnosis_form'):
        submit = st.form_submit_button("진단")

    # 버튼을 눌렀을 때 입력된 내용 처리
    if submit:
        # # OpenAI API 호출
        tooth_prompting()
        
        st.write(st.session_state.tooth_result)
        
        # 추가 도움말 링크 제공
        st.markdown("### 추가 도움말")
        st.markdown("- [치아 응급처치 방법](https://www.youtube.com/watch?v=Zd5kz2Q0U6Q)")
        st.markdown("- [치아 건강 관리 팁](https://www.youtube.com/watch?v=zlvJuN5Gyec)")


