import streamlit as st

def display_page8():
    # SVG 파일을 읽어오는 부분
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
    st.markdown(
        f'<div style="display : flex; justify-content : center; margin-bottom:5%;" align="center">{svg_content}</div>',
        unsafe_allow_html=True
    )

    # 폼 시작
    with st.form(key='symptom_form'):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:

            # 체크박스와 상태 추가
            if st.checkbox('경련이 일어납니다'):
                st.session_state.heat.append('경련')
            if st.checkbox('손,발목이 부었습니다'):
                st.session_state.heat.append('손,발목 부종')
            if st.checkbox('대상이 정신을 잃었습니다'):
                st.session_state.heat.append('의식 불명')

            # 텍스트 입력 필드
            heat_text = st.text_area("자세한 환자 상태를 입력해주세요!")
            if heat_text:
                st.session_state.heat.append(heat_text)

            # 폼 제출 버튼
            submit_button = st.form_submit_button(label='FirstAId에게 물어보기')

            # 폼 제출 후 동작
            if submit_button:
                if not st.session_state.heat:
                    st.warning('입력값이 없습니다!')
                else:
                    st.success("진단을 시작합니다...")
                    st.session_state.step = 8.2
                    st.rerun()

