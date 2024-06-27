import streamlit as st
import base64

def display_page7():
    st.title("골절 예상 부위")
    st.markdown("아픈 부위를 선택해주세요:")
    bone_names = [
       '안면부', '두개골', '척추', '흉곽', '쇄골',
       '어깨', '팔', '손목 및 손', '골반', '다리', '발목 및 발'
    ]
    
    if 'selected_bone' not in st.session_state:
        st.session_state.selected_bone = ""
    

    # 이미지 파일을 읽어 Base64 인코딩
    with open("./assets/body.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    # Base64 인코딩된 이미지를 HTML로 삽입
    st.markdown("""
        <style>
        .born-container {
            position:relative;
            height: auto;
            max-width: 600px;
        }
        .born-container img {
            width: 100%;
            max-width: 600px;
            display: block;
        }
        .button-overlay {
            position: absolute;
            background-color: transparent;
            border: none;
            cursor: pointer;
        }
        .button-overlay:hover {
            background-color: rgba(0, 0, 0, 0.3);
        }
        .button-overlay::before {
            content: attr(data-index);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: black;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

   
    st.markdown(f"""
        <div class="born-container">
            <img src="data:image/jpeg;base64,{img_base64}">
            <button class="button-overlay" data-index="1" style="top: 8%; left: 24.8%; width: 8%; height: 10%;"></button>
            <button class="button-overlay" data-index="2" style="top: 5%; left: 67.5%; width: 8%; height: 13%;"></button>
            <button class="button-overlay" data-index="2" style="top: 4%; left: 24%; width: 9.8%; height: 6%;"></button>
            <button class="button-overlay" data-index="3" style="top: 17%; left: 70.5%; width: 2%; height: 35%;"></button>
            <button class="button-overlay" data-index="4" style="top: 25%; left: 22%; width: 14%; height: 13%;"></button>
            <button class="button-overlay" data-index="4" style="top: 26%; left: 64%; width: 7%; height: 14%;"></button>
            <button class="button-overlay" data-index="4" style="top: 26%; left: 72%; width: 7%; height: 14%;"></button>
            <button class="button-overlay" data-index="5" style="top: 21.5%; left: 21%; width: 16%; height: 3%;"></button>
            <button class="button-overlay" data-index="6" style="top: 21.5%; left: 17%; width: 7%; height: 6%;"></button>
            <button class="button-overlay" data-index="6" style="top: 21.5%; left: 33%; width: 7%; height: 6%;"></button>
            <button class="button-overlay" data-index="6" style="top: 21.5%; left: 62%; width: 9%; height: 10%;"></button>
            <button class="button-overlay" data-index="6" style="top: 21.5%; left: 73%; width: 9%; height: 10%;"></button>
            <button class="button-overlay" data-index="7" style="top: 26%; left: 15.2%; width: 4%; height: 23.5%; transform: rotate(11deg);"></button>
            <button class="button-overlay" data-index="7" style="top: 26%; left: 38.3%; width: 4%; height: 23.5%; transform: rotate(-11deg);"></button>
            <button class="button-overlay" data-index="7" style="top: 26%; left: 58%; width: 4%; height: 23.5%; transform: rotate(11deg);"></button>
            <button class="button-overlay" data-index="7" style="top: 26%; left: 81%; width: 4%; height: 23.5%; transform: rotate(-11deg);"></button>
            <button class="button-overlay" data-index="8" style="top: 48.5%; left: 10%; width: 7%; height: 10%; transform: rotate(11deg);"></button>
            <button class="button-overlay" data-index="8" style="top: 48.5%; left: 40%; width: 7%; height: 10%; transform: rotate(-11deg);"></button>
            <button class="button-overlay" data-index="8" style="top: 48.5%; left: 53%; width: 7%; height: 10%; transform: rotate(11deg);"></button>
            <button class="button-overlay" data-index="8" style="top: 48.5%; left: 83%; width: 7%; height: 10%; transform: rotate(-11deg);"></button>
            <button class="button-overlay" data-index="9" style="top: 45.5%; left: 21%; width: 15.5%; height: 10%;"></button>
            <button class="button-overlay" data-index="9" style="top: 45.5%; left: 63.5%; width: 15.5%; height: 10%;"></button>
            <button class="button-overlay" data-index="10" style="top: 52%; left: 21%; width: 15.5%; height: 37%;"></button>
            <button class="button-overlay" data-index="10" style="top: 52%; left: 64%; width: 15.5%; height: 37%;"></button>
            <button class="button-overlay" data-index="11" style="top: 88%; left: 21%; width: 15.5%; height: 10%;"></button>
            <button class="button-overlay" data-index="11" style="top: 88%; left: 64%; width: 15.5%; height: 10%;"></button>
        </div>
    """, unsafe_allow_html=True)


    with st.form(key='bone_form'):
        bone_number = st.text_input("선택한 부위 번호를 입력하세요:")
        submit = st.form_submit_button("부위 선택")

    if submit:
          if bone_number.isdigit() and 1 <= int(bone_number) <= 11:
            st.session_state.selected_bone = bone_names[int(bone_number) - 1]
            st.markdown(f'선택된 부위: {int(bone_number)}번 {st.session_state.selected_bone}입니다. 맞으면 확인 버튼을 눌러주세요!')
          else:
            st.error("유효한 부위 번호를 입력하세요. (1-11)")

    # 선택된 부위 이름 표시 및 확인 버튼
    if st.session_state.selected_bone:
        if st.button("확인"):
            if int(bone_number)==1:
              st.session_state.step = 7.2# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==2:
              st.session_state.step = 7.3# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==3:
              st.session_state.step = 7.4# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==4:
              st.session_state.step = 7.5# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==5:
              st.session_state.step = 7.6# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==6:
              st.session_state.step = 7.7# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==7:
              st.session_state.step = 7.8# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==8:
              st.session_state.step = 7.9# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==9:
              st.session_state.step = 7.10# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==10:
              st.session_state.step = 7.11# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영
            if int(bone_number)==11:
              st.session_state.step = 7.12# 다음 페이지로 이동하기 위해 step 값을 설정
              st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영


    else:
        st.markdown('선택된 부위: 없음')

# 앱 실행 부분
if __name__ == "__main__":
    display_page7()