import streamlit as st
import os
import openai

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "여기에 발급받은 API 키를 입력해 주세요"

openai.api_key = os.environ.get("OPENAI_API_KEY")

def display_page5_2():
    st.title("치아 손상 진단")

    if 'selected_tooth' not in st.session_state or not st.session_state.selected_tooth:
        st.error("먼저 치아를 선택해 주세요.")
        return

    selected_tooth = st.session_state.selected_tooth

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
    additional_info = st.text_area("자세한 증상에 대해 설명해주세요.")

    # 폼 생성
    with st.form(key='diagnosis_form'):
        submit = st.form_submit_button("진단")

    # 버튼을 눌렀을 때 입력된 내용 처리
    if submit:
        # response = client.chat.completions.create(
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": text,
        #         },
        #         {
        #             "role": "system",
        #             "content": f"이 사용자는 일반인입니다. 어려운 설명은 이해하기 어려울 수 있습니다. 그러나 구체적으로 행동요령과 구급처치법을 설명해 주세요. 그리고 이 환자의 문제가 발생한 부분은 {selected_tooth}입니다.",
        #         },
        #     ],
        #     model="gpt-4",
        # )
        st.write(f"아픈 이빨: {selected_tooth}")
        st.write(f"선택한 증상: {selected_symptom}")
        st.write(f"추가 설명: {additional_info}")

        # # OpenAI API 호출
         

        # # 응답 출력
        # st.write(response['choices'][0]['message']['content'])


        # 추가 도움말 링크 제공
        st.markdown("### 추가 도움말")
        st.markdown("- [치아 응급처치 방법](https://www.youtube.com/watch?v=Zd5kz2Q0U6Q)")
        st.markdown("- [치아 건강 관리 팁](https://www.youtube.com/watch?v=zlvJuN5Gyec)")

# 앱 실행 부분
if __name__ == "__main__":
    display_page5_2()
