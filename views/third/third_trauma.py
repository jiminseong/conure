import streamlit as st
from PIL import Image
import io
import base64

def display_page3():
    
    # 로고 표시
    with open("./assets/logo.svg", "r") as f:
        svg_content = f.read()
        
    st.markdown(
        f'<div style="display: flex; justify-content: center; margin-bottom: 5%;" align="center">{svg_content}</div>', 
        unsafe_allow_html=True
    )

    # 파일 업로드 위젯
    st.subheader("상처 부위 사진 파일을 업로드하세요 (최대 3장까지)")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("상처 부위가 잘 보이는 사진을 사용 시 더 빠르게 정확한 응급처치 방법을 볼 수 있습니다.")
    st.session_state.uploaded_files = st.file_uploader("'Browse files'를 눌러 사진 업로드", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="1")
    
    if st.session_state.uploaded_files:
        if len(st.session_state.uploaded_files) > 3:
            st.error("최대 3개의 파일만 업로드할 수 있습니다.")
            st.session_state.uploaded_files = []
        else:
            pil_images = []
            encoded_images = []
            for uploaded_file in st.session_state.uploaded_files:
                pil_image = Image.open(uploaded_file)
                pil_images.append(pil_image)
                buffered = io.BytesIO()
                pil_image.save(buffered, format="PNG")
                encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
                encoded_images.append(encoded_image)
                st.session_state.trauma_input.append(encoded_images)
            cols = st.columns(3)  # 3개의 열 생성
            for idx, uploaded_file in enumerate(st.session_state.uploaded_files):
                image = Image.open(uploaded_file)
                with cols[idx % 3]:  # 3열로 나누어 배치
                    st.image(image, use_column_width=True)
                    
            
        if st.button("응급닥터에게 물어보기"):
            st.session_state.step = 3.2
            st.experimental_rerun()

    if st.button("뒤로 가기"):
        st.session_state.step -= 1
        st.experimental_rerun()
    
    # 스타일 적용
    st.markdown(
        """
        <style>
            .st-emotion-cache-13g0a2z, .st-emotion-cache-7oyfbm,st-emotion-cache-17h7n91 {
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

