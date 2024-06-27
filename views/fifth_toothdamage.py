import streamlit as st
import base64

def display_page5():
    st.title("치아 구조도 선택")
    st.markdown("아픈 부위를 선택해주세요:")

    teeth_names = [
        '왼쪽 위 제 2대구치', '왼쪽 위 제 1대구치', '왼쪽 위 제 2소구치', '왼쪽 위 제 1소구치',
        '왼쪽 위 송곳니', '왼쪽 위 측절치', '왼쪽 위 중절치', '오른쪽 위 중절치',
        '오른쪽 위 측절치', '오른쪽 위 송곳니', '오른쪽 위 제 1소구치', '오른쪽 위 제 2소구치',
        '오른쪽 위 제 1대구치', '오른쪽 위 제 2대구치', '왼쪽 아래 제 2대구치',
        '왼쪽 아래 제 1대구치', '왼쪽 아래 제 2소구치', '왼쪽 아래 제 1소구치',
        '왼쪽 아래 송곳니', '왼쪽 아래 측절치', '왼쪽 아래 중절치', '오른쪽 아래 중절치',
        '오른쪽 아래 측절치', '오른쪽 아래 송곳니', '오른쪽 아래 제 1소구치',
        '오른쪽 아래 제 2소구치', '오른쪽 아래 제 1대구치', '오른쪽 아래 제 2대구치',
        '윗 잇몸', '아래 잇몸'
    ]

    if 'selected_tooth' not in st.session_state:
        st.session_state.selected_tooth = ""

    # 이미지 파일을 읽어 Base64 인코딩
    with open("./assets/teeth.jpg", "rb") as f:
        img_bytes = f.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    # CSS 스타일 정의
    st.markdown("""
        <style>
        .teeth-container {
            position: relative;
            width: 100%;
            max-width: 600px;
        }
        .teeth-container img {
            width: 100%;
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

    # 치아 구조 이미지 및 버튼 오버레이
    st.markdown(f"""
        <div class="teeth-container">
            <img src="data:image/jpeg;base64,{img_base64}">
            <!-- 윗니 -->
            <button class="button-overlay" data-index="1" style="top: 33%; left: 3%; width: 4.5%; height: 15%;"></button>
            <button class="button-overlay" data-index="2" style="top: 33%; left: 6%; width: 5%; height: 17%;"></button>
            <button class="button-overlay" data-index="3" style="top: 33%; left: 11%; width: 5%; height: 20%;"></button>
            <button class="button-overlay" data-index="4" style="top: 33%; left: 17%; width: 6%; height: 22%;"></button>
            <button class="button-overlay" data-index="5" style="top: 33%; left: 24.5%; width: 6%; height: 22%;"></button>
            <button class="button-overlay" data-index="6" style="top: 33%; left: 32%; width: 7%; height: 21%;"></button>
            <button class="button-overlay" data-index="7" style="top: 33%; left: 41%; width: 8%; height: 21%;"></button>
            <button class="button-overlay" data-index="8" style="top: 33%; left: 50%; width: 8.8%; height: 21%;"></button>
            <button class="button-overlay" data-index="9" style="top: 33%; left: 61%; width: 7%; height: 21%;"></button>
            <button class="button-overlay" data-index="10" style="top: 33%; left: 68%; width: 7%; height: 22%;"></button>
            <button class="button-overlay" data-index="11" style="top: 33%; left: 75.5%; width: 7%; height: 22%;"></button>
            <button class="button-overlay" data-index="12" style="top: 33%; left: 82.7%; width: 6%; height: 21%;"></button>
            <button class="button-overlay" data-index="13" style="top: 33%; left: 87.5%; width: 5%; height: 17%;"></button>
            <button class="button-overlay" data-index="14" style="top: 33%; left: 91%; width: 5%; height: 15%;"></button>
            <!-- 아랫니 -->
            <button class="button-overlay" data-index="15" style="top: 54%; left: 5%; width: 3%; height: 15%;"></button>
            <button class="button-overlay" data-index="16" style="top: 56%; left: 8%; width: 3.5%; height: 18%;"></button>
            <button class="button-overlay" data-index="17" style="top: 57%; left: 12%; width: 5.5%; height: 20%;"></button>
            <button class="button-overlay" data-index="18" style="top: 57%; left: 19%; width: 5%; height: 22%;"></button>
            <button class="button-overlay" data-index="19" style="top: 57%; left: 26%; width: 6%; height: 22%;"></button>
            <button class="button-overlay" data-index="20" style="top: 57%; left: 34.5%; width: 6.5%; height: 21%;"></button>
            <button class="button-overlay" data-index="21" style="top: 57%; left: 41.5%; width: 8%; height: 21%;"></button>
            <button class="button-overlay" data-index="22" style="top: 57%; left: 50%; width: 8%; height: 21%;"></button>
            <button class="button-overlay" data-index="23" style="top: 57%; left: 58.8%; width: 6.5%; height: 21%;"></button>
            <button class="button-overlay" data-index="24" style="top: 57%; left: 67%; width: 7%; height: 22%;"></button>
            <button class="button-overlay" data-index="25" style="top: 57%; left: 75%; width: 6.5%; height: 22%;"></button>
            <button class="button-overlay" data-index="26" style="top: 57%; left: 81.5%; width: 6%; height: 21%;"></button>
            <button class="button-overlay" data-index="27" style="top: 55%; left: 88%; width: 4%; height: 19%;"></button>
            <button class="button-overlay" data-index="28" style="top: 54%; left: 92%; width: 3%; height: 15%;"></button>
            <!-- 잇몸 -->
            <button class="button-overlay" data-index="29" style="top: 0%; left: 0%; width: 100%; height: 40%;"></button>
            <button class="button-overlay" data-index="30" style="top: 80%; left: 0%; width:100%; height: 20%;"></button>
        </div>
    """, unsafe_allow_html=True)

    # 이빨 선택 폼
    with st.form(key='tooth_form'):
        tooth_number = st.text_input("선택한 치아 번호를 입력하세요:")
        submit = st.form_submit_button("이빨 선택")

    if submit:
        if tooth_number.isdigit() and 1 <= int(tooth_number) <= 30:
            st.session_state.selected_tooth = teeth_names[int(tooth_number) - 1]
            st.markdown(f'선택된 치아: {int(tooth_number)}번 {st.session_state.selected_tooth}입니다. 맞으면 확인 버튼을 눌러주세요!')
        else:
            st.error("유효한 치아 번호를 입력하세요. (1-30)")

    # 선택된 치아 이름 표시 및 확인 버튼
    if st.session_state.selected_tooth:
        if st.button("확인"):
            st.session_state.step = 52  # 다음 페이지로 이동하기 위해 step 값을 설정
            st.experimental_rerun()  # 페이지를 리프레시하여 step 값을 반영

    else:
        st.markdown('선택된 치아: 없음')

# 앱 실행 부분
if __name__ == "__main__":
    display_page5()